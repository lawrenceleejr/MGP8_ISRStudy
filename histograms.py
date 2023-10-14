from matplotlib import pyplot as plt
import numpy as np
import uproot

def transform_array_to_midpoint_array(arr):
    l = arr.tolist()
    new_arr = []
    for i in range(len(l)):
        try:
            new_arr.insert(i, (l[i] + l[i+1])/2)
        except IndexError:
            break

    return new_arr

def gluglu_pT_range_plot(rootfilepath, mass, savefig=None):
    with uproot.open(rootfilepath) as root:
        maxes = np.zeros(56)
        mins = np.full(56, 100000000)
        bins = []
        for key in root.keys():
            if 'pTsum' in key:
                arr = root[key].to_numpy()
                for i in range(len(arr[0])):
                    if arr[0][i] > maxes[i]:
                        maxes[i] = arr[0][i]
                    if arr[0][i] < mins[i]:
                        mins[i] = arr[0][i]
                bins = transform_array_to_midpoint_array(arr[1])
        mids = []
        for i in range(len(maxes)):
            mids.append(maxes[i]-mins[i])

        plt.plot(bins, mids)
        plt.fill_between(bins, mins, maxes, alpha=0.5, color='dodgerblue')
        plt.suptitle("Min/Max {} GeV".format(mass))
        plt.xlabel("gluglu pT (GeV)")
        plt.ylabel("Weighted Frequency")

        if savefig!=None:
            plt.savefig(savefig)
        else:
            plt.show()

rootpath = r"C:\Users\Colby\Box Sync\Larry work\gluglu_pT histograms\test.root"
gluglu_pT_range_plot(rootpath, 1000)