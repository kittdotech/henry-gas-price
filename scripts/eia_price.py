import pandas as pd
from datetime import date, timedelta
#Function for normalizing dates
def normalize_weekly(d):
	return  d - timedelta(days=d.weekday())

def normalize_monthly(d):
	return date(d.year, d.month, 1)

def normalize_yearly(d):
	return date(d.year, 1, 1)

#Download the source from the EIA in xls to pandas DF
html_daily = pd.read_excel("http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls",sheetname=1,skiprows=[0,1])
html_weekly = pd.read_excel("http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDw.xls",sheetname=1,skiprows=[0,1],converters={0:normalize_weekly})
html_monthly = pd.read_excel("http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls",sheetname=1,skiprows=[0,1],converters={0:normalize_monthly})
html_anually = pd.read_excel("http://www.eia.gov/dnav/ng/hist_xls/RNGWHHDa.xls",sheetname=1,skiprows=[0,1],converters={0:normalize_yearly})

#save to coresponding CSV
html_daily.to_csv('data/price_daily.csv',index = False)
html_weekly.to_csv('data/price_weekly.csv',index = False)
html_monthly.to_csv('data/price_monthly.csv',index = False)
html_anually.to_csv('data/price_yearly.csv',index = False)

