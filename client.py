import requests

# Step 1: Client-Side Validation
def is_valid_city(city):
    # Validate that the city name is non-empty and alphabetic (no numbers or special characters)
    if city and city.isalpha():
        return True
    return False

# Step 2: Get user input
city = input("Enter the city name for weather information: ")

# Step 3: Validate user input
if not is_valid_city(city):
    print("Invalid city name. Please enter a valid city name.")
else:
    # Step 4: Send GET Request to Proxy Server
    proxy_url = f"http://127.0.0.1:5000/weather?city={city}"

    try:
        result = requests.get(proxy_url)

        # Step 5: Display weather data if the response is successful
        if result.status_code == 200:
            data = result.json()
            print(data["name"], "의 날씨입니다.")
            print("날씨는 ", data["weather"][0]["description"], "입니다.")
            print("현재 온도는 ", data["main"]["temp"], "입니다.")
            print("체감 온도는 ", data["main"]["feels_like"], "입니다.")
            print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
            print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
            print("습도는 ", data["main"]["humidity"], "입니다.")
            print("기압은 ", data["main"]["pressure"], "입니다.")
            print("풍향은 ", data["wind"]["deg"], "입니다.")
            print("풍속은 ", data["wind"]["speed"], "입니다.")
        elif result.status_code == 404:
            print(f"City '{city}' not found. Please check the city name.")
        else:
            print(f"Failed to retrieve weather data. Error Code: {result.status_code}")
    
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the proxy server. Please ensure the server is running.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
