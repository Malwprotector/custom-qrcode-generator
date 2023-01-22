import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask

#place the name of your image here.
Logo_link = 'logo.jpg'

logo = Image.open(Logo_link)

basewidth = 100

#image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

#link or text to which the qrcode will redirect.
url = 'https://cutt.ly/st4lwolf'

#indicates that the url should be added to the QR code.
QRcode.add_data(url)

# generating QR code.
QRcode.make()

#sets the colour of the QR code.
QRcolor = 'White'

#sets the background colour of the QR code.
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="black").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
    (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

#name under which the QR code will be saved.
QRimg.save('output.png')

print('Finished, QR code generated!\n Made with <3 by St4lW | https://github.com/malwprotector')
