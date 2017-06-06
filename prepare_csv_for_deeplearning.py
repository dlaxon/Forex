## Prepare CSV files from downloaded forex data
## It creates two csv files
import os, sys, json
import pandas as pd
import numpy as np


wrangleoandadata=WrangleOandaData()

## get the dataframe with added features for each file
##      then put that dataframe in csv format, so that it can be loaded to dlaxon platform

oanda_file_dir = '/data/dlaxon/oanda_files'
processed_oanda_file_dir = '/data/dlaxon/oanda_files/processed'

if not os.path.isdir(processed_oanda_file_dir):
    ## make dir
    os.mkdir(processed_oanda_file_dir)

x=WrangleOandaData()
for file in  os.listdir(oanda_file_dir):
    if file.endswith('.csv'):
    #if file.endswith('H1.csv'):
        print "Processing file:",file
        if "JPY" in file:
            pair_has_JPY = 'Y'
        else:
            pair_has_JPY = 'N'

        window = file.split('_')[-1].split('.')[0]
        csv_file=os.path.join(oanda_file_dir,file)
        csv_file_new_name = os.path.join(processed_oanda_file_dir, 'processed_' + file)
        ml_csv_file_new_name = os.path.join(processed_oanda_file_dir, 'ml_processed_' + file)
        print "window :", window
        print "pair_has_JPY:",pair_has_JPY
        df = wrangleoandadata.AddFeatures( csv_file=csv_file, pair_has_JPY=pair_has_JPY, window=window)
        ## pickle is
        #pickle.dump(df, open('/tmp/usd_chf_15m.pkl', 'wb'))
        ## create csv file
        df = df.dropna()

        df.to_csv(csv_file_new_name ,encoding='utf-8',  sep=',',index=True, index_label='Index_ID_2')

        print df.columns
        df_ml = df[['highMid','lowMid','openMid','volume','diff_hl','diff_ho','diff_lo','diff_o_bbu','diff_bbl_o','touchedBBU','touchedBBL','pct_chg','pct_chg_class','pip_chg_high_open_class','pip_chg_low_open_class']]
        ## Add another column for RNN, when label col is not feature
        ## For that the next occurance of pct_chg_class , we have to shift it backward.
        ## e.g. with high, low and open values of this candle, we can predict pct_chg_class of next candle
        df_ml['pct_chg_class_next_candle'] = df['pct_chg_class'].shift(-1)
        df_ml = df_ml.dropna()
        df_ml.to_csv(ml_csv_file_new_name ,encoding='utf-8',  sep=',',index=True, index_label='Index_ID_2')