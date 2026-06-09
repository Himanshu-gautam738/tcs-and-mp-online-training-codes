import numpy as np

# Base class / Interface
class ImageFilter:
    def process(self, image):
        """Process the image and return the result"""
        raise NotImplementedError("Subclasses must override process()")


# Derived Filter: Blur
class BlurFilter(ImageFilter):
    def process(self, image):
        print("Applying Blur Filter")
        # Simple blur simulation: average with neighbors
        kernel = np.ones((3, 3)) / 9
        blurred = np.copy(image)
        # naive convolution for demonstration
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                blurred[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * kernel)
        return blurred


# Derived Filter: Sharpen
class SharpenFilter(ImageFilter):
    def process(self, image):
        print("Applying Sharpen Filter")
        # Simple sharpening: image * 2 - blur approximation
        blur = np.copy(image)
        kernel = np.ones((3, 3)) / 9
        for i in range(1, image.shape[0] - 1):
            for j in range(1, image.shape[1] - 1):
                blur[i, j] = np.sum(image[i-1:i+2, j-1:j+2] * kernel)
        sharpened = np.clip(image * 2 - blur, 0, 255)
        return sharpened


# Derived Filter: Grayscale
class GrayscaleFilter(ImageFilter):
    def process(self, image):
        print("Applying Grayscale Filter")
        if len(image.shape) == 3 and image.shape[2] == 3:  # RGB image
            gray = np.mean(image, axis=2)
            return gray
        return image


# Image Processor (core logic)
class ImageProcessor:
    def __init__(self):
        self.filters = []

    def add_filter(self, image_filter):
        """Add a new filter (plugin-style)"""
        self.filters.append(image_filter)

    def apply_filters(self, image):
        """Apply all filters dynamically using polymorphism"""
        result = image
        for f in self.filters:
            result = f.process(result)
        return result


# Example usage
if __name__ == "__main__":
    # Simulate a 5x5 grayscale image
    image = np.random.randint(0, 256, (5, 5), dtype=np.uint8)
    print("Original Image:\n", image)

    processor = ImageProcessor()
    processor.add_filter(BlurFilter())
    processor.add_filter(SharpenFilter())
    processor.add_filter(GrayscaleFilter())  # Redundant for grayscale but shows extensibility

    result_image = processor.apply_filters(image)
    print("Processed Image:\n", result_image)
