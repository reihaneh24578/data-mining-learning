
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""در هر روز 100 بیمار به بیمارستان مراجعه میکنند که به این احتمالات به این سه بخش میروند 
برای هزار روز این احتمال محاسبه میشود"""
ICU = 0.3
Surger = 0.6
El = 0.1
data_Multinomial = np.random.multinomial(n= 100, pvals=[ICU, Surger, El], size=1000)
print(data_Multinomial)

"""به طور میانگین در هر ساعت 5 مشتری وارد فروشگاه میشوند میخواهیم
احتمال اینکه در یک ساعت دقیقا 3 مشتری وارد شوند را حساب کنیم"""
data_poisson = np.random.poisson(lam=7, size=1000)
sns.displot(data_poisson)

data_exponential = np.random.exponential(scale=120, size=1000)
sns.displot(data_exponential, bins=100)

plt.show()
