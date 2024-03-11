from .CozyPoseReferenceFaceCustomNode import CozyPoseReferenceFaceCustomNode
from .CozyPoseReferenceBodyCustomNode import CozyPoseReferenceBodyCustomNode

NODE_CLASS_MAPPINGS = {
  "Cozy Pose Face Reference" : CozyPoseReferenceFaceCustomNode,
  "Cozy Pose Body Reference" : CozyPoseReferenceBodyCustomNode,
}

__all__ = ['NODE_CLASS_MAPPINGS']