import quandl
import seaborn as sns
import pandas as pd
from lab import calc_ts_pairwise_correlation
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
plt.switch_backend('agg')
from mail import Email
token='QWe8iSbyAFzRuod2aroM'

# Need to add many more markets
mkts={'SP 500':'CHRIS/CME_SP1',
    'Natural Gas':'CHRIS/CME_NG1',
      #'US 10Y':'CHRIS/CME_TY1',
      'Crude Oil':'CHRIS/CME_CL1',
      'Eurostoxx 50':'CHRIS/EUREX_FESX1',
      'Dollar Index':'CHRIS/ICE_DX1',
      #'Wheat':'CHRIS/CME_W7',
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
        data_index[m]=quandl.get(mkts[m],authtoken=token).Settle
data_pct=data_index.dropna().pct_change()
data=data_pct.dropna()
number=data.count().iloc[1]

window=20
results=pd.DataFrame()
for i in range(window+1,number):
    pca = PCA(n_components=5)
    pca.fit(data[i-window:i])
    results[data.iloc[i].name]=pd.Series(pca.explained_variance_)**.5

results.T['2018':].plot(kind='area',colormap='magma',title='Vol Explained').get_figure().savefig('vol_explained.png')

e=Email(to='mark.refermat@gmail.com',subject='Morning Update: Volatility explained by compoents')
e.add_attachment('vol_explained.png')
e.send()