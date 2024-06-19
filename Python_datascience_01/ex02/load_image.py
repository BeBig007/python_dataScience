import numpy
from PIL import Image

def ft_load(path: str) -> numpy.ndarray:
    """Load an image from a file.

    Args:
        path (str): Path to the image file.

    Returns:
        numpy.ndarray: Image as a numpy array.
    """
    try:
        assert isinstance(path, str), "The input must be string"
        with Image.open(path) as img:
            img.load()
            img_arr = numpy.array(img)
            print(f"The shape of image is: {img_arr.shape}")
            return img_arr
    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except FileNotFoundError:
        print(f"FileNotFoundError: The file at path '{path}' does not exist")
    except Exception as e:
        print(f"Error: {e}")
    return None

# img.show()
