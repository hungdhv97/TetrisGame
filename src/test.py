from PIL import Image, ImageDraw

im = Image.new('RGB', (210, 30), (0, 0, 0))
draw = ImageDraw.Draw(im)

draw.rectangle((0, 0, 30, 30), fill=(246, 0, 0))
draw.rectangle((30, 0, 60, 30), fill=(255, 140, 0))
draw.rectangle((60, 0, 90, 30), fill=(255, 238, 0))
draw.rectangle((90, 0, 120, 30), fill=(77, 233, 76))
draw.rectangle((120, 0, 150, 30), fill=(55, 131, 255))
draw.rectangle((150, 0, 180, 30), fill=(72, 21, 170))
draw.rectangle((180, 0, 210, 30), fill=(255, 26, 206))

im.save('textures/tiles.png', quality=100)