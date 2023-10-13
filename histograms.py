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

rootpath = r"C:\Users\Colby\Box Sync\Larry work\h_gluglu_pT histograms\h_gluglu_MGn50_1000GeV.root"
with uproot.open(rootpath) as root:
    #print(root['pTsum {};1'].keys())
    print(root.classnames())
    arr = root['pTsum {};1'].to_numpy()
    #bins = transform_array_to_midpoint_array(arr[1])
    #plt.hist(bins, weights=arr[0], color="dodgerblue", alpha=0.8, edgecolor='black', histtype="stepfilled")
    #plt.suptitle("Weighted MadGraph Samples, n=50, targetMass=1000GeV")
    #plt.xlabel("H -> GluinoGluino pT (GeV)")
    #plt.ylabel("Frequency (log scale)")
    #plt.yscale("log")
    #plt.show()

