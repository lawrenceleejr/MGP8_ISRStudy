#! /usr/bin/env python

from builtins import range
import ROOT
import sys
import os
from DataFormats.FWLite import Events, Handle

#Take arguments from command line
#Put "root://cmsxrootd.fnal.gov//" before file name
#inputFiles = sys.argv[1]
#outputFile = sys.argv[2]

# Make VarParsing object
# https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideAboutPythonConfigFile#VarParsing_Example
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
print("input=",options.inputFiles)
#options.outputFile = '/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/outputFiles/'+sys.argv[2]
#outputFilename = sys.argv[3]
options.register ('outputFilename','',VarParsing.multiplicity.singleton, VarParsing.varType.string, "outputFilename")
print("input=",options.inputFiles)
options.register ('targetMass','',VarParsing.multiplicity.singleton, VarParsing.varType.int, "targetMass")
options.register('isAOD',False,VarParsing.multiplicity.singleton, VarParsing.varType.bool, "isAOD")
options.register('printEvery',10000,VarParsing.multiplicity.singleton, VarParsing.varType.int, "printEvery")
options.register('targetStatus',102, VarParsing.multiplicity.singleton, VarParsing.varType.int, "targetStatus")
options.maxEvents = -1
print("input=",options.inputFiles)
print("output=",options.outputFilename)
options.parseArguments()
print("input=",options.inputFiles)
outputFilename = options.outputFilename
print("output=",options.outputFilename)
targetMass = options.targetMass
#if !options.isAOD:
#   targetStatus = 23
#   targetStatus = 102
#else:
#    targetStatus = 22
targetStatus = options.targetStatus

outputFile = ROOT.TFile(options.outputFilename, 'RECREATE')

#debug user given arguments & interpretation
doPrint=False
print("input=",options.inputFiles)
print("output=",outputFile)
print(options.outputFilename, targetMass)


# Events takes either
# - single file name
# - list of file names
# - VarParsing options

# use Varparsing object
events = Events (options)

# -bash-4.2$ edmDumpEventContent ../sampleFiles/176F47D3-A514-454B-82D4-019163A330F9.root
# vector<reco::GenParticle>             "genParticles"              ""                "DIGI2RAW"



genparticleLabel = "prunedGenParticles"
if options.isAOD :
    genparticleLabel = "genParticles"
# create handle outside of loop
handles = {}
handles[genparticleLabel]  = Handle ("std::vector<reco::GenParticle>")

# for now, label is just a tuple of strings that is initialized just
# like and edm::InputTag



# Create histograms, etc.
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.gROOT.SetStyle('Plain') # white background
#myFile = ROOT.TFile.Open("/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/outputFiles/"+outputFilename+".root", "RECREATE")
c1 = ROOT.TCanvas('c1','')
pT = ROOT.TH1F('pTsum','Transverse Momentum of Di-gluino sytem',int(2800/50),0,2800)
pT1 = ROOT.TH1F('pT1','Transverse Momentum of Stop 1;x; Events',100,0,targetMass*1.5)
pT2 = ROOT.TH1F('pT2','Transverse Momentum of Stop 2;x; Events',100,0,targetMass*1.5)
pT1.GetXaxis().SetTitle('P_{T}(#tilde{t}1) [GeV]')
pT1.SetStats(False)
pT2.GetXaxis().SetTitle('P_{T}(#tilde{t}2) [GeV]')
pT2.SetStats(False)
pT.GetXaxis().SetTitle('P_{T} [GeV]')
pT.SetStats(False)
Phi1 = ROOT.TH1F('Phi1','Phi of Stop 1;x; Events',100,-1*ROOT.TMath.Pi(),ROOT.TMath.Pi())
Phi2 = ROOT.TH1F('Phi2','Phi of Stop 2;x; Events',100,-1*ROOT.TMath.Pi(),ROOT.TMath.Pi())
Phi1.GetXaxis().SetTitle('#phi(#tilde{t}1)')
Phi1.SetStats(False)
Phi2.GetXaxis().SetTitle('#phi(#tilde{t}2)')
Phi2.SetStats(False)
Eta1 = ROOT.TH1F('Eta1','Eta of Stop 1;x; Events',100,-5,5)
Eta2 = ROOT.TH1F('Eta2','Eta of Stop 2;x; Events',100,-5,5)
Eta1.GetXaxis().SetTitle('#eta(#tilde{t}1)')
Eta1.SetStats(False)
Eta2.GetXaxis().SetTitle('#eta(#tilde{t}2)')
Eta2.SetStats(False)
Mass1 = ROOT.TH1F('Mass1','Mass of Stop 1;x; Events',100,0,2500)
Mass2 = ROOT.TH1F('Mass2','Mass of Stop 2;x; Events',100,0,2500)
Mass1.GetXaxis().SetTitle('Mass(#tilde{t}1) [GeV]')
Mass1.SetStats(False)
Mass2.GetXaxis().SetTitle('Mass(#tilde{t}2) [GeV]')
Mass2.SetStats(False)
#myFile = ROOT.TFile.Open(outputFile+".root", "RECREATE")

