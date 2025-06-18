import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4,)
qr.add_data("https://chatgpt.com/c/6852719c-a604-800a-b4db-97fd534d63ef")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("wscube_web.png")
