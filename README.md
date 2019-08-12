## Predict sleep efficiency from PSG data of Parkinson's patients with obstructive sleep apnea ##
I am not sure how to go about this, as this is a small and noisy dataset, but let's see what we can do. 
Sleep efficiency is a variable that can be easily computed once PSG data has been scored by a technician,
but as I don't have time to score all my data, I am hoping to use ML algorithm to score sleep (i.e., assign sleep stages; N1, N2, N3, REM) to then derive sleep efficiency. 

There are many challenges to this: first, sleep is heavily "impaired" in this population and individuals vary greatly from one another so it increasingly hard to draw patterns from the data. 

[This is a first pass idea for now]

### Ideas of things to look at : ###
- [ ] MOCA scores with % of N1/N2/N3/REM
- [ ] UPDRS with % of N1/N2/N3/REM
- [ ] sleep spindle density/amp with OSA episodes and MOCA
- [ ] Medication and sleep spindle density/amp, OSA episodes
- [ ] "derive" RBD diagnosis through threshold of EMG activity in REM

### Things I want to make : ###
- [ ] topo map of EEG activity across sleep stages for each ppant (animated if possible)

## but first... ##
Need to:
- remove artifacts (ICA needs a lot of electrodes (min 20channels) but regression approach requires less)
    - https://cbrnr.github.io/2018/01/29/removing-eog-ica/
    - https://cbrnr.github.io/2017/10/20/removing-eog-regression/

- epoch in 30s bins? (would this be useful)
- Would making a time-series df be useful??

### Some questions to explore? ###
If PD is linked with OSA (through autonimic dysfunction, weakened muscle, sleep fragmentation...); 
can there be a marker in the EMG activity of PD patients that predicts OSA severity???
 -> maybe can compute heart rate variability and use that as marker of "weakened autonomic dysfunction"
    refs: 
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4083342/
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5437978/
    https://link.springer.com/article/10.1007%2Fs11325-018-1729-0

