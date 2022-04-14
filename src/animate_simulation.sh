#!/bin/bash

mkdir ./outputs

g++-11 ./src/advection_simulation.cpp -o ./src/advection_simulation -fopenmp -O5 -mtune=native -march=native -ffast-math -Ofast

./src/advection_simulation 400 $1 1.0 1.0e6 5.0e-7 2.85e-7

rm ./src/advection_simulation

python3 ./src/generate_plots.py

rm ./static/movie.mp4
ffmpeg -i ./static/movie.avi -strict -2 ./static/movie.mp4         
rm ./static/movie.avi

rm -rf ./outputs/

echo "Done!"
