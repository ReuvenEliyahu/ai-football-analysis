from ultralytics import YOLO

model = YOLO(r"C:\Users\97254\Desktop\Football Analysis\models\best.pt")


results = model.predict(r"C:\Users\97254\Desktop\Football Analysis\08fd33_4.mp4", save=True)
print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)