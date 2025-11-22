# Fake Signature Detection Using CNN

This repository contains a full-stack Fake Signature Detection project using **Python**, **TensorFlow (Keras)**, **OpenCV**, **NumPy**, and **Flask** for the backend API. A simple frontend allows uploading a signature image and seeing prediction results from the model.

**Note:** This repo includes training script `train.py` that you should run locally to create the model file `model/model.h5` before using the prediction API. A fallback heuristic is provided when model is not trained.

---

## Structure

```
/app.py                # Flask backend API
/train.py              # Script to train a small CNN (requires dataset)
/model/predict.py      # Helper to load model and run prediction
/model/model.h5        # (created after running train.py)
/templates/index.html  # Frontend HTML (upload UI)
/static/js/main.js     # Frontend JS to call backend
/static/css/style.css  # Styles
/requirements.txt
/README.md
```

## Quick start (local)

1. Create virtual environment & install:
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. (Optional) Prepare dataset and train the model:
- Place your dataset in `dataset/` with subfolders `genuine/` and `forged/`.
- Run:
```bash
python train.py
# This will save model to model/model.h5
```

3. Run the backend:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
# By default backend runs on http://127.0.0.1:5000
```

4. Open the frontend: `http://127.0.0.1:5000/` and upload a signature image.

## Deploying

- Push the repo to GitHub.
- Deploy frontend to Vercel by connecting the GitHub repo (use `/` root).
- Deploy backend (Flask) to a Python-friendly host (Render, Railway, Heroku) and set environment variables as needed.
- Update frontend to point to your deployed backend `/predict` endpoint.

---

If you need, I can push this repo to your GitHub (you will need to provide access or do the push locally). I can also provide step-by-step deployment instructions for Render + Vercel.
