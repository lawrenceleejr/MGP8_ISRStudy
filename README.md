# MGP8_ISRStudy



* example MadGraph samples
	* https://cmsweb.cern.ch/das/request?instance=prod/global&input=file+dataset%3D%2FSMS-T1btbt-LLC1_ctau10to200-mGluino-1000to2800-mLSP0to2800_TuneCP2_13TeV-madgraphMLM-pythia8%2FRunIIFall17FSPremix-GridpackScan_94X_mc2017_realistic_v15-v1%2FAODSIM

From Sara F:

> here some MG gluino samples
> https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2FSMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8%2FRunIISummer20UL*MiniAODv2*%2FMINIAODSIM
> and here some stops samples
> https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2FSMS-T6ttZH_TuneCP5_13TeV-madgraphMLM-pythia8%2FRunIIS*MiniAODv*%2FMINIAODSIM


* Our Pythia samples
	* https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FHSCP*%2FRunIISummer20UL18RECO-106X*%2FAODSIM

For some notes on how to access files like this. You can open them in root:

```python
import ROOT
f = ROOT.TFile.Open("root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18RECO/HSCPgluino_M-1000_TuneCP5_13TeV-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/80000/176F47D3-A514-454B-82D4-019163A330F9.root")
```

or you can copy them to whereever you want with:

```bash
xrdcp root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18RECO/HSCPgluino_M-1000_TuneCP5_13TeV-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/80000/176F47D3-A514-454B-82\
D4-019163A330F9.root .
```

**I've already downloaded an example file to get you started here `/afs/cern.ch/user/l/leejr/work/public/ISRStudy//sampleFiles/176F47D3-A514-454B-82D4-019163A330F9.root`**

In order to see the contents of these files in an effective way you need to be in a CMSSW environment. Instructions for setting up CMSSW from Tamas:

```bash
cmsrel CMSSW_10_6_30
cd CMSSW_10_6_30/src/
cmsenv

scram b -j
```

Then you'll be able to run the `truth.py` example skeleton file from this repo.

The syntax for `truth.py` looks like this

python truth.py inputFiles_load=batch_of_files.list outputFile=dir/name_PYTHIA.root outputFilename=name_PYTHIA isAOD=True targetMass=100

You can instead opt to hand `truth.py` a single ROOT file by using 'inputFiles' rather than 'inputFiles_load'

isAOD takes a boolean and will change the status between 22 and 23 based on if the samples are AOD or MINIAOD

targetMass takes an int and refers to the mass of an individual particle in an event


**Instructions for generating .list files to pass to truth.py**

Once path to the dataset has been found from DAS, this command will generate the .list with the entries in the appropriate format.

```dasgoclient -query="file dataset=<dataset path>" | sed  's%^%root://cmsxrootd.fnal.gov//%' > ./input-files/<filename>.list```

The .list can then be passed to truth.py with the ```inputFiles_load``` command as outlined above.


**Helpful tips when running truth.py**

It may be useful to record the output of truth.py while also observing the output in the terminal. Rather than redirecting the output stream with ```>```, consider using ```tee```. Example:

```python truth.py inputFiles_load='./input-files/<input-list>.list' outputFilename='./output-files/<output_filename>.root' targetMass=200 isAOD=False printEvery=10000 2>&1 | tee ./text-logs/<log filename>.txt```

Note that this will overwrite the log.txt if run again. This is generally desireable, but you can append to an exisiting file by adding the ```-a``` flag to ```tee```. ```2>&1``` Ensures that the error outputstream is passed to ```tee``` so that any error output is recorded in the log. 

When passing Madgraph samples to truth.py, the target status must be given as a flag. Example: 

```python truth.py inputFiles_load='./input-files/<input-list>.list' outputFilename='./output-files/<output-filename>.root' targetMass=1000 isAOD=False printEvery=1000 targetStatus=62 2>&1 | tee ./text-logs/<log-filename>.txt```

