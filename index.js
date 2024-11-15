class WeatherObj {
  constructor({ location, conditions, precipProb, tempMin, tempMax }) {
    this.location = location;
    this.conditions = conditions;
    this.precipProb = precipProb;
    this.tempMin = tempMin;
    this.tempMax = tempMax;
  }
}

async function fetchData(city) {
  let cityData;
  try {
    let response = await fetch(
      `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/${city}/2024-09-29/2024-09-30?key=8CT7Y6AMEULH45Y3KZ5CBL92R`
    );
    cityData = await response.json();
    return cityData;
  } catch (err) {
    console.log(err);
  }
}

function createWeatherObj(cityData, index) {
  const cityDataFiltered = {
    location: cityData.resolvedAddress,
    conditions: cityData.currentConditions.conditions,
    precipProb: cityData.currentConditions.precipprob,
    tempMin: cityData.days[index].tempmin,
    tempMax: cityData.days[index].tempmax,
  };

  return new WeatherObj(cityDataFiltered);
}

async function getCityWeather(city = 'tokyo') {
  const fetchedData = await fetchData(city);
  const weatherobj = createWeatherObj(fetchedData, 0);
  return weatherobj;
}

console.log(getCityWeather('Tokyo'));
