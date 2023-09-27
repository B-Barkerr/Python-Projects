import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"  # You can change units to "metric" for Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    api_key = "b28e0f155b90deaeb30c611d2ce0b947"  # Replace with your OpenWeatherMap API key
    city = input("Enter the name of the city: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        # Extract relevant weather information from the API response
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°F")
        print(f"Description: {description.capitalize()}")
    else:
        print("Unable to fetch weather data. Please check your city name or API key.")

if __name__ == "__main__":
    main()
