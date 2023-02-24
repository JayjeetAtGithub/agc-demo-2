#!/bin/bash
set -ex

for i in {1..64};
do
    cp Run2012B_SingleMu-restructured-1000.parquet ../docker-presto/data/Run2012B_SingleMu-restructured-1000.${i}.parquet
done

docker exec -it docker-presto-namenode-1 hadoop fs -mkdir -p /dataset/
for i in {1..64};
do
    docker exec -it docker-presto-namenode-1 hadoop fs -put -f /data/Run2012B_SingleMu-restructured-1000.${i}.parquet /dataset/
done
