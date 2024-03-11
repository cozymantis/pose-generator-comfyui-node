import os
import numpy as np
import torch
from PIL import Image

class CozyPoseReferenceFaceCustomNode:
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "vertical_position": (["north", "center", "south"], {"default": "center"}),
        "horizontal_position": (["west", "half-west", "center", "half-east", "east"], {"default": "center"}),
        "size": (["512", "1024"], {}),
      },
    }

  RETURN_TYPES = ("IMAGE",)
  RETURN_NAMES = ("pose",)
  FUNCTION = "run"
  CATEGORY = "CozyMantis"

  def run(self, vertical_position, horizontal_position, size):
    vertical_prefix = "n" if vertical_position == "north" else "s" if vertical_position == "south" else ""
    horizontal_prefix = "w" if horizontal_position == "west" else "hw" if horizontal_position == "half-west" else "c" if horizontal_position == "center" else "he" if horizontal_position == "half-east" else "e"
    pose_path = os.path.join(os.path.dirname(__file__), "poses", "face", size, f"{vertical_prefix}{horizontal_prefix}.png")
    image = Image.open(pose_path)
    image = image.convert("RGB")
    image = np.array(image).astype(np.float32) / 255.0
    image = torch.from_numpy(image)[None,]

    return (image,)
