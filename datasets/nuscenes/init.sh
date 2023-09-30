#!/bin/bash

sudo mkdir -p /data/sets/nuscenes 

wget https://www.nuscenes.org/data/v1.0-mini.tgz 

sudo tar -xf v1.0-mini.tgz -C /data/sets/nuscenes 

rm v1.0-mini.tgz

pip install nuscenes-devkit &> /dev/null