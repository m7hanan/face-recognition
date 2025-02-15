import face_recognition
import cv2
import pickle

ENCODINGS_FILE = "C:/Users/user/Desktop/faces/encodings.pkl"  # Path updated

with open(ENCODINGS_FILE, 'rb') as f:
    data = pickle.load(f)

# Initialize the video capture
video_capture = cv2.VideoCapture(0)

# Set the video output path
output_file = 'output_video.avi'  # You can change this to your preferred file name and extension
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec
fps = 20.0  # Frame rate
frame_width = int(video_capture.get(3))  # Width of the frame
frame_height = int(video_capture.get(4))  # Height of the frame

# Create a VideoWriter object to save the video
out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(data["encodings"], face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = data["names"][match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Save the frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow("Face Recognition", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
out.release()  # Release the video writer
cv2.destroyAllWindows()
