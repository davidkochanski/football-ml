import cv2
from util.video import read_video, save_video
from tracking import Tracker

import ultralytics


def main():
    frames = read_video("data/video.mp4")

    tracker = Tracker("models/best.pt")
    
    tracker.get_object_tracks(frames)
    
    save_video("out/out.avi", frames)
    
if __name__ == "__main__":
    main()