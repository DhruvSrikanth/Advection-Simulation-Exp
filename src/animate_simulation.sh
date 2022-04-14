#!/bin/bash

mkdir ./outputs

g++-11 ./src/advection_simulation.cpp -o ./src/advection_simulation -fopenmp -O5 -mtune=native -march=native -ffast-math -Ofast -std=c++11

echo Enter the number of timesteps:
read NT
./src/advection_simulation 10000 $NT 1.0 1.0e6 5.0e-7 2.85e-7

rm ./src/advection_simulation

python3 ./src/generate_plots.py

rm -rf ./outputs/

echo "Done!"