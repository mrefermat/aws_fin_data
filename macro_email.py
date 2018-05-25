import quandl
import seaborn as sns
import boto3
from botocore.exceptions import ClientError
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
token='QWe8iSbyAFzRuod2aroM'


mkts={'SP 500':'CHRIS/CME_SP1',
      'US 10Y':'CHRIS/CME_TY1',
      'Crude Oil':'CHRIS/CME_CL1',
      'Eurostoxx 50':'CHRIS/EUREX_FESX1'
      }

data_index=pd.DataFrame()
for m in mkts.keys():
    try:
        data_index[m]=quandl.get(mkts[m],token=token).Last
    except:
        data_index[m]=quandl.get(mkts[m],token=token).Settle
data_pct=data_index.pct_change()

data_pct['2018':].cumsum().ffill().plot(colormap='brg').get_figure().savefig('YTD.png')

e=Email(to='mark.refermat@gmail.com',subject='Macro YTD Email')
e.add_attachments(['YTD.png'])
e.send()





