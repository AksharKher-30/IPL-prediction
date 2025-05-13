#  IPL Match Prediction 

This project is a Machine Learning model designed to predict the outcome of Indian Premier League (IPL) cricket matches based on historical data. It uses team statistics and match conditions to forecast which team is more likely to win a given match.


---

## 🔍 Project Overview

- **Goal**: Predict the winning team of an IPL match based on input parameters.
- **Tech Stack**: Python, Pandas, NumPy, Scikit-learn, Jupyter Notebook.
- **Model**: Logistic Regression / Random Forest / (specify if any other).
- **Input Features**:
  - Batting team
  - Bowling team
  - Venue
  - Toss winner
  - Toss decision
  - Match winner
  - Target score
  - Current score
  - Overs completed
  - Wickets fallen

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python (Pandas, Scikit-learn)  
- **ML Approach**: Content-based filtering using cosine similarity  
- **Data**: Preprocessed `.pkl` files for quick startup  

---

## 📊 Example Prediction

```python
Input:
- Batting Team: CSK
- Bowling Team: MI
- Current Score: 120/3
- Overs: 12
- Target: 180

Output:
- Predicted Winner: CSK
- Win Probability: 74%
```
---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/IPL-prediction.git
cd IPL-prediction
```
### 2. Create & Activate Virtual Environment (optional)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```


###🚦 Running the App
```bash
streamlit run app.py
```
Open the browser at the URL displayed (usually http://localhost:8501) to interact with the app.


