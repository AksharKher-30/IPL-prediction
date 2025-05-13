import streamlit as st
import pickle
import pandas as pd

# App styling
st.set_page_config(page_title="IPL Win Predictor", layout="centered")
st.markdown("<h1 style='text-align: center; color: #3f51b5;'>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# Load model
pipe = pickle.load(open('pipe.pkl','rb'))

# Dropdown options
teams = ['Royal Challengers Bangalore', 'Punjab Kings', 'Mumbai Indians', 'Kolkata Knight Riders',
         'Sunrisers Hyderabad', 'Rajasthan Royals', 'Chennai Super Kings', 'Delhi Capitals',
         'Lucknow Super Giants', 'Gujarat Titans']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
          'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
          'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 0,
          'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
          'Lucknow', 'Guwahati', 'Mohali']
cities = [str(city) for city in cities]

# Team and City Selection
st.markdown("### 🏏 Match Configuration")
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the **Batting Team**', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the **Bowling Team**', sorted(teams))

selected_city = st.selectbox('Select the **Host City**', sorted(cities))
target = st.number_input('🎯 Enter the Target Score', min_value=1)

# Current Match Situation
st.markdown("### 📋 Match Progress")
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Current Score', min_value=0)
with col4:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
with col5:
    wickets_out = st.number_input('Wickets Lost', min_value=0, max_value=10)

# Predict button
if st.button('Predict Win Probability'):
    if overs == 0:
        st.error("⚠️ Overs completed cannot be 0.")
    elif batting_team == bowling_team:
        st.error("⚠️ Batting and Bowling teams must be different.")
    else:
        runs_left = target - score
        balls_left = 120 - int(overs * 6)
        wickets = 10 - wickets_out
        crr = score / overs
        rrr = (runs_left * 6) / balls_left if balls_left != 0 else 0

        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [selected_city],
            'runs_left': [runs_left],
            'balls_left': [balls_left],
            'wickets': [wickets],
            'total_runs_x': [target],
            'crr': [crr],
            'rrr': [rrr]
        })

        # Prediction
        result = pipe.predict_proba(input_df)
        loss_prob = result[0][0]
        win_prob = result[0][1]

        # Results
        st.markdown("---")
        st.markdown("## 🧮 Win Probability")
        col6, col7 = st.columns(2)
        col6.metric(label=f"🏆 {batting_team}", value=f"{round(win_prob * 100)}%", delta_color="normal")
        col7.metric(label=f"🎯 {bowling_team}", value=f"{round(loss_prob * 100)}%", delta_color="inverse")

        st.progress(win_prob, text=f"{batting_team} Winning Probability")