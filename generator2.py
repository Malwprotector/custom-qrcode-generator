import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image

#place the name of your image here.
logo = Image.open('logo.png')

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L
    , version = 2
    , border=1
    , box_size=12,
)
qr.add_data('https://cutt.ly/st4lwolf') #link or text to which the qrcode will redirect.

#in back_color you can change the colour of the background, by changing the values with RGB data. To find out more, do an internet search on RGB colours.
qr_img = qr.make_image(image_factory=StyledPilImage, color_mask=ImageColorMask(back_color=(255,255,255), color_mask_image=logo)) 
#name under which the QR code will be saved.
qr_img.save('output.png')
print('Finished, QR code generated!\n Made with <3 by St4lW | https://github.com/malwprotector')
