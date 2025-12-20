import numpy as np



def con(img, kernel, stride=1,padding=1):


     if padding>0:
      img=np.pad(img, ((padding,padding),(padding,padding)), mode="constant")

     h,w=img.shape
     h1,w1=kernel.shape

     v=(h-h1)//stride+1
     c=(w-w1)//stride+1

     z=np.zeros((v,c))
     for i in range (v):
       for j in range (c):
        patch=img[i*stride:i*stride+h1,j*stride:j*stride+w1]
        z[i][j]=np.sum(patch*kernel)
     return z  



b=np.array([[1,2,3],[1,2,3]])
c=np.array([[1,2],[1,2]])


s=con(b,c)
print(s)