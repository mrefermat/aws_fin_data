import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
import time
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
key ='EXATBX3CPYNC2QAM'
sns.set_context("poster")
sns.set(font_scale=1)

def get_stock_adj_price(ticker):
	ts = TimeSeries(key=key, output_format='pandas')
	data, meta_data = ts.get_daily_adjusted(ticker,outputsize='full')
	data.index = pd.to_datetime(data.index)
	return data['5. adjusted close']

df=pd.DataFrame()
time.sleep(61)
df['Min Vol']=get_stock_adj_price('USMV')
df["Momentum"]=get_stock_adj_price('MTUM')
df['Quality']=get_stock_adj_price('QUAL')
df['Value']=get_stock_adj_price('FNDX')
time.sleep(61)
df['Size']=get_stock_adj_price('SIZE')

sp=get_stock_adj_price('VOO')

rets=df.dropna().pct_change()
hedged_factor=rets.subtract(sp.pct_change(),axis=0)

hedged_factor.dropna()['2019':].cumsum().plot(title='Hedged US factor (ETF Performance)').get_figure().savefig('factor.png',bbox_inches='tight')

e=Email(subject='Morning Update: Factor Performance')
e.add_attachment('factor.png')
e.send()