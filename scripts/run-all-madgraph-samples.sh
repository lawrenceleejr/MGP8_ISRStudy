#! /usr/bin/sh

cmsenv

echo "Running 'kinit -l 24h0m"
kinit -l 24h0m
echo "Running 'voms-proxy-init -voms cms'."
voms-proxy-init -voms cm

echo "Print every how many lines?"
read numLines
echo "Printing every $numLines lines."

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-1000.root' targetMass=1000 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-1000_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-1400.root' targetMass=1400 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-1400_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-1600.root' targetMass=1600 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-1600_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-1800.root' targetMass=1800 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-1800_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-2000.root' targetMass=2000 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-2000_log.txt

python truth.py /inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-2200.root' targetMass=2200 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-2200_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-2400.root' targetMass=2400 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-2400_log.txt

python truth.py inputFiles_load='./input-files/MGgluino2018_n50.list' outputFilename='./output-files/MGgluino2018_n50_50gev-bins_M-2600.root' targetMass=2600 isAOD=False printEvery=$numLines targetStatus=62 2>&1 | tee ./text-logs/MGgluino_n50_M-2600_log.txt
