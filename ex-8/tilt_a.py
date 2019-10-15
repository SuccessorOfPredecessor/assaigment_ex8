from origin import *

tilt_a= [] #倾斜DOE图
tilt_a_crop = []
tilt_a_sigma = []
tilt_a_sumI = []

for i in range(1,5,1):
    tilt_a.append(Spot('./data/tilt_a'+str(i)+'.jpg'))
    tilt_a_crop.append(Spot(tilt_a[-1].imcut(box)))
    tilt_a_sigma.append(tilt_a_crop[-1].sigma)
    tilt_a_sumI.append(tilt_a_crop[-1].Ibar)

x = np.arange(1,5,1)
plt.plot(x, tilt_a_sigma,'-o',label='sigma')
plt.legend(loc = 'upper right')
plt.savefig('tilt_a_sigma.png')
plt.show()
plt.plot(x, tilt_a_sumI,'-o',label='I')
plt.legend(loc = 'upper right')
plt.savefig('tilt_a_sumI.png')
plt.show()
