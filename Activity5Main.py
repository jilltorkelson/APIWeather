#Jill Torkelson
#ISQA 3900
#11/28/2023

# This program asks user for city and utilizes an API to gather weather data and
# output weather data to a file


import requests
from OutputWriter import write_file
from datetime import datetime
from formatTime import format_date

print("ISQA 3900 Weather API")
right_now = format_date(datetime.now())
print(right_now)
print("\n")
choice = "y"

try:
    #app configures url to generate JSON data
    api_start = 'https://api.tomorrow.io/v4/weather/forecast?'
    apikey = '&apikey=cI3XDIc1iWHlyCFcS2S78BnU9jF728aO'
except:
    print("Error")


while choice == "y":
    city = input("Enter city name: ")
    location = "location=" + city
    url = api_start + location + apikey
    print(url)

    json_data = requests.get(url).json()


# This API limits the number of requests per hour. try again later if your limit is reached.
    if 'type' in json_data.keys() and json_data['type'] == "Too Many Calls":
        print("API Call limit reached - try again later")
    #An invalid city name was entered - try again
    elif 'type' in json_data.keys() and json_data['type'] == 'Invalid Query Parameters':
        print("Invalid location entered")
    elif 'timelines' in json_data.keys():
        write_file(json_data, city)
    else:
        print("An error occurred: ")
        print(json_data)
    choice = input("\nWould you like to enter a new city (y or n): ")

