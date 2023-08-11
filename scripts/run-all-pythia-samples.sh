#! /usr/bin/sh

cmsenv

echo "Please ensure you have run 'voms-proxy-init -voms cms' prior to continuing this script."
echo "Print every how many lines?"
read numLines
echo "Printing every $numLines lines."

#python truth.py inputFiles_load='./input-files/PYgluino2018_M-100.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-100.root' targetMass=100 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-100_log.txt

#python truth.py inputFiles_load='./input-files/PYgluino2018_M-200.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-200.root' targetMass=200 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-200_log.txt

#python truth.py inputFiles_load='./input-files/PYgluino2018_M-400.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-400.root' targetMass=400 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-400_log.txt

#python truth.py inputFiles_load='./input-files/PYgluino2018_M-500.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-500.root' targetMass=500 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-500_log.txt

#python truth.py inputFiles_load='./input-files/PYgluino2018_M-800.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-800.root' targetMass=800 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-800_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-1000.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-1000.root' targetMass=1000 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-1000_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-1400.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-1400.root' targetMass=1400 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-1400_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-1600.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-1600.root' targetMass=1600 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-1600_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-1800.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-1800.root' targetMass=1800 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-1800_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-2000.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-2000.root' targetMass=2000 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-2000_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-2200.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-2200.root' targetMass=2200 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-2200_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-2400.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-2400.root' targetMass=2400 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-2400_log.txt

python truth.py inputFiles_load='./input-files/PYgluino2018_M-2600.list' outputFilename='./output-files/PYgluino2018_50gev-bin_M-2600.root' targetMass=2600 isAOD=True printEvery=$numLines 2>&1 | tee ./text-logs/PYgluino2018_M-2600_log.txt