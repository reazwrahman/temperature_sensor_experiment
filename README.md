To evaluate the consistency of the DHT22 temperature sensor's readings, I conducted a series of tests
comparing its data to the OpenWeatherMap API. For control, I used the OpenWeatherMap API to retrieve
weather data for my current location. Every five minutes, I pinged my backend API to gather readings
from the DHT22 sensor and the weather data from OpenWeatherMap.
