import numpy
from PIL import Image
from matplotlib import pyplot
from load_image import ft_load, ft_zoom


def ft_rotate(img_arr: numpy.ndarray) -> numpy.ndarray:
    """Rotate the image 90 degrees.

    Args:
        img_arr (numpy.ndarray): Image as a numpy array.

    Returns:
        numpy.ndarray: Rotated image as a numpy array.
    """
    try:
        assert isinstance(img_arr, numpy.ndarray), "Input must be a numpy array"

        flipped_img_arr = numpy.rot90(img_arr)
        print(f"New shape after Transpose: {flipped_img_arr.shape}")

        pyplot.imshow(flipped_img_arr, cmap='gray')
        pyplot.show()

        return flipped_img_arr

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")
    return None

def main():
    img = ft_load("animal.jpeg")
    if img is not None:
        zoomed_img = ft_zoom(img)
        if zoomed_img is not None:
            print(zoomed_img)
            rotated_img = ft_rotate(zoomed_img)
            if rotated_img is not None:
                print(rotated_img)


if __name__ == "__main__":
    main()
