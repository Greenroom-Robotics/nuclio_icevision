from PIL.Image import Image
from icevision.tfms import albumentations as A


class IcevisionModelHandler:
    def __init__(self, model, model_type, image_size=1024, labels={}):
        self.image_size = image_size
        self.labels = labels
        self.model = model
        self.model_type = model_type
        self.valid_tfms = A.Adapter([*A.resize_and_pad(image_size), A.Normalize()])
        self.class_map =

    def infer(self, image: Image, threshold: float = 0.0):
        pred_dict  = self.model_type.end2end_detect(
            image, 
            self.valid_tfms, 
            self.model, 
            class_map=self.class_map, 
            detection_threshold=threshold
        )
        print(pred_dict)

