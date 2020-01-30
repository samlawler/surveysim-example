import numpy as np
import pylab as plt

ta,te,tinc,tOmega,tomega,tM,tresamp,tq,tr,tMdisc,tmag,tH,tcolor=np.genfromtxt("tracked.dat",usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12),unpack=True)

da,de,dinc,dH,dresamp=np.genfromtxt("drawn.dat",usecols=(0,1,2,6,7),unpack=True)

mag,H,r,a,e,inc=np.genfromtxt("real31.txt",usecols=(1,2,3,4,5,6),unpack=True)



plt.figure(figsize=(6,8))
plt.subplots_adjust(hspace=0.3)

plt.subplot(321)
plt.plot(np.sort(tinc),np.arange(0.,1.,1./len(tinc))+1./len(tinc),'-k')
plt.plot(np.sort(dinc),np.arange(0.,1.,1./len(dinc))+1./len(dinc),':',c="#A4A4A4")
plt.plot(np.sort(inc),np.arange(0.,1.,1./len(inc))+1./len(inc),'ro',markersize=2)
plt.xlim(0,50)
plt.ylim(0,1)
plt.xlabel('inclination ($^{\circ}$)')
plt.ylabel('cumulative fraction')

plt.subplot(322)
plt.plot(np.sort(te),np.arange(0.,1.,1./len(te))+1./len(te),'-k')
plt.plot(np.sort(de),np.arange(0.,1.,1./len(de))+1./len(de),':',c="#A4A4A4")
plt.plot(np.sort(e),np.arange(0.,1.,1./len(e))+1./len(e),'ro',markersize=2)
plt.xlim(0.2,0.6)
plt.ylim(0,1)
plt.xlabel('eccentricity')

plt.subplot(323)
plt.plot(np.sort(tresamp),np.arange(0.,1.,1./len(tresamp))+1./len(tresamp),'-k')
plt.plot(np.sort(dresamp),np.arange(0.,1.,1./len(dresamp))+1./len(dresamp),':',c="#A4A4A4")
#plt.plot(np.sort(resamp[resamp<999]),np.arange(0.,1.,1./len(resamp[resamp<999]))+1./len(resamp[resamp<999]),'ro',markersize=2)
plt.xlim(0,180)
plt.ylim(0,1)
plt.xlabel('A$_{\phi}$ ($^{\circ}$)')
plt.ylabel('cumulative fraction')

plt.subplot(324)
plt.plot(np.sort(tH),np.arange(0.,1.,1./len(tH))+1./len(tH),'-k')
plt.plot(np.sort(dH),np.arange(0.,1.,1./len(dH))+1./len(dH),':',c="#A4A4A4")
plt.plot(np.sort(H),np.arange(0.,1.,1./len(H))+1./len(H),'ro',markersize=2)
plt.xlim(6,9.5)
plt.ylim(0,1)
plt.xlabel('H$_{r}$')


plt.subplot(325)
plt.plot(np.sort(tr),np.arange(0.,1.,1./len(tr))+1./len(tr),'-k')
plt.plot(np.sort(r),np.arange(0.,1.,1./len(r))+1./len(r),'ro',markersize=2)
plt.xlim(30,55)
plt.ylim(0,1)
plt.xlabel('dist. at detection [AU]')

plt.savefig('cumuplot31.png')
plt.show()
