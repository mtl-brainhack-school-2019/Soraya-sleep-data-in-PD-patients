### Short Bio: ###
I am currently a 2nd year Master's student based at the MNI and I study memory in Parkinson's disease patients. I have recently collected sleep data (polysomnography; includes EEG, EOG, ECG and EMG) and I am learning how to deal with this type of data for the first time. There are a lot of things I would like to learn through brainhack, but generally I would like to learn how to pre-process the data, visualize it and maybe use machine learning to predict some outcome variables.

### Data: ###
    Polysomnography (PSG) recordings of ~20 Parkinson's disease patients 
    with different severity of obstructive sleep apnea. PSG data contains:
    6 EEG channels (2 Frontal, 2 Central, 2 Occipital), 
    3 EMG channels (Chin, Right Leg, Left Leg), 
    2 EOG (Right eye, Left eye), 
    audio of snoring, and pulse oximetry (SaO2) measuring oxygen saturation. 
    Recording are nights sleep of around 8 hours for each participants.

## Brainhack 2019
------
#### Objectives  ##
- Pre-process PSG data:
    - Exclude artifacts (e.g., power line drifts in the signal)
- Detection of sleep spindles using MNE
- Visualization:
        - Plot topo-map of the EEG signal
        - Computer the power spectral density
        - Make animated plot of signal through time for different frequency bands _(I know this is possible with R, but i dont know about python)_
- If time permits, compute additional variables from the signal:
        - Use the ECG signal to compute heart rate variability
        - Use this variable to predict the severity of obstructive sleep apnea
#### Output:
- Binder of Jupyter notebooks with:
    a. pre-processing  scripts
    b. visualization scripts

#### Tools
* MNE
* visbrain
* [BioSSPY](https://github.com/PIA-Group/BioSPPy)
