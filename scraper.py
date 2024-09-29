import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.toshin.com/weather/forecast90days?id=856'  # For Kakamigahara
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.text
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    page_content = None

soup = BeautifulSoup(page_content, 'html.parser') if page_content else None

data = []

# Extract
if soup:
    days = soup.find_all(class_='detail_window_90')

    # Print the days
    for day in days:
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

print(data)

df = pd.DataFrame(data, columns=['date', 'min_temp', 'max_temp', 'rain_chance', 'total_rainfall', 'conditions'])

# Save to CSV
df.to_csv('weather_data.csv', index=False, encoding='utf-8-sig')  # 'utf-8-sig' to handle Japanese characters

print("Data has been saved to weather_data.csv")