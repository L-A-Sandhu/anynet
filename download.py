from tensorflow.keras.datasets import cifar10
import numpy as np
import os
import cv2
def load_data():
	(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()
	return(train_images, train_labels, test_images, test_labels)
train_images, train_labels, test_images, test_labels= load_data()
# for i in range(len(train_images))
x = np.unique(train_labels)
print(x)
for i in range(len(x)):
	if not os.path.isdir('data/train/n'+str(x[i])):
		os.makedirs('data/train/n'+str(x[i]))

for i in range(len(train_images)):
	img_name= 'data/train/n'+str(int(train_labels[i]))+'/'+str(i)+'.jpg'
	print(img_name)
	cv2.imwrite(img_name,train_images[i])

x = np.unique(test_labels)
print(x)
for i in range(len(x)):
	if not os.path.isdir('data/val/n'+str(x[i])):
		os.makedirs('data/val/n'+str(x[i]))

for i in range(len(test_images)):
	img_name= 'data/val/n'+str(int(test_labels[i]))+'/'+str(i)+'.jpg'
	print(img_name)
	cv2.imwrite(img_name,test_images[i])

