# MBTA Finder 🚇

A Flask web app that finds the nearest MBTA stop from any Boston address or landmark.

## Setup

1. **Clone the repo** and enter the directory.

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your API keys:**
   - Mapbox: [mapbox.com](https://mapbox.com) → sign up for a free access token
   - MBTA: [api-v3.mbta.com](https://api-v3.mbta.com) → request a free API key

4. **Create a `.env` file** (copy from `.env.example`):
   ```
   MAPBOX_TOKEN=your_mapbox_token_here
   MBTA_API_KEY=your_mbta_api_key_here
   ```

5. **Run the app:**
   ```bash
   python app.py
   ```
   Then open [http://localhost:5000](http://localhost:5000)

## How It Works

1. User enters a place name or address
2. Mapbox Geocoding API converts it to lat/lng coordinates
3. MBTA V3 API finds the nearest stop to those coordinates
4. Results are displayed with the stop name, routes served, wheelchair accessibility, and an interactive map

## Testing the Helper

You can test the data pipeline without Flask:
```bash
python mbta_helper.py
```

## Project Structure

```
mbta_app/
├── app.py           # Flask routes
├── mbta_helper.py   # API logic (geocoding + MBTA)
├── templates/
│   ├── index.html   # Search form
│   └── result.html  # Results + map
├── requirements.txt
├── .env             # Your API keys (never commit this!)
└── .gitignore
```
