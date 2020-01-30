import numpy as np

################
#builds up a population of resonant TNOs.
#relative populations and orbital distributions from CFEPS (Gladman et al. 2012)
#Roughly based on the GiMeObj routine from the OSSOS survey simulator
################
#user needs to set number of objects and filename

nobj=10000
f=open("biglistofres.aei","w")


class iv:
# Class to hold the initial variables (iv)
    e = None
    ei = 0
    el = 0
    firste = True

    e2 = None
    ei2 = 0
    el2 = 0
    firste2 = True

    inc = None
    inci = 0
    incl = 0
    firstinc=True

    resamp = None
    resampi = 0
    resampl = 0
    firstresamp = True

    resamp2 = None
    resampi2 = 0
    resampl2 = 0
    firstresamp2 = True


def drawinc(mu,sigma):
    size = 10**6

    ind = iv.inci
    if iv.firstinc == False and ind!= iv.incl:
        inc = iv.inc[ind]
        iv.inci += 1
        return inc

    incmin = 0
    incmax = 90*np.pi/180

    sigma = sigma*np.pi/180 # e.g. 6.9     
    mu = mu*np.pi/180 #e.g. 19.3 

    if iv.firstinc==True:
       iv.xpinc = np.arange(0,incmax, 0.01)
       y = (np.sin(iv.xpinc)*np.exp(-(iv.xpinc-mu)**2/(2*sigma**2))).cumsum()
       iv.yinc = y/max(y)

       iv.firstinc = False

    rv2 = np.random.rand(size)
    iv.inc = np.interp(rv2, iv.yinc, iv.xpinc)
    iv.inc = iv.inc[iv.inc>incmin]
    iv.incl = len(iv.inc)
    iv.inci = 0

    return iv.inc[0]

def drawinc(mu,sigma):
    size = 10**6

    ind = iv.inci
    if iv.firstinc == False and ind!= iv.incl:
        inc = iv.inc[ind]
        iv.inci += 1
        return inc

    incmin = 0
    incmax = 90*np.pi/180

    sigma = sigma*np.pi/180 # e.g. 6.9     
    mu = mu*np.pi/180 #e.g. 19.3 

    if iv.firstinc==True:
       iv.xpinc = np.arange(0,incmax, 0.01)
       y = (np.sin(iv.xpinc)*np.exp(-(iv.xpinc-mu)**2/(2*sigma**2))).cumsum()
       iv.yinc = y/max(y)

       iv.firstinc = False

    rv2 = np.random.rand(size)
    iv.inc = np.interp(rv2, iv.yinc, iv.xpinc)
    iv.inc = iv.inc[iv.inc>incmin]
    iv.incl = len(iv.inc)
    iv.inci = 0

    return iv.inc[0]

def drawecc(ec,ew):
    size = 10**6

    ind = iv.ei
    if iv.firste == False and ind!= iv.el:
        e = iv.e[ind]
        iv.ei += 1
        return e

    emin = 0.0
    emax = 1.0
                                                                                                                                                                           
    if iv.firste==True:
       iv.xpe = np.arange(emin,emax, 0.01)
       y = (np.exp(-(iv.xpe-ec)**2/(2*ew**2))).cumsum()
       iv.ye = y/max(y)

       iv.firste = False

    rv2 = np.random.rand(size)
    iv.e = np.interp(rv2, iv.ye, iv.xpe)
    iv.e = iv.e[iv.e>emin]
    iv.el = len(iv.e)
    iv.ei = 0

    return iv.e[0]

def drawecc2(ec2,ew2):
    size = 10**6

    ind = iv.ei2
    if iv.firste2 == False and ind!= iv.el2:
        e2 = iv.e2[ind]
        iv.ei2 += 1
        return e2

    emin = 0.0
    emax = 1.0
                                                                                                                                                                           
    if iv.firste2==True:
       iv.xpe2 = np.arange(emin,emax, 0.01)
       y = (np.exp(-(iv.xpe2-ec2)**2/(2*ew2**2))).cumsum()
       iv.ye2 = y/max(y)

       iv.firste2 = False

    rv2 = np.random.rand(size)
    iv.e2 = np.interp(rv2, iv.ye2, iv.xpe2)
    iv.e2 = iv.e2[iv.e2>emin]
    iv.el2 = len(iv.e2)
    iv.ei2 = 0

    return iv.e2[0]

def drawresamp(loamp,midamp,hiamp):
    size = 10**6

    ind = iv.resampi
    if iv.firstresamp == False and ind!= iv.resampl:
        resamp = iv.resamp[ind]
        iv.resampi += 1
        return resamp

                                                                                                                                                                          
    if iv.firstresamp==True:
       iv.xpresamp = np.arange(loamp,hiamp, 0.01)
       y1 = (1./(midamp-loamp)*iv.xpresamp[iv.xpresamp<midamp]-loamp/(midamp-loamp))
       y2 = (-1./(hiamp-midamp)*iv.xpresamp[iv.xpresamp>=midamp]+hiamp/(hiamp-midamp))
       y=np.append(y1,y2).cumsum()
       iv.yresamp = y/max(y)

       iv.firstresamp = False

    rv2 = np.random.rand(size)
    iv.resamp = np.interp(rv2, iv.yresamp, iv.xpresamp)
    iv.resamp = iv.resamp[iv.resamp>loamp]
    iv.resampl = len(iv.resamp)
    iv.resampi = 0

    return iv.resamp[0]

