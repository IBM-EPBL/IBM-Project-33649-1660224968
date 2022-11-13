from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

model = load_model('trained_model.h5')

def get_prediction(num):
  out = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',
         11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V',
         22:'W', 23:'X', 24:'Y', 25:'Z'}
  return out[num]

def predict(img_src):
  img = image.load_img(img_src, target_size=(128,128), color_mode='grayscale')
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  prediction = np.argmax(model.predict(x))
  return get_prediction(prediction)

