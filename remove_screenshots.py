from pathlib import Path

IMG_EXT = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".heic",
    ".heif",
}

def get_desktop_path():
    home = Path.home()
    return Path(home / 'Desktop')

def delete_desktop_images():
    desktop_path = get_desktop_path()

    for file_name in desktop_path.iterdir():
        if file_name.exists() and file_name.suffix in IMG_EXT:
            file_name.absolute().unlink()
            print(f"[{file_name.absolute()}] deleted")

if __name__ == "__main__":
    delete_desktop_images()
    print(f"Desktop images deleted successfully")
