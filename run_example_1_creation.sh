#!/bin/bash 
#SBATCH -n 1
#SBATCH -p medium 
#SBATCH -o output.txt 
#SBATCH -e output.txt
export TMPDIR=/scratch/$USER/temp
mkdir -p $TMPDIR
source /gpfs/scratch/afriedman/spike_gen_work/my_env/bin/activate
echo "Python path: $(which python)"
python -m pip list | grep MEArec
python create_recordings.py