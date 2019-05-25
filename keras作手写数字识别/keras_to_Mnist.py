import keras
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.models import load_model
from keras.datasets import mnist
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
import numpy as np
import struct
from skimage import io
from keras import backend as K
K.set_image_dim_ordering('tf')
# 数据加载
from PIL import Image
def decode_idx3_ubyte(idx3_ubyte_file):
    """
    解析idx3文件的通用函数
    :param idx3_ubyte_file: idx3文件路径
    :return: 数据集
    """
    # 读取二进制数据
    bin_data = open(idx3_ubyte_file, 'rb').read()

    # 解析文件头信息，依次为魔数、图片数量、每张图片高、每张图片宽
    offset = 0
    fmt_header = '>iiii'
    magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
    print('魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols))

    # 解析数据集
    image_size = num_rows * num_cols
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((num_images, num_rows, num_cols))
    for i in range(num_images):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
        offset += struct.calcsize(fmt_image)
    return images


def decode_idx1_ubyte(idx1_ubyte_file):
    """
    解析idx1文件的通用函数
    :param idx1_ubyte_file: idx1文件路径
    :return: 数据集
    """
    # 读取二进制数据
    bin_data = open(idx1_ubyte_file, 'rb').read()

    # 解析文件头信息，依次为魔数和标签数
    offset = 0
    fmt_header = '>ii'
    magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
    print('魔数:%d, 图片数量: %d张' % (magic_number, num_images))

    # 解析数据集
    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(num_images)
    for i in range(num_images):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
        offset += struct.calcsize(fmt_image)
    return labels

train_x = decode_idx3_ubyte('train-images.idx3-ubyte')
# test_x = decode_idx3_ubyte('t10k-images.idx3-ubyte')
# train_y = decode_idx1_ubyte('train-labels.idx1-ubyte')
# test_y = decode_idx1_ubyte('t10k-labels.idx1-ubyte')
print(train_x.shape)


# data = np.load('mnist.npz')
# train_x = data['x_train']
# train_y = data['y_train']
# test_x = data['x_test']
# test_y = data['y_test']

# (train_x, train_y), (test_x, test_y) = mnist.load_data()
# # 输入数据为 mnist 数据集
# train_x = train_x.reshape(train_x.shape[0], 28, 28, 1)
# test_x = test_x.reshape(test_x.shape[0], 28, 28, 1)
# train_x = train_x / 255
# test_x = test_x / 255
# train_y = keras.utils.to_categorical(train_y, 10)
# test_y = keras.utils.to_categorical(test_y, 10)
# print(test_x.shape)



# # 创建序贯模型
# model = Sequential()
# # 第一层卷积层: 6 个卷积核, 大小为 5*5, relu 激活函数
# model.add(Conv2D(6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
# # 第二层池化层: 最大池化
# model.add(MaxPooling2D(pool_size=(2, 2)))
# # 第三层卷积层: 16个卷积核， 大小为 5*5, relu 激活函数
# model.add(Conv2D(16, kernel_size=(5, 5), activation='relu'))
# # 第二层池化层: 最大池化
# model.add(MaxPooling2D(pool_size=(2, 2)))
# # 将参数进行扁平化, 在leNet5 中称为卷积层, 实际上这一层是一维向量, 和全连接层一样
# model.add(Flatten())
# model.add(Dense(120, activation='relu'))
# # 全连接层, 输出节点个数为 84 个
# model.add(Dense(84, activation='relu'))
# # 输出层, 用 softmax 激活函数计算分类概率
# model.add(Dense(10, activation='softmax'))
# # 设置损失函数和优化器配置
# model.compile(loss=keras.metrics.categorical_crossentropy, optimizer=keras.optimizers.Adam(), metrics=['accuracy'])
# # 传入训练数据进行训练
# model.fit(train_x, train_y, batch_size=128, epochs=2, verbose=1, validation_data=(test_x, test_y))
# # 对结果进行评估
# score = model.evaluate(test_x, test_y)
# model.save('my_model.h5')
# print('误差%0.4lf' %score[0])
# print('准确率:', score[1])





NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
CAPTCHA_LEN=1
CAPTCHA_CHARSET = NUMBER

def vec2text(vector):
    if not isinstance(vector, np.ndarray):
        vector = np.asarray(vector)
    vector = np.reshape(vector, [CAPTCHA_LEN, -1])
    print("vector: ",vector)
    text = ''
    for item in vector:
        text += CAPTCHA_CHARSET[np.argmax(item)]
    return text








from PIL import Image


img = Image.open('1.jpg',)
# img = img / 255
img = img.convert('1')
img.show()
I = np.asarray(img)
I = I.reshape(1,28,28,1)
print(I.shape)
model = load_model('my_model.h5')
predict_y = model.predict(I)
# # score = model.evaluate(test_x, test_y)
# model.save('my_model.h5')
# print('误差%0.4lf' %score[0])
# print('准确率:', score[1])
print(predict_y)
plt.imshow(predict_y)
plt.show()
print(vec2text(predict_y))