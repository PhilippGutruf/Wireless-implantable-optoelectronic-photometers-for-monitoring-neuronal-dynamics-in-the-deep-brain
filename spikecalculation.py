# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 13:29:04 2017

@author: bruchas
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 14:32:37 2016

@author: bruchas
"""



import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import peakutils
import scipy as sp
from scipy import signal
import seaborn as sns
import pandas as pd


'''
Detect peaks and calculate the spike frequency

using the 5*MAD dynamic threshold to detect spike for signals

function baseline_showdata is used for basline correction for the data, input
name = the input data variable
width = the width of the filter

output = the baseline corrected data


detect_peaks function is used to detect events(spike)
input
x : 1D array_like
        data.
    mph : {None, number}, optional (default = None)
        detect peaks that are greater than minimum peak height.
    mpd : positive integer, optional (default = 1)
        detect peaks that are at least separated by minimum peak distance (in
        number of data).
    threshold : positive number, optional (default = 0)
        detect peaks (valleys) that are greater (smaller) than `threshold`
        in relation to their immediate neighbors.
    edge : {None, 'rising', 'falling', 'both'}, optional (default = 'rising')
        for a flat peak, keep only the rising edge ('rising'), only the
        falling edge ('falling'), both edges ('both'), or don't detect a
        flat peak (None).
    kpsh : bool, optional (default = False)
        keep peaks with same height even if they are closer than `mpd`.
    valley : bool, optional (default = False)
        if True (1), detect valleys (local minima) instead of peaks.
    show : bool, optional (default = False)
        if True (1), plot data in matplotlib figure.
    ax : a matplotlib.axes.Axes instance, optional (default = None).

output 

ind : 1D array_like
        indeces of the peaks in `x`.
        
        here we use 5*MAD we as threshold

'''

#baseline correction using highpass filter

def baseline_showdata(name,width=0.01): #Read the raw csv data and store as a pandas dataframe
    global x    
    time=name['time']
    signals=name['signal']
    
    signals=signals[::n] #sampling down by n
    time=time[::n] #sampling down by n
    signals=signals.values
    time=time.values
    
    #plot the original signals
    plt.figure()
    plt.subplot(211)
    plt.plot(time,signals)
    plt.title('row')
   
    #butterfly highpassfilter
    dodl=np.nan_to_num(signals)
    b,a=signal.butter(3,width,'highpass')
    dodl=signal.filtfilt(b,a,dodl)
    dodl=abs(dodl)
    
    #plot the corrected signals
    plt.subplot(212)
    plt.plot(time,dodl)
    for xx in x:
        plt.axvline(xx,color='r',linestyle='--')
    #plt.ylim((-1,1))
    plt.title('corrected')
    
    #save it into dataframe
    correcteddata=pd.DataFrame({'time':time,
                           'signal':dodl})

    return correcteddata

correctedlist=[]
for data in dataset:
    co=baseline_showdata(data)
    correctedlist.append(co)


from detect_peaks import detect_peaks


# shock 1

#### spike detection and frequency calculataion
mad=np.nanmedian(np.abs(baseline-np.nanmedian(baseline)))
dind=detect_peaks(signals,threshold=5*mad,show=True)
bind=detect_peaks(baseline,threshold=5*mad,show=True)
dnum=np.size(dind)
bnum=np.size(bind)
dfre=dnum/TimeofBaseline # frequency for baseline 
bfre=bnum/TimeofPostshock  #frequency for postshock

