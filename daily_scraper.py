import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# List of cities and their respective URLs
city_urls = [
    {"city": "Kakamigahara", "url": "https://www.toshin.com/weather/forecast90days?id=62869"},
    {"city": "Tokyo", "url": "https://www.toshin.com/weather/forecast90days?id=281"},
    {"city": "Osaka", "url": "https://www.toshin.com/weather/forecast90days?id=58095"},
    {"city": "Sapporo", "url": "https://www.toshin.com/weather/forecast90days?id=59988"},
    {"city": "Okinawa", "url": "https://www.toshin.com/weather/forecast90days?id=856"},
]

# Function to save data to CSV
def save_to_csv(city_name, data):
    filename = f"{city_name}_weather_data.csv"
    df = pd.DataFrame(data, columns=['date', 'min_temp', 'max_temp', 'rain_chance', 'total_rainfall', 'conditions'])

    # Check if the file exists
    if os.path.exists(filename):
        # If the file exists, append without writing the header
        df.to_csv(filename, mode='a', index=False, header=False, encoding='utf-8-sig')
        print(f"Data appended to {filename}")
    else:
        # If the file doesn't exist, write a new file with header
        df.to_csv(filename, mode='w', index=False, header=True, encoding='utf-8-sig')
        print(f"New file created: {filename}")

# Function to scrape data for a given city
def scrape_city_data(city, url):
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.text
    else:
        print(f"Failed to retrieve page for {city}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(page_content, 'html.parser')

    data = []
    
    # Extract data
    day = soup.find(class_='detail_window_90')
    
    if day:
        date = day.find(class_='date').get_text(strip=True) if day.find(class_='date') else 'N/A'
        
        # Find min and max temperature element
        min_max_temp_elem = day.find(class_='detail_window_14_daily_temperature')
        if min_max_temp_elem:
            min_max_temp = min_max_temp_elem.get_text(strip=True)
            max_temp_str, min_temp_str = min_max_temp.split('|')
            max_temp = int(max_temp_str.replace('℃', '').strip())
            min_temp = int(min_temp_str.replace('℃', '').strip())
        else:
            min_max_temp = day.find_all(class_='detail_window_45_temp')
            max_temp_str = min_max_temp[0].get_text(strip=True)
            max_temp = int(max_temp_str.replace('℃', '').strip())
            min_temp_str = min_max_temp[1].get_text(strip=True)
            min_temp = int(min_temp_str.replace('℃', '').strip())

        # Find rain chance element
        rain_th = day.find('th', string='降水確率')
        if rain_th:
            rain_td = rain_th.find_next_sibling('td')
            rain_chance = rain_td.get_text(strip=True) if rain_td else 'N/A'
        else:
            rain_chance = 'N/A'

        # Find rainfall amounts
        rainfall_th = day.find('th', string='降水量(mm)')
        if rainfall_th:
            rainfall_tds = rainfall_th.find_next_siblings('td', class_='detail_window_14_hourly')
            total_rainfall = sum(float(td.get_text(strip=True)) for td in rainfall_tds)
        else:
            total_rainfall = 0.0

        # Find conditions
        conditions = None
        conditions_div = day.find(class_='detail_window_14_daily_icon_phrase')
        if not conditions_div:
            conditions_div = day.find(class_='detail_window_45_icon_phrase')
        if not conditions_div:
            conditions_div = day.find(class_='detail_window_90_icon_phrase')
        if conditions_div:
            conditions = conditions_div.get_text(strip=True)

        data.append({
            'date': date,
            'min_temp': min_temp,
            'max_temp': max_temp,
            'rain_chance': rain_chance,
            'total_rainfall': total_rainfall,
            'conditions': conditions
        })

    return data

# Iterate over each city and scrape data
for city_info in city_urls:
    city_name = city_info['city']
    city_url = city_info['url']
    
    print(f"Scraping data for {city_name}...")
    city_data = scrape_city_data(city_name, city_url)
    
    if city_data:
        # Save data for this city to its respective CSV file
        save_to_csv(city_name, city_data)
    else:
        print(f"No data found for {city_name}.")

print("Scraping completed.")
