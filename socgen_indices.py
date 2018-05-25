import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email


web_root='https://cib.societegenerale.com/fileadmin/indices_feeds/'
indices={'CTA':'CTA_Historical.xls',
         'CTA Mutual Funds':'CTAM_Historical.xls',
         'Trend Index':'Trend_Index_Historical.xls',
         'Short Term Traders Index':'STTI_Historical.xls',
         'Multi Alternative Risk Premia':'MARP_Historical.xls'
        }
data_index=pd.DataFrame()
for i in indices.keys():
    file='https://cib.societegenerale.com/fileadmin/indices_feeds/'+indices[i]
    data_index[i]=pd.read_csv(file,sep='\t',index_col=0,parse_dates=[0],usecols=[0,1]).ix[:,0]

data_pct=data_index.pct_change()

data_pct['2018':].cumsum().ffill().plot(colormap='jet').get_figure().savefig('socgen.png')

e=Email(to='mark.refermat@gmail.com',subject='Morning Update: Soc Gen Indices')
e.add_attachment('socgen.png')
e.send()