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
from scipy.io import savemat
import os
from extract_recordings import extract_recordings


recording_one = os.path.join(os.getcwd(),"1_100Neuron300SecondRecordingWithLevel4Noise.h5")
print("Finished setting recording one path")
extract_recordings(recording_one,os.path.join(os.getcwd(),"100Neuron300SecondRecordingWithLevel4Noise"))


#recording_two = os.path.join(os.getcwd(),"1_500Neuron300SecondRecordingWithLevel5Noise.h5")
#print("Finished setting recording two path")
#extract_recordings(recording_one,os.path.join(os.getcwd(),"500Neuron300SecondRecordingWithLevel5Noise"))

#recording_three = os.path.join(os.getcwd(),"3_400Neuron300SecondRecordingWithLevel4Noise.h5")
#print("Finished setting recording three path")
#extract_recordings(recording_three,os.path.join(os.getcwd(),"400Neuron300SecondRecordingWithLevel4Noise"))

#recording_four = os.path.join(os.getcwd(),"3_500Neuron300SecondRecordingWithLevel4Noise.h5")
#print("Finished setting recording four path")
#extract_recordings(recording_four,os.path.join(os.getcwd(),"500Neuron300SecondRecordingWithLevel4Noise"))


