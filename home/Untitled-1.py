# %%
import pickle

# %%
#importing libraries
import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras

# %%
# load saved model
with open('model.pkl' , 'rb') as f:
    lr = pickle.load(f)

# %%
#Saving the model

lr.save("model_dl.h5")

#Loading themodel

lr = keras.models.load_model("model_dl.h5") #look for local saved file

# %%
#We´ll use any image sample from the Kaggle dataset to test it 

from keras.preprocessing import image
batch_size = 32
img_height = 64
img_width = 64
#Creating a dictionary to map each of the indexes to the corresponding number or letter

dict = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f",16:"g",
        17:"h",18:"i",19:"j",20:"k",21:"l",22:"m",23:"n",24:"o",25:"p",26:"q",27:"r",28:"s",29:"t",30:"u",31:"v",32:"w",
        33:"x",34:"y",35:"z"}

#Predicting images

img = image.load_img("/content/hand1_0_bot_seg_1_cropped.jpeg", target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

image = np.vstack([x])
print(lr.predict(x))
classes = np.argmax(lr.predict(x), axis=-1)
print(np.shape(classes))
#probabilities = model_dl.predict(image, batch_size=batch_size)
#probabilities_formatted = list(map("{:.2f}%".format, probabilities[0]*100))

print(classes) #displaying matrix prediction position

print(f'The predicted image corresponds to "{dict[classes.item()]}"') #displaying matrix prediction position name (number or letter)

# %%



