import tempfile
tempfile.tempdir = "/scratch/lddavila/temp"

import MEArec as mr
import numpy as np
import matplotlib.pylab as plt
import spikeinterface.extractors as se
import spikeinterface.sorters as ss
import spikeinterface.widgets as sw
import spikeinterface.comparison as sc
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import spikeinterface.full as si
from generate_recordings_with_n_neurons import generate_recordings_with_n_neurons 

print("Finished importing packages")
templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "3_"
num_of_exc = 250;
num_of_inh = 250;
length_of_recording = 300;
noise_level = 4;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

print("finished first Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "3_"
num_of_exc = 150;
num_of_inh = 250;
length_of_recording = 300;
noise_level = 4;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)
print("Finished Second Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "1_"
num_of_exc = 50;
num_of_inh = 50;
length_of_recording = 300;
noise_level = 4;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)
print("Finished third Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "1_"
num_of_exc = 250;
num_of_inh = 250;
length_of_recording = 300;
noise_level = 5;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)