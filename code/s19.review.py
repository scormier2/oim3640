import request

# GET: read/fetch data
requests.get('https://oim.108122.xyz/words/random')
            json={'message': 'Hello, from Semaj}

# POST: send/submit data
requests.post('https://oim.108122.xyz/echo',
              json={'name': 'Alice', 'course': 'OIM3640'})




API_KEY = 'abc123...'  # Don't hardcode this!
url = (f'https://api.openweathermap.org/data/2.5/weather'
       f'?q=Boston&appid={API_KEY}&units=imperial')
data = requests.get(url).json()
print(f"Boston: {data['main']['temp']}°F")


