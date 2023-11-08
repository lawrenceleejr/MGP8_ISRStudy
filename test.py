from ROOT import TFile, TH1F
import numpy as np
import array

path = "/Users/colbythompson/PycharmProjects/MGP8_ISRStudy_LAdev/output-files/gluglu_MGn50_GeV1000.root"
bins = [0,50,100,150]
mg = TFile.Open(path)
mghist = mg.Get("pTsum 0;1")
