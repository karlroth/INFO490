
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib inline')
import datetime
import numpy as np
import pandas as pd
import seaborn as sns


# ## Problem 8.1. Delays at the O'Hare Airpot.
# 
# - When you are done, rename your file to `FirstName_LastName_ord_series.ipynb`
#   and submit it via Moodle.
# - In this problem, you will use Pandas time series functionality
#   to generate sequences of dates from the scheduled departure time at the O'Hare airport
#   and do a time-series analysis of expected arrival delay.

# In[2]:

df = pd.read_csv('/data/airline/2001.csv',
                 encoding='latin1',
                 usecols=('Year', 'Month', 'Origin', 'DayofMonth', 'CRSDepTime', 'ArrDelay'))


# ### Function: get\_ord\_arr\_delay()
# 
# - Write a function named that takes a Pandas DataFrame object,
#   which has `Year`, `Month`, `DayofMonth`, `CRSDepTime`, `Origin`, and `ArrDelay` columns.
#   The function should return a Pandas Series object of `ArrDelay` at the O'Hare airport (ORD) that
#   has the schedule departure time (Year + Month + DayofMonth + `CRSDepTime`) as Pandas DateTimeIndex.
#   
# To create the `DatetimeIndex` for Pandas objects, you can either
#   use [`datetime` module](https://docs.python.org/3.4/library/datetime.html)
#   or use [Pandas `to_datetime`](http://pandas.pydata.org/pandas-docs/dev/generated/pandas.tseries.tools.to_datetime.html).
#   The latter link has some useful examples at the bottom of the page.
#   
# You should use all of `Year`, `Month`, `DayofMonth` and `CRSDepTime` columns
#   in the 2001 flights data to create the index.
#   
# Don't forget that the `ArrDelay` column may have some missing values, which you should remove.
# 
# In the end, you should get
# 
# ```python
# >>> print(get_ord_arr_delay(df, 'ORD'))
# Date
# 2001-01-01 09:51:00    -9
# 2001-01-02 09:51:00    -6
# 2001-01-03 09:51:00    34
# 2001-01-04 09:51:00    18
# 2001-01-05 09:51:00   -10
# 2001-01-06 09:51:00   -14
# 2001-01-07 09:53:00     1
# 2001-01-08 09:53:00    -1
# 2001-01-09 09:53:00   -20
# 2001-01-10 09:53:00   -17
# 2001-01-11 09:53:00    -9
# 2001-01-12 09:53:00   -15
# 2001-01-13 09:53:00   -16
# 2001-01-14 09:53:00     4
# 2001-01-15 09:53:00    -6
# ...
# 2001-12-16 16:10:00    23
# 2001-12-17 16:10:00    78
# 2001-12-18 16:10:00    -1
# 2001-12-19 16:10:00     5
# 2001-12-20 16:10:00    -8
# 2001-12-21 16:10:00    11
# 2001-12-22 16:10:00    34
# 2001-12-23 16:10:00    27
# 2001-12-25 16:10:00    12
# 2001-12-26 16:10:00    15
# 2001-12-27 16:10:00    -6
# 2001-12-28 16:10:00     0
# 2001-12-29 16:10:00     7
# 2001-12-30 16:10:00     5
# 2001-12-31 16:10:00   -13
# Name: ArrDelay, Length: 321784
# ```

# In[119]:

def get_ord_arr_delay(df, airport):
    '''
    Takes a Pandas DataFrame and an airport
    and returns a Pandas Series of arrival delays.
    
    Parameters
    ----------
    df: A Pandas DataFrame with columns
        'Year', 'Month', 'Origin', 'DayofMonth', 'CRSDepTime', and 'ArrDelay'.
    airport: A str of three-letter airport code.
    
    Returns
    -------
    A pandas.Series object.
    '''
    
    # your code goes here
    df = df[df['Origin'] == airport] #mask all other airports
    
    df = df[ df['ArrDelay'].notnull() ] #mask out NaN ArrDelay values
    
    #converts a date from YYYYMMDDHHMinMinSS to YYYY-MM-DD HH:MinMin:SS
    dates = pd.to_datetime(df['Year']*100000000 + df['Month']*1000000 + df['DayofMonth']*10000+df['CRSDepTime'], format="%Y%m%d%H%M%S", coerce = "true")
    
    result = pd.Series(df['ArrDelay'], index = dates) #indexes the ArrDelay column with our new dates
    
    return result

