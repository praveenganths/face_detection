import cv2
import os

def create_user_dataset():
    # Ask user name
    user_name = input("Enter your name: ").strip()
    
    # Create dataset directory if not exists
    dataset_dir = "dataset"
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    # Create directory for this user
    user_dir = os.path.join(dataset_dir, user_name)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    # Start webcam
    cam = cv2.VideoCapture(0)

    count = 0
    print("Capturing 100 images. Press 'q' to quit early.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to access webcam")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Save image
        img_path = os.path.join(user_dir, f"{user_name}_{count}.jpg")
        cv2.imwrite(img_path, gray)

        # Show frame
        cv2.imshow("Capturing Images (Press q to exit)", gray)

        count += 1

        # Stop when 100 pictures are taken
        if count >= 50:
            print("Captured 100 images successfully!")
            break

        # Allow early exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Stopped by user.")
            break

    cam.release()
    cv2.destroyAllWindows()

    print(f"Dataset stored in folder: {user_dir}")

if __name__ == "__main__":
    create_user_dataset()
