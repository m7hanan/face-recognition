import face_recognition
import os
import pickle

DATASET_PATH = r"C:\Users\user\Desktop\faces"  # Folder Location

ENCODINGS_FILE = "encodings.pkl"

known_encodings = []
known_names = []

for person_name in os.listdir(DATASET_PATH):
    person_path = os.path.join(DATASET_PATH, person_name)
    if not os.path.isdir(person_path):
        continue
    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(person_name)

with open(ENCODINGS_FILE, 'wb') as f:
    pickle.dump({"encodings": known_encodings, "names": known_names}, f)

print("Encoding complete!")
