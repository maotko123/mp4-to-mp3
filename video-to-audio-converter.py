import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog, messagebox

def select_video_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    return file_path

def convert_to_audio(video_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        
        output_path = os.path.splitext(video_path)[0] + ".mp3"
        audio.write_audiofile(output_path)
        
        video.close()
        audio.close()
        
        return output_path
    except Exception as e:
        return str(e)

def main():
    video_path = select_video_file()
    if not video_path:
        print("No file selected. Exiting.")
        return

    print("Converting video to audio...")
    result = convert_to_audio(video_path)

    if result.endswith(".mp3"):
        messagebox.showinfo("Success", f"Audio saved as: {result}")
    else:
        messagebox.showerror("Error", f"Conversion failed: {result}")

if __name__ == "__main__":
    main()
