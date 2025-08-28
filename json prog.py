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
	new_country = ''
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





	if len(dataIn) == 6:
		new_country = {
		    "country": dataIn[1],
		    "airports": [
		        {
		            "airport_code": dataIn[2],
		            "estimated_yearly_passengers": float(dataIn[3]),
		            "location": {
		                "longitude": float(dataIn[4]),
		                "latitude": float(dataIn[5])
		            }
		        }
		    ]
		}

	elif len(dataIn) == 10:
		new_country = {
		    "country": dataIn[1],
		    "airports": [
		        {
		            "airport_code": dataIn[2],
		            "estimated_yearly_passengers": float(dataIn[3]),
		            "location": {
		                "longitude": float(dataIn[4]),
		                "latitude": float(dataIn[5])
		            }
		        },
		        {
		            "airport_code": dataIn[6],
		            "estimated_yearly_passengers": float(dataIn[7]),
		            "location": {
		                "longitude": float(dataIn[8]),
		                "latitude": float(dataIn[9])
		            }
		        }
		    ]
		}
	elif len(dataIn) == 14:
		new_country = {
		    "country": dataIn[1],
		    "airports": [
		        {
		            "airport_code": dataIn[2],
		            "estimated_yearly_passengers": float(dataIn[3]),
		            "location": {
		                "longitude": float(dataIn[4]),
		                "latitude": float(dataIn[5])
		            }
		        },
		        {
		            "airport_code": dataIn[6],
		            "estimated_yearly_passengers": float(dataIn[7]),
		            "location": {
		                "longitude": float(dataIn[8]),
		                "latitude": float(dataIn[9])
		            }
		        },
		        {
		            "airport_code": dataIn[10],
		            "estimated_yearly_passengers": float(dataIn[11]),
		            "location": {
		                "longitude": float(dataIn[12]),
		                "latitude": float(dataIn[13])
		            }
		        }
		    ]
		}
	elif len(dataIn) == 18:
		new_country = {
		    "country": dataIn[1],
		    "airports": [
		        {
		            "airport_code": dataIn[2],
		            "estimated_yearly_passengers": float(dataIn[3]),
		            "location": {
		                "longitude": float(dataIn[4]),
		                "latitude": float(dataIn[5])
		            }
		        },
		        {
		            "airport_code": dataIn[6],
		            "estimated_yearly_passengers": float(dataIn[7]),
		            "location": {
		                "longitude": float(dataIn[8]),
		                "latitude": float(dataIn[9])
		            }
		        },
		        {
		            "airport_code": dataIn[10],
		            "estimated_yearly_passengers": float(dataIn[11]),
		            "location": {
		                "longitude": float(dataIn[12]),
		                "latitude": float(dataIn[13])
		            }
		        },
		        {
		            "airport_code": dataIn[14],
		            "estimated_yearly_passengers": float(dataIn[15]),
		            "location": {
		                "longitude": float(dataIn[16]),
		                "latitude": float(dataIn[17])
		            }
		        }
		    ]
		}
	else:
		print("Error")
		break

	if new_country != '':
		data[dataIn[0]].append(new_country)
		with open(json_file, "w") as f:
			json.dump(data, f, indent=4)
		


