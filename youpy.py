from pytube import YouTube
from sys import argv, exit
from pathlib import Path
import os
import ffmpeg

if len(argv) <= 1:
    with open('help.txt') as f:
        content = f.read()
        print(content)
    exit(1)

if argv[1] != "--mp3" and argv[1] != "--mp4":
    raise Exception(f"Unknown output format: '{argv[1]}' \n Should be '--mp4' or '--mp3'")

if argv[2][:32] != "https://www.youtube.com/watch?v=":
    raise Exception("Wrong URL format")


yt = YouTube(argv[2])
mp3_mode: bool = argv[1] == "--mp3"

# get os $HOME 
if len(argv) < 4:
    output_dir = str(Path.home())
else:
    output_dir = argv[3]

if not os.path.exists(output_dir):
    raise Exception(f"Path isn't valid or doesn't exist: {output_dir}")


# ------------------------- #
# ---- Audio selection ---- #
# ------------------------- #


print("Searching for available audio streams...")

print("")

audio_choices = yt.streams.filter(only_audio=True)  # ABR selection
for i in range(len(audio_choices)):
    print(i + 1, '. ', audio_choices[i])

print("")
abr = int(input("Choose audio stream option: ")) - 1

print("")

audio = yt.streams.filter(only_audio=True)[abr]

print("Downloading audio file...")


# --------------------------------- #
# ---- Audio-file manipulation ---- #
# --------------------------------- #


# Downloads audio file to output_dir
audio.download(output_dir)

# Points to where the audio file in temporarily saved
audio_path = os.path.join(output_dir, audio.default_filename)

# Extract file's root and his extension
_, file_extension = os.path.splitext(audio_path)

# Modified audio_path :  $OUTPUT_DIR\foo.mp4-> $OUTPUT_DIR\audio.mp4
new_audioPath = os.path.join(output_dir, 'audio' + file_extension)

# Apply name modification to file.mp4
os.rename(audio_path, new_audioPath)

# Converts file to ffmpeg stream
audio_stream = ffmpeg.input(new_audioPath)


# Video section if 1st argument is "--mp4"

if not mp3_mode:

    print("Searching for available video streams...")

    print("")

    video_choices = yt.streams.filter(only_video=True)

    # ------------------------- #
    # ---- Video selection ---- #
    # ------------------------- #

    for i in range(len(video_choices)):
        print(i + 1, '. ', video_choices[i])

    print("")
    res = int(input("Choose video stream option: ")) - 1

    print("")

    video = yt.streams.filter(only_video=True)[res]

    print("Downloading video file...")

    # --------------------------------- #
    # ---- Video-file manipulation ---- #
    # --------------------------------- #

    # Downloads video file to output_dir
    video.download(output_dir)

    # Points to where the video file in temporarily saved
    video_path = os.path.join(output_dir, video.default_filename)

    # Extract file's root and his extension
    _, file_extension = os.path.splitext(video_path)

    # Modified audio_path :  $OUTPUT_DIR\foo.mp4-> $OUTPUT_DIR\video.mp4
    new_videoPath = os.path.join(output_dir, 'video' + file_extension)

    # Apply name modification to foo.mp4
    os.rename(video_path, new_videoPath)

    # Converts file to ffmpeg stream
    video_stream = ffmpeg.input(new_videoPath)

    # ----------------------------- #
    # ---- Audio-video merging ---- #
    # ----------------------------- #

    output_name = input("Choose a file name (Take default if empty) : ")
    output_name = (output_name, os.path.splitext(video.default_filename)[0])[output_name == ""]

    output_dir = os.path.join(output_dir, output_name + ".mp4")
    ffmpeg.output(audio_stream, video_stream, output_dir).run()

    # removes temp files
    os.remove(new_videoPath)
    os.remove(new_audioPath)

else:

    # -------------------------- #
    # ---- Audio conversion ---- #
    # -------------------------- #

    output_name = input("Choose a file name (Take default if empty) : ")
    output_name = (output_name, os.path.splitext(audio.default_filename)[0])[output_name == ""]

    output_dir = os.path.join(output_dir, output_name + ".mp3")
    ffmpeg.output(audio_stream, output_dir).run()

    # removes temp files
    os.remove(new_audioPath)
