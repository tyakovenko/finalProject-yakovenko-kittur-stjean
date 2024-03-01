import pandas as pd
import fns
import process as pc
import numpy as np

arrays = "/home/taya/finalProject-yakovenko-kittur-stjean/data/all_arrays.csv"#data with all the input arrays used for comparison

radarInput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/radarChartExperiment.csv"
radarErrorsOutput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/radarErrors.csv"
radarAvgErrorsGraphOrange = "/home/taya/finalProject-yakovenko-kittur-stjean/results/radarAvgErrorsOrange.png"
radarAvgErrorsGraphBlue = "/home/taya/finalProject-yakovenko-kittur-stjean/results/radarAvgErrorsBlue.png"
radarBarCompGraph = "/home/taya/finalProject-yakovenko-kittur-stjean/results/radarErrorsBlueOrange.png"


barInput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/barChartExperiment.csv"
barErrorsOutput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/barErrors.csv"
barAvgErrorsGraphBlue = "/home/taya/finalProject-yakovenko-kittur-stjean/results/barAvgErrorsBlue.png"
barAvgErrorsGraphOrange = "/home/taya/finalProject-yakovenko-kittur-stjean/results/barAvgErrorsOrange.png"
barBarCompGraph = "/home/taya/finalProject-yakovenko-kittur-stjean/results/barErrorsBlueOrange.png"



donutInput = ""

colNames = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'o10',
            'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10']

#take all the data arrays and find the true difference for each of the first two elements
dfArray = pd.read_csv("/home/taya/finalProject-yakovenko-kittur-stjean/data/all_arrays.csv")
dfArray['difference'] = dfArray['values'].map(lambda x: fns.compute_difference(x))
dif = dfArray['difference']
dataStd = fns.std(arrays)


#find all dataframe errors for each viz type
#radar chart processing and results
radarErrors = pc.errors(radarInput, colNames, dif, radarErrorsOutput)
radarErrorAvgs = radarErrors.mean().to_list() #average errors for each viz across all participants
pc.viz(dataStd, radarErrorAvgs[0:10], "Average Errors for Orange Radar Visualizations", radarAvgErrorsGraphOrange)
pc.viz(dataStd, radarErrorAvgs[10:], "Average Errors for Blue Radar Visualizations", radarAvgErrorsGraphBlue)
radarOrangeErrorsAvg = radarErrorAvgs[0:10]
radarBlueErrorsAvg = radarErrorAvgs[10:]
radarBarChartTitle = 'Comparison of Average Errors for Blue and Orange Visualizations for each Data Array for Radar Charts'
pc.createBarChart(radarBarChartTitle, radarOrangeErrorsAvg, radarBlueErrorsAvg, radarBarCompGraph)


#bar chart processing and results
barErrors = pc.errors(barInput, colNames, dif, barErrorsOutput)
barErrorAvgs = barErrors.mean().to_list() #average errors for each viz across all participants
pc.viz(dataStd, barErrorAvgs[0:10], "Average Errors for Orange Bar Visualizations", barAvgErrorsGraphOrange)
pc.viz(dataStd, barErrorAvgs[10:], "Average Errors for Blue Bar Visualizations", barAvgErrorsGraphBlue)
barOrangeErrorsAvg = barErrorAvgs[0:10]
barBlueErrorsAvg = barErrorAvgs[10:]
barBarChartTitle = 'Comparison of Average Errors for Blue and Orange Visualizations for each Data Array for Bar Charts'
pc.createBarChart(barBarChartTitle, barOrangeErrorsAvg, barBlueErrorsAvg, barBarCompGraph)

#graph the difference between the standard deviation and errors for the datasets
#orange errors; the first 10 values in the avg errors array
#blue errors



