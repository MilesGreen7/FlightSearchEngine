import json
import sys

continentList = ['North America', 'South America', 'Africa', 'Europe', 'Asia', 'Oceania']

data = ''
json_file = "airport data.json"

try:
    with open(json_file, "r") as f:
    	data = json.load(f)
except FileNotFoundError:
    print("Error")


while data != '':
	dataIn = input("\nEnter Continent, Country, code, passengers, longitude, latitude...\n\n")
	if dataIn == 'q':
		break
	if ',' not in dataIn:
		print('error')
		break


	index = 0
	while index < len(dataIn):
		if dataIn[index] == ',' and (dataIn[index-1] == ' ' or dataIn[index+1] == ' '):
			print("error")
			sys.exit()
		elif dataIn[index] == ' ' and (dataIn[index-1] == ' ' or dataIn[index+1] == ' '):
			print("error")
			sys.exit()
		index += 1


	dataIn = dataIn.split(',')
	if dataIn[0] not in continentList:
		print('error')
		sys.exit()


	new_country = ''

	if len(dataIn) >= 6 and len(dataIn) % 4 == 2:
		i = 2
		new_country = {
			"country": dataIn[1],
			"airports": []
		}
		while i < len(dataIn):
			new_country["airports"].append(
				{
					"airport_code": dataIn[i],
		            "estimated_yearly_passengers": float(dataIn[i+1]),
		            "location": {
		                "longitude": float(dataIn[i+2]),
		                "latitude": float(dataIn[i+3])
		            }
				}
			)
			i += 4

	else:
		print("Error")
		break

	if new_country != '':
		data[dataIn[0]].append(new_country)
		with open(json_file, "w") as f:
			json.dump(data, f, indent=4)
