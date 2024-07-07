"""
This module provides a simple Flask-based RESTful API for fetching current
weather information for a specified city using the WeatherAPI.com service.

Usage:

1. Obtain a WeatherAPI.com API key.
2. Replace 'YOUR_API_KEY' in this file with your actual API key.
3. Install dependencies: `pip3 install -r requirements.txt` (your pip command may differ based on your dev environment setup and operating system, for my Macbook its pip3, yours may simply be pip, etc.)
4. Run the script: `python3 app.py` (your python command may differ based on your dev environment setup and operating system, for my Macbook its python3, yours may simply be python, or py, etc.)
5. Access the API via:
   - Root URL: `http://127.0.0.1:5000/`
   - Weather endpoint: `http://127.0.0.1:5000/weather?city=<city_name>` 
   - For example: `http://127.0.0.1:5000/weather?city=London`
"""

import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Your WeatherAPI.com API key (replace with your actual key)
WEATHER_API_KEY = 'YOUR_API_KEY'

# Custom route for the root URL
@app.route('/')
def index():
    """
        Root endpoint: Provides a welcome message and instructions on how to use the API.
    """
    return "Welcome to the Weather API! Try accessing /weather?city=your_city, for example: http://127.0.0.1:5000/weather?city=London"

@app.route('/weather', methods=['GET'])
def get_weather():
    """
        Fetches current weather data for the specified city.

        Query parameters:
            city (str): Name of the city (required)

        Returns:
            JSON: Weather information (city, temperature, condition, humidity, wind speed) on success.
            JSON: Error message and appropriate status code (400, 401, 500) on failure.
    """
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    # Construct the WeatherAPI.com API URL
    base_url = 'http://api.weatherapi.com/v1/current.json'
    complete_url = f'{base_url}?key={WEATHER_API_KEY}&q={city}'

    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise exception for bad responses (4xx and 5xx)
        data = response.json()
        
        # Extract and return relevant weather data
        return jsonify({
            "city": data['location']['name'],
            "temperature": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity'],
            "wind_speed": data['current']['wind_kph']
        })

    except requests.exceptions.RequestException as e:
        # Handle different error scenarios
        if response.status_code == 400:
            return jsonify({"error": "Invalid city name"}), 400
        elif response.status_code == 401:
            return jsonify({"error": "Unauthorized: Invalid API key"}), 401
        else: # General error (could be API outage, network issue, etc.)
            return jsonify({"error": f"Error fetching weather data: {e}"}), 500
        
# Start the Flask development server if run directly
if __name__ == '__main__':
    app.run(debug=True)