from PIL import Image
from numba import cuda
import numpy as np
import math


@cuda.jit
def method(image1, image2, transparency, output_image):
    x, y, z = cuda.grid(3)
    output_image[y][x][z] = image1[y][x][z] * transparency + (image2[y][x][z]*(1-transparency))


def main(image1, image2):
    """Images must have same width and height."""
    data_image1 = np.array(image1, dtype='int64')
    data_image2 = np.array(image2, dtype='int64')
    print(data_image1.shape, data_image2.shape)

    threadsperblock = (16, 16, 4)
    blockspergrid_x = int(math.ceil(data_image1.shape[0] // threadsperblock[0]))
    blockspergrid_y = int(math.ceil(data_image1.shape[1] // threadsperblock[1]))
    blockspergrid_z = int(math.ceil(data_image1.shape[2] // threadsperblock[2]))
    blockspergrid = (blockspergrid_x, blockspergrid_y, blockspergrid_z)

    input1 = cuda.to_device(data_image1)
    input2 = cuda.to_device(data_image2)
    output_image = cuda.device_array(data_image1.shape)

    method[blockspergrid, threadsperblock](input1, input2, 0.4,output_image)
    print('done')

    output = output_image.copy_to_host()
    output = output.astype('uint8')
    output = Image.fromarray(output)
    output.save("output_image.png")


if __name__ == "__main__":
    image1 = Image.open('rgb.png')
    image2 = Image.open('sova.png')
    main(image1, image2)
