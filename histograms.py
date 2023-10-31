from matplotlib import pyplot as plt
import numpy as np
import uproot
import sys


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

def errorbar_ratioplot(mass, mgpath, pythiapath, double_bin_wth=False, savefig=None):
    '''
    :param mass: Gluino mass (GeV)
    :param mgpath: Path to the madgraph root file
    :param pythiapath: Path to the pythia root file
    :param double_bin_wth: If True, doubles the width of the bins
    :param savefig: Filepath to save the histogram, does not save by default
    :return: Minus Errorbars, Plus Errorbars
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
                bin_width = 2800/n
                normalized_frequency = arr[0]/(sum(arr[0])*bin_width)

                if key == 'pTsum 1;1': #Save this for use in the errorbar plot
                    zeroth = normalized_frequency

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
    zeroth_ratio, _ = get_ratio(zeroth, mgbins, pythiapath, double_bin_wth)
    upper_errorbar = maxratio - zeroth_ratio
    lower_errorbar = zeroth_ratio - minratio

    #Create the plot
    try:
        plt.errorbar(bins, zeroth_ratio, (lower_errorbar, upper_errorbar), fmt='+', capsize=capsize, color='dodgerblue')
    except ValueError:
        bins = bins[:-1]
        plt.errorbar(bins, zeroth_ratio, (lower_errorbar, upper_errorbar), fmt='+', capsize=capsize, color='dodgerblue')
    plt.suptitle('MG/Pythia, Gluino Target Mass = {} GeV'.format(mass))
    plt.xlabel('gluglu pT (GeV)')
    plt.xlim(0, 2800)
    plt.ylim(0,7)
    plt.ylabel('MG/Pythia')
    if savefig!=None:
        plt.savefig(savefig)
    else:
        plt.show()

    return lower_errorbar, upper_errorbar, bins

def errorbar_ratio_stackplot(masses, mgpathes, pythiapathes, double_bin_wth=False, savefig=None):
    '''
    :param mass: List of Gluino masses (GeV)
    :param mgpath: List of madgraph root paths
    :param pythiapath: List of the pythia root paths
    :param double_bin_wth: If True, doubles the width of the bins
    :param savefig: Filepath to save the histogram, does not save by default
    :return: gluglu pT Errorbar ratio stackplot
    '''
    for i in range(len(masses)):
        with uproot.open(mgpathes[i]) as root:
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
                    bin_width = 2800/n
                    normalized_frequency = arr[0]/(sum(arr[0])*bin_width)

                    if key == 'pTsum 1;1': #Save this for use in the errorbar plot
                        zeroth = normalized_frequency

                    #Double the bin widths if necessary
                    if double_bin_wth:
                        normalized_frequency, mgbins = double_bin_width(normalized_frequency, arr[1])
                        capsize=5
                    else:
                        mgbins = arr[1]
                        capsize=3

                    for j in range(len(mins)):
                        if normalized_frequency[j] < mins[j]:
                            mins[j] = normalized_frequency[j]
                        if normalized_frequency[j] > maxes[j]:
                            maxes[j] = normalized_frequency[j]

        #Get the min/max ratios
        minratio, bins = get_ratio(mins, mgbins, pythiapathes[i], double_bin_wth)
        maxratio, _ = get_ratio(maxes, mgbins, pythiapathes[i], double_bin_wth)
        zeroth_ratio, _ = get_ratio(zeroth, mgbins, pythiapathes[i], double_bin_wth)
        upper_errorbar = maxratio - zeroth_ratio
        lower_errorbar = zeroth_ratio - minratio

        #Create the plot
        try:
            plt.errorbar(bins, zeroth_ratio, (lower_errorbar, upper_errorbar), alpha=0.8, fmt='+', capsize=capsize, label='Glu Mass = {} GeV'.format(masses[i]))
        except ValueError:
            bins = bins[:-1]
            plt.errorbar(bins, zeroth_ratio, (lower_errorbar, upper_errorbar), alpha=0.8, fmt='+', capsize=capsize, label='Glu Mass = {} GeV'.format(masses[i]))

    plt.suptitle('MG/Pythia Errorbars')
    plt.xlabel('gluglu pT (GeV)')
    plt.xlim(0, 2800)
    plt.ylim(0,7)
    plt.ylabel('MG/Pythia')
    plt.legend()
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
        bin_width=50
        if double_bin_wth:
            bin_width=100
        pythia_data = pythia[0]/(sum(pythia[0])*bin_width)
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


def plot_ratio_errors(lower_errorbars, upper_errorbars, bins, mass, savefig=None):
    '''
    :param lower_errorbars: Array of lower errorbars
    :param upper_errorbars: Array of upper errorbars
    :param bins: X axis
    :param mass: Target mass of the gluino
    :param savefig: Path to save the plot
    :return: Plot of errorbars
    '''
    plt.clf() #Clear existing plots
    plt.scatter(bins, upper_errorbars, label='Upper error bar', marker='.')
    plt.scatter(bins, lower_errorbars, label='Lower error bar', marker='.')
    plt.suptitle('Upper and Lower MG/Pythia error bars, gluino target mass = {} GeV'.format(mass))
    plt.ylabel('Magnitude of error bar')
    plt.xlabel('gluglu pT (GeV)')
    plt.xlim(0,2800)
    plt.ylim(0,2)
    plt.legend()
    if savefig != None:
        plt.savefig(savefig)
    else:
        plt.show()


masses = [1000, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mg_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\gluglu_MGn50_GeV"
pythia_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\PYgluino_50gev-bin_M-"

#for i in range(len(masses)):
#    all_histograms(masses[i], mg_rootpath_base+"{}.root".format(masses[i]), True, r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\log_weighted_pT_{}GeV.png".format(masses[i]))

for i in range(len(masses)):
    savefig = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\MG_Pythia_ratio_{}GeV.png".format(masses[i])
    save_errors = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\histograms\MG_Pythia_ratio_errors{}GeV.png".format(masses[i])
    mgpath = mg_rootpath_base + "{}.root".format(masses[i])
    pythiapath = pythia_rootpath_base + "{}.root".format(masses[i])
    lower_errorbar, upper_errorbar, bins = errorbar_ratioplot(masses[i], mgpath, pythiapath, savefig=savefig)
    plot_ratio_errors(lower_errorbar, upper_errorbar, bins, masses[i], savefig=save_errors)

#mgpathes = []
#pythiapathes = []
#for i in range(len(masses)):
#    mgpathes.append(mg_rootpath_base + "{}.root".format(masses[i]))
#    pythiapathes.append(pythia_rootpath_base + "{}.root".format(masses[i]))
#errorbar_ratio_stackplot(masses, mgpathes, pythiapathes)