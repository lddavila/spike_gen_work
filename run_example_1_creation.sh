#!/bin/bash 
#SBATCH -n 40 
#SBATCH -p medium 
#SBATCH -o output.txt 
#SBATCH -e output.txt
source ~/my_env/bin/activate
python create_recordings.py