#LACEY - Need to print single event somewhere in here
filteredCount = 0
#set to -1 for all events
# loop over events
for ievent,event in enumerate(events):
    if ievent == 0:
        print("Running...")
	# *** Lacey debug START
	'''print(event)
	break
    print("This should not print")'''
    # Lacey debug END ***
    if ievent%options.printEvery==0 and options.printEvery > 0:
        doPrint = True
    else:
        doPrint = False
    # use getByLabel, just like in cmsRun
    event.getByLabel (genparticleLabel, handles[genparticleLabel])

    # get the product
    genparticles = handles[genparticleLabel].product()

    if doPrint:
        print ("------------------Event", ievent)
    gluinop4list = []
    for igenpart,genpart in enumerate(genparticles):
        status = genpart.status()
        pdgid = genpart.pdgId()
	
        mass = -1
        if options.isAOD:
            mass = genpart.mass()
        else:
            mass = genpart.mass()
        if abs(pdgid)!=1000021:
            continue
        #if doPrint:
		#print(status, pdgid)
	if status != targetStatus:
            continue
        if abs(targetMass-mass) >= targetMass*0.1:
            filteredCount += 1
            continue
        gluinop4list.append(genpart.p4())
    if len(gluinop4list) == 2:
	#print(type(gluinop4list[0]), gluinop4list[0], gluinop4list[1])
	pT.Fill((gluinop4list[0] + gluinop4list[1]).Pt())
	#print('Di-gluino pt', test)
        pT1.Fill(gluinop4list[0].Pt())
        pT2.Fill(gluinop4list[1].Pt())
        Phi1.Fill(gluinop4list[0].Phi())
        Phi2.Fill(gluinop4list[1].Phi())
        Eta1.Fill(gluinop4list[0].Eta())
        Eta2.Fill(gluinop4list[1].Eta())
        Mass1.Fill(gluinop4list[0].M())
        Mass2.Fill(gluinop4list[1].M())
        if doPrint:
            print(gluinop4list[0].M(), gluinop4list[1].M())
            print(gluinop4list[0].E(), gluinop4list[1].E())
            print(gluinop4list[0].Pt(),gluinop4list[1].Pt())
    else:
        if doPrint:
            print("List is empty.")
    

#output_path = os.path.expanduser("/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/HistogramPDFs/"+outputFilename+'_LowGeV'+".pdf")
#c1.SaveAs(output_path)
#output_path = os.path.expanduser("/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/HistogramPDFs/"+outputFilename+'_HighGeV'+".pdf")
#c1.SaveAs(output_path)
#myFile.WriteObject(h1, "LowGeV")
#myFile.WriteObject(h2, "HighGeV")
outputFile.Write()
outputFile.Close()
#myFile.Write()
#myFile.Close()
#myFile = ROOT.TFile.Open("/afs/cern.ch/user/t/twolfe/MGP8_ISRStudy/outputFiles/"+outputFilename+".root")
print("\n\nEND")


'''NOTE: This was directly copied from alexandersize/MGP8_ISRStudy_LAdev/truth.py on 04/02/24
In theory, this should be how to run the Pythia samples (needs to be integrated with other version and made nicer)
'''
