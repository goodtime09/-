from skimage import color
from sklearn.cluster import KMeans
import numpy as np
import PIL.Image as image

def load_data(filePath):
    with open(filePath,'rb') as f:
        data=[]
        img=image.open(f)
        width,height=img.size
        for x in range(width):
            for y in range(height):
                c1,c2,c3=img.getpixel((x,y))
                data.append([(c1+1)/260.0,(c2+1)/260.0,(c3+1)/260.0])
    return np.mat(data),width,height

img,width,height=load_data('weixin.jpg')
kmeans=KMeans(n_clusters=16)
label=kmeans.fit_predict(img)
label=label.reshape([width,height])
img=image.new('RGB',(width,height))
for x in range(width):
    for y in range(height):
        c1=kmeans.cluster_centers_[label[x,y],0]
        c2 = kmeans.cluster_centers_[label[x, y], 1]
        c3 = kmeans.cluster_centers_[label[x, y], 2]
        img.putpixel((x,y),(int(c1*256-1),int(c2*256-1),int(c3*256-1)))
img.save('weixin_new.jpg')
