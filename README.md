# YouPY
YouPY is a Python script that downloads Youtube videos. It can output mp4 and mp3 files.

This script has only been tested on Archlinux and Windows 11. However, it may work on other distros. Please feel free to give feedback or report bug.

The command's structure is as following:
```
python youpy.py {mode} {link} {output directory}
```
The script can take up to 3 arguments:
1. The output format ("--mp4" for mp4 file and "--mp3" for mp3 file)
2. The youtube video link
3. The output directory (optionnal for windows users)

By default, ouput directories are *Music* folder for mp3 files and *Videos* folder for mp4. On Linux or Mac, as those directories does not exist, you must specify the output directory.

## HTUI :
How to use it? Well it's quite simple. First, make sure that all dependencies are fullfilled. Then you can use your favorite command line interpreter to run the python script like this : 
```
python youpy.py --mp4 https://www.youtube.com/watch?v=dQw4w9WgXcQ
```
You can then choose the audio quality (higher abr means better quality). If you choosed to download video, you can choose the video quality (higher res means better quality).
The script will ask you to enter a file name (if empty, it will take the video file name). This will then download the YouTube video to your *Videos* folder.

## Dependencies :
Given version are the only one tested for now, the software way work or not with different version.

### Plugins and Softwares :

-Python v**3.10.5**
  [Python Official Release Page](https://www.python.org/downloads/release/python-3105/)
 
-FFmpeg Plugin v**5.0.1**
  [FFmpeg Download Page](https://ffmpeg.org/download.html)
  
  or using chocolatey (What i used for my windows as i don't understand the file architecture :sweat_smile:):
  ```
  choco install ffmpeg
  ```

### Python Modules :

Install instructions are provided for pip-install

-Pytube v**12.1.0**
  ```
  pip install pytube
  ```
  
-ffmpeg-python v**0.2.0** (wrapper)
  ```
  pip install ffmpeg-python
  ```
  
-future v**0.18.2** (retro-compat)
  ```
  pip install future
  ```
