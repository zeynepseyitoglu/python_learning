#the goal is to learn too use csv files with pandas
#csv is just tabular data
import pandas
import csv

with open('weather_data.csv', 'r') as data_file:
    #data = data_file.readlines()
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

data_two = pandas.read_csv('weather_data.csv')
print(data_two)