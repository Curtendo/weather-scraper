import pandas as pd
from datetime import datetime

# Translation dictionary
translations = {
    "晴れのち曇": "Sunny then cloudy",
    "曇のち晴れ": "Cloudy then sunny",
    "曇時々晴れ": "Cloudy with occasional clear skies",
    "時々曇り": "Occasionally cloudy",
    "曇り": "Cloudy",
    "おおむね曇り": "Mostly cloudy",
    "所により晴れ": "Mostly cloudy",
    "所により晴れ時々雨": "Mostly cloudy with occasional rain",
    "雨": "Rain",
    "雷雨": "Thunderstorm",
    "おおむね晴れ": "Mostly Sunny",
    "晴れ": "Sunny",
    "晴": "Sunny",
    "晴れ時々雨": "Clear with occasional rain",
    "雨時々晴れ": "Rain with occasional clear skies",
    "雨時々曇": "Rain and occasional clouds",
    "晴れ時々曇": "Sunny with occasional clouds",
    "にわか雨": "Showers",
    "雨や雪": "Rain or snow",
    "雨時々雪": "Rain and occassional snow",
    "曇時々雨": "Cloudy with occassional rain",
    "曇時々雪": "Cloudy with occassional snow",
    "雪時々晴れ": "Snow with occassional sunny skies",
    "雪時々曇": "Snow and occassionally cloudy",
    "晴れ時々雪": "Sunny with occassional snow",
    "雪時々雨": "Snow with occassional rain",
    "雪": "Snow",
    "曇": "Cloudy",
    "雨のち曇": "Rain then cloudy",
    "雨時々止む": "Rain sometimes stopping",
}

# Load the CSV file
df = pd.read_csv("Kakamigahara_90_weather_data.csv")

# Update the date format
def format_date(m_d):
    # Add year and convert to yyyy-mm-dd
    formatted_date = f"2024/{m_d}"
    date_obj = datetime.strptime(formatted_date, "%Y/%m/%d")
    return date_obj.strftime("%Y-%m-%d")

df["date"] = df["date"].apply(format_date)

# Translate the conditions
df["conditions"] = df["conditions"].map(translations)

# Save the updated data to a new CSV
df.to_csv("Kakamigahara_90_weather_data_conv.csv", index=False)

print("Data updated and saved")