import face_recognition

def recognize_face(unknown_image):
    known_faces = []
    user_images = UserImage.objects.all()
    for user_image in user_images:
        known_image = face_recognition.load_image_file(user_image.image.path)
        known_encoding = face_recognition.face_encodings(known_image)[0]
        known_faces.append(known_encoding)

    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(known_faces, unknown_encoding)
    if True in results:
        matched_index = results.index(True)
        return user_images[matched_index].name
    return None
