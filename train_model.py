import cv2
import os
import numpy as np

def train_model():
    dataset_path = "dataset"
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces = []
    labels = []
    label_map = {}  # map names to numeric labels
    current_label = 0

    # Loop through each user folder
    for user_name in os.listdir(dataset_path):
        user_folder = os.path.join(dataset_path, user_name)
        if not os.path.isdir(user_folder):
            continue
        
        label_map[current_label] = user_name

        for img_name in os.listdir(user_folder):
            img_path = os.path.join(user_folder, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            
            faces.append(img)
            labels.append(current_label)

        current_label += 1

    # Convert to numpy arrays
    faces = np.array(faces)
    labels = np.array(labels)

    # Train model
    recognizer.train(faces, labels)

    # Save model + label map
    recognizer.write("face_model.yml")
    
    # Save mapping
    with open("labels.txt", "w") as f:
        for label, name in label_map.items():
            f.write(f"{label}:{name}\n")

    print("Training complete! Model saved as face_model.yml")

if __name__ == "__main__":
    train_model()
