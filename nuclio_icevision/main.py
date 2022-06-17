from __future__ import annotations
import json
import base64
from PIL import Image
import io
import numpy as np
import yaml

from icevision.models import model_from_checkpoint
from icevision_model_handler import IcevisionModelHandler


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def init_context(context):
    context.logger.info("Init context...  0%")

    # Read labels
    with open("/opt/nuclio/function.yaml", "rb") as function_file:
        functionconfig = yaml.safe_load(function_file)
    annotations = functionconfig["metadata"]["annotations"]

    # Read the DL model
    checkpoint_and_model = model_from_checkpoint(annotations["checkpoint_path"])
    model_handler = IcevisionModelHandler(checkpoint_and_model=checkpoint_and_model)
    context.user_data.model = model_handler

    context.logger.info("Init context...100%")


def handler(context, event):
    context.logger.info("Run Icevision model")
    data = event.body
    buf = io.BytesIO(base64.b64decode(data["image"]))
    threshold = float(data.get("threshold", 0.5))
    image = Image.open(buf)

    results = context.user_data.model.infer(image, threshold)

    return context.Response(
        body=json.dumps(results, cls=NpEncoder),
        headers={},
        content_type="application/json",
        status_code=200,
    )
