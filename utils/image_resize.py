from PIL import Image
import sys
import os

'''
how to use:

python3 image_resize.py <path to image dir>
e.g.:
python3 image_resize.py ~/workplace/beam-website/images/2020_2021staff/
'''

def resize_images(path):
    im_dir = os.listdir(path)
    for im_name in im_dir:
        full_path = path+im_name
        if full_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            print(full_path)
            im = Image.open(full_path)
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
            name, ext = os.path.splitext(full_path)
            resized = im.resize((300, 300), Image.ANTIALIAS)
            resized.save(name+ext, 'JPEG', quality=100)

def main(path):
    print("resizing images in path: " + path)
    resize_images(path)

if __name__ == "__main__":
    main(sys.argv[1])