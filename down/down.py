import os

import requests
import pandas as pd
from datetime import datetime, timedelta
from log.log import setup_logger

logger = setup_logger(__name__, log_file="down.log")

class DownloadData:
    def __init__(self, location: list=None, start_date: str = "2000-01-01",
                 end_date: str = "", save_path:str = "datasets") -> None:
        self.url_template = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{name}/{start_date}/{end_date}?unitGroup=metric&key=Z8S3WF67S4GGD8GVW7EZXCYKR&options=preview&contentType=json"
        if end_date == "":
            end_date = datetime.today().__str__()
        self.start_date = start_date
        self.end_date = end_date
        self.save_path = save_path
        if location is None:
            location = ["Hanoi", "DaNang", "HoChiMinh"]
        self.location = location

    # Function to get weather data for a specific range of dates
    def fetch_weather_data(self, name:str, start_date:str, end_date:str) -> dict | None:
        url = self.url_template.format(name = name, start_date=start_date, end_date=end_date)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to retrieve data for {start_date} to {end_date}. HTTP Status Code: {response.status_code}")
            return None

    # Function to split the date range into chunks and fetch data
    def fetch_data_in_chunks(self, name, chunk_size=1000):
        start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
        all_data = []
        current_date = start_date_obj

        while current_date < datetime.now():
            chunk_end_date = current_date + timedelta(days=chunk_size - 1)
            data = self.fetch_weather_data(name, current_date.strftime("%Y-%m-%d"), chunk_end_date.strftime("%Y-%m-%d"))

            if data and 'days' in data:
                for day in data['days']:
                    all_data.append({
                        "name": data.get("resolvedAddress", "Unknown"),
                        "datetime": day.get("datetime"),
                        "tempmax": day.get("tempmax"),
                        "tempmin": day.get("tempmin"),
                        "temp": day.get("temp"),
                        "feelslikemax": day.get("feelslikemax"),
                        "feelslikemin": day.get("feelslikemin"),
                        "feelslike": day.get("feelslike"),
                        "dew": day.get("dew"),
                        "humidity": day.get("humidity"),
                        "precip": day.get("precip"),
                        "precipprob": day.get("precipprob"),
                        "precipcover": day.get("precipcover"),
                        "preciptype": day.get("preciptype"),
                        "snow": day.get("snow"),
                        "snowdepth": day.get("snowdepth"),
                        "windgust": day.get("windgust"),
                        "windspeed": day.get("windspeed"),
                        "winddir": day.get("winddir"),
                        "sealevelpressure": day.get("sealevelpressure"),
                        "cloudcover": day.get("cloudcover"),
                        "visibility": day.get("visibility"),
                        "solarradiation": day.get("solarradiation"),
                        "solarenergy": day.get("solarenergy"),
                        "uvindex": day.get("uvindex"),
                        "severerisk": day.get("severerisk"),
                        "sunrise": day.get("sunrise"),
                        "sunset": day.get("sunset"),
                        "moonphase": day.get("moonphase"),
                        "conditions": day.get("conditions"),
                        "description": day.get("description"),
                        "icon": day.get("icon"),
                        "stations": day.get("stations")
                    })

                    # Update the current_date to the last day fetched
                    current_date = datetime.strptime(day['datetime'], "%Y-%m-%d")
                    # Break the loop if we've fetched up to the last available date
                    if current_date > datetime.now():
                        break

            else:
                break

        return all_data


    def run(self):
        for name in self.location:
            data = self.fetch_data_in_chunks(name)
            df = pd.DataFrame(data)
            os.makedirs(self.save_path, exist_ok=True)
            df.to_csv(os.path.join(self.save_path, f"{name}.csv"), index=False)
            logger.info(f"Data fetched and saved to {name}.csv. Total records: {len(data)}")

# name = "DaNang"
# # Fetch data from 2000-01-01
# start_date = "2000-01-01"
# data = fetch_data_in_chunks(name, start_date, chunk_size=1000)
#
# # Convert to DataFrame and save to CSV
# df = pd.DataFrame(data)
# df.to_csv(f"{name}.csv", index=False)
#
# print(f"Data fetched and saved to {name}.csv. Total records: {len(data)}")
