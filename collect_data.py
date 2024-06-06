import requests
import time
import datetime 
import pytz

LOCAL_API = "http://192.168.1.209:8080/currentState" 
WEATHER_API = "https://api.openweathermap.org/data/2.5/weather?lat=40.683961&lon=-73.817874&units=metric&appid=8a757115f1d5c68d542ff30473fdf820" 
WAIT_TIME = 300 # seconds

def fetch_weather_data():
    output_file = "data_june5_night.txt" 
    est = pytz.timezone('US/Eastern')
    while True:
        try:
            # Call the first weather API
            response1 = requests.get(WEATHER_API)
            data1 = response1.json()
            temp1 = data1['main']['temp']
            humidity1 = data1['main']['humidity']

            # Call the second weather API
            response2 = requests.get(LOCAL_API)
            data2 = response2.json()
            temp2 = data2['last_temperature']  # Replace with actual JSON key
            humidity2 = data2['last_humidity']  # Replace with actual JSON key'''

           # Get the current timestamp in UTC, convert to EST and format it
            timestamp_utc = datetime.datetime.now(pytz.utc)
            timestamp_est = timestamp_utc.astimezone(est)
            #timestamp_str = timestamp_est.strftime("%Y-%m-%d %H:%M")

            # Write data to the file
            with open(output_file, 'a') as file:
                file.write(f"{timestamp_est},{temp1},{humidity1},{temp2},{humidity2}\n")

            print(f"{timestamp_est},{temp1},{humidity1},{temp2},{humidity2}")
            time.sleep(WAIT_TIME)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(WAIT_TIME) 


fetch_weather_data()