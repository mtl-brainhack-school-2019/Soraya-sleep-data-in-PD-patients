import mne
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from mne.time_frequency import psd_welch

# load data #
filename = input('Enter a filename: ')
data = np.loadtxt(filename, 
                  delimiter=',')
data = data.T
# Then make a list of the channel names, this info is usually in an accompanying .txt file #
ch_names = ['COUNTER', 'INTERPOLATED','AF3','F7','F3','FC5','T7','P7','O1','O2','P8','T8','FC6',
 'F4','F8','AF4','RAW_CQ','CQ_AF3','CQ_F7','CQ_F3','CQ_FC5','CQ_T7','CQ_P7','CQ_O1','CQ_O2','CQ_P8',
 'CQ_T8','CQ_FC6','CQ_F4','CQ_F8','CQ_AF4','CQ_CMS','CQ_DRL','GYROX','GYROY', 'MARKER']
# set the sampling rate, this information should also be in the .txt file containing the channel names
sfreq = 128
# using these variables, create an MNE info object which we will use to create our MNE raw object #
info = mne.create_info(ch_names, sfreq)
# then we combine the info and the .csv file to create a MNE Raw object #
raw = mne.io.RawArray(data, info)

# crop file #
max_hour = (np.max(raw.times/(60*60)))
hour = input('How many hours do you want to visualize (min: 1, max: %s)?   ' % (max_hour))
hour = int(hour)
crop = raw.crop(tmin=0 , tmax=(3600*hour))

# change type of channels #
crop.set_channel_types(mapping={'AF3': 'eeg',
 'F7':'eeg',
 'F3':'eeg',
 'FC5':'eeg',
 'T7':'eeg',
 'P7':'eeg',
 'O1':'eeg',
 'O2':'eeg',
 'P8':'eeg',
 'T8':'eeg',
 'FC6':'eeg',
 'F4':'eeg',
 'F8':'eeg',
 'AF4':'eeg'})

# load data and add a filter #
crop.load_data() ## Need to load data to pass a filter ##
crop.filter(0.1, 50., fir_design='firwin')
# Set EEG montage. See MNE documentation for available options #
crop.set_montage(montage='standard_1020')

# dropping non-EEG channels #
drop = ['COUNTER', 'INTERPOLATED','RAW_CQ','CQ_AF3','CQ_F7','CQ_F3','CQ_FC5','CQ_T7']
crop.drop_channels(ch_names=drop)

# computing PSD of signal#
final_df = pd.DataFrame()
x = []
tmin = 0
tmax = 300
count = 0
## We define the time until we want to loop, here since we only took 2 hours we are using 3600 * 2 ##
max_time = (3600*hour)
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, n_per_seg=256)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    final_df = final_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('There is a total of %s windows' % (count))
# copy the resulting dataframe #
px_plot = final_df
# compute log of PSD #
px_plot['log'] = np.log(px_plot['PSD'])

## Do the same for individual channels ##

# AF3

AF3_df = pd.DataFrame()
x = []
tmin = 0
tmax = 300
chan = ['AF3']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    AF3_df = AF3_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel AF3')

# F7

tmin = 0
tmax = 300
F7_df = pd.DataFrame()
x = []
chan = ['F7']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    F7_df = F7_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel F7')

#  F3
tmin = 0
tmax = 300
F3_df = pd.DataFrame()
x = []
chan = ['F3']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    F3_df = F3_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel F3')

# FC5
tmin = 0
tmax = 300
FC5_df = pd.DataFrame()
x = []
chan = ['FC5']

count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    FC5_df = FC5_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel FC5')

# FC6
tmin = 0
tmax = 300
FC6_df = pd.DataFrame()
x = []
chan = ['FC6']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    FC6_df = FC6_df.append(df)
    tmin += 300
    tmax += 300
    count +=1
    
print('Channel FC6')

# T7 
tmin = 0
tmax = 300
T7_df = pd.DataFrame()
x = []
chan = ['T7']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    T7_df = T7_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel T7')

# O1
tmin = 0
tmax = 300
O1_df = pd.DataFrame()
x = []
chan = ['O1']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    O1_df = O1_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel O1')

# O2
tmin = 0
tmax = 300    
O2_df = pd.DataFrame()
x = []
chan = ['O2']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    O2_df = O2_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel O2')

# T8
tmin = 0
tmax = 300
T8_df = pd.DataFrame()
x = []
chan = ['T8']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    T8_df = T8_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel T8')

# F8
tmin = 0
tmax = 300
F8_df = pd.DataFrame()
x = []
chan = ['F8']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    F8_df = F8_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel F8')

# AF4
tmin = 0
tmax = 300
AF4_df = pd.DataFrame()
x = []
chan = ['AF4']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    AF4_df = AF4_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel AF4')

