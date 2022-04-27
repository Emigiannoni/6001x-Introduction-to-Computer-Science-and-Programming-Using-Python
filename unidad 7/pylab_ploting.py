# -*- coding: utf-8 -*-
"""
Ejemplo modo de uso pylab para graficar. 
Basado en MIT 6.00.1X Lecture, by Eric Grimson.

"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myQubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myQubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', linewidth=2.0)
plt.ylim(0, 30)
plt.title('Linear')
plt.xlabel('sample points')
plt.ylabel('linear funcion')

plt.figure('quad')
plt.clf()
plt.plot(mySamples, myQuadratic, 'ro', linewidth=3.0)
plt.ylim(0, 800)
plt.title('Quadratic')
plt.xlabel('sample points')
plt.ylabel('quadratic funcion')

plt.figure('cube')
plt.clf()
plt.plot(mySamples, myQubic, 'g^', linewidth=4.0)
plt.ylim(0, 25000)
plt.title('Qubic')
plt.xlabel('sample points')
plt.ylabel('qubic funcion')

plt.figure('expo')
plt.clf()
plt.plot(mySamples, myExponential, 'r--', linewidth=5.0)
plt.ylim(0, 140000)
plt.title('Exponential')
plt.xlabel('sample points')
plt.ylabel('exponential funcion')

plt.figure('linquad')
plt.clf()
plt.title('Lineal vs Quadratic')
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.ylim(0, 1000)
plt.legend()


plt.figure('qubexp')
plt.clf()
plt.title('Qubic vs Exponential')
plt.plot(mySamples, myQubic, label='qubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.ylim(0, 25000)
plt.legend(loc='upper left')


plt.figure('subplot')
plt.clf()
plt.subplot(221)
plt.plot(mySamples, myLinear, 'b-', linewidth=2.0)
plt.subplot(222)
plt.plot(mySamples, myQuadratic, 'ro', linewidth=3.0)
plt.subplot(223)
plt.plot(mySamples, myQubic, 'g^', linewidth=4.0)
plt.subplot(224)
plt.plot(mySamples, myExponential, 'r--', linewidth=5.0)