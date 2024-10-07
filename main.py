from moviepy.editor import ImageClip, concatenate_videoclips
import os
from os.path import isfile, join
from random import choice

class Video:
    def __init__(self):
        self.nclips = 5
        self.footage_path = ""
        self.clip_duration = 1
        self.clips = []
        self.target_resolution = (1080, 1920)  

    def select_randomclips(self):
        images = [choice([f for f in os.listdir(self.footage_path) if isfile(join(self.footage_path, f))]) for f in range(self.nclips)]
        clips = []
        
        for img in images:
            clip = ImageClip(join(self.footage_path, img)).set_duration(self.clip_duration)
            clip = clip.resize(height=self.target_resolution[1])  
            clip = clip.crop(width=self.target_resolution[0], height=self.target_resolution[1], 
                             x_center=clip.w / 2, y_center=clip.h / 2) 
            clips.append(clip)
        
        video = concatenate_videoclips(clips, method="compose")
        video.write_videofile("slideshow.mp4", fps=24)

if __name__ == "__main__":
    video = Video()
    video.nclips = 50
    video.footage_path = "/Users/dominiclye/Desktop/Projects/TiktokAutomation/study_motivation"
    video.clip_duration = 0.2
    video.select_randomclips()
