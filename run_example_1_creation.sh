#!/bin/bash 
#SBATCH -n 40 
#SBATCH -p medium 
#SBATCH -o output.txt 
#SBATCH -e output.txt
source /gpfs/scratch/lddavila/spike_gen_work/my_env/bin/activate
python create_recordings.py