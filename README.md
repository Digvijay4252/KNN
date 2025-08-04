<!-- # Logistic-Regression

<img width="913" height="906" alt="image" src="https://github.com/user-attachments/assets/b22d4d5c-77be-480e-876f-8ba689834320" />
 -->

## KNN – k-Nearest Neighbors Classifier Web App

This project implements a K-Nearest Neighbors (KNN) classification model using Flask and scikit-learn. It predicts whether a student will Pass or Fail based on their academic engagement using an intuitive web interface.
---

---

##  How It Works

- User enters values for study hours, attendance, assignments, and sleep.

- The app uses the trained KNN model to predict if the student will Pass or Fail.

- Output is displayed instantly in the browser.

---

##  Project Structure
```
KNN/
├── app.py                     # Flask web app
├── train_model.py             # KNN model training script
├── model.pkl                  # Trained KNN model
├── pass_map.pkl               # Encoded label map for Pass/Fail
├── student_performance.csv    # Dataset for training
├── templates/
│   └── index.html             # HTML input form
└── static/
    └── style.css              # Optional CSS styling

```
---

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/KNN.git
cd KNN
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py

```
Open in browser

Visit: http://localhost:10000


## Screenshots
<img width="913" height="906" alt="image" src="https://github.com/user-attachments/assets/b22d4d5c-77be-480e-876f-8ba689834320"

## Future Improvements
Train on a larger dataset

Add prediction confidence scores

Show visualizations of KNN clusters (optional)

Support for uploading CSV data for bulk predictions

Add a REST API version