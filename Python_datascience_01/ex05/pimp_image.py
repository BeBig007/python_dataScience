import numpy
from PIL import Image
from matplotlib import pyplot


def ft_invert(array) -> numpy.ndarray:
    """Inverts the color of the image received.

Args:
    array (numpy.ndarray): Image as a numpy array.

Returns:
    numpy.ndarray: Inverted image as a numpy array.
    """
    try:
        assert isinstance(array, numpy.ndarray), "Input must be a numpy array"

        img = Image.fromarray(array)
        r, g, b = img.split()
        inv_r = Image.new('L', img.size)
        inv_g = Image.new('L', img.size)
        inv_b = Image.new('L', img.size)

        for x in range(img.width):
            for y in range(img.height):
                inv_r.putpixel((x, y), 255 - r.getpixel((x, y)))
                inv_g.putpixel((x, y), 255 - g.getpixel((x, y)))
                inv_b.putpixel((x, y), 255 - b.getpixel((x, y)))

        inverted_image = Image.merge("RGB", (inv_r, inv_g, inv_b))

        pyplot.imshow(inverted_image)
        pyplot.axis('off')
        pyplot.title("Invert")
        pyplot.show()

        return numpy.array(img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")

    return None

# import PIL.ImageOps
# inverted_image = PIL.ImageOps.invert(img)


def ft_red(array) -> numpy.ndarray:
    """Display the red channel of the image.

Args:
    array (numpy.ndarray): Image as a numpy array.

Returns:
    numpy.ndarray: Image with only the red channel as a numpy array.
    """
    try:
        assert isinstance(array, numpy.ndarray), "Input must be a numpy array"

        red_chan = array[:, :, 0]
        red_img = numpy.zeros(array.shape, dtype=array.dtype)
        red_img[:, :, 0] = red_chan

        pyplot.imshow(red_img)
        pyplot.axis('off')
        pyplot.title("Red")
        pyplot.show()

        return numpy.array(red_img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")

    return None


def ft_green(array) -> numpy.ndarray:
    """Display the green channel of the image.

Args:
    array (numpy.ndarray): Image as a numpy array.

Returns:
    numpy.ndarray: Image with only the green channel as a numpy array.
    """
    try:
        assert isinstance(array, numpy.ndarray), "Input must be a numpy array"

        green_chan = array[:, :, 1]
        green_img = numpy.zeros(array.shape, dtype=array.dtype)
        green_img[:, :, 1] = green_chan

        pyplot.imshow(green_img)
        pyplot.axis('off')
        pyplot.title("Green")
        pyplot.show()

        return numpy.array(green_img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")

    return None


def ft_blue(array) -> numpy.ndarray:
    """Display the blue channel of the image.

Args:
    array (numpy.ndarray): Image as a numpy array.

Returns:
    numpy.ndarray: Image with only the blue channel as a numpy array.
    """
    try:
        assert isinstance(array, numpy.ndarray), "Input must be a numpy array"

        blue_chan = array[:, :, 2]
        blue_img = numpy.zeros(array.shape, dtype=array.dtype)
        blue_img[:, :, 2] = blue_chan

        pyplot.imshow(blue_img)
        pyplot.axis('off')
        pyplot.title("Blue")
        pyplot.show()

        return numpy.array(blue_img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")

    return None


def ft_grey(array) -> numpy.ndarray:
    """Display the image in grayscale.

Args:
    array (numpy.ndarray): Image as a numpy array.

Returns:
    numpy.ndarray: Grayscale image as a numpy array.
    """
    try:
        assert isinstance(array, numpy.ndarray), "Input must be a numpy array"

        img = Image.fromarray(array)
        gray_img = img.convert("L")

        pyplot.imshow(gray_img, cmap='gray')
        pyplot.axis('off')
        pyplot.title("Grey")
        pyplot.show()

        return numpy.array(img)

    except AssertionError as msg:
        print(f"AssertionError: {msg}")
    except Exception as e:
        print(f"Error: {e}")

    return None