# F4
tmin = 0
tmax = 300
F4_df = pd.DataFrame()
x = []
chan = ['F4']
count = 0
while tmax < max_time:
    psd_df = psd_welch(crop, tmin=tmin, tmax=tmax, picks=chan, verbose=False)
    x = psd_df[0]
    x = x[0]
    y = psd_df[1]
    y = pd.DataFrame(y)
    x = pd.DataFrame(x)
    frame = [y,x]
    df = pd.concat(frame, axis=1)
    df.columns = ['Freq','PSD']
    df['epoch'] = tmax
    F4_df = F4_df.append(df)
    tmin += 300
    tmax += 300
    count +=1

print('Channel F4')

## Setting the EEG coordinates ##
F3_df['theta'] = 39
F3_df['r'] = 30
F3_df['Channel'] = 'F3'

F4_df['theta']= -39
F4_df['r'] = 30
F4_df['Channel'] = 'F4'

AF3_df['theta']= 25
AF3_df['r'] = 16
AF3_df['Channel'] = 'AF3'

AF4_df['theta']= -25
AF4_df['r'] = 16
AF4_df['Channel'] = 'AF4'

F7_df['theta']= 54
F7_df['r'] = -2
F7_df['Channel'] = 'F7'

F8_df['theta']= -54
F8_df['r'] = -2
F8_df['Channel'] = 'F8'

FC5_df['theta']= 69
FC5_df['r'] = 18
FC5_df['Channel'] = 'FC5'

FC6_df['theta']= -69
FC6_df['r'] = 18
FC6_df['Channel'] = 'FC6'

O2_df['theta']= -162
O2_df['r'] = -2
O2_df['Channel'] = 'O2'

O1_df['theta']= 162
O1_df['r'] = -2
O1_df['Channel'] = 'O1'

T7_df['theta']= 90
T7_df['r'] = -2
T7_df['Channel'] = 'T7'

T8_df['theta']= -90
T8_df['r'] = -2
T8_df['Channel'] = 'T8'

frames = [F4_df, F3_df, AF3_df, AF4_df, O1_df, O2_df, T8_df, T7_df, FC5_df, FC6_df, F8_df, F7_df]

test = pd.concat(frames, sort=False)
test['log'] = np.log(test['PSD'])
test = test[test['Freq'] < 50]

## DASH APP ##

print('Creating the Dash App...')

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
test['bins'] = pd.qcut(test['log'], 10, labels=['1','2','3','4','5','6','7','8','9','10' ])
bins = {
    '1' : "#f2fffb",
    '2' : "#bbffeb",
    '3' : "#98ffe0",
    '4' : "#79ffd6",
    '5' : "#6df0c8",
    '6' : "#69e7c0",
    '7' : "#59dab2",
    '8' : "#45d0a5",
    '9' : "#31c194",
    '10' : "#2bb489"
}

test['color'] = test['bins'].map(bins)

fig = px.scatter_polar(test)

app.layout = html.Div(
    id="root",
    children=[
        html.Div(
        id='Header',
        children=[
            html.H4(children="Interactive visualization of PSG data"),
            html.P(
            id="description",
            children="Project for Brainhack 2019 Soraya Lahlou")],
            style = {'padding' : '40px' , 
                             'backgroundColor' : '#008B8B'}),
    html.Header(""),
    dbc.Row(
        [
            dbc.Col(
            [dcc.Graph(id='heatmap',figure=
                {
                    'data': [
                        go.Heatmap(
                        z=px_plot['log'],
                        x=px_plot['epoch'],
                        y=px_plot['Freq'], colorscale='viridis')],
                    'layout' :dict(
                        margin=dict(t=20, r=0, b=100, l=6))
                    }
                    )],
                    width=6, align='center'),
            dbc.Col([
                html.Div(id='a-blank',
                        children=[html.P(id='a-blank-desc',
                                        children="Topomap of EEG activity across time. Use the slider to change time")]),
                html.Div([
                    dcc.Graph(id='topo', figure={
                'data': [fig]
                    })]),
            dcc.Slider(id='slider-hours', 
                    min=test['epoch'].min(),
                    max=test['epoch'].max(),
                    value=test['epoch'].min(),
                    marks={str(epoch): str(epoch) for epoch in test['epoch'].unique()}, 
                    step=None)
                    ], width=5, align='center')
                    
              ]),
        html.Div(id="end")
    ])


@app.callback(
    Output('topo', 'figure'),
    [Input('slider-hours', 'value')])

def update_figure(selected_hours):
    filter_df = test[test.epoch == selected_hours]
    traces = []
    for channel in filter_df.Channel.unique():
        Channel_df = filter_df[filter_df['Channel'] == channel]
        traces.append(go.Scatterpolar(
            r=Channel_df['r'],
            theta=Channel_df['theta'],
            text=Channel_df['Channel'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 25,
                'color': Channel_df['color'],
                'line': {'width': 0.5, 'color': Channel_df['color']},
            },
            subplot= 'polar',
            name= channel,
            
        ))
    return {
        'data': traces,
        'layout': go.Layout(
            polar={'angularaxis': {'rotation': 90}}, 
            margin=dict(t=20, r=0, b=100, l=70))
    }

if __name__ == "__main__":
    app.run_server(debug=False)

