import quandl
import seaborn as sns
import pandas as pd
from lab import calc_ts_pairwise_correlation
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
token='QWe8iSbyAFzRuod2aroM'

# Need to add many more markets
mkts={'SP 500':'CHRIS/CME_SP1',
      'US 10Y':'CHRIS/CME_TY1',
      'Crude Oil':'CHRIS/CME_CL1',
      'Eurostoxx 50':'CHRIS/EUREX_FESX1',
      'Dollar Index':'CHRIS/ICE_DX1'
      }

data_index=pd.DataFrame()
for m in mkts.keys():
    try:
        data_index[m]=quandl.get(mkts[m],authtoken=token).Last
    except:
        data_index[m]=quandl.get(mkts[m],authtoken=token).Settle
data_pct=data_index.pct_change()

calc_ts_pairwise_correlation(data_pct).plot(colormap='jet').get_figure().savefig('pairwise.png')

e=Email(to='mark.refermat@gmail.com',subject='Morning Update: Pairwise Correlation')
e.add_attachment('pairwise.png')
e.send()