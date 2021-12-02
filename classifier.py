import os
import tensorflow as tf
import numpy as np
import local_config as lc
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array


print('Loading Model..')
model = tf.keras.models.load_model(os.path.join(lc.MODEL_DIR, lc.MODEL_FILE))
model.trainable = False


def allowed_file(filename):
    """
    Checks if a given file `filename` is of type image with 'png', 'jpg', or 'jpeg' extensions
    """
    allowed_extensions = {'png', 'jpg', 'jpeg', 'jfif'}
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in allowed_extensions)


def prepare_image(image_path):
    """
    Loads image from the given `image_path` parameter
    """
    image = load_img(image_path, target_size=(lc.SIZE, lc.SIZE))
    return np.expand_dims(preprocess_input(img_to_array(image)), axis=0)


def make_prediction(filename):
    """
    Predicts a given `filename` file
    """
    print('Filename is ', filename)
    full_path = os.path.join(lc.OUTPUT_DIR, filename)
    test_data = prepare_image(full_path)
    predictions = model.predict(test_data)
    print(predictions)
    return lc.CLASSES[np.argmax(predictions[0])]
