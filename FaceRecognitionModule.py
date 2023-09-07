import cv2
import numpy as np
import face_recognition
import os

class FaceRecognitionModule:
    def __init__(self, images_path='Images'):
        self.images_path = images_path
        self.class_images = {}
        self.encodeListKnown = []

    def load_images(self):
        images = os.listdir(self.images_path)
        for class_name in images:
            img_path = os.path.join(self.images_path, class_name)
            current_image = cv2.imread(img_path)
            if current_image is not None:
                class_name_without_extension = os.path.splitext(class_name)[0]
                self.class_images[class_name_without_extension] = current_image
            else:
                print(f"Skipping invalid image: {img_path}")

    def find_encoding(self):
        for class_name, img in self.class_images.items():
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(img)

            if face_encodings:
                encode = face_encodings[0]
                self.encodeListKnown.append({'class_name': os.path.splitext(class_name)[0], 'encoding': encode})
            else:
                print(f"No face detected in the image '{class_name}'.")

    def run_face_recognition(self, image):
        image_small = cv2.resize(image, (0, 0), None, 0.25, 0.25)
        image_small = cv2.cvtColor(image_small, cv2.COLOR_BGR2RGB)
        face_location = face_recognition.face_locations(image_small)
        face_encoding = face_recognition.face_encodings(image_small, face_location)

        for face_locate, encode_face in zip(face_location, face_encoding):
            celebrity_encoding = encode_face
            closest_celebrity = None
            closest_distance = float('inf')  
            for known_encoding in self.encodeListKnown:
                distance = face_recognition.face_distance([known_encoding['encoding']], celebrity_encoding)[0]
                if distance < closest_distance:
                    closest_distance = distance
                    closest_celebrity = known_encoding

                    if closest_celebrity:
                        closest_celeb_img = self.class_images[closest_celebrity["class_name"]]
                        closest_celeb_img_rgb = cv2.cvtColor(closest_celeb_img, cv2.COLOR_BGR2RGB)
                        similarity_percentage = (1 - closest_distance) * 100
                        

                        text_size, _ = cv2.getTextSize(f'{closest_celebrity["class_name"]} {similarity_percentage:.0f}%', cv2.FONT_HERSHEY_PLAIN, 1, 2)
                        text_width, text_height = text_size

                        x1 = 0
                        y1 = text_height + 10
                        rectangle_height = text_height + 10
                        cv2.rectangle(closest_celeb_img_rgb, (x1, y1 - rectangle_height), (x1 + text_width + 5, y1), (0, 255, 0), -1)
                        cv2.putText(closest_celeb_img_rgb, f'{closest_celebrity["class_name"]} {similarity_percentage:.0f}%', (x1, y1 - 5), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

        return closest_celeb_img_rgb
            

if __name__ == "__main__":
    recognizer = FaceRecognitionModule()
    recognizer.load_images()
    recognizer.find_encoding()

    #input_image = cv2.imread('e.jpg')
    result_image = recognizer.run_face_recognition()
    
    #cv2.imshow('image', result_image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
