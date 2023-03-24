from requests import Request, Session
import requests
import json
import pprint
import datetime
import time
import os
from config import *

SLEEP_TIME = 0.2

# ##
# ## setup config_cmc.py in the same folder
# ##

# EXCHANGES=["OKX"]  # only one

# WANTED_CURRENCIES = ['USDT']  # only one


# # # Do not alter below easily
# # Group size is the max number of coins per each .txt file (output)
# GROUP_SIZE = len(EXCHANGES) * 1000

# URL = 'https://www.okx.com/api/v5/market/tickers?instType=SPOT'
# ## end of Config file


#===== Setup Date and Time #======== 
# Date
generation_date = datetime.datetime.now()
generation_date = generation_date.strftime("%d_%m_%Y")


# Time now
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
#print(current_time)


#generation_time = now.strftime("%H:%M:%S")


# ======================== ### 
## Making the Call
# ======================== ### 


response = requests.get(URL)
#print(response.json())

coins = response.json()['data']

#print(coins[0]['instID'])

result = []
for coin in coins:
    if coin['instId'][-len(WANTED_CURRENCIES[0]):] == WANTED_CURRENCIES[0]:
        result.append(coin['instId'].replace('-', ''))

#print(result)



#================================================
# Group a list of many items 
#
# to a list containing lists of n 
# =============================================== ### 

# Group size, in production n=400
n=GROUP_SIZE

def group_into_n(data_list, n):
    return [data_list[i:i+n] for i in range(0, len(data_list), n)]

#test = [1,2,3,4,5,6,7,8]
#print(group_into_n(test, n))

grouped_pairs = group_into_n(result, n)

#print(grouped_pairs)


#================================================
# Step 5 #

# write a function to output each of the group in step 4 
# to a separate file
# =============================================== ### 


#def output_to_text_file(nested_grouped_pairs):
#    for idx, group in enumerate(nested_grouped_pairs):
#        with open(f'{idx+1}CMC p.{idx+1} {generation_date}.txt ', 'w') as f:
#            for pair in group:
#                f.write("%s,\n" % pair)


# /Users/raysonkong/code/python/webscrapping/scripts_v2/cmc_api_to_tradingview/outputs
def output_to_text_file(nested_grouped_pairs):
    for idx, group in enumerate(nested_grouped_pairs):
            filename=f"{os.getcwd()}/{EXCHANGES[0]}_ALL_{generation_date}total{len(result)}/-0.4 {EXCHANGES[0]}_ALL p.{idx+1} ({generation_date}).txt"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "w") as f:
                for pair in group:
                  f.write("%s,\n" % pair)

#output_to_text_file(grouped_pairs)


def run_srapper():
    output_to_text_file(grouped_pairs)


    print("== OKX All Tickers Retrieved ==")
    print('\n')
    #print("======================================================")
if __name__ =='__main__':
    run_srapper()

