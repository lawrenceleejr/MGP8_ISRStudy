from matplotlib import pyplot as plt
import numpy as np
import uproot
import sys
import ROOT
import array

def all_histograms(mass, mgpath, log=False, savefig=None):
    '''
    :param mass: Mass of the root file
    :param mgpath: Path to the root file
    :param log: If True, makes the y axis log scale
    :param savefig: Path to save the histogram
    :return: All normalized weighted pT histograms on one plot
    '''
    plt.clf()
    with uproot.open(mgpath) as root:
        for key in root.keys():
            if 'pTsum' in key:
                if key == 'pTsum 0;1':
                    continue
                arr = root[key].to_numpy()
                normalized_frequency = arr[0]/(sum(arr[0])*50)
                plt.plot(arr[1][:-1], normalized_frequency, color='dodgerblue')
        plt.suptitle('Weighted pT, Gluino Target Mass = {} GeV'.format(mass))
        plt.xlabel('gluglu pT (GeV)')
        plt.xlim(0, 2800)
        if log:
            plt.yscale('log')
            plt.ylabel('Normalized Frequency (log)')
            plt.ylim(0.0000001, 0.01)
        else:
            plt.ylabel('Normalized Frequency')
            plt.ylim(0,0.01)
        if savefig != None:
            plt.savefig(savefig)
        else:
            plt.show()

def errorbar_ratioplot(mass, bins, mgpath, pythiapath, outputpath):
    '''
    :param mass: Gluino mass (GeV)
    :param bins: List of bins in the histogram
    :param mgpath: Path to the madgraph root file
    :param pythiapath: Path to the pythia root file
    :param outputpath: Filepath to save the ROOT file
    :return: ROOT file with the ratio systematic errors
    '''
    #Define the number of madgraph histograms that exist
    n_weights = 45

    #Open ROOT files
    pyfile = ROOT.TFile.Open(pythiapath)
    mgfile = ROOT.TFile.Open(mgpath)

    #Iterate through all madgraph histograms, return one histogram with all max bins values, another with all min values
    pythiahist = pyfile.Get("pTsum;1")
    pythiahist_rebinned = rebin(pythiahist, bins)
    pythiahist_rebinned.Scale(1. / pythiahist_rebinned.Integral())
    mins = np.repeat(10000000, len(bins))
    maxes = np.zeros(len(bins))
    zeroth = 0
    for i in range(n_weights):
        mghist = mgfile.Get("pTsum {};1".format(i))
        mghist_rebinned = rebin(mghist, bins)
        mghist_rebinned.Scale(1. / mghist_rebinned.Integral())
        if i == 0:
            zeroth = mghist_rebinned
        for bin in range(len(bins)):
            n_entries_in_bin = mghist_rebinned.GetBinContent(bin+1)
            if n_entries_in_bin < mins[bin]:
                mins[bin] = n_entries_in_bin
            if n_entries_in_bin > maxes[bin]:
                maxes[bin] = n_entries_in_bin

    #Create the min/max histograms
    min_hist, max_hist = create_min_max_hists(bins, mins, maxes)

    #Get the min/max ratio plots (converted to TGraphAsymmErrors)
    min_ratio = ratioPlot(min_hist, pythiahist_rebinned)
    max_ratio = ratioPlot(max_hist, pythiahist_rebinned)
    zeroth_ratio = ratioPlot(zeroth, pythiahist_rebinned)

    #Fill the ratio plots to a histogram
    min_ratio_hist = pythiahist_rebinned.Clone("Minimum Ratio")
    max_ratio_hist = pythiahist_rebinned.Clone("Maximum Ratio")
    zeroth_ratio_hist = pythiahist_rebinned.Clone("Zeroth Ratio")
    ratioHistFill(min_ratio, min_ratio_hist, bins)
    ratioHistFill(max_ratio, max_ratio_hist, bins)
    ratioHistFill(zeroth_ratio, zeroth_ratio_hist, bins)

    #Create the 0th ratio histogram, fill errors from the min/max
    c1 = ROOT.TCanvas("c1", "min ratio")
    min_ratio_hist.Draw()
    c1.Update()
    app.Run()


