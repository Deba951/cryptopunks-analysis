from moralis import evm_api
import numpy as np
import pandas as pd
from pandas import json_normalize
import matplotlib.pyplot as plt
import datetime
import time
import os
from dotenv import load_dotenv

# Initialize environment variables
load_dotenv()

moralis_api_key = os.getenv("api_key")

page_cursor = ''
data_frame = pd.DataFrame()

# Retrieve data from API
for iteration in range(2):
    api_response = evm_api.nft.get_nft_contract_transfers(
        api_key=moralis_api_key,
        params={
            "address": "0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB", 
            "chain": "eth",
            "cursor": page_cursor
        }
    )
    page_cursor = api_response["cursor"]
    temp_df = json_normalize(api_response['result'])
    if data_frame.empty:
        data_frame = temp_df
    else:
        data_frame = pd.concat([data_frame, temp_df])
    time.sleep(1.1)

# Clean and process the data
data_frame = data_frame[data_frame['value'] != '0']
data_frame['Date'] = data_frame.apply(lambda row: datetime.datetime.strptime(row.block_timestamp[0:10], '%Y-%m-%d').strftime('%b %d'), axis=1)
unique_dates = data_frame.Date.unique()[0:7]
unique_dates = unique_dates[::-1]

daily_volumes = []
daily_averages = []

for date in unique_dates:
    date_df = data_frame[data_frame.Date == date]
    eth_values = [int(val) / 1e18 for val in date_df['value']]
    daily_volumes.append(np.sum(eth_values))
    daily_averages.append(np.mean(eth_values))

# Plot the results
plt.style.use('dark_background')
figure, axis1 = plt.subplots()
figure.set_facecolor('#202225')
axis1.set_facecolor("#202225")
axis1.grid(axis="y", zorder=0, color="#36383F")
axis1.bar(x=unique_dates, height=daily_volumes, width=0.4, zorder=3, color="#E6E8EB")
axis1.yaxis.set_major_locator(plt.MaxNLocator(3))
axis1.set_ylabel("Volume (ETH)", fontweight='heavy', labelpad=20)
axis1.spines['top'].set_visible(False)
axis1.spines['right'].set_visible(False)
axis1.spines['bottom'].set_visible(False)
axis1.spines['left'].set_visible(False)

axis2 = axis1.twinx()
axis2.plot(unique_dates, daily_averages, color='#5B60E0')
axis2.yaxis.set_major_locator(plt.MaxNLocator(3))
axis2.set_ylabel("Average Price (ETH)", fontweight='heavy', rotation=270, labelpad=20)
axis2.spines['top'].set_visible(False)
axis2.spines['right'].set_visible(False)
axis2.spines['bottom'].set_visible(False)
axis2.spines['left'].set_visible(False)

plt.title('CryptoPunks Volume and Price', loc='left', fontsize=16, fontweight="heavy", verticalalignment="top")
plt.show()
