from matplotlib import pyplot as plt
import numpy as np
import uproot


def midpoint_binning(array):
    '''
    :param array: Array of bins you would like to midpoint
    :return: Transformed array of length n-1 that locates the midpoints between the array. For example [0,10,20] -> [5,15]
    '''
    difference = array[1] - array[0]
    length = len(array)
    transformed = []
    i = 0
    while i < length-1:
        transformed.append(difference/2 + difference*i)
        i+=1

    return transformed

def prepare_array_for_hist(frequency, bins):
    '''
    :param frequency: The array that contains the frequency data (y axis values on hist)
    :param bins: The array that contains the bins (x axis on hist)
    :return: Converts the frequency array to a form better suited for histograms
    '''
    arr = np.array([])
    for i in range(len(frequency)):
        arr = np.concatenate((arr, np.repeat(bins[i], frequency[i])))

    return arr


def all_histograms(mass, rootpath, directorypath):
    '''
    :param mass: Mass of the root file
    :param rootpath: Path to the root file
    :param directorypath: Path to the directory to store histograms
    :return: Saves all histograms to the directory
    '''
    with uproot.open(rootpath) as root:
        for key in root.keys():
            plt.clf()
            if 'pTsum' in key:
                arr = root[key].to_numpy()
                frequency = prepare_array_for_hist(arr[0], arr[1])
                plt.hist(frequency, arr[1], color='dodgerblue')
                plt.suptitle('Weighted Histogram {} Mass = {} GeV'.format(key, mass))
                plt.ylabel('Frequency')
                plt.xlabel('gluglu pT (GeV)')
                path = directorypath + '/{}.png'.format(key)
                plt.savefig(path)

def errorbar_ratioplot(mass, mgpath, pythiapath, savefig=None):
    '''
    :param mass: Gluino mass (GeV)
    :param mgpath: Path to the madgraph root file
    :param pythiapath: Path to the pythia root file
    :param savefig: Filepath to save the histogram, does not save by default
    :return: gluglu pT Errorbar ratio plot
    '''
    plt.clf() #Clear existing plots
    with uproot.open(mgpath) as root:
        mins = np.repeat(100000, 56)
        maxes = np.zeros(56)
        for key in root.keys():
            if 'pTsum' in key:
                if key == 'pTsum 0;1':
                    #Get the ratio
                    with uproot.open(pythiapath) as pythiaroot:
                        ratio, bins = get_ratio(root, pythiaroot)
                else:
                    #Get the madgraph errorbars
                    arr = root[key].to_numpy()
                    for i in range(len(mins)):
                        if arr[0][i] < mins[i]:
                            mins[i] = arr[0][i]
                        if arr[0][i] > maxes[i]:
                            maxes[i] = arr[0][i]

    #Get the ratio errorbars
    ratio_errors = get_ratio_errorbars(mins, maxes, ratio)

    #Create the plot
    bins = bins[:-1]
    plt.errorbar(bins, ratio, ratio_errors, ls='none', capsize=5)
    plt.suptitle('Weighted Frequency Range, Gluino Target Mass = {} GeV'.format(mass))
    plt.xlabel('gluglu pT (GeV)')
    plt.ylabel('Frequency')
    if savefig!=None:
        plt.savefig(savefig)
    else:
        plt.show()


def get_ratio(mgroot, pythiaroot):
    '''
    :param mg: Array of the madgraph values
    :param pythia: Array of the pythia values
    :return: Min/Max ratios and the histogram bins
    '''
    mg = mgroot['pTsum 0;1'].to_numpy()
    pythia = pythiaroot['pTsum;1'].to_numpy()
    ratio = np.array([])
    for i in range(len(mg[0])):
        try:
            ratio = np.append(ratio, mg[0][i]/pythia[0][i])
        except IndexError:
            bins = pythia[1]
            return ratio, bins

    bins = mg[1]
    return ratio, bins


def get_ratio_errorbars(mins, maxes, ratio):
    '''
    :param mins: Array of minimum madgraph values
    :param maxes: Array of maximum madgraph values
    :param ratio: Array of madgraph/pythia ratios
    :return: Ratio errorbars
    '''
    mg_sigma = (maxes - mins) / 2
    mids = mins + mg_sigma
    relative_uncertainty = mg_sigma/mids
    try:
        ratio_error = relative_uncertainty * ratio
    except ValueError:
        #Fix shape difference by reducing larger array
        length_difference = abs(len(relative_uncertainty) - len(ratio))
        if len(relative_uncertainty) < len(ratio):
            ratio = ratio[:-length_difference]
        else:
            relative_uncertainty = relative_uncertainty[:-length_difference]
        ratio_error = relative_uncertainty * ratio

    return ratio_error


masses = [1000, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
mg_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\gluglu_MGn50_GeV"
pythia_rootpath_base = r"C:\Users\Colby\PycharmProjects\MGP8_ISRStudy_LAdev\output-files\PYgluino_50gev-bin_M-"

for i in range(len(masses)):
    mgpath = mg_rootpath_base + "{}.root".format(masses[i])
    pythiapath = pythia_rootpath_base + "{}.root".format(masses[i])
    errorbar_ratioplot(masses[i], mgpath, pythiapath)