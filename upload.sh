#!/bin/bash
set -ex

docker exec -it docker-presto-namenode-1 hadoop fs -mkdir -p /dataset/
for i in {1..64};
do
    docker exec -it docker-presto-namenode-1 hadoop fs -put -f /data/Run2012B_SingleMu-1000.${i}.parquet /dataset/
done
