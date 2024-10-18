import cv2
from util.video import read_video, save_video

import ultralytics


def main():
    yo = ultralytics.YOLO("models/best.pt")

    result = yo.predict("data/video.mp4", save=True)
    
if __name__ == "__main__":
    main()