def drawresamp2(loamp2,midamp2,hiamp2):
    size = 10**6

    ind = iv.resampi2
    if iv.firstresamp2 == False and ind!= iv.resampl2:
        resamp2 = iv.resamp2[ind]
        iv.resampi2 += 1
        return resamp2

                                                                                                                                                                          
    if iv.firstresamp2==True:
       iv.xpresamp2 = np.arange(loamp2,hiamp2, 0.01)
       y1 = (1./(midamp2-loamp2)*iv.xpresamp2[iv.xpresamp2<midamp2]-loamp2/(midamp2-loamp2))
       y2 = (-1./(hiamp2-midamp2)*iv.xpresamp2[iv.xpresamp2>=midamp2]+hiamp2/(hiamp2-midamp2))
       y=np.append(y1,y2).cumsum()
       iv.yresamp2 = y/max(y)

       iv.firstresamp2 = False

    rv2 = np.random.rand(size)
    iv.resamp2 = np.interp(rv2, iv.yresamp2, iv.xpresamp2)
    iv.resamp2 = iv.resamp2[iv.resamp2>loamp2]
    iv.resampl2 = len(iv.resamp2)
    iv.resampi2 = 0

    return iv.resamp2[0]




#from CFEPS
#3:2, 5:2, 4:3, 5:3, 7:3, 7:4, 2:1
resfrac=[0.31,0.29,0.02,0.12,0.10,0.07,0.09]
resname=['3:2','5:2','4:3','5:3','7:3','7:4','2:1']

print>>f, "#a, e, inc, node, peri, M, resname"

#n1obj=int(sum(resfrac[6:9])*nobj)
#n234obj=nobj-n1obj

def draw_candidate(j,k,ec,ew,sigma,loamp,midamp,hiamp):
  #choose a within 0.5 of 30.1*(j/k)^(2/3)
  a = np.random.rand()*(1.0)-0.5 +30.1*(j/k)**(2./3.)
  e = drawecc(ec,ew)
  inc = drawinc(0.,sigma)
  resamp=drawresamp(loamp,midamp,hiamp)  #best from Volk+ 2016: 0, 75, 155
  return a,e,inc,resamp

def draw_candidate2(j,k,ec,ew,sigma,loamp,midamp,hiamp):
  #choose a within 0.5 of 30.1*(j/k)^(2/3)
  a = np.random.rand()*(1.0)-0.5 +30.1*(j/k)**(2./3.)
  e = drawecc2(ec,ew)
  inc = drawinc(0.,sigma)
  resamp=drawresamp2(loamp,midamp,hiamp)  #best from Volk+ 2016: 0, 75, 155
  return a,e,inc,resamp

counto=0
##3:2, ignoring Kozai in all resonances
while counto<resfrac[0]*nobj:
  j=3.
  k=2.
  #print counto, resname[0]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.18,0.06,16,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi #- 2.*np.pi*int(np.random.rand())
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*4.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[0]

##5:2
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:2])*nobj:
  j=5.
  k=2.
  #print counto, resname[1]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.3,0.1,14,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*4.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[1]

##4:3
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:3])*nobj:
  j=4.
  k=3.
  #print counto, resname[1]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.12,0.06,8,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*6.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[2]


##5:3
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:4])*nobj:
  j=5.
  k=3.
  #print counto, resname[1]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.16,0.06,11,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*6.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[3]

##7:3
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:5])*nobj:
  j=7.
  k=3. 
  #print counto, resname[1]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.16,0.06,11,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*6.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[4]

##7:4
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:6])*nobj:
  j=7.
  k=4.
  #print counto, resname[1]
  counto+=1
  a,e,inc,resamp = draw_candidate(j,k,0.16,0.06,11,0.,75.,155.)
  #choose value of phi sinusoidally from resamp
  phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*8.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[5]

##2:1
iv.firste = True
iv.firstinc=True
iv.firstresamp = True
while counto<sum(resfrac[0:7])*nobj:
  j=2.
  k=1.
  #print counto, resname[1]
  counto+=1
  #I can't think of a cute way to do this without using if statements. Oh well.
  if np.random.rand()<0.1:  #symmetric
    a, e, inc, resamp = draw_candidate(j,k,0.25,0.1,7.,120,150,170)
    #choose value of phi sinusoidally from resamp
    phi=np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
  else:  #asymmetric
    a, e, inc, resamp = draw_candidate2(j,k,0.2,0.1,7.,10,40,60)
    phi=80./180.*np.pi +np.sin(2.*np.pi*np.random.rand())*resamp/180.*np.pi
    if np.random.rand()>0.5:  #half in leading island, half in trailing island
      phi=2.*np.pi-phi
  # Assign two angles randomly
  node = np.random.rand()*2.*np.pi
  M = np.random.rand()*2.*np.pi
  #assign last angle so that phi works
  lambdaN=346.66462*np.pi/180.  #Neptune's mean longitude on 26 Feb 2019
  peri = (1./k*(phi - j*M) - node + lambdaN)%(2.*np.pi)
  print>>f, a, e, inc*180./np.pi, node*180./np.pi, peri*180./np.pi, M*180./np.pi, resname[6]


