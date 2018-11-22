import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from mail import Email
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
key ='B22889019-EABCFEE1'

def get_sector_data():
      sp=SectorPerformances (key=key, output_format='pandas')
      data,_ = sp.get_sector()
      df = pd.DataFrame()
      df['1M Performane']=data['Rank D: Month Performance']
      df['YTD Performance']=data['Rank F: Year-to-Date (YTD) Performance']
      df['1Y Performance']=data['Rank G: Year Performance']
      df['3Y Performance']=(data['Rank H: Year Performance']+1)**.33333333-1
      df['10Y Performance']=(data['Rank J: Year Performance']+1)**.1-1
      return df

get_sector_data().plot(kind='bar',colormap='jet',title='Performance (Long term Annualized)').get_figure().savefig('sector.png',bbox_inches='tight')

e=Email(to=['mark.refermat@gmail.com','mark.refermat@gam.com'],subject='Morning Update: Sector Performance')
e.add_attachment('sector.png')
e.send()