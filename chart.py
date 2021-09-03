import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./RDS-B.csv')
df = pd.DataFrame(data, columns=['Date', 'Close'])
print(df)
df.plot(x="Date", y=["Close"])
plt.show()
