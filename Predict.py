from ultralytics import YOLO
from dotenv import load_dotenv
import os
import random
import numpy as np

load_dotenv()

model = YOLO(os.environ.get("official_model_path"))  # load an official model
model = YOLO(os.environ.get("custom_model_path"))  # load a custom model

def load_random_image(root_dir):
    ''' Choose a random image from a random class for prediction'''

    root_dir = os.environ.get("root_dir")
    test_dir = os.path.join(root_dir, sorted(os.listdir(root_dir))[0])

    dog_breeds = [os.path.join(test_dir, x) for x in os.listdir(test_dir)]

    selected_breed_dir = random.choice(dog_breeds)
    selected_breed = selected_breed_dir.split('\\')[-1]

    # print(f"Selected Breed: {selected_breed}")
    # print(f"Selected Breed Dir: {selected_breed_dir}")

    random_img = os.path.join(
        selected_breed_dir,
        os.listdir(selected_breed_dir)[random.randint(0, 50)]
    )

    # print(random_img)
    return random_img

def predict_image(model, image, selected_breed=None):
    '''Predict results on a given image using the given YOLOv8 model.
        selected_breed is a parameter used to verify the class name initially chosen 
        (applicable when manually choosing image for prediction)
        {not applicable when predicting on unknown images, eg: realtime}'''

    # Predict with the model
    results = model(image)  # predict on an image

    names_dict = results[0].names
    probs = results[0].probs.numpy().data

    # Get the indices that would sort the probabilities in descending order
    sorted_indices = np.argsort(probs)[::-1]

    # Get the top 3 indices
    top_3_indices = sorted_indices[:3]

    # Get the corresponding probabilities for the top 3 indices
    top_3_probabilities = probs[top_3_indices]

    if selected_breed:
        print(f"Actual Class: {selected_breed}")

    print(f"Predicted Classes: {names_dict[top_3_indices[0]]}, {names_dict[top_3_indices[1]]}, {names_dict[top_3_indices[2]]}")
    print(f"Predicted Probs:   {top_3_probabilities[0]}, {top_3_probabilities[1]}, {top_3_probabilities[2]}")

    # Set up a counter and for loop to handle upto 3 wrong guesses
    counter = 0
    for i in range(3):
        if names_dict[top_3_indices[i]] != selected_breed:
            if counter < 2:
                counter += 1
                print("Sorry, I seemed to have guessed that wrong.")
            else:
                print("I got all 3 guesses wrong.")
                break
        else:
            print(f"Predicted it right on try: {i+1}.")
            break