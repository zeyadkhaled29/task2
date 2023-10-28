from scipy import fft
import numpy as np
import pandas as pd
class signal():
    def __init__(self):
        self.MAX_SAMPLES = 3000
        self.x_data = []
        self.y_data = []
        self.samples_time = []
        self.samples_amplitude = []
        self.fsampling = 1
        self.Max_frequency= 0
        self.reconstructed=[]
    def upload_signal_data(self,x_data,y_data,max_freq=0):
        self.MAX_SAMPLES = 3000
        self.fsampling = 1
        self.Max_frequency= 0
        if(len(x_data)<self.MAX_SAMPLES ):
            self.MAX_SAMPLES = len(x_data)
        self.x_data=x_data[0:self.MAX_SAMPLES]
        self.y_data=y_data[0:self.MAX_SAMPLES]
        if(max_freq==0):
            self.get_max_frequency()
        else:
            self.fsampling = 2*max_freq
            self.Max_frequency= max_freq
        
    def get_max_frequency(self):
        self.fsampling = 1/(self.x_data[1]- self.x_data[0])

        sampling_frequency = self.fsampling
        max_analog_frequency = (1/2)*self.fsampling
        magnitude_array = self.y_data
        total_samples = len(self.y_data)
        time_array = []
        for index in range(total_samples):
                    time_array.append(index/self.fsampling)
        sample_period = time_array[1] - time_array[0]
        n_samples = len(time_array)

                # gets array of fft magnitudes
        fft_magnitudes = np.abs(fft.fft(magnitude_array))
                # gets array of frequencies
        fft_frequencies = fft.fftfreq(n_samples, sample_period)
                # create new "clean array" of frequencies
        fft_clean_frequencies_array = []
        for index in range(len(fft_frequencies)):
                    # checks if signigifcant frequency is present
            if fft_magnitudes[index] > 0.001 and fft_frequencies[index]>self.Max_frequency:
                        self.Max_frequency=fft_frequencies[index]

        print("Max frequency fft: " + str(self.Max_frequency)) 


    def sample_signal(self):
        # Calculate the time step between samples
        sample_freq=2*self.Max_frequency
        time_step = 1 / sample_freq

        # Generate the time array based on the sample frequency
        max_time = self.x_data[self.MAX_SAMPLES-1]
        sampled_time = np.arange(0, max_time, time_step)

        # Interpolate the amplitude data at the sampled time points
        sampled_amplitude = np.interp(sampled_time, self.x_data, self.y_data)

        self.samples_time = sampled_time
        self.samples_amplitude = sampled_amplitude
        self.fsampling = sample_freq
    def reconstruct_from_samples(self):
         self.reconstructed = np.zeros_like(self.x_data)
         for i, ti in enumerate(self.x_data):
            self.reconstructed[i] = np.sum(self.samples_amplitude * np.sinc(2*self.Max_frequency* (ti - self.samples_time )))