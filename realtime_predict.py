import cv2

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

# Load label map
label_map = {}
with open("labels.txt", "r") as f:
    for line in f:
        label, name = line.strip().split(":")
        label_map[int(label)] = name

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                    "haarcascade_frontalface_default.xml")

# Start webcam
cam = cv2.VideoCapture(0)

print("Starting real-time recognition. Press 'q' to quit.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to access webcam.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        # Predict
        label_id, confidence = recognizer.predict(roi_gray)

        # Lower confidence = better match. Tune threshold:
        if confidence < 70:
            name = label_map.get(label_id, "Unknown")
        else:
            name = "Unknown"

        # Draw Box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show Name
        cv2.putText(frame, name, (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow("Real-Time Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
