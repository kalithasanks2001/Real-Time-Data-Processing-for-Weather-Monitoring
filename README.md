# Real-Time Data Processing for Weather Monitoring

This Python script provides real-time weather data monitoring by fetching information from the OpenWeatherMap API. The data is processed and stored for analysis, with options to generate visualizations for temperature trends over time.

## Features

- Fetch real-time weather data from the OpenWeatherMap API for multiple cities.
- Store the weather data in a list for analysis and visualization.
- Convert temperature from Kelvin to Celsius.
- Automatically fetch and update weather data at regular intervals using `schedule`.
- Visualize weather trends using `matplotlib`.

## Requirements

- Python 3.x
- Required Python libraries: `requests`, `schedule`, `matplotlib`
  
  You can install them using the following command:

  pip install requests schedule matplotlib

- An API key from [OpenWeatherMap](https://openweathermap.org/).

## Setup

1. Clone the repository:

   git clone https://github.com/kalithasanks2001/Real-Time-Data-Processing-Weather-Monitoring.git

2. Navigate to the project directory:

   cd Real-Time-Data-Processing-Weather-Monitoring

3. Install the required dependencies:

   pip install -r requirements.txt

4. Replace the placeholder API key with your own in the script:

   ```python
   api_key = '4d0b73ac6ef7c3d413df5ed712ed2081'
   ```

## Usage

1. Add the cities you want to monitor by updating the `cities` list in the script:

   python
   cities = ['London', 'New York', 'Tokyo', 'Mumbai']

2. Run the script:

   python RealTimeWeatherMonitoring.py

   The script will fetch weather data at regular intervals and store it in the global `weather_data` list.

3. Visualize the temperature data by generating a plot:

   ```python
   # Example of generating a temperature trend plot
   plot_weather_data(weather_data)
   ```

## Example

```python
# Example to fetch and visualize weather data
cities = ['London', 'Paris', 'Berlin']
fetch_weather_data(api_key, cities)
plot_weather_data(weather_data)
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements.
