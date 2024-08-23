from PIL import Image, ImageFilter
import os

path = "Write the address of the location where the images are located"
pathOut = "Type the address of the file where the edited images will be placed"


if not os.path.exists(pathOut):
    os.makedirs(pathOut)

for filename in os.listdir(path):
    img_path = os.path.join(path, filename)
    
    if os.path.isfile(img_path):
        try:
            img = Image.open(img_path)

            edit = img.filter(ImageFilter.SHARPEN).convert("L")

            factor=1.5
            enhancer=ImageEnhance.Contrast(edit)
            edit=enhancer.enhance(factor)

            clean_name = os.path.splitext(filename)[0]
            save_path = os.path.join(pathOut, f"{clean_name}_edited.jpg")

            edit.save(save_path)
            print(f"{filename} processed and saved as {save_path}.")
        except Exception as e:
            print(f"{filename} An error occurred while processing: {e}")
    else:
        print(f"{img_path} is not a file or does not exist.")