arr_delay = get_ord_arr_delay(df, 'ORD')
print(arr_delay)


# ### Function: get\_daily\_delay()
# 
# - Write a function named `get_daily_delay()` that takes a Pandas Series,
#   and returns the **daily means** of the column.
#   
# In the end, you should get
# 
# ```python
# Date
# 2001-01-01    11.929385
# 2001-01-02    11.277481
# 2001-01-03    27.546771
# 2001-01-04     7.348812
# 2001-01-05     8.911012
# 2001-01-06    -1.947236
# 2001-01-07    -1.755149
# 2001-01-08    -1.424947
# 2001-01-09    -1.910901
# 2001-01-10    -2.027311
# 2001-01-11     0.658281
# 2001-01-12     7.828633
# 2001-01-13    -1.032134
# 2001-01-14    32.323308
# 2001-01-15    12.141892
# ...
# 2001-12-17     4.673966
# 2001-12-18     2.437198
# 2001-12-19    14.024125
# 2001-12-20    10.971084
# 2001-12-21     2.755030
# 2001-12-22    17.882812
# 2001-12-23    14.736909
# 2001-12-24    -1.488584
# 2001-12-25    -0.873773
# 2001-12-26    13.679565
# 2001-12-27     8.130542
# 2001-12-28     5.186785
# 2001-12-29     4.854839
# 2001-12-30    16.721290
# 2001-12-31    -0.887160
# Freq: D, Name: ArrDelay, Length: 365
# ```

# In[122]:

def get_daily_delay(ts):
    '''
    Takes a Pandas Series object and returns the daily mean values.
    
    Parameter
    ---------
    ts: A pandas.Series object.
    
    Returns
    -------
    A pandas.Series object.
    '''
    
    # your code goes here
    
    result = ts
    return result

daily = get_daily_delay(arr_delay)


# ### The Plot of Daily Arrival Delay
# 
# - Use the `get_daily_delay` function to create a plot of daily
#   mean arrival delays at the O'Hare airport.

# In[ ]:

sns.tsplot(daily)


# ### Function: get\_hourly\_delay()
# 
# - Write a function named `get_hourly_delay()` that takes a Pandas Series
#   and a date in string format `'YYYY-MM-DD'`,
#   and returns the **hourly means** of the column on the specified date.
#   
# In the end, you should get
# 
# ```python
# >>> print(get_hourly_delay(arr_delay, '2001-03-14')
# Date
# 2001-03-14 05:00:00    -6.000000
# 2001-03-14 06:00:00    -2.553846
# 2001-03-14 07:00:00     0.756098
# 2001-03-14 08:00:00    -1.354430
# 2001-03-14 09:00:00    -3.303571
# 2001-03-14 10:00:00    -0.155172
# 2001-03-14 11:00:00    -2.647887
# 2001-03-14 12:00:00     0.407407
# 2001-03-14 13:00:00    -1.762500
# 2001-03-14 14:00:00     1.653846
# 2001-03-14 15:00:00     2.100000
# 2001-03-14 16:00:00    10.436364
# 2001-03-14 17:00:00     9.477273
# 2001-03-14 18:00:00    14.500000
# 2001-03-14 19:00:00     3.684211
# 2001-03-14 20:00:00     1.779412
# 2001-03-14 21:00:00    -1.941176
# 2001-03-14 22:00:00    -3.357143
# Freq: H, Name: ArrDelay, dtype: float64
# ```

# In[ ]:

def get_hourly_delay(ts, date):
    '''
    Takes a Pandas Series object and a str with 'YYYY-MM-DD' format
    and returns a Pandas Series object of hourly mean values of that day.
    
    Parameter
    ---------
    ts: A pandas.Series object.
    date: A str. In 'YYYY-MM-DD' format.
    
    Returns
    -------
    A pandas.Series.
    '''
    
    # your code goes here
    
    return result

hourly = get_hourly_delay(arr_delay, '2001-03-14')


# ### The Plot of Hourly Arrival Delay
# 
# - Pick any day you wish, and use the `get_hourly_delay` function to
#   create a plot of hourly mean arrival delays at the O'Hare airport
#   on that date.

# In[ ]:

# your code goes here
sns.tsplot(hourly)


# In[ ]:



