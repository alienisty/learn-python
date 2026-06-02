
class RequestsClient:
    def get(self, url):
        raise NotImplementedError("Real network calls are disabled in tests!")

class WeatherFetcher:
    def __init__(self, client):
        self.client = client

    def fetch_temperature(self, city):
        try:
            response = self.client.get(f"https://api.weather.com/v1/{city}")
            if response.status_code == 200:
                return response.json().get("temp")
            return -999.0
        except Exception:
            return -999.0
