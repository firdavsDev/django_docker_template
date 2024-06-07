import os
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
    """File rename & repath

    Args:
        object: renamed path
    """

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split(".")[-1]
        filename = filename.split(".")[0]
        filename = f"{filename}_{uuid4().hex[:4]}.{ext}"
        return os.path.join(self.path, filename)
