# Calculates the number of objects in an H distribution for a specified H with a distribution that has been specified and pegged for a number N at an Hn
class Hdist:
    
    def __init__(self,af,ab,Hd,c, Hn, N):
        self.af = af
        self.ab = ab
        self.Hd = Hd
        self.c = c
        self.Hn = Hn
        self.N = N #The number at some H, Hn

        if Hn <= Hd:
            self.kb = self.N/(10.0**(self.ab*self.Hn))
            self.kf = self.kb*self.ab/self.af*(10**(self.ab*self.Hd))/(10**(self.af*self.Hd)*self.c)
        if Hn>Hd:
            self.Nbd = self.N *( 1. + self.ab/self.af/self.c*(10**(self.af*(self.Hn-self.Hd))-1))**(-1.)
            self.Nad = self.N-self.Nbd
            
            self.kf = self.Nad*(10**(self.af*self.Hn)-10**(self.af*self.Hd))**(-1)
            self.kb = self.kf/(self.ab/self.af*(10**(self.ab*self.Hd))/(10**(self.af*self.Hd)*self.c))


    def Hlt(self,H, type='Divot'):
        if H> self.Hd and type is not 'SPL':
            Nbd = self.kb*10**(self.ab*self.Hd)
            Nad = self.kf*(10**(self.af*H)-10**(self.af*self.Hd))
            return (Nbd+Nad)
        if type is 'SPL' or H<=self.Hd:
            return (self.kb*(10.0**(self.ab*H)))



# specify the size distribution in the following format
#      Hdist(af,ab,Hd,c, Hn, N)
#      af = the faint side slope for knees/divots. Set to the same as bright for Single Power-Law (SPL)
#      ab = the bright side slope
#      Hd = the H magnitude of the break (change to divot/knee). Set to your faintest H for SPL
#      c = the contrast for your divot. c=1 is a knee or SPL, c>1 a divot
#      Hn = the H magnitude your number N (next variable) is measured at. e.g. the number of drawn files from the survey simulator
#      N = the number of objects in the distribution at a specified H=Hn


n = 150400. * 12.0 / 100.0

# Here is a divot
divot = Hdist(0.5,0.9,8.3,3.16,10,n)
# now here you calculate the number at any H magnitude you want. You just have to specify if your size distribution is a SPL or not.
# If it is not an SPL, you just put in the H mag you want the number for as below:
num = divot.Hlt(8)
print num
#print "%1.2e"%(num*0.33) # .33 is fraction in the d range 30-50 au, which volk and malhotra need


#n = 370585869.0 * 22.0/1000.0

# here is a SPL
# note that I've put ab = af = 0.8, c=1 and set Hd=Hn
#divot2 = Hdist(0.4,0.9,8.3,1,14,n)

#num = divot2.Hlt(17.3)

#print "%1.2e"%(num*0.33) # .33 is fraction in the d range 30-50 au, which volk and malhotra need


#divot2 = Hdist(0.9,0.9,8,1,8,500000)

#num = divot2.Hlt(17.3)

#print "%1.2e"%(num*0.33) # .33 is fraction in the d range 30-50 au, which volk and malhotra need


#splSed = Hdist(0.8,0.8,4,1,1.6,80)

#num = splSed.Hlt(8.7)

#print 'Seda population to H = 8: %1.2e'%(num)


## if it is an SPL, just specify the type like so
#num = spl.Hlt(7,type='SPL')
## now calculate the number for a different H
#num2 = spl.Hlt(12, type='SPL') 
##Should be the same as 1000 as that's what we input for H=9
#num3 = spl.Hlt(9, type='SPL') 
#print num, num2, num3



