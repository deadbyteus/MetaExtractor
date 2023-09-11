import os
import piexif
from PIL import Image

# Set the parent directory where images are located
PARENT_DIRECTORY = r"/path/to/images/dir"

def extract_metadata(image_path):
    try:
        if image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(image_path)
            metadata = image.info
            return metadata
        else:
            exif_dict = piexif.load(image_path)
            return exif_dict
    except Exception as e:
        print(f"Error extracting metadata from {image_path}: {e}")
        return {}

def save_metadata_to_txt(image_path, metadata):
    txt_path = os.path.splitext(image_path)[0] + ".txt"
    with open(txt_path, "w", encoding='utf-8', errors='ignore') as txt_file:
        for key, value in metadata.items():
            txt_file.write(f"{key}: {value}\n")
    print(f"PNG metadata saved to {txt_path}")

def extract_user_comment(image_path):
    try:
        if image_path.lower().endswith(('.jpg', '.jpeg')):
            exif_dict = piexif.load(image_path)
            user_comment = exif_dict['Exif'].get(piexif.ExifIFD.UserComment, None)
            return user_comment.decode('utf-8', errors='ignore') if user_comment else None
        else:
            return None
    except Exception as e:
        print(f"Error extracting metadata from {image_path}: {e}")
        return None

def save_user_comment_to_txt(image_path, user_comment):
    if user_comment:
        txt_path = os.path.splitext(image_path)[0] + ".txt"
        with open(txt_path, "w", encoding='utf-8', errors='ignore') as txt_file:
            txt_file.write(user_comment)
        print(f"JPG metadata saved to {txt_path}")

def main():
    for subdir, _, files in os.walk(PARENT_DIRECTORY):
        for file in files:
            image_path = os.path.join(subdir, file)
            if not file.startswith('.') and not file.startswith('._'):
                if image_path.lower().endswith(('.jpg', '.jpeg')):
                    user_comment = extract_user_comment(image_path)
                    if user_comment:
                        save_user_comment_to_txt(image_path, user_comment)
                else:
                    metadata = extract_metadata(image_path)
                    save_metadata_to_txt(image_path, metadata)

if __name__ == "__main__":
    main()
