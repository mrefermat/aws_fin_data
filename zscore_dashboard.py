import quandl
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
token='QWe8iSbyAFzRuod2aroM'


mkts={'SP 500':'CHRIS/CME_SP1',
      'US 10Y':'CHRIS/CME_TY1',
      'Crude Oil':'CHRIS/CME_CL1',
      'Eurostoxx 50':'CHRIS/EUREX_FESX1',
      'Dollar Index':'CHRIS/ICE_DX1',
      'US 3M T-bills':'FRED/DTB3',
      'Fed Funds Effective Rate':'FRED/DFF',
      'US Investment Grade':'COM/CDXNAIG',
      'US High Yield':'COM/CDXNAHY',
      'US 20 Year Treasury':'FRED/DGS20',
      'TED Spread':'FRED/TEDRATE',
      'Wheat':'CHRIS/CME_W7',
      'Corn':'CHRIS/CME_C1',
      'Dax':'CHRIS/EUREX_FDAX1',
      'FTSE100':'CHRIS/LIFFE_Z1',
      'Eurodollar':'CHRIS/CME_ED1',
      'Euro':'CHRIS/CME_EC1',
      'GBP':'CHRIS/CME_BP1',
      'Gold':'CHRIS/CME_EC1'
      }

data_index=pd.DataFrame()
for m in mkts.keys():
    try:
        data_index[m]=quandl.get(mkts[m],authtoken=token).Last
    except:
        try:
            data_index[m]=quandl.get(mkts[m],authtoken=token).Settle
        except:
            try:
                data_index[m]=quandl.get(mkts[m],authtoken=token).Value
            except:
                try:
                    data_index[m]=quandl.get(mkts[m],authtoken=token).value
                except:
                	try:
                		data_index[m]=quandl.get(mkts[m],authtoken=token).Rate
                	except: 
                		print(m)
data_pct=data_index.pct_change()  

mu=pd.ewma(data_pct,260)
sd=pd.ewmstd(data_pct,260)
zscores=(data_pct-mu)/sd
last=zscores.iloc[-2].dropna().sort_values()
last.plot(kind='barh',colormap='jet',ylim=[-3,3]).get_figure().savefig('zscore.png',bbox_inches='tight' )


e=Email(to='mark.refermat@gmail.com',subject='Morning Update: Macro Dashboard')
e.add_attachment('zscore.png')
e.send()