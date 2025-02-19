[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mtl-brainhack-school-2019/Soraya-sleep-data-in-PD-patients/master)

### Brainhack project 2019 

##### *Summary:* 
The following project consisted of creating an interactive visualization of polysomnography data (i.e., Sleep EEG). The goal is to ultimately be able to summarize data that is usually very dense, into a more intuitive visualization. The goal was to then re-use this interactive visualization in the context of lab meetings or informal meetings with labmates to discuss about sleep data more easily.

##### *Project definition:* 
Ultimately, as mentioned earlier, I wanted to make data that is usually very hard to understand more accessible. This interactive visualization could then be used as a tool to communicate potential interesting things about particular participants, or also be used as a way to look at a single participant's data as a whole to get a general idea of his/her sleep. The point was to communicate the 'gist' of a participant's sleep. Additionally, for me the main goal was to use this as an opportunity to learn how to process sleep EEG and familiarize myself with the tools used to that end. The current code is a working prototype, but I wish to add more sleep variables down the road-- to really get an interesting and complete overall picture of a participant's night of sleep.

##### *Learning experience:* 
To analyze EEG data, I extensively used the MNE library --to load, shape, analyze data. I've also extensively used plot.ly for the interactive visualization, as well as Dash to create a dashboard containing the interactive visualizations. I've also familiarized myself with Git/Github, and have gotten a good first feel of how to go about processing and analyzing EEG data. Although my final project does not include it, I have also looked into ML techniques but haven't implemented any. In the first steps of data processing and data cleaning, I have also implemented an ICA to clean my data (to reject individual components that seemed to be artifact-based). But because of the low number of electrodes in my initial patient data, I have decided agaisnt using an ICA and instead passed a low-pass filter that filters out high-frequency noise. I found this was enough. For the purpose of this repo, I had to re-run my project using open-source data which was only available in .csv instead of .edf (the format I originally had used). So I also learned how to use a .csv to re-construct an EEG object.

##### *Results:* 
The deliverables of my project consist of a **Jupyter notebook** (which is binder compatible -- although I've realized this may be useless as the data files do not reside in the repo) detailing the process of loading, processing and transforming the sleep EEG data to create two interactive figures and a dashboard. One figure consists of showcasing the power spectral density across hours of sleep; which can be used to a) very broadly infer sleep stages b) look at distrubances during sleep (e.g., waking up, moving). The second figure consist of a topomap of the EEG activity across all the channels throughout time (using a slider to move across different timepoints); this allows to a) very broadly localize the sleep activity (e.g., is the activity more frontal or more central?) and b) identify faulty electrodes (e.g., if a single electrode shows very high activity compared to others for a sustained period of time, it may have detached during sleep). 

I have also included a separate **Python script** to run the dashboard directly through the command line.

###### Deliverables:
- Jupyter notebook detailing each steps towards making the two figures and the dashboard
- Python script to run the dashboard directly from command line
