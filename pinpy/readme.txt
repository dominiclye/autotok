pinpy - a pinterest board/pin downloader.

.-------------------------.
|         .:::::.         |
|        :: ::::::        |
|        ````:::::        |
|  .:::::::::::::: iiii.  |
| :::::::::::::::: iiiiii |
| :::::: ..........iiiiii |
|  ':::: iiiiiiiiiiiiii'  |
|        iiiii....        |
|        iiiiii ii        |
|         'iiiii'         |
'-------------------------'

Table of Contents:
    [0x00000000] - About
    [0x00000001] - Usage

[0x00000000]:
    Downloading images from Pinterest is annoying.
    
    A slow and tedious way of downloading images is combing through the site's HTML to find the image url 
    which becomes even impossible when you want to download an entire board of "pins" (images).
    
    This program helps with that.

[0x00000001]:
    Install the needed libraries with pip, they're in the 'requirements.txt' file.
    pip -r requirements.txt

    Then once they're installed, run the script with:
    python3 src/pinpy.py.

    The images should start downloading in the directory that you ran the script from.
    In a future update, a GUI version will be released that will allow you to pick
        what folder the images should be downloaded to.