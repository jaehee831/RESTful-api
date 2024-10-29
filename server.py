from flask import Flask, request, render_template, jsonify
import requests
import json
from time import time

app = Flask(__name__)
# Server-side cache (in-memory storage)
cache = {}
# Cache expiry time in seconds (1 hour)
CACHE_EXPIRY = 3600

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page for user input

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get city name from request query
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    # Step 1: Check the cache first
    if city in cache:
        cached_data, timestamp = cache[city]
        # If the cached data is not expired, return it
        if time() - timestamp < CACHE_EXPIRY:
            print("Returning cached data.")
            return jsonify(cached_data)  
    
    # Step 2: If no cache or cache expired, call the weather API
    apikey = "f4ffc2b9468cb52aecf9cc68ebce09a2"  
    lang = "kr"
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

    result = requests.get(api)
    
    if result.status_code == 200:
        data = json.loads(result.text)
        
        # Step 3: Store the fetched data in the cache
        cache[city] = (data, time())
        # Step 4: Set browser caching using HTTP headers (Cache-Control)
        response = jsonify(data)  
        response.headers['Cache-Control'] = 'public, max-age=3600'  # Cache for 1 hour
        return response
    else:
        return jsonify({"error": "Failed to retrieve data from OpenWeatherMap"}), result.status_code

if __name__ == '__main__':
    app.run(debug=True)