#!/bin/bash
make
cd build
cp $(cat ../target.txt) --target-directory=/build/ 
cd .. 
make clean
