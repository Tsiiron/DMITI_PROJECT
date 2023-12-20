// weather-api.js

function getWeather(city, apiKey, callback) {
    var apiUrl = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + apiKey;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            if (data.cod === '404') {
                callback('Город не найден', null);
                return;
            }

            var weatherData = {
                city: data.name,
                country: data.sys.country,
                temperature: Math.round(data.main.temp - 273.15),
                description: data.weather[0].description
            };

            callback(null, weatherData);
        })
        .catch(error => {
            callback('Ошибка при запросе погоды', null);
        });
}
