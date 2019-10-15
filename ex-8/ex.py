from origin import *


ex = Spot("./data/ex.jpg")
ex_crop = Spot(ex.imcut(box))

sumI_ex = ex.sumI
sumI_ex_crop = ex_crop.sumI
eta1 = sumI_ex/sumI
eta2 = sumI_ex_crop/sumI_ex
sigma = ex_crop.sigma

print("eta1 = %f"%eta1) #>1是因为原先过曝了，图像中最大只能到255。
print("eta2 = %f"%eta2) #因此这个相对值更有价值
print("sigma_ex = %f"%sigma) #这个值代表了平整度
print("Dx = %f"%ex_crop.D_column) #这两个值代表了平整度
print("Dy = %f"%ex_crop.D_row)
print("relative Dx = %f"%ex_crop.D_column_R) #这两个值代表了D与图片尺度的相对值，表达了平整度，说明图片中有突出的部分
print("relative Dy = %f"%ex_crop.D_row_R)
#ex.bar3d("ex.png")


