import os
import numpy as np
import torch
from PIL import Image

class CozyPoseReferenceBodyCustomNode:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "angle": ("INT", {"default": 0, "min": 0, "max": 315, "step": 45}),
        "size": (["512", "1024"], {}),
      },
    }

  RETURN_TYPES = ("IMAGE",)
  RETURN_NAMES = ("pose",)
  FUNCTION = "run"
  CATEGORY = "CozyMantis"

  def run(self, angle, size):
    pose_path = os.path.join(os.path.dirname(__file__), "poses", "body", size, f"{angle}.png")
    image = Image.open(pose_path)
    image = image.convert("RGB")
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image)[None,]

    return (image,)
