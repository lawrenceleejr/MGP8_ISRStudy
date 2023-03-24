#! /usr/bin/env python

from builtins import range
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

#Take arguments from command line
#Put "root://cmsxrootd.fnal.gov//" before file name
#inputFiles = sys.argv[1]
#outputFile = sys.argv[2]

# Make VarParsing object
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideAboutPythonConfigFile#VarParsing_Example
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.parseArguments()
options.outputFile = '/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/outputFiles/'+sys.argv[2]
outputFilename = sys.argv[2].replace('outputFile=','')

# Events takes either
# - single file name
# - list of file names
# - VarParsing options

# use Varparsing object
#events = Events ("root://cmsxrootd.fnal.gov//" + inputFiles)
events = Events (options)

# -bash-4.2$ edmDumpEventContent ../sampleFiles/176F47D3-A514-454B-82D4-019163A330F9.root
# vector<reco::GenParticle>             "genParticles"              ""                "DIGI2RAW"

print(events)

# create handle outside of loop
handles = {}
handles["genParticles"]  = Handle ("std::vector<reco::GenParticle>")

# for now, label is just a tuple of strings that is initialized just
# like and edm::InputTag
labels = ["genParticles"]


# Create histograms, etc.
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.gROOT.SetStyle('Plain') # white background
c1 = ROOT.TCanvas('c1','Transverse Momentum')
bins = 55
xmin = 0
xmax = 1e-04
h1 = ROOT.TH1F('h1','Transverse Momentum of the Digluino System;x; Events',bins,xmin,xmax)
h1.GetXaxis().SetTitle('P_{T}(#tilde{g}#tilde{g}) [GeV]')
h1.SetStats(False)
#myFile = ROOT.TFile.Open(outputFile+".root", "RECREATE")
myFile = ROOT.TFile.Open(outputFilename+".root", "RECREATE")
# loop over events
for ievent,event in enumerate(events):
    # use getByLabel, just like in cmsRun
    for label in labels:
        event.getByLabel (label, handles[label])

    # get the product
    genparticles = handles["genParticles"].product()

    if ievent%1==0:
        print ("------------------Event", ievent)
    gluinop4list = []
    for igenpart,genpart in enumerate(genparticles):
        status = genpart.status()
        pdgid = genpart.pdgId()
        if abs(pdgid)!=1000021:
            continue
        if status !=23:
            continue
        print(status, pdgid)
        gluinop4list.append(genpart.p4())
    gluglu = gluinop4list[0]+gluinop4list[1]
    h1.Fill(gluglu.Pt())
    print(gluinop4list[0].E(), gluinop4list[1].E())
h1.Draw()
myFile.WriteObject(h1, "MyObject")
myFile = ROOT.TFile.Open(outputFilename+".root")
c1.SaveAs(outputFilename+".pdf")