from Cv_Image import Image, Rectangle, Blur


cv = Image("assignment2.png")  # OpenCv2 class init
image = cv.read_image()  # Image read
cv.display_image(1000)  # Display image #1

brd = 4  # border size for rectangle
# rectangle shape creation
rec = Rectangle(image.copy(), brd).draw_rectangle((280, 0), (730, 600))
cv.display_image(1000, rec)  # Display image with rectangle #2

blur = Blur(image, (20, 20)).blur_image()  # Blur the original image
# mask creation for the combgination
mask = Rectangle(image, brd).cut_mask((280+brd, 0+brd), (730-brd, 600-brd))
# combined and blured shrek
cv.display_image(1000, cv.combiner(blur, mask, rec))
