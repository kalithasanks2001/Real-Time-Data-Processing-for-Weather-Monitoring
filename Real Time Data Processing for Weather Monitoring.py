#!/usr/bin/env python
# coding: utf-8

# # Real Time Data Processing for Weather Monitoring

# # Importing Libraries

# In[4]:


import requests
import schedule
import time
from datetime import datetime
import matplotlib.pyplot as plt


# # Global variables to store weather data

# In[5]:


weather_data = []
daily_summary = {}


# # Function to convert temperature from Kelvin to Celsius

# In[6]:


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


# # Function to fetch weather data from OpenWeatherMap API

# In[7]:


def fetch_weather_data(api_key, cities):
    global weather_data
    for city in cities:
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather_info = {
                    "city": city,
                    "temp": kelvin_to_celsius(data['main']['temp']),
                    "feels_like": kelvin_to_celsius(data['main']['feels_like']),
                    "main": data['weather'][0]['main'],
                    "timestamp": datetime.now()
                }
                weather_data.append(weather_info)
                print(f"Weather data for {city}: {weather_info}")
            else:
                print(f"Failed to retrieve data for {city}. Error: {data.get('message', 'Unknown error')}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # After fetching all data, calculate daily summary and visualize it
    calculate_daily_summary()
    visualize_daily_summary()


# # Function to calculate daily aggregates

# In[8]:


def calculate_daily_summary():
    global weather_data, daily_summary
    
    # Group data by city
    cities = list(set([entry['city'] for entry in weather_data]))
    for city in cities:
        city_data = [entry for entry in weather_data if entry['city'] == city]
        
        # Calculate daily aggregate metrics
        avg_temp = sum([entry['temp'] for entry in city_data]) / len(city_data)
        max_temp = max([entry['temp'] for entry in city_data])
        min_temp = min([entry['temp'] for entry in city_data])
        dominant_weather = max(set([entry['main'] for entry in city_data]), key=[entry['main'] for entry in city_data].count)
        
        daily_summary[city] = {
            "average_temp": avg_temp,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "dominant_weather": dominant_weather,
            "last_updated": datetime.now()
        }
        print(f"Daily summary for {city}: {daily_summary[city]}")


# # Function to visualize data

# In[9]:


def visualize_daily_summary():
    if not daily_summary:
        print("No data available to visualize.")
        return
    
    cities = list(daily_summary.keys())
    avg_temps = [daily_summary[city]['average_temp'] for city in cities]
    max_temps = [daily_summary[city]['max_temp'] for city in cities]
    min_temps = [daily_summary[city]['min_temp'] for city in cities]

    plt.figure(figsize=(10, 5))
    bar_width = 0.25
    x = range(len(cities))

    plt.bar(x, avg_temps, width=bar_width, color='blue', label='Average Temp')
    plt.bar([p + bar_width for p in x], max_temps, width=bar_width, color='red', alpha=0.5, label='Max Temp')
    plt.bar([p + bar_width*2 for p in x], min_temps, width=bar_width, color='green', alpha=0.5, label='Min Temp')

    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Weather Summary')
    plt.xticks([p + bar_width for p in x], cities)
    plt.legend()
    plt.tight_layout()
    plt.show()


# # Function to schedule tasks

# In[10]:


def schedule_tasks(api_key, cities, interval=5):
    # Schedule data fetch every 'interval' minutes
    schedule.every(interval).minutes.do(fetch_weather_data, api_key=api_key, cities=cities)
    
    while True:
        schedule.run_pending()
        time.sleep(1)


# # Main function to start the weather monitoring system

# In[ ]:


if __name__ == "__main__":
    # Replace with your API key from OpenWeatherMap
    API_KEY = '4d0b73ac6ef7c3d413df5ed712ed2081'
    CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    
    # Start scheduling tasks
    schedule_tasks(API_KEY, CITIES, interval=5)


# In[ ]:




