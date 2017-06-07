__author__ = 'kashif'
import os, sys, json
import pandas as pd
import numpy as np
import cPickle as pickle
import matplotlib.pyplot as plt



class WrangleOandaData:
    pass


    def __init__(self):
        #self.oanda_base_url = "https://api-fxtrade.oanda.com/v1/"

        print "I am in WrangleOandaData class"

    ###############################
    ## func to classify pct change
    ###############################
    def pct_chg_class_func (self, pct_chg, window=None):
        pct_chg_class = None

        ## if window is 15 min then pct change mostly happens in 0-15pct range
        #if window == 'M15':
        if window == 'M1' or window == 'M5' or window == 'M15' or window == 'M30' or window == 'H1':

            if pct_chg > 0.0 and pct_chg <= 0.01  :
                pct_chg_class = '0_1_pos'
            elif pct_chg > 0.01 and pct_chg <= 0.02  :
                pct_chg_class = '1_2_pos'
            elif pct_chg > 0.02 and pct_chg <= 0.03  :
                pct_chg_class = '2_3_pos'
            elif pct_chg > 0.03 and pct_chg <= 0.04  :
                pct_chg_class = '3_4_pos'
            elif pct_chg > 0.04 and pct_chg <= 0.05  :
                pct_chg_class = '4_5_pos'
            elif pct_chg > 0.05 and pct_chg <= 0.06  :
                pct_chg_class = '5_6_pos'
            elif pct_chg > 0.06 and pct_chg <= 0.07  :
                pct_chg_class = '6_7_pos'
            elif pct_chg > 0.07 and pct_chg <= 0.08  :
                pct_chg_class = '7_8_pos'
            elif pct_chg > 0.08 and pct_chg <= 0.09  :
                pct_chg_class = '8_9_pos'
            elif pct_chg > 0.09 and pct_chg <= 0.10  :
                pct_chg_class = '9_10_pos'
            elif pct_chg > 0.10 and pct_chg <= 0.25  :
                pct_chg_class = '10_25_pos'


            elif pct_chg < 0.0 and pct_chg >= -0.01  :
                pct_chg_class = '0_1_neg'
            elif pct_chg < -0.01 and pct_chg >= -0.02  :
                pct_chg_class = '1_2_neg'
            elif pct_chg < -0.02 and pct_chg >= -0.03  :
                pct_chg_class = '2_3_neg'
            elif pct_chg < -0.03 and pct_chg >= -0.04  :
                pct_chg_class = '3_4_neg'
            elif pct_chg < -0.04 and pct_chg >= -0.05  :
                pct_chg_class = '4_5_neg'
            elif pct_chg < -0.05 and pct_chg >= -0.06  :
                pct_chg_class = '5_6_neg'
            elif pct_chg < -0.06 and pct_chg >= -0.07  :
                pct_chg_class = '6_7_neg'
            elif pct_chg < -0.07 and pct_chg >= -0.08  :
                pct_chg_class = '7_8_neg'
            elif pct_chg < -0.08 and pct_chg >= -0.09  :
                pct_chg_class = '8_9_neg'
            elif pct_chg < -0.09 and pct_chg >= -0.10  :
                pct_chg_class = '9_10_neg'
            elif pct_chg < -0.10 and pct_chg >= -0.25  :
                pct_chg_class = '10_25_neg'

        else:

            if pct_chg > 0.0 and pct_chg <= 0.25  :
                pct_chg_class = '0_25_pos'
            elif pct_chg < 0.0 and pct_chg >= -0.25  :
                pct_chg_class = '0_25_neg'


        if pct_chg == 0.0 :
            pct_chg_class = 'no_change'
        elif pct_chg > 0.25 and pct_chg <= 0.50  :
            pct_chg_class = '25_50_pos'
        elif pct_chg > 0.50 and pct_chg <= 0.75  :
            pct_chg_class = '50_75_pos'
        elif pct_chg > 0.75 and pct_chg <= 1.00  :
            pct_chg_class = '75_100_pos'
        elif pct_chg > 1.00   :
            pct_chg_class = '100_plus_pos'
        elif pct_chg < -0.25 and pct_chg >= -0.50  :
            pct_chg_class = '25_50_neg'
        elif pct_chg < -0.50 and pct_chg >= -0.75  :
            pct_chg_class = '50_75_neg'
        elif pct_chg < -0.75 and pct_chg >= -1.00  :
            pct_chg_class = '75_100_neg'
        elif pct_chg < -1.00   :
            pct_chg_class = '101_plus_neg'
        print pct_chg_class
        return pct_chg_class

    ###############################
    ## func to classify pip change
    ###############################
    def pip_chg_class_func (self, pip_chg):
        pip_chg_class = None
        if pip_chg == 0 :
            pip_chg_class = 'no_change'
        elif pip_chg > 0 and pip_chg <= 10  :
            pip_chg_class = '0_10_pips_pos'
        elif pip_chg > 10 and pip_chg <= 25  :
            pip_chg_class = '11_25_pips_pos'
        elif pip_chg > 25 and pip_chg <= 50  :
            pip_chg_class = '26_50_pips_pos'
        elif pip_chg > 50 and pip_chg <= 75  :
            pip_chg_class = '51_75_pips_pos'
        elif pip_chg > 75 and pip_chg <= 100  :
            pip_chg_class = '76_100_pips_pos'
        elif pip_chg > 100   :
            pip_chg_class = '100_plus_pips_pos'
        elif pip_chg < 0 and pip_chg >= -10  :
            pip_chg_class = '0_10_pips_neg'
        elif pip_chg < 10 and pip_chg >= -25  :
            pip_chg_class = '11_25_pips_neg'
        elif pip_chg < -25 and pip_chg >= -50  :
            pip_chg_class = '26_50_pips_neg'
        elif pip_chg < -50 and pip_chg >= -75  :
            pip_chg_class = '51_75_pips_neg'
        elif pip_chg < -75 and pip_chg >= 100  :
            pip_chg_class = '76_100_pips_neg'
        elif pip_chg < -100   :
            pip_chg_class = '101_plus_pips_neg'
        print pip_chg_class
        return pip_chg_class

    def AddFeatures(self, pd_df=None, csv_file=None, pair_has_JPY ='N', window=None):
        if pd_df is None and csv_file is None:
            print "Error: Pls provide csv_file with full path or pandas dataframe with Oanda candles midpoint data.\n exiting now.."
            sys.exit(1)
        elif csv_file is not None and pd_df is None :
            self.csv_file = csv_file
            ## check whether that file exists or not
            if os.path.exists(csv_file):
                print csv_file ," file exists."
            else:
                print "Error: ",csv_file, " does not exist.\n exiting now.."
                sys.exit(1)
            ## convert csv file to pandas dataframe
            self.df = pd.read_csv(csv_file)
        elif pd_df is not None and csv_file is not None:
            print "Error: Pls provide either csv_file or pandas dataframe, but not both.\n exiting now.."
            sys.exit(1)


        if pair_has_JPY != 'Y':
            pip_multiplier = 10000 ##(for non JPY pairs)
        else:
            pip_multiplier = 100   ##(for JPY pairs)

        #### get the fluctuation in candle, and also multiple by 100 in 15M window
        if window is None or window == 'M15' or window == 'M1' or window == 'M5' or window == 'M30' or window == 'H1':
            general_multiplier = 100
        else :
            general_multiplier = 100
        self.df['diff_hl'] = ((self.df['highMid'] - self.df['lowMid'])  * pip_multiplier) / general_multiplier        ## dividing by 100 to keep ready for ML
        self.df['diff_ho'] = ((self.df['highMid'] - self.df['openMid']) * pip_multiplier) / general_multiplier        ## dividing by 100 to keep ready for ML
        self.df['diff_lo'] = ((self.df['lowMid']  - self.df['openMid']) * pip_multiplier) / general_multiplier        ## dividing by 100 to keep ready for ML


        ## get the bollinger band with SMA 15
        self.df['BBU15'] = (pd.rolling_mean(self.df['openMid'], 15)) + 2*(pd.rolling_std(self.df['openMid'],15))
        self.df['BBL15'] = (pd.rolling_mean(self.df['openMid'], 15)) - 2*(pd.rolling_std(self.df['openMid'],15))
        ## get the difference between upper BB and Opening candle price, also diff between lower BB and Opening price
        ##      This tells whether the trend is turning upwards, downwards or slowing down
        self.df['diff_o_bbu'] =   ((self.df['openMid'] - self.df['BBU15'])  * pip_multiplier) / general_multiplier
        self.df['diff_bbl_o'] =   ((self.df['BBL15'] - self.df['openMid'])  * pip_multiplier) / general_multiplier
        ## Check if highMid crosses BB Upper band, and lowMid corsses BB Lower band
        self.df['touchedBBU'] = np.where(self.df['highMid'] > self.df['BBU15']   , 1, 0)
        self.df['touchedBBL'] = np.where(self.df['BBL15'] >   self.df['lowMid']  , 1, 0)

        ## get the pct change in openMid
        self.df['pct_chg'] = self.df['openMid'].pct_change() * 100
        ## Add classes based on pct_change
        self.df['pct_chg_class'] = self.df['pct_chg'].map(lambda  x: self.pct_chg_class_func(x, window=window))
        ## Add classes based on pip change from Open to High
        self.df['pip_chg_high_open_class'] = ((self.df['highMid'] - self.df['openMid']) * pip_multiplier).map(lambda  x: self.pip_chg_class_func(x))
        ## Add classes based on pip change from Open to Low
        self.df['pip_chg_low_open_class']  = ((self.df['lowMid']  - self.df['openMid']) * pip_multiplier).map(lambda  x: self.pip_chg_class_func(x))


        return self.df
