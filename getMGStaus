#!/bin/bash

mass=('90' '100' '125' '150' '175' '200' '225' '250' '275' '300' '350' '400' '450' '500' '550' '600')
lifetime=('5' '50' '1' '10' '100' '1000' '10000' '0p5' '0p05' '0p1' '0p01')
version=('3' '4')

> MGstau2018.list

for m in "${mass[@]}"; do
    for l in "${lifetime[@]}"; do
        for v in "${version[@]}"; do
            echo "Querying dataset in $m, $l, $v"
            dasgoclient -query="file dataset=/SMS-TStauStau_MStau-${m}_ctau-${l}mm_mLSP-1_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-SUS_106X_upgrade2018_realistic_v16_L1v1-v${v}/MINIAODSIM" | sed 's%^%root://cmsxrootd.fnal.gov/%' >> MGstau2018.list
        done
    done
done

# Note that if any of these combos DNE, they just get safely skipped
