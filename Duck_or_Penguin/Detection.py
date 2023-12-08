import tensorflow as tf
import numpy as np

def detection(image_path):
    if image_path:
        model = tf.keras.models.load_model("Duck_or_Penguin/CNN_Model/")
        canard = tf.keras.utils.load_img(image_path, target_size=(224,224))
        img_array = tf.keras.utils.img_to_array(canard)
        img_array = tf.expand_dims(img_array, 0)

        prediction = model.predict(img_array)
        score = tf.nn.softmax(prediction[0])
        return (np.argmax(score))
    else:
        return (None)