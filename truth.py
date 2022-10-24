#! /usr/bin/env python

from builtins import range
import ROOT
import sys
from DataFormats.FWLite import Events, Handle

# Make VarParsing object
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideAboutPythonConfigFile#VarParsing_Example
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.parseArguments()

# Events takes either
# - single file name
# - list of file names
# - VarParsing options

# use Varparsing object
events = Events ("/afs/cern.ch/user/l/leejr/work/public/ISRStudy/sampleFiles/176F47D3-A514-454B-82D4-019163A330F9.root")


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

# loop over events
for ievent,event in enumerate(events):
    # use getByLabel, just like in cmsRun
    for label in labels:
        event.getByLabel (label, handles[label])

    # get the product
    genparticles = handles["genParticles"].product()

    if ievent%1==0:
        print ("------------------Event", ievent)
    for igenpart,genpart in enumerate(genparticles):
        status = genpart.status()
        pdgid = genpart.pdgId()
        if abs(pdgid)!=1000021:
            continue
        print(status, pdgid)
