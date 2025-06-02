import requests
from dotenv import dotenv_values


class VisualCrossingRepo:

    def __init__(self):

        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        config = dotenv_values(".env")
        self.api_key = config["VISUAL_CROSSING_API_KEY"]

    def _get_weather_data(self, url: str):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            error_text = getattr(err.response, 'text', '')
            raise RuntimeError(
                f"Weather API error: {err} - {error_text}") from err

    def get_weather_from_lat_long(self, request_body: dict):
        url = (
            f"{self.base_url}{request_body['lat']},{request_body['long']}"
            f"?unitGroup=metric&key={self.api_key}&contentType=json"
        )
        return self._get_weather_data(url)

    def get_weather_from_us_zipcode(self, zipcode: int):
        url = (
            f"{self.base_url}{zipcode}"
            f"?unitGroup=us&key={self.api_key}&contentType=json"
        )
        return self._get_weather_data(url)


if __name__ == "__main__":
    # python src/repositories/visual_crossing_repo.py
    repo = VisualCrossingRepo()
    repo.get_weather_from_location("xxx")
