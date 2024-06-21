import numpy
from PIL import Image
from matplotlib import pyplot
from load_image import ft_load


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
        print(f"New shape after slicing: {gray_img_arr.shape}")

        pyplot.imshow(gray_img_arr, cmap='gray')
        pyplot.show()

        return gray_img_arr

    except AssertionError as msg:
        print(f"AssertionError: {msg}")

    except Exception as e:
        print(f"Error: {e}")

    return None


def main():
    img = ft_load("animal.jpeg")
    if img is not None:
        print(img)
        zoomed_img = ft_zoom(img)
        if zoomed_img is not None:
            print(zoomed_img)


if __name__ == "__main__":
    main()
