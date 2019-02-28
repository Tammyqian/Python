# -*- coding:utf8 -*-
import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
z = np.sqrt(xs ** 2 + ys **2)

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
from mongo import MongoIns
models_data, _ = MongoIns().m_list('wt_model', dbname='windfarm', host='192.168.111.10:27037')
print models_data
print len(models_data)
models_map = dict((item.get('_id', ''),[item.get('power'),item.get('speed'),item.get('rated-power',0)]) for item in models_data )
print models_map



