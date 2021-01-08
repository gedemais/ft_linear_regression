import pandas as pd
import os

learning_rate = 0.0001

data_frame = pd.read_csv('data.csv', delimiter=',')

def estimator(t0, t1, mileages):
    return t0 + (t1 * mileages)

def sumTheta0(t0, t1, mileages, prices, length):
    val = 0
    for i in range(length):
        val += estimator(t0, t1, mileages[i]) - prices[i]
    return val

def sumTheta1(t0, t1, mileages, prices, length):
    val = 0
    for i in range(length):
        val += (estimator(t0, t1, mileages[i]) - prices[i]) * mileages[i]
    return val

def trainer(mileages, prices, i):
    t0 = 0.0
    t1 = 0.0
    length = len(mileages)
    for i in range(i):
        tmp0 = sumTheta0(t0, t1, mileages, prices, length) / length
        tmp1 = sumTheta1(t0, t1, mileages, prices, length) / length

        t0 -= (learning_rate * tmp0)
        t1 -= (learning_rate * tmp1)

    return t0, t1



mileages = []
prices = []

for shit in data_frame.iterrows():
    try:
        mileages.append(int(shit[1]['km']))
        prices.append(int(shit[1]['price']))
    except:
        exit(1)

t0 = 0.0
t1 = 0.0
for i in range(10):
    t0, t1 = trainer(mileages, prices, i)
    print(str(i + 1) + ' times : t0 = ' + str(t0) + '\n          t1 = ' + str(t1) + '\n----------')
#t0, t1 = trainer(mileages, prices, t0, t1)
#print(estimator(t0, t1, 74000))
#t0, t1 = trainer(mileages, prices, t0, t1)
#print(estimator(t0, t1, 74000))
#t0, t1 = trainer(mileages, prices, t0, t1)
#print(estimator(t0, t1, 74000))
#t0, t1 = trainer(mileages, prices, t0, t1)
#print(estimator(t0, t1, 74000))

# lets try ?
