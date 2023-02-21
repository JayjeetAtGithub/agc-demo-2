#!/bin/bash
set -ex

docker exec -it docker-presto-namenode-1 hadoop fs -mkdir /dataset
docker exec -it docker-presto-namenode-1 hadoop fs -put /data/Run2012B_SingleMu-restructured-1000.4.parquet /dataset/
