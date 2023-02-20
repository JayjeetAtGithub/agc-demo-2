#!/bin/bash
set -ex

rm -rf /tmp/dataset
mkdir -p /tmp/dataset

for i in {1..64};
do 
    cp Run2012B_SingleMu-restructured-1000.parquet /tmp/dataset/Run2012B_SingleMu-restructured-1000.${i}.parquet
done
