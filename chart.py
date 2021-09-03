import csv

import pandas as pd
import matplotlib.pyplot as plt
import math

v = open('./RDS-B.csv')
r = csv.reader(v)
row0 = r.next()
row0.append('berry')
print(row0)
for item in r:
    item.append(item[0])
    print(item)

# data = pd.read_csv('./RDS-B.csv')
# df = pd.DataFrame(data, columns=['Date', 'Close'])
# # df = pd.DataFrame(
# #     {'date': df_st.Date, 'steps': df_st['Close']})
# print(df)
# df.plot(x="Date", y=["Close"])
# plt.show()

# x = pd.DataFrame(data, columns=['Date'])
# y = pd.DataFrame(data, columns=['Date'])
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
#
# plt.plot(x, y)
# plt.xlim(-3, 3)
# plt.ylim(-3, 3)
#
# ax.set_aspect('equal', adjustable='box')
#
# plt.xlabel("x")
# plt.ylabel("sinx")
#
# plt.show()
