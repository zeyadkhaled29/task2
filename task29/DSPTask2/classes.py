from scipy import fft
import numpy as np

MAX_SAMPLES = 3000
class sinwaves():
   def __init__(self,index=0,amplitude=1,frequency=1,added=False):   
      self.index = index
      self.amplitude = amplitude
      self.frequency = frequency
      self.added = added
      self.Xaxis=np.linspace(0,2*np.pi,MAX_SAMPLES)
      self.Yaxis=(self.amplitude)/(np.sin(self.Xaxis*self.frequency*2*np.pi))

      def add(self,sinwaves1):
         return sinwaves1.Yaxis + self.Yaxis
      def Getfrequncy(self):
         return self.frequency
      
class signal():
   def __init__(self):
        self.MAX_SAMPLES = 3000
        self.temp_arr_x = []
        self.temp_arr_y = []
        fsampling = 1
        self.Max_frequency= float("-inf")
        
   def max_frequency(self):
        self.fsampling = 1/(self.temp_arr_x[1]- self.temp_arr_x[0])

        sampling_frequency = self.fsampling
        max_analog_frequency = (1/2)*self.fsampling
        magnitude_array = self.temp_arr_y
        total_samples = len(self.temp_arr_y)
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