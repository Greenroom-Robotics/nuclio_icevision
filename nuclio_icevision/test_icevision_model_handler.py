from PIL import Image
import os
from icevision.models import model_from_checkpoint

from icevision_model_handler import IcevisionModelHandler


def test_icevision_model_handler():
    """
    Runs the icevision model handler (bypassing nuclio)
    Should detect milk bottle in the image
    """
    checkpoint_path = "https://github.com/airctic/model_zoo/releases/download/m6/fridge-retinanet-checkpoint-full.pth"

    checkpoint_and_model = model_from_checkpoint(checkpoint_path)
    model_handler = IcevisionModelHandler(checkpoint_and_model=checkpoint_and_model)
    image = Image.open(os.path.join(os.getcwd(), "./fixtures/milk.jpg"))

    result = model_handler.infer(image, 0.8)

    assert len(result) == 1
    assert result[0]["label"] == "milk_bottle"
    assert result[0]["points"] == (240, 190, 356, 494)
