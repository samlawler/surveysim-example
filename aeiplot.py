import numpy as np
import pylab as plt

a,e,inc,Om,om,M=np.genfromtxt("biglistofres.aei",unpack=True,usecols=(0,1,2,3,4,5))

plt.figure(figsize=(6,8))
plt.subplot(211)
plt.plot(a,e,'.',markersize=1.)
plt.ylabel("e")

plt.subplot(212)
plt.plot(a,inc,'.',markersize=1.)
plt.ylabel("i [deg]")
plt.xlabel("a [AU]")

plt.savefig("aei.jpg")
plt.show()
