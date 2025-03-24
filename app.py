import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import time
from food_recommendations import get_food_recommendations
from theme_handler import apply_theme
import warnings

warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Personal Fitness Tracker", 
    layout="wide",
    page_icon="🏋️"
)

theme = st.sidebar.radio("Select Theme:", ["Light Mode", "Dark Mode"])
apply_theme(theme)

# Main Header
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/2936/2936886.png", width=100)  # Default fitness icon
    with col2:
        st.title("Personal Fitness Tracker")
        st.caption("Predict your calories burned and get personalized nutrition recommendations")

st.sidebar.header("User Input Parameters")

@st.cache_resource
def load_model():
    calories = pd.read_csv("calories.csv")
    exercise = pd.read_csv("exercise.csv")
    exercise_df = exercise.merge(calories, on="User_ID").drop(columns="User_ID")
    exercise_df["BMI"] = round(exercise_df["Weight"] / ((exercise_df["Height"] / 100) ** 2), 2)
    exercise_df["Gender"] = exercise_df["Gender"].map({"Male": 1, "Female": 0})
    exercise_df = pd.get_dummies(exercise_df, columns=["Activity_Level"], drop_first=True)
    
    X_train = exercise_df.drop("Calories", axis=1)
    y_train = exercise_df["Calories"]
    model = RandomForestRegressor(n_estimators=1000, max_features=3, max_depth=6)
    model.fit(X_train, y_train)
    return model

def validate_inputs(age, height, weight, duration):
    if height < 100 or height > 250:
        st.error("Please enter a valid height between 100cm and 250cm")
        return False
    if weight < 30 or weight > 200:
        st.error("Please enter a valid weight between 30kg and 200kg")
        return False
    return True

def user_input_features():
    with st.sidebar:
        age = st.number_input("Age:", min_value=10, max_value=100, value=30, step=1)
        height = st.number_input("Height (cm):", min_value=100, max_value=250, value=170, step=1)
        weight = st.number_input("Weight (kg):", min_value=30, max_value=200, value=70, step=1)
        duration = st.number_input("Exercise Duration (min):", min_value=0, max_value=120, value=30, step=1)
        activity_level = st.radio("Activity Level:", ["No activity", "Light walking", "Regular exercise"], index=1)
        body_temp = st.number_input("Body Temperature (°C):", min_value=35.0, max_value=42.0, value=37.0, step=0.1)
        gender_button = st.radio("Gender:", ("Male", "Female"))
        
        gender = 1 if gender_button == "Male" else 0
        bmi = round(weight / ((height / 100) ** 2), 2)
        bmi_category = "Underweight" if bmi < 18.5 else "Normal weight" if bmi < 24.9 else "Overweight" if bmi < 29.9 else "Obese"
        bmi_color = "green" if bmi_category == "Normal weight" else "yellow" if bmi_category in ["Underweight", "Overweight"] else "red"
        
        tracker = st.checkbox("Using a fitness tracker?")
        heart_rate = st.number_input("Heart Rate (bpm):", min_value=40, max_value=200, value=80, step=1) if tracker else 0
        steps = st.number_input("Steps Taken Today:", min_value=0, max_value=50000, value=0, step=100) if tracker else 0
        kms_walked = st.number_input("Kilometers Walked:", min_value=0.0, max_value=50.0, value=0.0, step=0.1) if tracker else 0
        pulse_rate = st.number_input("Pulse Rate Throughout the Day:", min_value=40, max_value=200, value=80, step=1) if tracker else 0
        hours_slept = st.number_input("Hours Slept:", min_value=0.0, max_value=24.0, value=7.0, step=0.1) if tracker else 0
        blood_oxygen = st.number_input("Blood Oxygen Level (%):", min_value=70, max_value=100, value=98, step=1) if tracker else 0
        water_intake = st.number_input("Water Intake (liters):", min_value=0.0, max_value=10.0, value=2.0, step=0.1)
        
        food_suggestions = st.checkbox("Do you want food suggestions?")
        if food_suggestions:
            diet_preference = st.selectbox("Select your dietary preference:", 
                                         ["Vegetarian", "Vegan", "Non-Vegetarian", "Eggitarian", 
                                          "Gluten-Free", "Keto", "Paleo", "Mediterranean", "Other"])
        else:
            diet_preference = None
        
        if st.checkbox("Track Progress Over Time"):
            st.write("### Progress Tracker")
            progress_date = st.date_input("Select date")
            progress_weight = st.number_input("Today's Weight (kg)", 
                                           min_value=30.0, max_value=200.0, 
                                           value=float(weight), step=0.1)
            
            if st.button("Save Progress"):
                st.success("Progress saved!")
        
        st.markdown("---")
        with st.expander("ℹ️ Help"):
            st.write("""
            - **BMI Categories:**
              - Underweight: <18.5
              - Normal: 18.5-24.9
              - Overweight: 25-29.9
              - Obese: ≥30
            - For accurate results, fill all available fields
            - Wearable tracker data improves accuracy
            """)
        
        submit = st.button("Submit", type="primary")
        
        data_model = {
            "Age": age,
            "Height": height,
            "Weight": weight,
            "BMI": bmi,
            "Duration": duration,
            "Activity_Level": activity_level,
            "Body_Temp": body_temp,
            "Gender": gender,
            "Heart_Rate": heart_rate,
            "Steps_Taken": steps,
            "Kms_Walked": kms_walked,
            "Pulse_Rate": pulse_rate,
            "Hours_Slept": hours_slept,
            "Blood_Oxygen": blood_oxygen,
            "Water_Intake": water_intake
        }
        return pd.DataFrame(data_model, index=[0]), bmi_category, bmi_color, food_suggestions, diet_preference, submit

