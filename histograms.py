from matplotlib import pyplot as plt
import numpy as np
import uproot
import sys


def all_histograms(mass, mgpath, savefig=None):
    '''
    :param mass: Mass of the root file
    :param mgpath: Path to the root file
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
                normalized_frequency = arr[0]/sum(arr[0])
                plt.plot(arr[1][:-1], normalized_frequency, color='dodgerblue')
        plt.suptitle('Weighted pT, Gluino Target Mass = {} GeV'.format(mass))
        plt.ylabel('Normalized Frequency')
        plt.xlabel('gluglu pT (GeV)')
        if savefig != None:
            plt.savefig(savefig)
        else:
            plt.show()

def errorbar_ratioplot(mass, mgpath, pythiapath, double_bin_wth=False, savefig=None):
    '''
    :param mass: Gluino mass (GeV)
    :param mgpath: Path to the madgraph root file
    :param pythiapath: Path to the pythia root file
    :param double_bin_wth: If True, doubles the width of the bins
    :param savefig: Filepath to save the histogram, does not save by default
    :return: gluglu pT Errorbar ratio plot
    '''
    plt.clf() #Clear existing plots
    with uproot.open(mgpath) as root:
        if double_bin_wth:
            n=28
        else:
            n=56
        mins = np.repeat(100000.0, n)
        maxes = np.zeros(n)
        for key in root.keys():
            if 'pTsum' in key:
                if key == 'pTsum 0;1':
                    continue
                #Get the madgraph errorbars
                arr = root[key].to_numpy()
                normalized_frequency = arr[0]/sum(arr[0])

                #Double the bin widths if necessary
                if double_bin_wth:
                    normalized_frequency, mgbins = double_bin_width(normalized_frequency, arr[1])
                    capsize=5
                else:
                    mgbins = arr[1]
                    capsize=3

                for i in range(len(mins)):
                    if normalized_frequency[i] < mins[i]:
                        mins[i] = normalized_frequency[i]
                    if normalized_frequency[i] > maxes[i]:
                        maxes[i] = normalized_frequency[i]

    #Get the min/max ratios
    minratio, bins = get_ratio(mins, mgbins, pythiapath, double_bin_wth)
    maxratio, _ = get_ratio(maxes, mgbins, pythiapath, double_bin_wth)
    diff = (maxratio-minratio)/2
    midratio = diff + minratio

    #Create the plot
    try:
        plt.errorbar(bins, midratio, diff, ls='none', capsize=capsize, color='dodgerblue')
    except ValueError:
        bins = bins[:-1]
        plt.errorbar(bins, midratio, diff, ls='none', capsize=capsize, color='dodgerblue')
    plt.suptitle('MG/Pythia, Gluino Target Mass = {} GeV'.format(mass))
    plt.xlabel('gluglu pT (GeV)')
    plt.ylabel('MG/Pythia')
    if savefig!=None:
        plt.savefig(savefig)
    else:
        plt.show()


def get_ratio(mg_normalized_frequency, mg_bins, pythiaroot, double_bin_wth=False):
    '''
    :param mg_normalized_frequency: Array of the madgraph normalized values
    :param mg_bins: Array of bins from the MG data
    :param pythiaroot: Path to pythia root file
    :param double_bin_wth: If true, doubles the bin widths
    :return: Ratio array and bins
    '''
    with uproot.open(pythiaroot) as pyroot:
        pythia = pyroot['pTsum;1'].to_numpy()
        pythia_data = pythia[0]/sum(pythia[0])
        pybins = pythia[1]

    if double_bin_wth:
        pythia_data, pybins = double_bin_width(pythia_data, pythia[1])

    ratio = np.array([])
    for i in range(len(mg_normalized_frequency)):
        try:
            ratio = np.append(ratio, mg_normalized_frequency[i]/pythia_data[i])
        except IndexError:
            return ratio, pybins

    bins = mg_bins
    return ratio, bins


def double_bin_width(data, bins):
    '''
    :param data: Array of frequencies
    :param bins: Array of bins
    :return: New data and bins (with double bin width)
    '''
    bin_difference = 2*(bins[1]-bins[0])
    new_data = []
    new_bins = []
    i = 0
    while i <= len(bins):
        try:
            new_data.append(data[i] + data[i+1])
            new_bins.append((i/2) * bin_difference)
            i+=2
        except IndexError:
            break

    return np.array(new_data), np.array(new_bins)




masses = [1000, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mg_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\gluglu_MGn50_GeV"
pythia_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\PYgluino_50gev-bin_M-"

#for i in range(len(masses)):
#    all_histograms(masses[i], mg_rootpath_base+"{}.root".format(masses[i]), r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\weighted_pT_{}GeV.png".format(masses[i]))

for i in range(len(masses)):
    mgpath = mg_rootpath_base + "{}.root".format(masses[i])
    pythiapath = pythia_rootpath_base + "{}.root".format(masses[i])
    errorbar_ratioplot(masses[i], mgpath, pythiapath, True, r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\MG_Pythia_ratio_doublewidth{}GeV.png".format(masses[i]))