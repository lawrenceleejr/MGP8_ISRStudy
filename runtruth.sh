#!/bin/bash
#Bash script to run truth.py

mass=('1400' '1600' '1800' '2000' '2200' '2400' '2600') #Note that 1000 is also a mass to consider but I have already ran over 1000GeV
for str in ${mass[@]};
do
	echo Running truth.py for targetMass = $str GeV
	python truth.py inputFiles_load=input-files/MGgluino2018_n50.list outputFilename=output-files/gluglu_MGn50_GeV$str.root targetMass=$((str)) isAOD=False printEvery=1000 targetStatus=62
done
