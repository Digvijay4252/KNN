
<!-- # Logistic-Regression
=======
# KNN
>>>>>>> 353930f1251d8f21ca4311180cb8bcc97094f00c

<img width="913" height="906" alt="image" src="https://github.com/user-attachments/assets/b22d4d5c-77be-480e-876f-8ba689834320" />
 -->

# KNN – k-Nearest Neighbors Classifier Web App

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

### Step 1
<img width="1881" height="890" alt="image" src="https://github.com/user-attachments/assets/22dd6c4e-2b5c-4fd0-a014-6139760f5a70" />

### Step 2
<img width="1864" height="845" alt="image" src="https://github.com/user-attachments/assets/12fac56d-0b51-418e-8276-6ac51ff6eac3" />

### Step 3
<img width="1903" height="913" alt="image" src="https://github.com/user-attachments/assets/77dd7d6b-2fdd-4458-8f42-5548ab4c2c14" />


## Future Improvements
Train on a larger dataset

Add prediction confidence scores

Show visualizations of KNN clusters (optional)

Support for uploading CSV data for bulk predictions

Add a REST API version
