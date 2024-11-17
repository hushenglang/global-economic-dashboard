import requests


class FredService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stlouisfed.org/fred/series/observations"

    def get_cpi_data(self, series_id="CPIAUCSL", start_date=None, end_date=None):
        """
        Fetch CPI data from FRED API.

        :param series_id: The ID of the series to fetch. Default is 'CPIAUCSL' for CPI.
        :param start_date: The start date for the data in YYYY-MM-DD format.
        :param end_date: The end date for the data in YYYY-MM-DD format.
        :return: JSON response containing CPI data.
        """
        params = {
            "series_id": series_id,
            "api_key": self.api_key,
            "file_type": "json",
            "observation_start": start_date,
            "observation_end": end_date
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()


# Example usage:
# Replace 'your_api_key_here' with your actual FRED API key
fred_service = FredService(api_key='your_api_key_here')
cpi_data = fred_service.get_cpi_data(start_date='2020-01-01', end_date='2023-01-01')
print(cpi_data)
