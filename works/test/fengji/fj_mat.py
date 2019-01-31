import dask.dataframe as dd
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline


def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)
    ybar = np.sum(y) / len(y)
    ssreg = np.sum((yhat - ybar) ** 2)
    sstot = np.sum((y - ybar) ** 2)
    results['determination'] = ssreg / sstot
    return results


def get_mode(_df, power):
    # return stats.mode(_df[power].get_values()[:,0])[0][0]
    return _df[power].describe().at['75%', 'Power']


def get_curve(fj_num, date):
    df = pd.read_csv('/data/hzk/result/f' + str(fj_num) + '/5T/mean_' + date + '.csv')

    df = df[['WindSpeed', 'Power']]
    hist, bin_edges = np.histogram(df.WindSpeed, bins=100)

    cuts = pd.cut(df["WindSpeed"], bin_edges)
    gdf = df.groupby(cuts)
    modes = gdf.apply(get_mode, ['Power'])
    print(len(modes))

    keys = []
    ns = []
    for i, (key, item) in enumerate(gdf):
        if item.Power.count() > 0:
            keys.append(item.WindSpeed.mean())
            ns.append(modes[i])

    print(len(keys))
    z1 = polyfit(keys, ns, 2)
    print(z1)
    p1 = np.poly1d(z1['polynomial'])
    print(p1)
    print(len(keys))
    Y1 = [p1(i) for i in keys]
    plt.scatter(df.WindSpeed, df.Power)
    plt.plot(keys, ns, 'r')
    # plt.plot(keys,Y1,'r')
    plt.show()

get_curve(141,'201702*')