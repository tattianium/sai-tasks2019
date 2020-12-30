#!/usr/bin/python3

# Сайт https://openweathermap.org/

def hourly_weather_KGO(URL, lattitude, longitude, API_key, name_table):
    """Take weather parameters each minute or hour"""
    
    import requests
    import json
    import csv
    import pandas as pd
        
    json_data = requests.get(URL).json()
    name_table.writerow([pd.Timestamp.now(), json_data['current']['temp'], json_data['current']['feels_like'], json_data['current']['pressure'], json_data['current']['humidity'], json_data['current']['clouds'],json_data['current']['wind_speed'],json_data['current']['wind_deg'], json_data['current']['visibility']])
    print('Данные записаны', pd.Timestamp.now()) #отображаем время в которое произошла запись данных
    return




def main():
    import schedule 
    import csv
    
    fieldnames = ['current_time','temperature','temperature_feel','pressure','humidity','clouds','wind_speed','wind_degree','visibility']

    with open('hourly_weather_KGO.csv', 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)

        with open('api_key.txt') as a:				
            api_key0 = str(a.readline()[:-1])

        api_key = api_key0
        lat = "43.74611" # KGO coordinates
        lon = "42.6675"
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
        
        schedule.every(1).minutes.do(hourly_weather_KGO, url, lat, lon, api_key, writer) # поминутное накопление(для упрощения проверки)
        #schedule.every(1).hour.do(hourly_weather_KGO, url, lat, lon, api_key, writer) # почасовое накопление
        while True:   
            schedule.run_pending()

    return




if __name__ == "__main__":
    main()