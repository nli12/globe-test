import csv 
import math

data_file = open('dates_coordinates_rounded.csv')
data_csv = csv.reader(data_file)

decades_file = open('decades.json', 'w')

decades_data = {1970:{},1980:{},1990:{},2000:{},2010:{}}

for row in data_csv:

	year = int(row[0])
	latitude = int(row[1])
	longitude = int(row[2])
	decade = year - (year % 10)
	
	# Ensures that each decade has the same number of data points 
	for decade_temp in decades_data:
		if not ((latitude,longitude) in decades_data[decade_temp]):
			decades_data[decade_temp][(latitude,longitude)] = 0;
    
    # Increments the frequency for that coordinate in that decade
	decades_data[decade][(latitude,longitude)] += 0.0005
	

# Formats the dictionary data and writes it to a JSON file

first = True

decades_file.write('[')

for decade in decades_data:

	json_list = []

	if (first):
		first = False
	else:
		decades_file.write(',')

	decades_file.write('["' + str(decade) + '",[')

	for coordinate in decades_data[decade]:
		json_list.extend([str(coordinate[0]), str(coordinate[1]), str(decades_data[decade][coordinate])])
	decades_file.write(','.join(json_list))

	decades_file.write(']]')

decades_file.write(']')

decades_file.close()

