@app.route('/new')       # when someone visits /new
def upload():            # run this function
    return 'Upload page'
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/square/<int:n>')
def square(n):
    return f'{n} squared is {n ** 2}'
from flask import Flask, render_template

@app.route('/hello/<name>')
def greet(name):
    return render_template('hello.html', name=name)



python app.py
# Then open:
#   http://127.0.0.1:5000/weather/London
#   http://127.0.0.1:5000/weather/Tokyo
#   http://127.0.0.1:5000/stock/AAPL
#   http://127.0.0.1:5000/stock/NVDA

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/square/<int:n>')
def square(n):
    return f'{n} squared is {n ** 2}'

@app.route('/hello/<name>')
def greet(name):
    return render_template('hello.html', name=name)

@app.route('/weather/<city>')
def weather(city):
    try:
        url = f'https://api.open-meteo.com/v1/forecast?latitude=0&longitude=0&current=temperature_2m'
        response = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json')
        data = response.json()
        if data['results']:
            lat = data['results'][0]['latitude']
            lon = data['results'][0]['longitude']
            weather_url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m'
            weather_data = requests.get(weather_url).json()
            temp = weather_data['current']['temperature_2m']
            return f'<h1>{city}</h1><p>Current Temperature: {temp}°C</p>'
        return f'City {city} not found'
    except:
        return 'Error fetching weather data'

@app.route('/stock/<ticker>')
def stock(ticker):
    try:
        url = f'https://query1.finance.yahoo.com/v10/finance/quoteSummary/{ticker}?modules=price'
        response = requests.get(url)
        data = response.json()
        price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
        return f'<h1>{ticker}</h1><p>Current Price: ${price}</p>'
    except:
        return f'Error fetching stock data for {ticker}'

@app.route('/new')
def upload():
    return 'Upload page'

if __name__ == '__main__':
    app.run(debug=True)
