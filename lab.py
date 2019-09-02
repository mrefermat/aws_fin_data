import pandas as pd
import quandl 
token='QWe8iSbyAFzRuod2aroM'

def get_sp_future():
    return quandl.get("CHRIS/CME_SP1", authtoken=token).resample(rule='d').last().Last.dropna()

# Simple Sharpe ratio calculation
def calc_Sharpe(pnl,N=12):
    return np.sqrt(N) * pnl.mean() / pnl.std()

# Calculate absolute value pairwise correlation for just a non-timeseries correlation matrix
def calc_pairwise_correlation(corr_matrix):
    n=corr_matrix.count().count()
    return (corr_matrix.abs().sum()-1).sum()/(n*(n-1))

# Calculate timeseries of pairwise correlation using days look back accros as many numbers as needed
def calc_ts_pairwise_correlation(data_pct,days=250):
	corrts=pd.ewmcorr(data_pct,days,min_periods=days)
	s = pd.Series()
	for i in data_pct.index:
		x=corrts.ix[i]
		x=x[x.count()!=0].T[x.count()!=0]
		s[i]=calc_pairwise_correlation(x)
	return s