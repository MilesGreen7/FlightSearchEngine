import pandas as pd
import json
import sys
import pyperclip
import math


def passengerFormat(s):
    if isinstance(s, float):
        if math.isnan(s):
            return 0.0
        return s

    if 'NA' in s or 'N/A' in s:
        return 0.0

    acceptableChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    w = 0
    newFloat = ''
    flag = False
    while w < len(s):
        if s[w] == '.':
            print('error')
            sys.exit()
        elif s[w] in acceptableChar:
            newFloat += s[w]
            flag = True
        w += 1
    if not flag:
        print('error')
        sys.exit()
    return float(newFloat)*10**(-6)

def internationDomestic(x):
    if x[0:3] == 'Yes':
        return 'international'
    if x[0:2] == 'No':
        return 'domestic'
    print('error')
    sys.exit()

        
continentList = ['North America', 'South America', 'Africa', 'Europe', 'Asia', 'Oceania']

CONTINENT = input("Enter continent: ")
COUNTRY = input("Enter country: ")
FILENAME = input("Enter csv filename: ")

if CONTINENT not in continentList:
    print('error')
    sys.exit()
if not COUNTRY.isalpha():
    print('error')
    sys.exit()

df = pd.read_csv(FILENAME)


data = ''
json_file = "airport data - big countries.json"

try:
    with open(json_file, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error")

new_country = {
    "country": COUNTRY,
    "airports": []
}


if data == '':
    print('error')
    sys.exit()
clipBoardStr = ''
for index, row in df.iterrows():
    new_country["airports"].append(
        {
            "airport_code": row['IATA'],
            "international/domestic": internationDomestic(row['InternationalService']),
            "estimated_yearly_passengers": passengerFormat(row['LatestPassengers']),
            "location": {
                "longitude": float(row['Longitude']),
                "latitude": float(row['Latitude'])
            }
        }
    )
    clipBoardStr += row['IATA'] + ','

clipBoardStr = clipBoardStr[:-1]

data[CONTINENT].append(new_country)
pyperclip.copy(clipBoardStr)
with open(json_file, "w") as f:
    json.dump(data, f, indent=4)
