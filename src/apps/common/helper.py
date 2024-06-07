from django.core.exceptions import ValidationError
from PIL import Image


def validate_file_size(value):
    filesize = value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value
    
def validate_image_size(value):
    img = Image.open(value)
    width, height = img.size
    if width > 1920 or height > 1080:
        raise ValidationError("The maximum image size that can be uploaded is 1920x1080")
    else:
        return value
    