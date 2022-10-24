#! /usr/bin/env python3

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
# events = Events ("../bigtest/TOP-RunIISummer20UL18wmLHEGEN-00003.root")
# events = Events ("../bigtest/pickevents_SIM.root")
events = Events ("../bigtest/pickevents_electrons_SIM.root")
# events = Events ("../bigtest/pickevents_status2decay_SIM.root")
# events = Events (sys.argv[1])
isSim = True
# isSim = False




# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsPixelBarrelHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsPixelBarrelLowTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsPixelEndcapHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsPixelEndcapLowTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTECHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTECLowTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTIBHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTIBLowTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTIDHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTIDLowTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTOBHighTof"   "SIM"
# vector<PSimHit>                       "g4SimHits"                 "TrackerHitsTOBLowTof"   "SIM"

print(events)
print(dir(events))
# print(events.fileIndex())
# for event in events:
#     print(event)
#     print(dir(event))


# create handle outside of loop
handles = {}
handles["genParticles"]  = Handle ("std::vector<reco::GenParticle>")
# handles[]

handles["g4SimHits" ] = Handle("vector<SimTrack>")
handles["TrackerHitsPixelBarrelHighTof" ] = Handle("vector<PSimHit>")
# handles["TrackerHitsPixelBarrelLowTof" ]  = Handle("std::vector<PSimHit>")
# handles["TrackerHitsPixelEndcapHighTof" ] = Handle("std::vector<PSimHit>")
# handles["TrackerHitsPixelEndcapLowTof" ]  = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTECHighTof" ]         = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTECLowTof" ]          = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTIBHighTof" ]         = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTIBLowTof" ]          = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTIDHighTof" ]         = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTIDLowTof" ]          = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTOBHighTof" ]         = Handle("std::vector<PSimHit>")
# handles["TrackerHitsTOBLowTof" ]          = Handle("std::vector<PSimHit>")



# for now, label is just a tuple of strings that is initialized just
# like and edm::InputTag
labels = ["genParticles",
    # "g4SimHits",
    # "TrackerHitsPixelBarrelLowTof" ,
    ]
# labels = ("genParticles")

# Create histograms, etc.
ROOT.gROOT.SetBatch()        # don't pop up canvases
ROOT.gROOT.SetStyle('Plain') # white background
zmassHist = ROOT.TH1F ("zmass", "Z Candidate Mass", 50, 20, 220)


def printKidInfo(part, prefix="", printMomentum=False):
    for ikid in range(part.numberOfDaughters()):
        print("%s Child >>> pdgid: %d, status %d, index %d, R %f" % (prefix, part.daughter(ikid).pdgId(), part.daughter(ikid).status(), part.daughterRef(ikid).index()+1, part.daughter(ikid).vertex().R() ) )
        if printMomentum:
            print("%s Child momentum >>> %.20f %.20f %.20f" % (prefix, part.daughter(ikid).pt(), part.daughter(ikid).eta(), part.daughter(ikid).phi() ) )
        # print(" >>> ")
        printKidInfo(part.daughter(ikid), prefix+" ... ",printMomentum)


listOfInterestingEvents = []

counterForBadEvents = 0

