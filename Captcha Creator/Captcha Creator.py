from captcha.image import ImageCaptcha

# Specify the image size
image = ImageCaptcha(width = 360, height = 186)
# Specify the text for captcha
captcha_text = input("Enter Captcha: ")
# generate the image of the given text
data = image.generate(captcha_text)
# write the image on the given fiLe and save it
image.write(captcha_text, 'D:\Captcha.png')

from PIL import Image

Image.open('D:\Captcha.png')