import requests


def get_cpi_data(start_date=None, end_date=None, series_id="CPIAUCSL"):
    """
    Fetch CPI data from FRED API.
    """
    params = {
        "series_id": series_id,
        "api_key": "0b65a013028012c3b238833b5c0c30c3",
        "file_type": "json",
        "observation_start": start_date,
        "observation_end": end_date
    }
    response = requests.get("https://api.stlouisfed.org/fred/series/observations", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cpiDate = get_cpi_data("2020-01-01", "2024-11-15")
    print(cpiDate)
