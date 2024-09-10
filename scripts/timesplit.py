import pandas as pd

def season(month):
    if month in [12,1,2]:
        return 'Winter'
    if month in [3,4,5]:
        return 'Spring'
    if month in [6,7,8]:
        return 'Summer'
    if month in [9,10,11]:
        return 'Autumn'
    return ''

def split_day(hour):
    if hour >= 22 or hour < 8:
        return 'night'
    elif hour >= 8 and hour < 22:
        return 'day'

def group(df, freq):
    group_df = df.copy()
    group_df.dt = pd.to_datetime(group_df.dt, unit='s')
    group_df.set_index('dt', inplace=True)
    group_df.rename(columns={'snow_1h': 'snow', 'rain_1h': 'rain'}, inplace=True)
    
    if freq == 'year':
        group_df = group_df.groupby(pd.Grouper(freq='Y')).agg({'temp': 'mean', 'temp_min': 'min', \
                                                             'temp_max': 'max', 'pressure': 'mean', \
                                                             'snow': 'sum', 'rain': 'sum'})
        group_df["year"] =  pd.to_numeric(group_df.index.strftime('%Y'))


    if freq == 'month':
        group_df = group_df.groupby(pd.Grouper(freq='M')).agg({'temp': 'mean', 'temp_min': 'min', \
                                                             'temp_max': 'max', 'pressure': 'mean', \
                                                             'snow': 'sum', 'rain': 'sum'})
        #group_df["year"] =  group_df.index.strftime('%Y-%m')
        group_df["month"] =  pd.to_numeric(group_df.index.strftime('%m'))
        group_df["season"] = group_df.month.apply(season)
        
    return group_df