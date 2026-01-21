from pathlib import Path 
from PIL import Image
import pillow_heif

HEIC = ".heic"

def get_download_path():
    home_path = Path.home()
    return Path(f"{home_path.absolute()}/Downloads")

def convert_all_to_jpg():
    pillow_heif.register_heif_opener()

    downloads = get_download_path()

    for f in downloads.iterdir():
        if f.suffix == HEIC:
            src = f.absolute()
            dst = src.with_suffix(".jpg")

            with Image.open(src) as img:
                img.convert("RGB").save(dst, "JPEG")
            
            f.unlink()
            print(f"Successfully deleted and converted {f.name} to JPG.")

if __name__ == "__main__":
    convert_all_to_jpg()