# Sentiment Analysis on Social Media Using LSTM

## Overview
This project implements a deep learning-based sentiment analysis system using an LSTM (Long Short-Term Memory) network. The model classifies text data from social media platforms into Positive, Neutral, or Negative sentiments.

The project uses combined Reddit and Twitter datasets to improve linguistic diversity and model generalization.

## Google Colab Notebook
Colab Link:  
https://colab.research.google.com/your_notebook_link_here

## Datasets
- Reddit comments dataset  
- Twitter tweets dataset  

(Datasets are located in the `data/` folder)

## Model Details
- Model Type: LSTM (Recurrent Neural Network)  
- Framework: TensorFlow / Keras  
- Task: Multi-class sentiment classification  
- Validation Accuracy: ≥ 85%  

## Project Structure
- `notebook/` : Google Colab notebook for training and evaluation  
- `data/` : Reddit and Twitter datasets  
- `app/` : Flask deployment files  
- `requirements.txt` : Required Python libraries  

## Deployment
The trained model is deployed using Flask to provide real-time sentiment prediction.  
Due to GitHub file size limits, trained model files may be hosted externally and linked if required.

## How to Run the Application

```bash
pip install -r requirements.txt
cd app
python app.py

--Google Colab Notebook
https://colab.research.google.com/drive/1Zt-qU8d5Vp_Ihfl6JRGrOmPepM9L16Wu?authuser=0#scrollTo=Esm8SzfgnZdK
