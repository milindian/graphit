# graphit.py
This tool provides a GUI for creating a data points directly in a graph and converting that into a range-specified data-set. This script will:
* Record mouse clicks in a canvas as coordinates
* Convert those coordinates into a data set based off of specifed x-axis and y-axis range
* Write the dataset to a CSV (wiping any previous data points)

## Pre-requesites
None

## Usage
* Install Python 3 and Conda
* Create new virtual environment
* Install packages in requirement_coordinates.txt
*  Run the python script from the terminal. For example:
```
python3 graphit.py
```
* In the settings dialog, specify "Maximum X-axis value" and "Maximum Y-axis value". This will adjust the axis coordinates so that the output data points are relevant to the assay/measurement that you are trying to emulate
* In the settings dialog, click "Start". This will wipe any previous files and ready the canvas for plotting
* In the canvas dialog, left-click to create data points in the shape of the graph you want
* In the settings dialog, click "Done" to convert the coordinates to data points, process them and write them to a CSV, which will automatically open once this button is pressed. 

## Note
Remember to close the coordinates.csv file when you are done
