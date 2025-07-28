Face Recognition AI Model
This project is a Face Recognition AI model trained on five images of my face. It uses deep learning techniques to accurately recognize my face from new input images.

Features
Trains a face recognition model using five reference images.

Detects and recognizes my face in real-time or static images.

Built with popular libraries: Python, OpenCV, dlib, and the face_recognition library.

High accuracy for personal face recognition tasks.

Easy to extend or adapt to other faces with more training images.

Technologies Used
Python – Programming language

OpenCV – Computer vision library for image processing and face detection

dlib – Machine learning toolkit with facial landmark detection

face_recognition – Library for face recognition built on top of dlib

Installation
Clone the repository:


git clone https://github.com/m7hanan/face-recognition.git
cd face-recognition
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install the required packages:

pip install -r requirements.txt
Usage
Add your training images (at least five images of your face) to the training_images/ folder.

Run the face recognition script:


python face_recognition.py
The model will detect faces in the input images or camera feed and highlight recognized faces.

How It Works
The system encodes facial features from the training images.

It compares these encodings to faces detected in new images or video frames.

If a match is found with sufficient confidence, it identifies the face.

Folder Structure

face-recognition/
├── training_images/        # Your five face images for training
├── face_recognition.py     # Main face recognition script
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
Future Improvements
Add more training images to improve accuracy.

Implement real-time video stream face recognition.

Add GUI for easier use.

Support multiple persons recognition.

License
This project is licensed under the MIT License.

Contact
For questions or suggestions, feel free to contact me:

GitHub: m7hanan

Email: m7hanan@gmail.com

