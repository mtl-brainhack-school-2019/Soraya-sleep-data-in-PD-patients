### Short Bio: ###
I am currently a 2nd year Master's student based at the MNI and I study memory in Parkinson's disease patients. I have recently collected sleep data (polysomnography; includes EEG, EOG, ECG and EMG) and I am learning how to deal with this type of data for the first time. There are a lot of things I would like to learn through brainhack, but generally I would like to learn how to pre-process the data, visualize it and maybe use machine learning to predict some outcome variables.

### Data: :zzz:
Openly available data from Nathalie Regard [80 days in dreams project](http://dreamsessions.org/80days.html). ((Having some issues with the data, so I emailed Nathalie))


## Brainhack 2019 
------
### Objectives   :date:

**Goal is to make an interactive tutorial for the processing and visualizing sleep data using Open source PSG data**
- [ ] Remove artifacts using ICA or the [Autoreject package](https://autoreject.github.io/)
- [ ] Detect sleep spindles ([Tutorial 1](https://github.com/raphaelvallat/yasa) or [Tutorial 2](https://raphaelvallat.com/spindles.htmli))
- [ ] Detect slow oscillations
- [ ] Pass a sleep-stage detection algorithm ([Tutorial/package](https://github.com/skjerns/AutoSleepScorer))
- [ ] Localize the sleep events (i.e., sleep spindles and slow oscillations) on the head

- [ ] **Visualization**:
    - Plot topo map of the EEG signal (Hoping to reproduce this figure) [Fig. 1B and 1D](https://www.cell.com/neuron/pdfExtended/S0896-6273(17)31073-5)
    ![Verynicefig](images/Fig_from_walker.jpg)
    - Interactive graph (with Plot.ly) of activity (diff frequency bands) across different hours through the night and represented on a topography map (i.e., localizing the events on the scalp)
- [ ] Source reconstruction: 
    - Because Nathalie has MRI available, it is pssible to do source reconstruction using Freesurfer's watershed algorithm through [MNE](https://martinos.org/mne/dev/manual/appendix/bem_model.html) (may need to do this on ComputeCanada)
- [ ] Analysis:
    - Dreams??


### Output: :file_folder:
- Interactive Jupyter notebooks with the processing and the visualization

### Tools: :computer:
Aside numpy/pandas/seaborn/matplotlib,
* [MNE](https://martinos.org/mne/stable/index.html)
* [visbrain](http://visbrain.org/sleep.html)
* [Plotly](https://plot.ly/python/)
