#对微信页面进行分割
from sklearn.cluster import KMeans
import PIL.Image as image
from sklearn import preprocessing
import numpy as np
from skimage import color

def load_data(filePath):
    # 读文件
    with open(filePath,'rb') as f:
        data=[]
        # 得到图像的像素值
        img=image.open(f)
        # 得到图像尺寸
        width,height=img.size
        for x in range(width):
            for y in range(height):
                # 得到点(x,y)的三个通道值
                c1,c2,c3=img.getpixel((x,y))
                data.append([c1,c2,c3])
    # 采用Min-Max规范化
    mm=preprocessing.MinMaxScaler()
    data=mm.fit_transform(data)
    return np.mat(data),width,height


if __name__=='__main__':
    img,width,height=load_data('weixin.jpg')
    kmeans=KMeans(n_clusters=16)
    kmeans.fit(img)
    label=kmeans.predict(img)
    # 将图像聚类的结果，转化成图像尺寸的矩阵
    label=label.reshape([width,height])



    # # 创建个新图像pic_mark,用来保存图像聚类的结果，并设置不同的灰度值
    # pic_mark=image.new('L',(width,height))
    # for x in range(width):
    #     for y in range(height):
    # #         # 根据类别设置图像灰度，类别0灰度值为255，类别1灰度值设为127:
    #         pic_mark.putpixel((x,y),int(256/(label[x][y]+1)-1))
    # pic_mark.save('weixin_mark.jpg','JPEG')



    # 将聚类标识矩阵转化为不同颜色的矩阵
    label_color = (color.label2rgb(label) * 255).astype(np.uint8)
    # 互换第一维和第二维
    label_color = label_color.transpose(1, 0, 2)
    # 通过矩阵生成图像
    images = image.fromarray(label_color)
    images.save('weixin_color.jpg')