**Current Status**
```[cthompso@lxplus773 src]$ python truth.py inputFiles_load=input-files/MGgluino2018_n50.list outputFilename=real_MG.root targetMass=1000 isAOD=False printEvery=1000 targetStatus=62
('input=', ['root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/E8E03006-260C-1C4F-A818-8A682CE0CE15.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/A23D1A87-B3C4-0740-8E14-55C9C7F32ACE.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/E585AE7E-5B70-4B4A-929B-3C63A128B285.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/40F2A38E-DCE6-0E40-9BF7-45CA7C024505.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/5B5D07C8-CF34-9843-9232-BA14DBAFF007.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/7E74555C-773D-D84C-87EB-62A2A91AA8EC.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/96AE891C-EE47-C64B-AFC7-D3660988BA7F.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/F0250B1C-DD02-DF46-A9FD-890327D246EB.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/8456DDAB-872E-BD46-95A3-A33AA7478768.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/664BB09C-6669-8A43-A2DA-84EB417E049C.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/CCD1E12C-6EC8-434C-8DE7-0DF0C7D34FA4.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/58E83B93-8839-6548-9685-BD1A1191B6B0.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/EE3D69D4-B650-1F47-B73E-E8448B92A769.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/B059C1B6-E790-5A4C-85E0-A5053D4D344B.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/E908FF9B-5079-2E40-A205-DB1A256A724D.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/382E986F-FB37-AB41-B52D-5E3E9F78049F.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/50A8BD93-2592-5443-8C42-7063EB88C2D5.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/26142A04-2E69-D04E-95E8-FCE23F0D6D6E.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/F050CD0A-8F39-9C4A-87C6-11A8AA21E4D9.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/6F7C171D-FB9F-8243-8F61-A55AFA37DA1C.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/850EE571-616C-2345-AC81-85B84CB31AC0.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/69ADDF6D-1220-5040-BFE1-A0E6179FD3BD.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/DEC97E18-73AE-A447-911B-5541F03F2181.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/EEA93A3B-156B-E64D-87F2-3488DE3682E8.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/045A015E-0938-AA42-9B20-C247207D76F5.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/259E25D3-B885-3445-8341-70D89971A2E4.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/133F2AD1-0BC5-5846-8664-5C2335A8E301.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/00ABFD98-9A9D-5C4A-8F03-B7EDDB257F77.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/8255874B-8189-974B-A575-57EEAEBAE49F.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/28257F10-2522-0249-B5CE-1E920F4BC7FA.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/BAA37EA8-347C-024F-9E93-CE11D3A01859.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/9D0E22A5-80C9-AC47-9811-2E7C87474257.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/5EF5C273-B47C-074B-9A04-A94C106539BD.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/541EBB26-296A-FB42-961B-D704C21C41FE.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/05DB9B54-7CFB-E04D-9482-AC050BE57157.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/7C32C8B0-7C87-C540-95C7-4AD74A724610.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/6455591A-953B-BF4F-BD8C-7A51EFDF242C.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/5CE68724-904F-394C-B3C7-1B622E4E42CF.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/EC0851CF-E7C0-794D-9283-763770F6D7AC.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/F650E6B5-5162-7A4B-A660-D083353604F9.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/D777D53F-EB27-AA4D-A552-946F47A49AD2.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/ADEB5496-5572-CE40-89B9-D4BC13E7E8EA.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/3AEE0855-128D-5C4A-ABF6-17FC67898A33.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/ED9F49DD-9308-B74A-A07E-B5FAA01E24DF.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/0C440BAE-0A83-244C-9519-8FEBBF200171.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/14EABAC7-30A4-C34D-A0F0-137A4BF4294D.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/8E1A9748-C06C-4045-BDC7-EF2373034B90.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/15AA91E0-70A5-5D4C-B88B-93C100026C14.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/421B1A51-213E-7B4E-A0C2-1B9B4EFBA92B.root', 'root://cmsxrootd.fnal.gov///store/mc/RunIISummer20UL18MiniAODv2/SMS-T5qqqqWH_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/FSUL18_106X_upgrade2018_realistic_v16_L1v1-v3/50000/4A74C330-8476-EE4B-BCEE-495C0ACEF9C5.root'])
('output=', <ROOT.TFile object ("real_MG.root") at 0x5a66100>)
('real_MG.root', 1000)
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
TFile::Append:0: RuntimeWarning: Replacing existing TH1: pTsum {} (Potential memory leak).
Unable to load sec.protocol plugin libXrdSecztn.so
Unable to load sec.protocol plugin libXrdSecztn.so
Unable to load sec.protocol plugin libXrdSecztn.so
Unable to load sec.protocol plugin libXrdSecztn.so
Unable to load sec.protocol plugin libXrdSecztn.so
Running...
Traceback (most recent call last):
  File "truth.py", line 125, in <module>
    eventinfo = handles["generator"].product()
  File "/cvmfs/cms.cern.ch/slc7_amd64_gcc820/cms/cmssw/CMSSW_10_6_30/python/DataFormats/FWLite/__init__.py", line 87, in product
    raise self._exception
RuntimeError: ("getByLabel not called for '%s'", <DataFormats.FWLite.Handle instance at 0x7f8ea7eeb440>)
[cthompso@lxplus773 src]$```
