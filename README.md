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

![image.png](image.png)

![image.png](image%201.png)

![image.png](image%202.png)

![image.png](image%203.png)

- The above image shows how the weather information (temperature, humidity, wind speed, etc.) is fetched from the server and displayed in the web and terminal.

## How Browser Cache Was Implemented

Browser caching is implemented using HTTP headers, specifically the `Cache-Control` header in the server's response. This instructs the client browser to cache the response for a specified duration (1 hour in this case). After the initial request, any subsequent request for the same weather data within the caching period will retrieve the cached response, reducing the need for redundant API calls.

![server.py](image%204.png)

server.py

## How Server Cache Was Implemented

Server-side caching is implemented using an in-memory dictionary (`cache`). The weather data for each city is cached along with the timestamp of when it was fetched. If the same city is requested within 1 hour, the cached data is returned instead of making a new API request. The cache is automatically invalidated after the expiration time (1 hour).

![server.py](image%205.png)

server.py

## Authentification in Server

The OpenWeatherMap API requires authentication using an API key. The `server.py` code uses the API key via the `apikey` variable, and API calls are made by including it in the URL.

![image.png](image%206.png)