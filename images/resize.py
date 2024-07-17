from PIL import Image

image_path = "/Users/finch/Desktop/Homepage/oufuzhao.github.io/images/My_profile5.jpg"
image = Image.open(image_path)

resized_image = image.resize((180, 180))

output_path = "/Users/finch/Desktop/Homepage/oufuzhao.github.io/images/apple-touch-icon.png"
resized_image.save(output_path, "PNG")