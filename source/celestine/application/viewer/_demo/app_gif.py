import PIL.Image
import PIL.ImageDraw
import random

images = []

images.append(PIL.Image.open("file/logo.jpg"))

images[0].save('anitest.gif',
               save_all=True,
               append_images=images[1:],
               duration=1,
               loop=1)


# images[0].save('anitest.gif',
#               save_all=True,
#               append_images=extra_images,
#               duration=10,
#               loop=1)


names = ['img{:02d}.gif'.format(i) for i in range(200)]


im = PIL.Image.new("RGB", (128, 128), 'green')


def random_image(image_to_transform, threshold):
    # convert any image to RGB
    output_image = image_to_transform.convert("RGB")
    # The threshold is the percentage of random pixels to generate

    for x in range(output_image.width):
        for y in range(output_image.height):
            output_image.putpixel((x, y), (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)))
    return output_image


random_image(images[0], 1)


pos = 0
for n in names:
    frame = random_image(images[0], 1)
    frame.save(n)
    pos += 10


# Open all the frames
images = []

for n in names:
    frame = PIL.Image.open(n)
    images.append(frame)

# Save the frames as an animated GIF
images[0].save('anicircle.gif',
               save_all=True,
               append_images=images[1:],
               duration=100,
               loop=0)
