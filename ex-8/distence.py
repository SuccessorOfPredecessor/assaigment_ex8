from origin import *

dis = []
dis_crop = []
dis_sumI = []
dis_crop_sumI = []
dis_sumI_R = []
dis_DxR = []
dis_DyR = []

for i in range(-3,5,1):
    dis.append(Spot('./data/dis_'+str(i)+'.jpg'))
    dis_crop.append(Spot(dis[-1].imcut(box)))
    dis_sumI.append(dis[-1].sumI)
    dis_crop_sumI.append(dis_crop[-1].sumI)
    dis_sumI_R.append(dis_crop_sumI[-1]/dis_sumI[-1])
    dis_DxR.append(dis[-1].D_column_R)
    dis_DyR.append(dis[-1].D_row_R)

x = np.arange(-3,5,1)

plt.plot(x, dis_sumI_R,'-o',label='relative_I')
plt.legend(loc = 'upper right')
plt.savefig('dis_I_ratio.png')
plt.show()
plt.plot(x, dis_DxR,'-o',label='DxR')
plt.plot(x, dis_DyR,'-o',label='DyR')
plt.legend(loc = 'upper right')
plt.savefig('dis_D.png')
plt.show()