def create_min_max_hists(bins, mindata, maxdata):
    '''
    :param bins: List of bins to set the histograms
    :param mindata: Numpy array of min weights for each bin
    :param maxdata: Numpy array of max weights for each bin
    :return: Minimum and maximum histograms
    '''
    #Create the raw histograms
    min_hist = ROOT.TH1F("Minimum Madgraph", "Minimum Madgraph", len(bins), array.array('d', bins))
    max_hist = ROOT.TH1F("Maximum Madgraph", "Maximum Madgraph", len(bins), array.array('d', bins))
    min_hist.GetXaxis().SetLimits(min(bins), max(bins))
    max_hist.GetXaxis().SetLimits(min(bins), max(bins))

    #Fill the histograms with the data
    for i in range(len(mindata)):
        min_hist.SetBinContent(i + 1, mindata[i])
    for i in range(len(maxdata)):
        max_hist.SetBinContent(i + 1, maxdata[i])

    return min_hist, max_hist


def rebin(histogram, new_bins):
    '''
    :param histogram: Input TH1F histogram you would like to rebin
    :param new_bins: New bins to transform the histogram into
    :return: Returns new TH1F histogram with transformed bins
    '''
    newHist = histogram.Clone("newHistogram")
    double_type_bins = array.array('d', new_bins) #This fixes an error concering the type of the bins
    newHist = newHist.Rebin(len(new_bins)-1, "newHistogram", double_type_bins)

    return newHist


def ratioPlot(mghist, pythiahist):
    ratioPlot = ROOT.TRatioPlot(mghist, pythiahist)
    ratioTempGraph = ratioPlot.GetLowerRefGraph()

    return ROOT.TGraphAsymmErrors(ratioTempGraph)


def ratioHistFill(ratioTempGraph, ratioHist, bins):
    '''
    :param ratioTempGraph: TRatioPlot
    :param ratioHist: TH1F with the expected format
    :param bins: Bins of the histogram
    :return: Fills a histogram with the ratio information
    '''
    for bin in range(bins[0], bins[-1]):
        x , y = 0., 0.
        ratioTempGraph.GetPoint(bin, x, y)
        ratioHist.SetBinContent(ratioHist.FindBin(x), y)


def error3D():
    return None


app = ROOT.TApplication("app",0,0)
masses = [1000, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mg_rootpath_base = "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV"
pythia_rootpath_base = "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/pythia-M-"
new_bins = [0,50,100,150,200,250,300,350,450,550,650,800,950,1150,1450,2800]
mgpath = mg_rootpath_base + "{}.root".format(masses[0])
pypath = pythia_rootpath_base + "{}.root".format(masses[0])
errorbar_ratioplot(masses[0], new_bins, mgpath, pypath, '')

### Plot all of the madgraph histograms ###
#for i in range(len(masses)):
#    all_histograms(masses[i], mg_rootpath_base+"{}.root".format(masses[i]), True, r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\log_weighted_pT_{}GeV.png".format(masses[i]))

### Plot the ratio plots ###
#for i in range(len(masses)):
#    savefig = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\MG_Pythia_ratio_{}GeV.png".format(masses[i])
#    save_errors = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\MG_Pythia_ratio_errors{}GeV.png".format(masses[i])
#    mgpath = mg_rootpath_base + "{}.root".format(masses[i])
#    pythiapath = pythia_rootpath_base + "{}.root".format(masses[i])
#    lower_errorbar, upper_errorbar, bins = errorbar_ratioplot(masses[i], mgpath, pythiapath, savefig=savefig)
#    plot_ratio_errors(lower_errorbar, upper_errorbar, bins, masses[i], savefig=save_errors)

### Plot the plus minus ratio errors ###
#mgpathes = []
#pythiapathes = []
#for i in range(len(masses)):
#    mgpathes.append(mg_rootpath_base + "{}.root".format(masses[i]))
#    pythiapathes.append(pythia_rootpath_base + "{}.root".format(masses[i]))
#errorbar_ratio_stackplot(masses, mgpathes, pythiapathes)