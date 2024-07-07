# Designing and Implementing a RESTful API for a Simple Weather App

 
## Objective:

In this assignment, you will apply the concepts and techniques learned in the lesson to design and implement a RESTful API for a simple weather app. You will demonstrate your understanding of API endpoints, HTTP methods, and API design principles.

 
## Problem Statement:

You are tasked with building a RESTful API for a simple weather app. The API should allow users to retrieve weather information for a specific city using data from WeatherAPI.com.

 

## Requirements:

### Sign up for a free account at WeatherAPI.com to obtain an API key.
Design and implement the following API endpoint:
   - Retrieve weather information for a specific city:

     - Endpoint: GET /weather

     - Query parameter: city (name of the city)

     - Response: HTTP 200 OK with a JSON object containing the following weather information:

       - City name

       - Current temperature

       - Weather condition (e.g., sunny, cloudy, rainy)

       - Humidity

       - Wind speed

### Follow RESTful API design principles and best practices:
   - Use appropriate HTTP methods for the endpoint (GET)

   - Use meaningful and consistent naming conventions for the endpoint and query parameter

   - Return appropriate status codes for different scenarios (e.g., 200, 404)

### Implement the API endpoint using a programming language of your choice (e.g., Node.js, Python, Java).
Use the WeatherAPI.com API to fetch the weather data for the specified city. You will need to make an HTTP request to the WeatherAPI.com API using your API key and parse the JSON response to extract the relevant weather information.
Handle error scenarios gracefully:
   - If the city is not found or the WeatherAPI.com API returns an error, return an appropriate error response (e.g., HTTP 404 Not Found) with an error message.

### Write clear and concise documentation for your API, including:
   - Description of the endpoint and its functionality

   - Request and response formats for the endpoint

   - Instructions on how to run the API server

   - Instructions on how to obtain an API key from WeatherAPI.com

### Test your API endpoint using a tool like Postman or cURL to ensure it is functioning as expected.
 

# Deliverables:

Source code for the implemented API endpoint
API documentation file (in PDF or Markdown format)
Postman collection or cURL commands for testing the API endpoint