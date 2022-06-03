from tensorflow import keras

class KerasModel:
    def __init__(self):
        # Load preprocessing layer
        self.preprocessing_layer = keras.models.load_model('./Models/preprocessing_layer')

        # Load encoder model
        self.encoder_model = keras.models.load_model('./Models/encoder_model')

    
    def preprocess_and_encode(self, item_features_dict):
        p_item = self.preprocessing_layer(item_features_dict)
        encoded_item = self.encoder_model(p_item)

        return encoded_item