# test_face_recognition.py

try:
    import face_recognition
    print("face_recognition imported successfully")
except ImportError as e:
    print("Error importing face_recognition:", e)

try:
    import face_recognition_models
    print("face_recognition_models imported successfully")
except ImportError as e:
    print("Error importing face_recognition_models:", e)