# loop over events
for ievent,event in enumerate(events):
    # print("Event %d"%ievent)
    # continue
    # use getByLabel, just like in cmsRun
    for label in labels:
        event.getByLabel (label, handles[label])
    # event.getByLabel (label, handles["genParticles"])
    # get the product
    genparticles = handles["genParticles"].product()
    # print(genparticles)

    if ievent%100==0:
        print ("Event", ievent)
    # if ievent>200000:
    #     break
    if ievent!=40:
        continue
    for igenpart,genpart in enumerate(genparticles):
        # print(type(genpart.vertex()))
        # print((genpart.vertex().R()))
        # print((genpart.vertex().Rho()))
        # sys.exit()
        status = genpart.status()
        r = genpart.vertex().R()
        # if r<2.9:
        #     continue
        if abs(genpart.pdgId())!=11:
            continue
        if status>3:
            # print("got one")
        # if status==91:
            # print(dir(genpart))

            # hasStatus1Kid = False
            # for ikid in range(genpart.numberOfDaughters()):
            #     if genpart.daughter(ikid).status()==1:
            #         hasStatus1Kid = True
            #         break
            # if hasStatus1Kid == False:
            #     continue

            # hasStatus2Parent = False
            # for ikid in range(genpart.numberOfMothers()):
            #     if genpart.mother(ikid).status()==2:
            #         hasStatus2Parent = True
            #         break
            # if hasStatus2Parent == False:
            #     continue



            print("----------------------------------------------------------------------")
            print("")
            print ("Event", ievent)
            print("Status %d... Index %d"%(status,igenpart+1) )
            print("")
            listOfInterestingEvents.append(ievent)

            # print(dir(genpart) )
            # print(dir(genpart.daughterRef(0)) )
            # print((genpart.daughterRef(0).index() ) )
            # sys.exit()

            print("PDGID: %d"%genpart.pdgId() )
            print("R: %f"%genpart.vertex().R() )
            print("Status: %d"%genpart.status() )
            print("pt eta phi:", genpart.pt(), genpart.eta(), genpart.phi() )
            print("n children: %d"%genpart.numberOfDaughters() )

            for ikid in range(genpart.numberOfMothers()):
                # print("Parent >>>", genpart.mother(ikid).pdgId(), genpart.mother(ikid).status(), genpart.motherRef(ikid).index() )
                print("%s Parent >>> pdgid: %d, status %d, index %d" % ("", genpart.mother(ikid).pdgId(), genpart.mother(ikid).status(), genpart.motherRef(ikid).index()+1 ) )
                print("%s Parent momentum >>> %.20f %.20f %.20f" % ("", genpart.mother(ikid).pt(), genpart.mother(ikid).eta(), genpart.mother(ikid).phi() ) )


            printKidInfo(genpart,"",True)
            # for ikid in range(genpart.numberOfDaughters()):
            #     print("Child >>>", genpart.daughter(ikid).pdgId(), genpart.daughter(ikid).status(), genpart.daughterRef(ikid).index() )
            # print(genpart.numberOfDaughters() )


            if not isSim:
                continue

            print("grabbing g4track collection and checking for nearby g4tracks")

            event.getByLabel ("g4SimHits", "", handles["g4SimHits"])
            simhits = handles["g4SimHits"].product()

            # event.getByLabel ("g4SimHits", "TrackerHitsPixelBarrelHighTof", handles["TrackerHitsPixelBarrelHighTof"])
            # simhits = handles["TrackerHitsPixelBarrelHighTof"].product()

            pdgIdList = []

            for simhit in simhits:
                # print(dir(simhit))
                # print(simhit.trackId())
                # sys.exit()
                # sys.exit()
                # print(simhit.genpartIndex())

                # tlv1 = ROOT.TLorentzVector()
                # tlv2 = ROOT.TLorentzVector()
                # tlv1.SetPtEtaPhiM(simhit.momentum().Pt(), simhit.momentum().Eta(), simhit.momentum().Phi(), simhit.momentum().M())
                # # print(dir(genpart))
                # tlv2.SetPtEtaPhiM(genpart.pt(), genpart.eta(), genpart.phi(), genpart.mass())
                # if tlv1.DeltaR(tlv2)<0.05:
                #     print(simhit.trackId(), simhit.genpartIndex(),genparticles[simhit.genpartIndex()-1].pdgId(), simhit.momentum().Pt(), simhit.momentum().Eta(),simhit.momentum().Phi() )
                try:
                    if 0.95<genpart.pt()/simhit.momentum().Pt()<1.05 and 0.95<genpart.eta()/simhit.momentum().Eta()<1.05 and 0.95<genpart.phi()/simhit.momentum().Phi()<1.05:
                        print(simhit.trackId(), simhit.genpartIndex(),genparticles[simhit.genpartIndex()-1].pdgId(), simhit.momentum().Pt(), simhit.momentum().Eta(),simhit.momentum().Phi() )
                        pdgIdList.append( genparticles[simhit.genpartIndex()-1].pdgId() )
                    # printKidInfo(genpart,"", False)
                except:
                    continue
                # if igenpart+1==simhit.genpartIndex():
                #     print("Match!!!")
                #     print("gen particle pt eta phi:", genpart.pt(), genpart.eta(), genpart.phi() )
                #     printKidInfo(genpart,"", True)
                    # sys.exit()
                # print(simhit.genpartIndex())
                # print(dir(simhit))
                # sys.exit()
            # sys.exit()
            if pdgIdList.count(genpart.pdgId()) > 1:
                print("I found the same PDGID twice with similar momentum!!!!!!!!!!!!!!!!!!!!!")
                counterForBadEvents+=1
                if counterForBadEvents>1:
                    sys.exit()


print("Number of bad events here:")
print (counterForBadEvents)

    # use muons to make Z peak
    # numMuons = len (muons)
    # print(numMuons)

if not isSim:

    listOfInterestingEvents = set(listOfInterestingEvents)

    print("Potentially interesting events...")
    print(listOfInterestingEvents)
    print("Offsetting these by 1")
    print([x+1 for x in listOfInterestingEvents])

    print("")
    print("Formatting for skimmer")
    print( ",".join(["1:1:%d"%(x+1) for x in listOfInterestingEvents]) )

sys.exit()