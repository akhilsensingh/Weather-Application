# Weather-Application
This code is a weather application that takes a city name as input and returns the temperature, feels like, and description for that city. The program uses the requests and json libraries to retrieve and parse data from the OpenWeatherMap API.

The API key for OpenWeatherMap is defined as a string api_key = "58e9fa81e3043c1b5009008f964335ff".

The get_weather_info function takes a city name and api_key as input and returns a dictionary with the temperature, feels like, and description for that city.

The function starts by constructing the API endpoint using the city name and API key. It then makes a GET request to the API using the requests.get function and stores the response in the response variable.

The code checks if the request was successful by checking if the response.status_code is equal to 200. If the request was successful, the function parses the JSON data from the response using the json.loads function and stores the result in the data variable.

The relevant information from the JSON data is extracted by accessing the values stored in the main and weather keys of the data. The temperature, feels like, and description are stored in the temperature, feels_like, and description variables, respectively.

The function returns a dictionary with the extracted information as its values. If the request was not successful, the function returns an error message string "Error: Could not retrieve weather information".

Finally, the code includes an example usage of the program by prompting the user to enter a city name and storing the input in the city variable. The weather_info variable stores the result of calling the get_weather_info function with the city and api_key as input. The print function is then used to display the temperature, feels like, and description for the given city.
