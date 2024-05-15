'''0798547112f0c4825cd75cd5bd62bb94 api'''
import requests

def get_weather(api_key, state, city):
    """Get current weather data from OpenWeatherMap API"""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    """Display weather information in a user-friendly format"""
    if data["cod"] == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print(f"Wind speed(m/s) : {data['wind']['speed']}")
        print(f"humidity(%) : {data['main']['humidity']}")
    else:
        print("Failed to fetch weather data. Please check the location.")

def main():
    api_key = "0798547112f0c4825cd75cd5bd62bb94"
    state = input("Enter the state: ")
    city = input("Enter the city: ")

    weather_data = get_weather(api_key, state, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
