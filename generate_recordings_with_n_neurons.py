import MEArec as mr
def generate_recordings_with_n_neurons(num_of_exc,num_of_inh,length_of_rec,noise_level,templates_filename,save_name_of_rec):
   
    recording_params = mr.get_default_recordings_params()
    # Set parameters
    recording_params['spiketrains']['n_exc'] = num_of_exc
    recording_params['spiketrains']['n_inh'] = num_of_inh
    recording_params['spiketrains']['duration'] = 600
    #recording_params['spiketrains']['seed'] = 0


    recording_params['templates']['min_amp'] = 40
    recording_params['templates']['max_amp'] = 800
    #recording_params["recordings"]["bursting"] = True;
    #recording_params['templates']['seed'] = 0

    recording_params['recordings']['modulation'] = 'electrode'
    recording_params['recordings']['noise_mode'] = 'uncorrelated'
    recording_params['recordings']['noise_level'] = noise_level;
    # use chunk options
    recording_params['recordings']['chunk_conv_duration'] = 20
    recording_params['recordings']['chunk_noise_duration'] = 20
    recording_params['recordings']['chunk_filter_duration'] = 20
    #recording_params['recordings']['seed'] = 0

    recording_params['spiketrains']['duration'] = length_of_rec
    recgen = mr.gen_recordings(templates=templates_filename, params=recording_params)
    # save recording
    mr.save_recording_generator(recgen, save_name_of_rec)