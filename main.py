# Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of X

import pandas as pd

df = pd.DataFrame({
    'values': [1, 2, 3],
    'date': ['2023-01-05', '2023-03-25', '2023-01-24']
})


df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

#             values
# date
# 2023-01-31       4
# 2023-02-28       0
# 2023-03-31       2
print(df.resample('M').sum())