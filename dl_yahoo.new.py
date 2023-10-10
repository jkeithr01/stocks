# dl_yahoo.py
#
# AUTHOR
# J. Keith Ratliff
#
# DESCRIPTION
# Download prices for a collection of symbols from Yahoo Finance
import sys
import datetime as dt

# Get input from user
import getpass


# Snowflake, Inc. stock price download URL:
# https://query1.finance.yahoo.com/v7/finance/download/SNOW?period1=1614187583&period2=1645723583&interval=1d&events=history&includeAdjustedClose=true
# This URL downloads a CSV format dataset with a single header line with
# start_time = 1614187583 (Wed 24 Feb 2021 10:26:23 AM MST)
# end_time = 1645723583 (Thu 24 Feb 2022 10:26:23 AM MST)
# Timestamps are Unix time, seconds since epoch

# Get the prices for date range 2021-01-01 to 2021-12-31
# Use SNOW as first
# https://query1.finance.yahoo.com/v7/finance/download/SNOW?period1=1609484400&period2=1640934000&interval=1d&events=history&includeAdjustedClose=true

symbol = input('Enter stock symbol: ')
year = input('Year for historical records: ')
# Convert year to start = 1 jan (year) and end = 31 dec (year)
# Truncate end to today's date if year = this year
# start = 1609484400
# end = 1640934000
rightnow = int(dt.datetime.now().timestamp())
start = int(dt.datetime(int(year), 1, 1, 0, 0, 0).timestamp())
end = int(dt.datetime(int(year), 12, 31, 11, 59, 59).timestamp())
if (start > rightnow):
    sys.exit("Start time is after current time")
if (end > rightnow):
    end = rightnow

# Gather the stock data for the date range and ticker symbol
import urllib.request
price_history_url = 'https://query1.finance.yahoo.com/v7/finance/download/'+symbol+'?period1='+str(start)+'&period2='+str(end)+'&interval=1d&events=history&includeAdjustedClose=true'
prices_response = urllib.request.urlopen(price_history_url).read()
prices_for_year = prices_response.decode('utf-8')

from io import StringIO
import pandas as pd
import numpy as np
prices_df = pd.read_table(StringIO(prices_for_year), sep=",")
print(prices_df.head(10))
print(prices_df.tail(10))

# Make "Show plot?" optional from user input
import matplotlib.pyplot as plot
prices_df.plot.line(0,1)
plot.show(block=True);

# Prompt whether to print the data to the console
# print(prices_for_year)

# Prompt whether to write the data to a CSV file
# out_file_name = '/home/keith/stockprices_'+symbol+'_'+year+'.csv'
# with open(out_file_name, "wb") as fs:
#     fs.write(prices_for_year)

# Now that we have stock prices, let's upload them to AWS S3, MS Azure Blob,
# and Google GCS

# I shall also take the data sets and plot them
