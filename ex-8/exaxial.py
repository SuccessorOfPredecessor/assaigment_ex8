from origin import *

exaxial = []
exaxial_crop = []
exaxial_sigma = []
exaxial_DxR = []
exaxial_DyR = []



for i in range(1,5,1):
    exaxial.append(Spot('./data/exaxial'+str(i)+'.jpg'))
    exaxial_crop.append(Spot(exaxial[-1].imcut(box)))
    exaxial_sigma.append(exaxial_crop[-1].sigma)
    exaxial_DxR.append(exaxial_crop[-1].D_column_R)
    exaxial_DyR.append(exaxial_crop[-1].D_row_R)


x = np.arange(1,5,1)
plt.plot(x, exaxial_sigma,'-o', label='sigma')
plt.legend(loc = 'upper right')
plt.savefig('exaxial_sigma.png')
plt.show()

plt.plot(x, exaxial_DxR,'-o',label='DxR')
plt.plot(x, exaxial_DyR,'-o',label='DyR')
plt.legend(loc = 'upper right')
plt.savefig('exaxial_D.png')
plt.show()

