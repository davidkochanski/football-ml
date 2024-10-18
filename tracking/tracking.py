# Tracks objects detected between frames

from ultralytics import YOLO
import supervision
import os

class Tracker:
    def __init__(self, model):
        self.model = YOLO(model=model)
        self.tracker = supervision.ByteTrack()
        
    def detect_frames(self, frames):
        detections = [] 
        for i in range(0,len(frames), 20):
            detections.append(self.model.predict(frames[i:i+20],conf=0.1))
        return detections

    def get_object_tracks(self, frames):

        detections = self.detect_frames(frames)

        tracks = {
            "players":[],
            "referees":[],
            "ball":[]
        }

        for frame_num, detection in enumerate(detections):
            cls_names = detection.names
            name_to_id = {v:k for k,v in cls_names.items()}

            detection_supervision = supervision.Detections.from_ultralytics(detection)