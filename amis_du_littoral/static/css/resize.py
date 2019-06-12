from PIL import Image
import os
foo = Image.open("\Users\bgaut\Desktop\QQQO2\images\image-1533549844502")
foo = foo.resize((160,300),Image.ANTIALIAS)
foo.save("\Users\bgaut\Desktop\QQQO2\image_scaled.jpg",quality=95)
foo.save("\Users\bgaut\Desktop\QQQO2\image_scaled_opt.jpg",optimize=True,quality=95)
