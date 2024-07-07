# Weather API

This project provides a simple RESTful API to retrieve current weather information for a specific city using WeatherAPI.com.

## Features

- **Real-time weather data:** Fetches up-to-date weather conditions from WeatherAPI.com.
- **Easy-to-use endpoint:**  A single, intuitive GET endpoint (`/weather`) for requesting data.
- **JSON response format:** Returns weather details in a structured and easy-to-parse JSON format.
- **Error handling:**  Handles common errors like invalid city names, API key issues, and service unavailability.

## Endpoint

- **GET /weather**

    - **Query parameter:** `city` (name of the city)
    - **Response:** JSON object containing:
        - `city` (string)
        - `temperature` (float)
        - `condition` (string)
        - `humidity` (int)
        - `wind_speed` (float)
    - **Status Codes:**
        - `200 OK`: Successful request
        - `400 Bad Request`: Missing or invalid city parameter
        - `401 Unauthorized`: Invalid WeatherAPI.com API key
        - `404 Not Found`: City not found 
        - `500 Internal Server Error`: Error fetching data from WeatherAPI.com


## Setup

1. **Obtain an API Key:**
   - Sign up for a free account at [WeatherAPI.com](https://www.weatherapi.com/) to obtain your API key.

2. **Install Python:**
   - If you don't have Python installed, download and install it from [python.org](https://www.python.org/).

3. **Install Dependencies:**
   - Navigate to the project directory in your terminal and run (your pip command may differ based on your dev environment setup and operating system, for my Macbook its pip3, yours may simply be pip, etc.):
     ```bash
     pip3 install -r requirements.txt
     ```

4. **Configure the API:**
   - Open the `app.py` file and replace `'YOUR_API_KEY'` with your actual API key from WeatherAPI.com.

5. **Run the API Server:**
   - In your terminal, execute the following command (your python command may differ based on your dev environment setup and operating system, for my Macbook its python3, yours may simply be python, or py, etc.):
     ```bash
     python3 app.py
     ```

## Usage

Once the API server is running (typically at `http://127.0.0.1:5000/`), you can make requests using your web browser, Postman, curl, or any HTTP client.

**Example URL for your request:**

```http://127.0.0.1:5000/weather?city=London```

**Example Response (Success):**

```json
{
    "city": "London",
    "temperature": 12.5,
    "condition": "Partly cloudy",
    "humidity": 70,
    "wind_speed": 15.4
}
```
**Accreditation Notes:**

- I used Google Gemini Advanced to help me debug some of the traceback calls that I could not solve using online resources in addition to the course materials such as Stack Overflow, and to help me with some details for this readme file.

- I use Stack Overflow & W3 Schools as a resource in most of my coding, mostly to help understand what is happening in the terminal errors when I cannot find the information in the course materials.
