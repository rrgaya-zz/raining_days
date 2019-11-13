import requests, datetime

headers = {'content-type': 'application/json'}
payload = {
    "appid": "68baaa307fcaa4be0ed45fe1e4dceb52",
    "id": 3451328,
    "units": "metric"
}

def get_humudity_data():
    """Get humidity data of Weather
    """
    url_api = "http://api.openweathermap.org/data/2.5/forecast"
    df_weather = requests.get(url_api, params=payload, headers=headers).json()
    weather_list = df_weather['list']
    humidity = {n["dt"]:n['main']['humidity'] for n in weather_list}
    return humidity


def weather():
    humudity = get_humudity_data()
    days_qte_70 = []
    for key, value in humudity.items():
        data_weekday = datetime.datetime.fromtimestamp(key).strftime("%A")
        if value >= 70:
            if data_weekday not in days_qte_70:
                days_qte_70.append(data_weekday)
    print("You should take an umbrella in these days: {}.".format(', '.join(days_qte_70)))


if __name__ == "__main__":
    weather()