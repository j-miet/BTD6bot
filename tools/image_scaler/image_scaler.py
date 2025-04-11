"""For scaling pictures to same resolution, in particular all map images, so they can be used in GUI."""

from pathlib import Path
import os

from PIL import Image

scaled_res = (320, 195) # set your output res here, current GUI image res is 320x195.

def list_format(img_list: list[str]) -> list[str]:
    """Formats a list of strings.
    
    Replaces newlines with whitespaces, then remove any leading and trailing whitespaces to get clean list for
    image resizing.

    Args:
        img_list: List of all map names.
        
    Returns:
        clean_list: List of all map names, now without newspace or extra space characters.
    """
    clean_list = []
    for map_img in img_list:                                        
        new = map_img.replace('\n', ' ').strip() 
        if not new:
            continue
        clean_list.append(new)
    return clean_list  

def scale_images() -> None:
    """Scale images to desired resolution.

    Reads all map names in 'raw map images', resizes them and saves them in 'map images'. So make sure there's no other 
    file types than images.
    Creates new folder for scaled images if it doesn't already exists.
    """
    if os.path.exists(Path(__file__).parent/'raw map images'):
        ...
    else:
        print("Didn't find folder 'raw map images', creating one...")
        os.mkdir(Path(__file__).parent/'raw map images')   # this is your new folder, located inside 'map images'.
    images = os.listdir(Path(__file__).parent/'raw map images')

    if os.path.exists(Path(__file__).parent/'map images'):
        ...
    else:
        print("Didn't find folder 'map images', creating one...")
        os.mkdir(Path(__file__).parent/'map images')
    
    print('Resizing images...')
    for im in images:
        try:
            temp = Image.open(Path(__file__).parent/'raw map images'/im)
            scaled = temp.resize(scaled_res)
            scaled.save(Path(__file__).parent/'map images'/im)
            temp.close()
        except FileNotFoundError:
            ... # skipping over 
    print('Done!')