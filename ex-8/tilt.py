from origin import *

tilt= [] #倾斜DOE图
tilt_crop = []
tilt_crop_sigma = []
tilt_crop_DxR = []
tilt_crop_DyR = []

for i in range(1,5,1):
    tilt.append(Spot('./data/tilt'+str(i)+'.jpg'))
    tilt_crop.append(Spot(tilt[-1].imcut(box)))
    tilt_crop_sigma.append(tilt_crop[-1].sigma)
    tilt_crop_DxR.append(tilt_crop[-1].D_column_R)
    tilt_crop_DyR.append(tilt_crop[-1].D_row_R)

x = np.arange(1,5,1)
plt.plot(x, tilt_crop_sigma,'-o',label='sigma')
plt.legend(loc = 'upper right')
plt.savefig('tilt_sigma.png')
plt.show()
plt.plot(x, tilt_crop_DxR,'-o',label='DxR')
plt.plot(x, tilt_crop_DyR,'-o',label='DyR')
plt.legend(loc = 'upper right')
plt.savefig('tilt_D.png')
plt.show()