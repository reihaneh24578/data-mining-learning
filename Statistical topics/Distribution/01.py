import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

data_normal = stats.norm.rvs(size=1000000, loc=0, scale=1)
sns.displot(data_normal, bins=100, kde=True)

data_uniform = stats.uniform.rvs(size=1000, loc=0, scale=20)
sns.displot(data_uniform, bins=100)

data_bernoulli = stats.bernoulli.rvs(size=1000, p=0.2)
sns.displot(data_bernoulli, bins=100)

data_Binomial = stats.binom.rvs(size=1000, n=100, p=0.2)
sns.displot(data_Binomial, bins=100)

