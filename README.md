# Fake Signature Detection Using CNN
This project detects genuine vs forged signatures using a Convolutional Neural Network (CNN).
It includes a model training script, Flask API for prediction, and a simple frontend for uploading signature images.

# Features
- Detects forged and genuine signatures using CNN
- Flask API for real-time prediction
- Simple UI to upload signature images
- Supports custom datasets
- High accuracy with evaluation metrics (accuracy, precision, recall)

# Tech Stack / Tools Used
- Programming Language: Python
- Frameworks: TensorFlow (Keras), Flask
- Libraries: OpenCV, NumPy, Matplotlib
- Frontend: HTML, CSS, JavaScript
- Environment: Virtualenv

# Project Structure
  app.py                # Flask backend
  train.py              # Model training
  model/predict.py      # Prediction helper
  model/model.h5        # Saved CNN model
  templates/index.html  # Frontend upload page
  static/js/main.js     # Frontend logic
  static/css/style.css  # UI styles
  requirements.txt

# Future Enhancements
  Add advanced CNN models (ResNet, MobileNet)
  Improve signature preprocessing
  Deploy on cloud (Vercel/Render)
