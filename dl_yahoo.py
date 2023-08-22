# dl_yahoo.py
#
# AUTHOR
# J. Keith Ratliff
#
# DESCRIPTION
# Download prices for a collection of symbols from Yahoo Finance
import datetime

# Get input from user
import getpass

# Create some example data points and create a scatter plot
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plot
# data = [(2, 4), (23, 28), (7, 2), (9, 10)]
# df = pd.DataFrame(data=data, columns=['A','B']);
# df.plot.scatter(0,1)
# plot.show(block=True);


# Snowflake, Inc. stock price download URL:
# https://query1.finance.yahoo.com/v7/finance/download/SNOW?period1=1614187583&period2=1645723583&interval=1d&events=history&includeAdjustedClose=true
# This URL downloads a CSV format dataset with a single header line with
# start_time = 1614187583 (Wed 24 Feb 2021 10:26:23 AM MST)
# end_time = 1645723583 (Thu 24 Feb 2022 10:26:23 AM MST)
# Timestamps are Unix time, seconds since epoch

# Get the prices for date range 2021-01-01 to 2021-12-31
# https://query1.finance.yahoo.com/v7/finance/download/SNOW?period1=1609484400&period2=1640934000&interval=1d&events=history&includeAdjustedClose=true

# Use SNOW as first
symbol = 'SNOW'
right_now = datetime.datetime.now()
year = right_now.year
# Adjust from defaults to user input
user_symbol = input('Enter stock symbol (leave blank for SNOW): ')
user_year = input('Year for historical records (leave blank for this year): ')
symbol = user_symbol if user_symbol != '' else symbol
year = user_year if user_year != '' else year
# Convert year to start = 1 jan (year) and end = 31 dec (year)
# Truncate end to today's date if year = this year
end = int(datetime.datetime(int(year),12,31).timestamp()) if user_year != '' else int(right_now.timestamp())
start = int(datetime.datetime(int(year),1,1).timestamp())
print(f'Using year {year}')
import urllib.request
price_history_url = 'https://query1.finance.yahoo.com/v7/finance/download/'+symbol+'?period1='+str(start)+'&period2='+str(end)+'&interval=1d&events=history&includeAdjustedClose=true'
prices_for_year = urllib.request.urlopen(price_history_url).read()
print(prices_for_year)
out_file_name = './stockprices_'+symbol+'_'+str(year)+'.csv'
with open(out_file_name, "wb") as fs:
    fs.write(prices_for_year)
