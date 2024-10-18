import ultralytics
yo = ultralytics.YOLO("models/best.pt")

result = yo.predict("data/video.mp4", save=True)

print(result[0])

for box in result[0].boxes:
    print(box)
    print("===========")