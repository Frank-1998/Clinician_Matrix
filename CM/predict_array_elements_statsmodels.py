import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# ARIMA: Autoregressive Integrated Moving Average, it's a time series forecasting method.

# 1 week's data: suggestive occurences of each complex skill level 3 scarcity on each day
# of a
historical_data = {
    "2023-01-01": [1, 0, 0, 1, 4, 3, 2, 1, 0, 0, 3, 0],
    "2023-01-02": [1, 1, 3, 2, 4, 3, 2, 1, 0, 0, 3, 0],
    "2023-01-03": [1, 2, 4, 3, 0, 3, 2, 1, 0, 0, 1, 0],
    "2023-01-04": [1, 2, 5, 4, 1, 3, 2, 0, 0, 0, 2, 0],
    "2023-01-05": [1, 1, 6, 2, 0, 3, 2, 1, 1, 0, 2, 0],
    "2023-01-06": [1, 2, 6, 6, 2, 3, 2, 1, 1, 0, 1, 0],
    "2023-01-07": [0, 2, 6, 7, 3, 2, 2, 2, 2, 0, 3, 0]
}
LEVEL_3_SKILLS = ['Recognizing/Managing Anaphylaxis',
'Intravenous infusion Therapy peripheral',
'Intravenous infusion Therapy central',
'Medication Administration simple',
'Medication Administration complex',
'Blood Administration (complex)',
'Tracheostomy care (complex)',
'Urinary Catheterization',
'Drains - simple',
'Drains - complex',
'Wound Care - simple',
'Wound Care - complex']

# Convert data to a DataFrame
df = pd.DataFrame.from_dict(historical_data, orient='index', columns=['Elem1', 'Elem2', 'Elem3', 'Elem4', 'Elem5', 'Elem6', 'Elem7', 'Elem8', 'Elem9', 'Elem10', 'Elem11', 'Elem12'])

# Separate each element into its own time series
time_series_per_element = {elem: df[f'Elem{elem}'] for elem in range(1, 13)}

# Train ARIMA models for each element
arima_models = {elem: ARIMA(time_series, order=(1, 1, 1)).fit() for elem, time_series in time_series_per_element.items()}
"""
(1, 1, 1) == (p,d,q) might need more tuning
p is the order of the autoregressive part,
d is the degree of differencing,
q is the order of the moving average part."""
# Forecast the next period (Day 6) for each element
forecast_values = {elem: model.forecast(steps=1)[0] for elem, model in arima_models.items()}

print(f'Forecast for next week: {forecast_values}')
l = list(forecast_values.values())
for i in range(len(l)):
    print(f'Number of Nurses needing training for {LEVEL_3_SKILLS[i]}: {round(l[i])}')
