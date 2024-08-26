from PIL import Image
from matplotlib import cm
import numpy as np

class Noise:
    def __init__(self, image_shape = (600, 800), frequency = 50):
        self.random_array = np.random.random(image_shape)

    def get_sample(self, x, y):
        return self.image[y, x]
    
    def generate_image(self):
        colored_image = np.uint8(self.random_array * 255)
        return Image.fromarray(colored_image)

if __name__ == "__main__":
    noise_generator = Noise(frequency = 150)
    generated_image = noise_generator.generate_image()
    generated_image.show()