## If start time is given, and we want to pull data till today then, we have to bring data in 5000 increments

granularities = ['M1','M5','M15','M30','H1','H2','H4','H8','D','W','M']

## 10 Insturments
insrtuments = ['EUR_USD','GBP_USD','USD_CAD','USD_CHF','USD_JPY','EUR_GBP','EUR_CHF','AUD_USD','EUR_JPY','GBP_JPY']
#insrtuments = ['GBP_USD','USD_CAD','USD_CHF','USD_JPY','EUR_GBP','EUR_CHF','AUD_USD','EUR_JPY','GBP_JPY']
for instrument in insrtuments:
    for granularity in granularities:
        start_time = '2000-01-01 00:00'
        end_time = '2008-05-20 22:00'
        current_date_reached = 'No'
        last_time = None
        print "---"*40
        print  "instrument:",instrument
        while current_date_reached == 'No' :
            if last_time is None:
                df = y.getCandlesData(insrtument=instrument, count=4999, candleFormat='midpoint' ,granularity=granularity, start=start_time, end=None, csv='Y')
                last_time = df['time'][df.index[-1]]
                last_time_in_datetime_format = datetime.datetime.strptime(last_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                last_time = last_time.replace('T',' ')[0:16]
                print "=="*40
                print "last_time:", last_time
                print "=="*40
            ## check if last_time has passed current time
            if last_time_in_datetime_format >= datetime.datetime.now():
                current_date_reached = 'Yes'
                print "Data pulled till: ", last_time, " Now pulling data process is complete."
                break
            else :
                print "Data pulled till: ", last_time, " continuing pulling data....."
                try:
                    df = y.getCandlesData(insrtument=instrument, count=4999, candleFormat='midpoint' ,granularity=granularity, start=last_time, end=None, csv='Y', includeFirst='false')
                    last_time = df['time'][df.index[-1]]
                    last_time_in_datetime_format = datetime.datetime.strptime(last_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                    last_time = last_time.replace('T',' ')[0:16]
                    print "=="*40
                    print "last_time:", last_time
                    print "=="*40
                except Exception as e:
                    print "ERROR: ", instrument, granularity , " had error "
                    print "--"*40
                    break

