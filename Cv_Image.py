import cv2
import os
import numpy as np


def get_shape(image):
    """Return cv2 image shape in pixels - width and height"""
    return image.shape[1], image.shape[0]


class Image:
    """An OpenCV Image class to read and display images"""

    __slots__ = '__image'

    def __init__(self, image):
        """Constructs cv2 image for the class"""
        self.__image = image

    def get_name(self):
        """Returns the image name without extension"""
        return os.path.splitext(self.__image)[0]

    def read_image(self, mat=None):
        """Returns cv2 image"""
        if mat is None:
            return cv2.imread(self.__image)
        return mat

    def display_image(self, duration=0, img=None):
        """Displays image for passed duration"""
        if img is None:
            cv2.imshow(self.get_name(), self.read_image())
        else:
            cv2.imshow(self.get_name(), img)
        cv2.waitKey(duration)

    def combiner(self, target, mask, image=None):
        """Returns combines image and target image using mask"""
        if image is None:
            return np.where(mask == 0,  self.read_image(), target)
        return np.where(mask == 0,  image, target)


class Rectangle:
    """
    A class which:
    Expands image borders,
    creates rectangles in the image,
    and creates masks of rectangular form
    """

    __slots__ = '__image', '__border'

    def __init__(self, image, border):
        """Constructs cv2 image and border size for the class"""
        self.__image = image
        self.__border = border

    def replicate_border(self):
        """Return cv2 image with expanded borders"""
        b = self.__border
        img = self.__image
        return cv2.copyMakeBorder(img, b, b, b, b, cv2.BORDER_REPLICATE)

    def draw_rectangle(self, p0=None, p1=None, clr=(255, 0, 0)):
        """Return cv2 rectangle around image"""
        b = self.__border
        if (p0, p1) == (None, None) or (p0, p1) == ((0, 0), None):
            replicated = self.replicate_border()
            shape = get_shape(replicated)
            return cv2.rectangle(replicated, (0, 0), shape, clr, b)
        return cv2.rectangle(self.__image, p0, p1, clr, b)

    def cut_mask(self, p0, p1):
        """Return the rectangular form of mask"""
        shape = get_shape(self.__image)
        blank = np.zeros((shape[1], shape[0], 3), dtype='uint8')
        return cv2.rectangle(blank, p0, p1, (255, 255, 255), -1)


class Blur:
    """A class which blurs cv2 images"""

    __slots__ = '__image', '__blur'

    def __init__(self, image, size):
        """Constructs cv2 image and blur level for the class"""
        self.__image = image
        self.__blur = size

    def blur_image(self):
        """Returns blured cv2 image"""
        return cv2.blur(self.__image, self.__blur)