df, bmi_category, bmi_color, food_suggestions, diet_preference, submit = user_input_features()

if submit:
    if not validate_inputs(df["Age"].values[0], df["Height"].values[0], 
                         df["Weight"].values[0], df["Duration"].values[0]):
        st.stop()
    
    st.write("---")
    
    with st.container():
        st.header("📊 Your Fitness Analysis")
        
        with st.expander("BMI Analysis", expanded=True):
            bmi_col1, bmi_col2 = st.columns(2)
            with bmi_col1:
                st.metric(label="Your BMI", value=f"{df['BMI'].values[0]:.1f}")
            with bmi_col2:
                st.metric(label="Category", value=bmi_category)
            
            if bmi_category == "Normal weight":
                st.success("🎉 Your BMI is in the healthy range! Maintain your current habits.")
            elif bmi_category in ["Underweight", "Overweight"]:
                st.warning("⚠️ Your BMI suggests room for improvement. Consider consulting a nutritionist.")
            else:
                st.error("❗ Your BMI indicates significant health risk. Please consult a healthcare professional.")
        
        with st.expander("Calorie Prediction", expanded=True):
            st.write("### Predicted Calories Burned:")
            with st.spinner('Calculating...'):
                random_reg = load_model()
                df_model = df.reindex(columns=random_reg.feature_names_in_, fill_value=0)
                calories = random_reg.predict(df_model)
                st.metric(label="Estimated Calories Burned", 
                         value=f"{round(calories[0], 2)} kcal",
                         delta=f"~{round(calories[0]/30, 2)} kcal/min")
            
            st.progress(min(int(df['Duration'].values[0]/120*100), 100))
            st.caption(f"Based on {df['Duration'].values[0]} minutes of activity")
        
     
        if food_suggestions:
            with st.expander("🍽️ Food Recommendations", expanded=True):
                recommendations = get_food_recommendations(bmi_category, df["Activity_Level"].values[0], diet_preference)
                
                tab1, tab2, tab3, tab4 = st.tabs(["BMI Analysis", "Activity", "Diet", "Meal Plan"])
                
                with tab1:  
                    st.write("**Focus Area:**")
                    st.info(recommendations["BMI Analysis"]["Focus Area"])
                    st.write("**Recommended Foods:**")
                    st.info(", ".join(recommendations["BMI Analysis"]["Recommended Foods"]))
                    st.write("**Nutrition Tips:**")
                    st.info(recommendations["BMI Analysis"]["Nutrition Tips"])
                
                with tab2:  
                    st.write("**Pre-Workout:**")
                    st.info(recommendations["Activity Recommendations"]["Pre-Workout"])
                    st.write("**Post-Workout:**")
                    st.info(recommendations["Activity Recommendations"]["Post-Workout"])
                    st.write("**General Advice:**")
                    st.info(recommendations["Activity Recommendations"]["General Advice"])
                    st.write("**Hydration Guide:**")
                    st.info(recommendations["Activity Recommendations"]["Hydration Guide"])
                
                with tab3:  
                    if "proteins" in recommendations["Diet-Specific Guidance"]:
                        st.write("**Protein Sources:**")
                        st.info(", ".join(recommendations["Diet-Specific Guidance"]["proteins"]))
                    if "meals" in recommendations["Diet-Specific Guidance"]:
                        st.write("**Meal Ideas:**")
                        st.info("\n".join([f"- {meal}" for meal in recommendations["Diet-Specific Guidance"]["meals"]]))
                    if "advice" in recommendations["Diet-Specific Guidance"]:
                        st.info(recommendations["Diet-Specific Guidance"]["advice"])
                
                with tab4:  
                    st.write("**Breakfast:**")
                    st.info(recommendations["Meal Timing Suggestions"]["Breakfast"])
                    st.write("**Lunch:**")
                    st.info(recommendations["Meal Timing Suggestions"]["Lunch"])
                    st.write("**Dinner:**")
                    st.info(recommendations["Meal Timing Suggestions"]["Dinner"])
                    st.write("**Snacks:**")
                    st.info(recommendations["Meal Timing Suggestions"]["Snacks"])
                    
                    st.write("**Sample Indian Meals:**")
                    st.info("\n".join([f"- {meal}" for meal in recommendations["Sample Meal Plans"]["Indian"]]))
                    
                    st.write("**Additional Tips:**")
                    st.info("\n".join([f"- {tip}" for tip in recommendations["Additional Tips"]]))

# Footer
st.markdown("---")
footer = """
<style>
.footer {
    text-align: center;
    padding: 10px;
    margin-top: 2rem;
}
</style>
<div class="footer">
<p>Developed by Christina | <a href="#" style="color: var(--accent-color);">Privacy Policy</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)