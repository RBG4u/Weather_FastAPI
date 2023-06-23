from fastapi import FastAPI
import requests
import config
app = FastAPI()


@app.get('/weather/{city}')
def get_weather(city: str) -> dict[str, str | int]:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return {'city': city, 'temperature': temperature}
    else:
        data = response.json()
        return {'city': data['message'], 'temperature': data['message']}


if __name__ == '__main__':
    print(get_weather(city='Moscow'))
