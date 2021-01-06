import pandas as pd

learning_rate = 0.001

data_frame = pd.read_csv('data.csv', delimiter=',')

def estimator(t0, t1, mileage):
    return t0 + (t1 * mileage)


def trainer(mileages, prices, t0, t1):
    tmp0 = 0
    tmp1 = 0

    length = len(mileages)

    rate = learning_rate * (1.0 / float(length)) # ca on peut le faire qu'une fois

    print(rate)
    for i in range(length):
        tmp0 += estimator(t0, t1, mileages[i]) - prices[i]
        tmp1 += (estimator(t0, t1, mileages[i]) - prices[i]) * mileages[i]

    t0 += rate * (tmp0 / length)
    t1 += rate * (tmp1 / length)

    return t0, t1



mileages = []
prices = []

for shit in data_frame.iterrows():
    try:
        mileages.append(int(shit[1]['km']))
        prices.append(int(shit[1]['price']))
    except:
        exit(1)

t0 = 0
t1 = 0

t0, t1 = trainer(mileages, prices, t0, t1)
print(estimator(t0, t1, 74000))
t0, t1 = trainer(mileages, prices, t0, t1)
print(estimator(t0, t1, 74000))
t0, t1 = trainer(mileages, prices, t0, t1)
print(estimator(t0, t1, 74000))
t0, t1 = trainer(mileages, prices, t0, t1)
print(estimator(t0, t1, 74000))

# lets try ?
