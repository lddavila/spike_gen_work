import tempfile
tempfile.tempdir = "/scratch/afriedman/temp"

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
number = "1_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 1;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

print("finished first Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "2_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 2;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)
print("Finished Second Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "3_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 3;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)
print("Finished third Recording")


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "4_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 4;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "5_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 5;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "6_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 6;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "7_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 7;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "8_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 8;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)


templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "9_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 9;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)

templates_filename = 'templates_300_neuropixels.h5'
tempgen = mr.load_templates(templates_filename)
print("Finished loading templates")
number = "10_"
num_of_exc = 300;
num_of_inh = 300;
length_of_recording = 300;
noise_level = 10;
recording_file_name = number+str(num_of_exc+num_of_inh)+"Neuron"+str(length_of_recording)+"SecondRecordingWithLevel"+str(noise_level)+"Noise.h5"
print("Finished setting parameters")
generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_recording,noise_level,templates_filename,recording_file_name)