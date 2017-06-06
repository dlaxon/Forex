# Forex
1. **OandaHistoricalData.py** :  is for downloading Forex Data from Oanda, by using Oanda's provided rest api
2. **download_all_data.py** : is for downloading candle data of 10 currency insturments for different time-intervals
  When you run this code, set start_time, end_time, granualarities and instruments, as per your needs.

- start_time = '2000-01-01 00:00'
- end_time = '2018-05-20 22:00'
- granularities = ['M1','M5','M15','M30','H1','H2','H4','H8','D','W','M']
- insrtuments = ['EUR_USD','GBP_USD','USD_CAD','USD_CHF','USD_JPY','EUR_GBP','EUR_CHF','AUD_USD','EUR_JPY','GBP_JPY']

3. **WrangleOandaData.py** : is for processing downloaded forex candle data, and adds columns like
- Bollinger Band
- High Low difference
- High Open difference
- Low Open difference
- Percentage Change
- Bands of pct change
- Bands of pips change

You can modify this class to add your favorite studies.

4. **prepare_csv_for_deeplearning.py** : is for creating csv files with processed data. It creates two csv files, one is with all columns, and other is with less columns, which are mainly focused on deep learning.

*Do not forget to change following paths*
- oanda_file_dir = 'exact path where downloaded files are kept'
- processed_oanda_file_dir = 'exact path where new processed csv files can be stored'
