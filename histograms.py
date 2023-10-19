from matplotlib import pyplot as plt
import numpy as np
import uproot


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

def weighted_sum_histograms(masses, rootpaths, log=False, savefig=None):
    '''
    :param mass: List of root file masses
    :param rootpath: List of paths to the root files
    :param log: If True, transforms the yscale of the histogram to log scale
    :param savefig: Filepath to save the histogram, does not save by default
    :return: Histogram of the weighted gluglu pT sums
    '''
    for i in range(len(masses)):
        with uproot.open(rootpaths[i]) as root:
            final_arr = np.zeros(56)
            for key in root.keys():
                if 'pTsum' in key:
                    arr = root[key].to_numpy()
                    final_arr += arr[0]

            bins = arr[1]
            frequency = prepare_array_for_hist(final_arr, bins)
            plt.hist(frequency, bins, histtype=u'step', label="Glu Mass {} GeV".format(masses[i]))

    plt.suptitle("Sum of Weighted Histograms for Various Gluino Masses")
    plt.xlabel("gluglu pT (GeV)")
    plt.legend()
    if log:
        plt.ylabel("Frequency (log)")
        plt.yscale('log')
    else:
        plt.ylabel("Frequency")
    if savefig!=None:
        plt.savefig(savefig)
    else:
        plt.show()

masses = [1400, 1600, 1800, 2000, 2200, 2400]
rootpaths = ["/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV1400.root",
             "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV1600.root",
             "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV1800.root",
             "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV2000.root",
             "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV2200.root",
             "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV2400.root"]
weighted_sum_histograms(masses, rootpaths, True, savefig="/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/histograms/weightedHistSumLog.png")