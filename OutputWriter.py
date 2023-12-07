# Jill Torkelson
# ISQA 3900
# 11/28/2023

# This program asks user for city and utilizes an API to gather weather data and
# output weather data to a file


from datetime import datetime
from formatTime import format_date
import pytemperature


def write_file(json_data, city):
    # functions not working because wtime is a string
    # I had previously set up to use now - which is date time object
    # I need to find a diff regex to pull out the date time or use the now?
    wtime = json_data['timelines']['minutely'][0]['time']
    today = datetime.strptime(wtime, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = format_date(today)
    ctemp = json_data['timelines']['minutely'][0]['values']['temperature']
    ftemp = str(pytemperature.c2f(ctemp))
    cloud_cover = str(json_data['timelines']['minutely'][0]['values']['cloudCover'])
    humidity = str(json_data['timelines']['minutely'][0]['values']['humidity'])
    prec_prob = str(json_data['timelines']['minutely'][0]['values']['precipitationProbability'])
    wind_dirc = str(json_data['timelines']['minutely'][0]['values']['windDirection'])
    wind_speed = str(json_data['timelines']['minutely'][0]['values']['windSpeed'])

    print("\n\n\ntime = " + wtime)
    print("temp in C = " + str(ctemp))
    print("temp in F = " + ftemp)
    print("% Cloud Cover: " + cloud_cover)
    print("Humidity: " + humidity)
    print("Precipitation Probability: " + prec_prob)
    print("Wind Direction: " + wind_dirc)
    print("Wind Speed: " + wind_speed)

    try:
        with open('weather.txt', 'w') as outfile:
            outfile.write("Current weather for " + city + " on " + formatted_date + "\n")
            outfile.write("temp in C = " + str(ctemp) + "\n")
            outfile.write("temp in F = " + str(ftemp) + "\n")
            outfile.write("% Cloud Cover: " + cloud_cover + "\n")
            outfile.write("Humidity: " + humidity + "\n")
            outfile.write("Precipitation Probability: " + prec_prob + "\n")
            outfile.write("Wind Direction: " + wind_dirc + "\n")
            outfile.write("Wind Speed: " + wind_speed + "\n")
    except FileNotFoundError:
        print(f'Could not find file\n')
    except Exception:
        print("Error writing to file\n")