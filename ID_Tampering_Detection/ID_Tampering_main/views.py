from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTING_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# Route to home page
@app.route("/", methods=["GET", "POST"])
def index():

    # Execute if request is get
    if request.method == "GET":
        return render_template("index.html")

    # Execute if request is post
    if request.method == "POST":
        # Get uploaded image
        file_upload = request.files['file_upload']
        filename  = file_upload.filename

        # Resize and save the uploaded image
        uploaded_image = Image.open(file_upload).resize(250,160)
        uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

        # Resize and save the original image
        original_image = Image.open(os.path.join(app.config['EXISTING_FILE'], 'image.jpg')).resize(250,160)
        original_image.save(os.path.join(app.config['EXISTING_FILE'], 'image.jpg'))

        # Read uploaded and original image as array
        original_image = cv2.imread(os.path.join(app.config['EXISTING_FILE'], 'image.jpg'))
        uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS', 'image.jpg']))

        # Convert Image 
        original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)