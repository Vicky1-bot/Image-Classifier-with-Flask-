# Image Classifier Web App

Image classifier web app template to deploy a `tf.keras` model using Flask.

The model used in this example was then trained to distinguish between images of glass and tables. The dataset used is Glasses vs Tables .

## Setup

Clone the repository

`git clone https://github.com/Vicky1-bot/Image-Classifier-with-Flask-.git`

Change directory

`cd Image-Classifier`

Get trained model by uisng this link: 

 https://drive.google.com/file/d/1ap0kmsFlbIW34wqpQvcy4ukFkMTJLb73/view?usp=sharing
  
  Download trained model and place into folder called model in 'Image-classifier' project.
  
Create virtual environment

`python -m venv venv`

Activate virtual environment (Windows)

`venv\Scripts\activate`

Activate virtual environment (Mac / Linux)

`source venv/bin/activate`

Install the requirements

`python -m pip install -r requirements.txt`

Run the app

`python app.py`

Since the model was trained on images of glass or tables, you should ideally upload images of either glass or table and hopefully, the model will be able to predict accurately.

## Upload a file

![upload](assets/upload.png)

## Get a prediction

![predict](assets/predict.png)


<img width="935" alt="predict2" src="https://user-images.githubusercontent.com/76062756/144380846-a5d1b202-dec8-412b-ac32-e90292e2dedb.png">
