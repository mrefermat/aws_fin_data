import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
from lab import *
sns.set_context("poster")
sns.set(font_scale=1)

sp=get_sp_future()
pct_returns=sp.pct_change()
short_days=1
long_days=60
z=(pd.Series.ewm(pct_returns,short_days).mean()-pd.Series.ewm(pct_returns,long_days).mean())/(pd.Series.ewm(pct_returns,long_days).std())

if z.abs().iloc[-1]>1:
	df=pd.DataFrame()
	df['SP']=sp
	df['Z score']=z
	ax=df['2018':].plot(secondary_y='SP')
	ax.get_figure().savefig('zscore_sp.png')
	e=Email(subject='Morning Update: S&P 500 1sd Move')
	e.add_attachments(['zscore_sp.png'])
	e.send()
else:
	print('No email')

