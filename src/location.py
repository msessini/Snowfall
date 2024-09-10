import pandas as pd
import numpy as np

class Location:

    def __init__(self, name):
        self.data = pd.read_csv(f'../data/{name}.csv')
        self.lon = self.data.lon[0]
        self.lat = self.data.lat[0]
        self.name = self.data.city_name[0]

    def get_data(self, clean=True):
        """
        Get full data set and clean it by
        default to remove unecessary columns
        """
        if clean:
            self.data.drop(['lat', 'lon', 'snow_3h', 'city_name', \
                            'dt_iso', 'feels_like', 'weather_icon', \
                            'timezone', 'rain_3h', 'grnd_level', \
                            'sea_level', 'visibility', 'wind_gust'], axis='columns', inplace=True)
        return self.data
    







#data_df["month"] =  pd.to_numeric(pd.to_datetime(data_df.dt, unit='s').dt.strftime('%m'))
#data_df["day"] =  pd.to_numeric(pd.to_datetime(data_df.dt, unit='s').dt.strftime('%d'))
#data_df["time"] = pd.to_numeric(pd.to_datetime(data_df.dt, unit='s').dt.strftime('%H'))
