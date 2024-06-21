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
            return numpy.array(img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    except FileNotFoundError:
        print(f"FileNotFoundError: The file at path '{path}' does not exist")

    except Exception as e:
        print(f"Error: {e}")

    return None


def ft_zoom(img_arr: numpy.ndarray) -> numpy.ndarray:
    """Zoom in on a section of the image and convert to grayscale.

    Args:
        img_arr (np.ndarray): Image as a numpy array.

    Returns:
        np.ndarray: Zoomed and grayscale image as a numpy array.
    """
    try:
        assert isinstance(img_arr, numpy.ndarray), \
            "Input must be a numpy array"

        img = Image.fromarray(img_arr)
        gray_img = img.crop((450, 100, 850, 500)).convert("L")
        gray_img_arr = numpy.array(gray_img)
        gray_img_arr = gray_img_arr[:, :, numpy.newaxis]
        print(f"The shape of image is: {gray_img_arr.shape}")

        return gray_img_arr

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    except Exception as e:
        print(f"Error: {e}")

    return None
