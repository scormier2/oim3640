import requests
fron pprint import pprint
from dovtenv import load_dotenv
import os

API_KEY = 'abc123...'  # Don't hardcode this!
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")


