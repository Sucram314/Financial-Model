import yfinance as yf

from matplotlib import pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np

from datetime import datetime
from datetime import timedelta

#Thirty Year T-Bond
thirtyYear = yf.Ticker("^TYX")
thirtyData = pd.DataFrame(thirtyYear.history(period="10y"))

#Plot Thirty Year Trend
thirtyData['Close'].plot(kind='line', figsize=(8, 4), title='Close')
plt.gca().spines[['top', 'right']].set_visible(False)

#Ten Year T-Bond
tenYear = yf.Ticker("^TNX")
tenData = pd.DataFrame(tenYear.history(period="10y"))

#Plot Ten Year Trend
tenData['Close'].plot(kind='line', figsize=(8, 4), title='Close')
plt.gca().spines[['top', 'right']].set_visible(False)

#Five Year T-Bond
fiveYear = yf.Ticker("^FVX")
fiveData = pd.DataFrame(fiveYear.history(period="10y"))

#Plot Five Year Trend
fiveData['Close'].plot(kind='line', figsize=(8, 4), title='Close')
plt.gca().spines[['top', 'right']].set_visible(False)

#Thirteen Week T-Bill
thirteenWeek = yf.Ticker("^IRX")
thirteenData = pd.DataFrame(thirteenWeek.history(period="10y"))

#Plot Thirteen Week Trend
thirteenData['Close'].plot(kind='line', figsize=(8, 4), title='Close')
plt.gca().spines[['top', 'right']].set_visible(False)

#Combined Plot
thirteenData['Close'].plot(kind='line', figsize=(8, 4), title='Close', label="thirteen week")
thirtyData['Close'].plot(kind='line', figsize=(8, 4), title='Close', label="thirtyData")
tenData['Close'].plot(kind='line', figsize=(8, 4), title='Close', label="tenData")
fiveData['Close'].plot(kind='line', figsize=(8, 4), title='Close', label="fiveData")
plt.gca().spines[['top', 'right']].set_visible(False)
plt.legend()

#Bar Graph of Yields at Select Times 
thirteenClose = thirteenData['Close']
fiveClose = fiveData['Close']
tenClose = tenData['Close']
thirtyClose = thirtyData['Close']

yields = {'Thirteen Week':thirteenClose[-1], 'Five Year':fiveClose[-1], 'Ten Year':tenClose[-1], 'Thirty Year':thirtyClose[-1]}
x = list(yields.keys())
y = list(yields.values())

plt.bar(x, y, color='Maroon', width=0.4)
plt.ylim(3,5)
plt.xlabel("Time to Maturity")
plt.ylabel("Yield")


#Line Graph of Treasury Bond Yields at Multiple Times
x = [0, 1, 2, 3]
y = []

#Today
y.append(thirteenClose[-1])
y.append(fiveClose[-1])
y.append(tenClose[-1])
y.append(thirtyClose[-1])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2024-10-18')

#Pre-Expansion
y = []
y.append(thirteenClose[2023-10-15])
y.append(fiveClose[2023-10-15])
y.append(tenClose[2023-10-15])
y.append(thirtyClose[2023-10-15])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2023-10-15')

#Pre-election
y = []
y.append(thirteenClose[2020-10-15])
y.append(fiveClose[2020-10-15])
y.append(tenClose[2020-10-15])
y.append(thirtyClose[2020-10-15])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2020-10-15')

#Flat
y = []
y.append(thirteenClose[2022-4-14])
y.append(fiveClose[2022-4-14])
y.append(tenClose[2022-4-14])
y.append(thirtyClose[2022-4-14])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2022-04-14')

#Interest Increase
y = []
y.append(thirteenClose[2015-1-14])
y.append(fiveClose[2015-1-14])
y.append(tenClose[2015-1-14])
y.append(thirtyClose[2015-1-14])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2015-1-14')

#Pre-Crash
y = []
y.append(thirteenClose[2021-12-15])
y.append(fiveClose[2021-12-15])
y.append(tenClose[2021-12-15])
y.append(thirtyClose[2021-12-15])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2021-12-15')

#Flat
y = []
y.append(thirteenClose[2022-4-14])
y.append(fiveClose[2022-4-14])
y.append(tenClose[2022-4-14])
y.append(thirtyClose[2022-4-14])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2022-04-14')

#Pre-Expansion
y = []
y.append(thirteenClose[2020-4-1])
y.append(fiveClose[2020-4-1])
y.append(tenClose[2020-4-1])
y.append(thirtyClose[2020-4-1])

plt.scatter(x,y)

p=np.poly1d(np.polyfit(x, y, 5))
t = np.linspace(0, 3, 250)
plt.plot(x, y, 'o', t, p(t), '-', label='2020-04-01')

plt.legend()
