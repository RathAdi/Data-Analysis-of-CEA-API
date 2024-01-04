# Data Analysis of CEA API
A visualization of the data provided by the Central Electricity Authority of India on their [website](https://cea.nic.in/api-for-central-electricity-authority-data/?lang=en).
Currently, the project is in development.

## Prerequisites
### FFmpeg Installation
The bar_chart_race module requires FFMpeg to be installed in your computer's path to be able to generate a .mp4 file.
Download can be found [here](https://www.ffmpeg.org/download.html).

The Python bindings for FFmpeg are installed through:
```pip install python-ffmpeg```

## Contents
### Generating Capacity Bar Chart Races
The CEA API gives the distribution of total generation capacity across coal, hydro and other forms of generation, divided across grid regions. The given data is presented as bar chart races to show the growth over the period of time provided in the API.