# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:15:35 2022

@author: Emi Giannoni
"""

import numpy as np
import matplotlib.pyplot as plt

# Linear graphs

x = np.linspace(0, 10, 20)
y1 = x**2
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=2, markersize=4, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=4, label="Second")
plt.xlabel("$X$")
plt.xlabel("$Y$")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("myfig.png")

plt.show()

z = np.logspace(0, 1, 10)
y3 = z**2
plt.loglog(z, y3, "bo-")

plt.show()

# Histograms

x = np.random.normal(size=1000)

plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))

x = np.random.gamma(2, 3, 100000)

plt.figure()
plt.subplot(221)
plt.hist(x, bins=30)
plt.subplot(222)
plt.hist(x, bins=30, density=True)
plt.subplot(223)
plt.hist(x, bins=30, cumulative=True)
plt.subplot(224)
plt.hist(x, bins=30, density=True, cumulative=True, histtype="step")
