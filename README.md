# ReadMe.md

## **Python and Library Environment**

The following Python environment and libraries are required for this project:

- Python Version: 3.8+
- Libraries:
    - Flask: To create the server and handle HTTP requests.
    - Requests: To send HTTP requests to the OpenWeatherMap API.
    - Time: To handle server-side cache expiration.
    - JSON: To handle JSON data formatting and parsing.

To install the required libraries, run the following command:

```bash
pip install Flask requests
```

## Usage Instructions

1. **Run the Flask server**:
    
    ```bash
    python server.py
    ```
    
2. **Run the client code**:
    
    ```bash
    python client.py
    ```
    
3. **Access the web interface**:
If you implemented the web interface, navigate to `http://127.0.0.1:5000/` in your browser and input a city name(ex. Seoul) to get the weather information. Make sure to batch `index.html` in `/templates`

Hierachy

```bash
/project-directory
│
├── server.py  
├── client.py  
├── /templates
│   └── index.html   
```

## Client Testing Image

Here is an example of the client testing interface showing weather information for the city of Seoul:

![image](https://github.com/user-attachments/assets/88ebd297-dab7-4ef8-8644-240c3ac2abf2)
![image 1](https://github.com/user-attachments/assets/47025f0f-81e5-400d-bac9-f2560c951e99)
![image 2](https://github.com/user-attachments/assets/2449eb37-cbd4-4136-bab4-c88e5fc2400f)
![image 3](https://github.com/user-attachments/assets/118b9dbc-f8b1-40ab-93a6-437fc24e2a57)

- The above image shows how the weather information (temperature, humidity, wind speed, etc.) is fetched from the server and displayed in the web and terminal.

## How Browser Cache Was Implemented

Browser caching is implemented using HTTP headers, specifically the `Cache-Control` header in the server's response. This instructs the client browser to cache the response for a specified duration (1 hour in this case). After the initial request, any subsequent request for the same weather data within the caching period will retrieve the cached response, reducing the need for redundant API calls.

![image 4](https://github.com/user-attachments/assets/143fe5c3-d7d1-4798-960d-2a94d21ee595)

server.py

## How Server Cache Was Implemented

Server-side caching is implemented using an in-memory dictionary (`cache`). The weather data for each city is cached along with the timestamp of when it was fetched. If the same city is requested within 1 hour, the cached data is returned instead of making a new API request. The cache is automatically invalidated after the expiration time (1 hour).

![image 5](https://github.com/user-attachments/assets/ccc6855c-3ada-42c6-bd8d-264477bd7874)

server.py

## Authentification in Server

The OpenWeatherMap API requires authentication using an API key. The `server.py` code uses the API key via the `apikey` variable, and API calls are made by including it in the URL.

![image 6](https://github.com/user-attachments/assets/1d531e7c-4f1e-4bba-901b-20efa64f15dc)
