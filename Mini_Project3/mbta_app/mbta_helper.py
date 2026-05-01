import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

MBTA_BASE = "https://api-v3.mbta.com"

ROUTE_TYPE_LABELS = {
    0: "Light Rail",
    1: "Subway",
    2: "Commuter Rail",
    3: "Bus",
    4: "Ferry",
}


def geocode_place(place_name: str) -> dict:
    """Convert a place name to lat/lng using Mapbox Geocoding API."""
    if not MAPBOX_TOKEN:
        return {"error": "Mapbox token not configured."}

    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{requests.utils.quote(place_name)}.json"
    params = {
        "access_token": MAPBOX_TOKEN,
        "limit": 1,
        "country": "US",
        "bbox": "-71.9,41.2,-69.9,42.9",  # Rough bounding box around Greater Boston
    }

    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        return {"error": f"Mapbox API error: {e}"}

    features = data.get("features", [])
    if not features:
        return {"error": f"Could not find location: '{place_name}'"}

    lon, lat = features[0]["geometry"]["coordinates"]
    place_label = features[0].get("place_name", place_name)
    return {"lat": lat, "lon": lon, "label": place_label}


def get_nearest_stop(place_name: str) -> dict:
    """Given a place name, return info about the nearest MBTA stop."""
    geo = geocode_place(place_name)
    if geo.get("error"):
        return geo

    lat, lon = geo["lat"], geo["lon"]

    headers = {}
    if MBTA_API_KEY:
        headers["x-api-key"] = MBTA_API_KEY

    params = {
        "filter[latitude]": lat,
        "filter[longitude]": lon,
        "sort": "distance",
        "page[limit]": 1,
    }

    try:
        resp = requests.get(
            f"{MBTA_BASE}/stops", params=params, headers=headers, timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        return {"error": f"MBTA API error: {e}"}

    stops = data.get("data", [])
    if not stops:
        return {"error": "No MBTA stops found near that location."}

    stop = stops[0]
    attrs = stop.get("attributes", {})

    wheelchair = attrs.get("wheelchair_boarding", 0)
    wheelchair_label = {1: "Yes", 2: "No", 0: "Unknown"}.get(wheelchair, "Unknown")

    stop_lat = attrs.get("latitude")
    stop_lon = attrs.get("longitude")

    # Fetch routes serving this stop
    stop_id = stop["id"]
    routes_info = get_routes_for_stop(stop_id, headers)

    return {
        "stop_name": attrs.get("name", "Unknown"),
        "stop_id": stop_id,
        "wheelchair": wheelchair_label,
        "wheelchair_accessible": wheelchair == 1,
        "place_lat": lat,
        "place_lon": lon,
        "place_label": geo["label"],
        "stop_lat": stop_lat,
        "stop_lon": stop_lon,
        "routes": routes_info,
    }


def get_routes_for_stop(stop_id: str, headers: dict) -> list:
    """Return a list of route names/types serving a stop."""
    try:
        resp = requests.get(
            f"{MBTA_BASE}/routes",
            params={"filter[stop]": stop_id},
            headers=headers,
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException:
        return []

    routes = []
    for route in data.get("data", []):
        attrs = route.get("attributes", {})
        route_type = attrs.get("type", -1)
        routes.append(
            {
                "name": attrs.get("long_name") or attrs.get("short_name", "Unknown"),
                "short_name": attrs.get("short_name", ""),
                "color": attrs.get("color", "888888"),
                "text_color": attrs.get("text_color", "FFFFFF"),
                "type": ROUTE_TYPE_LABELS.get(route_type, "Transit"),
            }
        )
    return routes


if __name__ == "__main__":
    test_places = ["Boston Common", "Fenway Park", "MIT", "Logan Airport"]
    for place in test_places:
        print(f"\nSearching for: {place}")
        result = get_nearest_stop(place)
        if result.get("error"):
            print(f"  ERROR: {result['error']}")
        else:
            print(f"  Nearest stop: {result['stop_name']}")
            print(f"  Wheelchair accessible: {result['wheelchair']}")
            routes = result.get("routes", [])
            if routes:
                print(f"  Routes: {', '.join(r['name'] for r in routes[:3])}")
