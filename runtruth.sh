#!/bin/bash
#Bash script to run truth.py
#cd /afs/cern.ch/user/c/cthompso/private/CMSSW_10_6_30/src
#cmsenv
#scram b -j
#voms-proxy-init -voms cms
#Inf291501
#pymass=('1800' '2000' '2200' '2400' '2600')
#mgmass=('1000' '1400' '1600' '1800' '2000' '2200' '2400' '2600')
pymass=('200' '247' '308' '432' '557' '651' '745' '871' '1029' '1218' '1409')

for str in ${pymass[@]};
do
	echo Running truth.py on pythia for targetMass = $str GeV
	#python truth.py inputFiles_load=input-files/PYgluino2018_M-$str.list outputFilename=output-files/pythia-M-$str.root targetMass=$((str)) isAOD=True printEvery=1000
	python PYtest_truth.py inputFiles_load='/afs/cern.ch/user/l/ldishman/private/hscp/pythia/CMSSW_10_6_30/StopStau/MGP8_ISRStudy/input-files/PYgmsbStau2018_M-$str.list' outputFilename='/afs/cern.ch/user/l/ldishman/private/hscp/pythia/CMSSW_10_6_30/StopStau/MGP8_ISRStudy/output-files/PYgmsbStau2018_M-$str.root' targetMass=$((str)) isAOD=True printEvery=1000 targetStatus=? # Can't use until I get correct targetStatus!!
done

#for str in ${mgmass[@]};
#do
#	echo Running truth.py on madgraph for targetMass = $str GeV
#	python truth.py inputFiles_load=input-files/MGgluino2018.li#st outputFilename=output-files/gluglu_MG_GeV$str.root targetMass=$((str)) isAOD=False printEvery=100000 targetStatus=62 2>&1 | tee ./text-logs/MG$str.txt
#done
