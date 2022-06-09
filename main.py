from Cv_Image import Image, Rectangle, Blur


cv = Image("assignment2.png")
image = cv.read_image()
cv.display_image(1000)
brd = 4
rec = Rectangle(image.copy(), brd).draw_rectangle((280, 0), (730, 600))
cv.display_image(1000, rec)
blur = Blur(image, (20, 20)).blur_image()
mask = Rectangle(image, brd).cut_mask((280+brd, 0+brd), (730-brd, 600-brd))
cv.display_image(1000, cv.combiner(blur, mask, rec))
