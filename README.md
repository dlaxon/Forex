# Forex
1. WrangleOandaData.py:  is for downloading Forex Data from Oanda, by using Oanda's provided rest api
2. download_all_data.py: is for downloading candle data of 10 currency insturments for different time-intervals
                          When you run this code, set start_time, end_time, granualarities and instruments, as per your needs.
                          e.g.
                          start_time = '2000-01-01 00:00'
                          end_time = '2018-05-20 22:00'
                          granularities = ['M1','M5','M15','M30','H1','H2','H4','H8','D','W','M']
                          insrtuments = ['EUR_USD','GBP_USD','USD_CAD','USD_CHF','USD_JPY','EUR_GBP','EUR_CHF','AUD_USD','EUR_JPY','GBP_JPY']
