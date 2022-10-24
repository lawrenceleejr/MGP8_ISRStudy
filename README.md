# MGP8_ISRStudy



* example MadGraph samples
	* https://cmsweb.cern.ch/das/request?instance=prod/global&input=file+dataset%3D%2FSMS-T1btbt-LLC1_ctau10to200-mGluino-1000to2800-mLSP0to2800_TuneCP2_13TeV-madgraphMLM-pythia8%2FRunIIFall17FSPremix-GridpackScan_94X_mc2017_realistic_v15-v1%2FAODSIM
* Our Pythia samples
	* https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FHSCP*%2FRunIISummer20UL18RECO-106X*%2FAODSIM


```
f = ROOT.TFile.Open("root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18RECO/HSCPgluino_M-1000_TuneCP5_13TeV-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/80000/176F47D3-A514-454B-82D4-019163A330F9.root")
```



Instructions for setting up CMSSW from Tamas:

```bash
cmsrel CMSSW_10_6_30
cd CMSSW_10_6_30/src/
cmsenv

scram b -j

```



