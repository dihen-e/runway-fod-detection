"""
This script is used to select images from a dataset based on certain criteria. It allows users to filter images by various attributes such as size, format, and content.
The selected images can then be saved to a specified directory for further analysis or processing, this module filters raw pavement imagery before it is used in the FOD
preprocessing pipeline.

Issue faced : The source pavement dataset contains images of varying resolutions, with some much smaller than the target 256x256 CNN input size.
 Upscaling these low-resolution images would increase pixel dimensions but fail to enhance visual detail, potentially degrading the texture and
   edge information necessary for the model.

Solution : Implement a filtering script to exclude images using their original width and height and are retained only if they satisfy a 
minimum resolution threshold
1. Scans the asphalt, concrete, and concrete-plate source directories.
2. Measures the native dimensions of each supported image.
3. Reports the number of samples meeting the configured threshold.
4. Copies qualifying images into a cleaned dataset directory.
5. Preserves the original image files without resizing or recompression.

This would ensure that the dataset would contain images that are suitable for the 256 x 256 CNN model without compromising the visual quality of the images.
The script is designed to be efficient and user-friendly, allowing for easy integration into existing workflows.
"""

import os
import shutil
from PIL import Image

def filter_images(source_base_dir, output_base_dir, min_size=150):
    categories = ["asphalt", "concrete", "concrete plates"]

    for category in categories:
        source_folder = os.path.join(source_base_dir, category)
        output_folder = os.path.join(output_base_dir, category)

        os.makedirs(output_folder, exist_ok=True)

        kept = 0

        for filename in os.listdir(source_folder):

            image_path = os.path.join(source_folder, filename)

            # Check if the file is an image based on its extension
            if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
                continue

            try:
                with Image.open(image_path) as img:
                    width, height = img.size

                    # Check if the image meets the minimum size requirements and if so, copy it to the output folder
                    if width >= min_size and height >= min_size:
                        shutil.copy2(image_path, output_folder)
                        kept += 1

            except Exception:
                continue

        print(f"{category}: {kept} images kept")




