

# Calculate absolute value pairwise correlation for just a non-timeseries correlation matrix
def calc_pairwise_correlation(corr_matrix):
    n=corr_matrix.count().count()
    return (corr_matrix.abs().sum()-1).sum()/(n*(n-1))

# Calculate timeseries of pairwise correlation using days look back accros as many numbers as needed
def calc_ts_pairwise_correlation(data_pct,days=250):
	corrts=pd.ewmcorr(data.dropna(),days,min_periods=days)
	s = pd.Series()
	for i in data.dropna().index:
		s[i]=calc_pairwise_correlation(corrts.ix[i])
	return s

