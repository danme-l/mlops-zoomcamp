#!/usr/bin/env python
# coding: utf-8

# Week 4 - Deployment Hmwk

import pickle
import pandas as pd

# parametrizing
import sys
input_colour = sys.argv[1]
input_year = sys.argv[2]
input_month = sys.argv[3]

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

categorical = ['PULocationID','DOLocationID']

def read_data(colour, year, month):
    """ reads data from the NYC taxi website: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
    takes taxi colour, year, month, configures the data for duration prediction
    that we've been using throughout the course
    """
    df = pd.read_parquet(f'https://d37ci6vzurychx.cloudfront.net/trip-data/{colour}_tripdata_{year}-{month}.parquet')

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    # create artificial ride_id column
    df['ride_id'] = f'{year}/{month}_' + df.index.astype('str')

    return df

# parametrized scripts means this doesn't need to be hardcoded in
# df = read_data('yellow','2022','02')
df = read_data(input_colour, input_year, input_month)

# get predictions
dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)

# results data frame
df_result = pd.DataFrame(df['ride_id']).join(pd.DataFrame(y_pred))
df_result = df_result.rename(columns={0: "prediction"})
df_result

df_result.to_parquet(
    'results',
    engine='pyarrow',
    compression=None,
    index=False
)

print("Mean predicted ride duration:")
print(df_result['prediction'].mean())