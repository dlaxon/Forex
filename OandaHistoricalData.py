__author__ = 'kashif'

import requests, json, sys, os
import pandas as pd
import datetime
import rfc3339      ## sudo pip install rfc3339
class OandaHistoricalData:
    'Oanda Historical Data Class'
    oanda_base_url = "https://api-fxtrade.oanda.com/v1/"
    ## insrtument = 'EUR_USD' ,'GBP_USD', 'USD_CAD','USD_CHF' ,'USD_JPY','EUR_GBP','EUR_CHF','AUD_USD'
    ##              'EUR_JPY', 'GBP_JPY'
    ## candleFormat = 'midpoint' or 'bidask'
    ## granularity = 'S10','M1','M5','M15','M30','H1','H2','H4','H8','D1','W1','M1'
    ## count = max 5000 count should not be specified if both the start and end parameters are also specified.
    ## start , end = valid datetime format  in rfc3339 format.
    ## start = 2017-05-18 22:00
    ## end   = 2017-05-19 22:00


    def __init__(self):
        self.oanda_base_url = "https://api-fxtrade.oanda.com/v1/"

        print "OandaHistoricalData "

    import rfc3339, datetime



    def getCandlesData(self, insrtument='EUR_USD', count=500, candleFormat='midpoint' ,granularity='H4',includeFirst='true', start=None, end=None, csv='N', csv_path=None):
        self.oanda_base_url = "https://api-fxtrade.oanda.com/v1/"
        self.insrtument     = insrtument
        self.count          = count
        self.candleFormat   = candleFormat
        self.granularity    = granularity
        self.start          = start
        self.end            = end
        self.csv            = csv
        self.csv_path       = csv_path
        self.includeFirst   = includeFirst

        if self.start is None:
            url = self.oanda_base_url + "candles?" + "instrument=" + self.insrtument +"&count=" + str(self.count) + "&candleFormat=" + self.candleFormat + "&granularity=" + self.granularity + "&includeFirst=" + self.includeFirst
        elif self.start is not None and self.end is None:
            ## check whether format is datetime
            self.start_time = datetime.datetime.strptime(self.start, "%Y-%m-%d %H:%M")

            self.start_time_rfc3339 = rfc3339.rfc3339(self.start_time)
            self.start_time_rfc3339 = self.start_time_rfc3339.replace(":", "%3A")

            url = self.oanda_base_url + "candles?" + "instrument=" + self.insrtument +"&count=" + str(self.count) + "&candleFormat=" + self.candleFormat + "&granularity=" + self.granularity + "&start=" + self.start_time_rfc3339 + "&includeFirst=" +self.includeFirst

        elif self.start is not None and self.end is not None:
            ## check whether format is datetime
            self.start_time = datetime.datetime.strptime(self.start, "%Y-%m-%d %H:%M")
            self.start_time_rfc3339 = rfc3339.rfc3339(self.start_time)
            self.start_time_rfc3339 = self.start_time_rfc3339.replace(":", "%3A")
            print self.start_time_rfc3339

            self.end_time = datetime.datetime.strptime(self.end, "%Y-%m-%d %H:%M")
            self.end_time_rfc3339 = rfc3339.rfc3339(self.end_time)
            self.end_time_rfc3339 = self.end_time_rfc3339.replace(":", "%3A")
            print self.end_time_rfc3339

            url = self.oanda_base_url + "candles?" + "instrument=" + self.insrtument + "&candleFormat=" + self.candleFormat + "&granularity=" + self.granularity + "&start=" + self.start_time_rfc3339 + "&end="+ self.end_time_rfc3339 + "&includeFirst=" +self.includeFirst


        print "--"*40
        print url
        print "--"*40


        data = r.json()
        df = pd.io.json.json_normalize(data['candles'])

        ## if csv file needs to be created then check its csv_path, if that does not exist then create that
        if self.csv == 'Y':
            if self.csv_path is None:
                self.csv_path = '/data/dlaxon/oanda_files'
                if not os.path.isdir(self.csv_path):
                    self.csv_path = '/tmp/'
            else :
                if not os.path.isdir(self.csv_path):
                    os.mkdir(self.csv_path)



            self.filename = self.insrtument + "_"+ self.granularity + ".csv"
            self.csv_file = os.path.join(self.csv_path, self.filename)
            #if csv file already exists then append to it
            if os.path.exists(self.csv_file):
                pass
                df.to_csv(self.csv_file ,encoding='utf-8',  sep=',',index=True, index_label='Index_ID', header=False, mode='a')
            else :
                df.to_csv(self.csv_file ,encoding='utf-8',  sep=',',index=True, index_label='Index_ID')

            print "=======CSV FILE STORED AT  =========="
            print self.csv_file
            print "====================================="

        return df

