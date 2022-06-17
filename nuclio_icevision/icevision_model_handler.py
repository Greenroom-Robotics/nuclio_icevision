from typing import Any
from PIL.Image import Image
from icevision.tfms import albumentations as A


class IcevisionModelHandler:
    def __init__(self, checkpoint_and_model: Any):
        self.model_type = checkpoint_and_model["model_type"]
        self.backbone = checkpoint_and_model["backbone"]
        self.class_map = checkpoint_and_model["class_map"]
        self.img_size = checkpoint_and_model["img_size"]
        self.model = checkpoint_and_model["model"]

        print(f"Model type: {self.model_type}")
        print(f"Backbone: {self.backbone}")
        print(f"Class map: {self.class_map}")
        print(f"Image Size: {self.img_size}")

        self.valid_tfms = A.Adapter([*A.resize_and_pad(self.img_size), A.Normalize()])

    def infer(self, image: Image, threshold: float = 0.0):
        pred_dict = self.model_type.end2end_detect(
            image,
            self.valid_tfms,
            self.model,
            class_map=self.class_map,
            detection_threshold=threshold,
        )
        # pred_dict["img"].show()

        detections = []

        for score, label, bbox in zip(
            pred_dict["detection"]["scores"],
            pred_dict["detection"]["labels"],
            pred_dict["detection"]["bboxes"],
        ):
            detections.append(
                {
                    "confidence": round(score, 2),
                    "label": label,
                    "points": (bbox.xmin, bbox.ymin, bbox.xmax, bbox.ymax),
                    "type": "rectangle",
                }
            )

        return detections
