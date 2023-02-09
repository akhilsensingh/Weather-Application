import requests
import json

# API key for OpenWeatherMap
api_key = "58e9fa81e3043c1b5009008f964335ff"

# Function to retrieve weather information for a specific location
def get_weather_info(place, api_key):
    # API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}"
    
    # Make a request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = json.loads(response.text)
        
        # Extract the relevant information from the JSON data
        main_info = data["main"]
        weather_info = data["weather"][0]
        temperature = main_info["temp"]
        feels_like = main_info["feels_like"]
        description = weather_info["description"]
        
        # Return the information as a dictionary
        return {
            "temperature": temperature,
            "feels_like": feels_like,
            "description": description
        }
    else:
        # Return an error message if the request was not successful
        return "Error: Could not retrieve weather information due to some issue"

# Example usage
place = input("Enter a place name: ")
weather_info = get_weather_info(place, api_key)

print("Temperature of this place :", weather_info["temperature"])
print("Feels like :", weather_info["feels_like"])
print("Description :", weather_info["description"])