import pandas as pd
import fns
import process as pc
import matplotlib

arrays = "/home/taya/finalProject-yakovenko-kittur-stjean/data/all_arrays.csv"
radarInput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/radarChartExperiment.csv"
radarErrorsOutput = "/home/taya/finalProject-yakovenko-kittur-stjean/analysis/masterData/radarErrors.csv"

colNames = ['o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8', 'o9', 'o10',
            'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10']

#take all the data arrays and find the true difference for each of the first two elements
dfArray = pd.read_csv("/home/taya/finalProject-yakovenko-kittur-stjean/data/all_arrays.csv")
dfArray['difference'] = dfArray['values'].map(lambda x: fns.compute_difference(x))
dif = dfArray['difference']
dataStd = fns.std(arrays)


#find all dataframe errors for each viz type
radarErrors = pc.errors(radarInput, colNames, dif, radarErrorsOutput)
radarErrorAvgs = radarErrors.mean().to_list() #average errors for each viz across all participants
pc.viz(dataStd, radarErrorAvgs[0:10], "Average Errors for Orange Radar Visualizations")



#graph the difference between the standard deviation and errors for the datasets
#orange errors; the first 10 values in the avg errors array
#blue errors



