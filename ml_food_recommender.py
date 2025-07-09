import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import random

class MLFoodRecommender:
    def __init__(self):
        # Sample food database with nutritional information
        self.food_data = self._create_sample_food_data()
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self._prepare_model()
    
    def _create_sample_food_data(self):
        """Create a sample food database with nutritional information"""
        data = {
            'food': [
                'Oatmeal with berries', 'Grilled chicken with vegetables', 'Salmon with quinoa',
                'Greek yogurt with honey', 'Egg white omelet with spinach', 'Brown rice with tofu',
                'Avocado toast', 'Grilled fish with sweet potato', 'Fruit smoothie',
                'Grilled vegetables with hummus', 'Chicken salad', 'Quinoa bowl with vegetables',
                'Cottage cheese with fruits', 'Whole wheat pasta with tomato sauce', 'Grilled shrimp salad'
            ],
            'calories': [300, 400, 450, 200, 280, 350, 250, 380, 320, 280, 350, 400, 220, 420, 300],
            'protein': [12, 35, 30, 20, 25, 15, 8, 25, 10, 8, 30, 12, 25, 15, 28],
            'carbs': [50, 20, 40, 20, 10, 60, 25, 40, 50, 30, 15, 70, 10, 75, 15],
            'fat': [5, 15, 20, 5, 15, 10, 15, 15, 5, 12, 20, 8, 5, 10, 18],
            'fiber': [8, 6, 5, 2, 4, 7, 6, 5, 4, 8, 5, 9, 2, 6, 4],
            'meal_type': ['breakfast', 'lunch', 'dinner', 'snack', 'breakfast', 
                         'lunch', 'breakfast', 'dinner', 'snack', 'snack',
                         'lunch', 'dinner', 'snack', 'lunch', 'dinner'],
            'diet_type': ['vegetarian', 'non-vegetarian', 'pescatarian', 'vegetarian', 'vegetarian',
                         'vegetarian', 'vegetarian', 'pescatarian', 'vegetarian', 'vegan',
                         'non-vegetarian', 'vegan', 'vegetarian', 'vegetarian', 'pescatarian']
        }
        return pd.DataFrame(data)
    
    def _prepare_model(self):
        """Prepare the recommendation model"""
        # Create a combined text feature for content-based filtering
        self.food_data['features'] = self.food_data['food'] + ' ' + self.food_data['meal_type'] + ' ' + self.food_data['diet_type']
        self.tfidf_matrix = self.vectorizer.fit_transform(self.food_data['features'])
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
    
    def get_recommendations(self, bmi_category: str, activity_level: str, diet_preference: str, n_recommendations: int = 5):
        """
        Get food recommendations based on user profile
        
        Args:
            bmi_category: User's BMI category
            activity_level: User's activity level
            diet_preference: User's dietary preference
            n_recommendations: Number of recommendations to return
            
        Returns:
            List of recommended food items with details
        """
        try:
            # Filter by diet preference
            filtered_foods = self.food_data.copy()
            if diet_preference.lower() != 'no preference':
                filtered_foods = filtered_foods[
                    filtered_foods['diet_type'].str.lower() == diet_preference.lower()
                ]
            
            if len(filtered_foods) == 0:
                filtered_foods = self.food_data  # Fallback to all foods if no matches
            
            # Get random sample for variety
            if len(filtered_foods) > n_recommendations:
                filtered_foods = filtered_foods.sample(n=n_recommendations, random_state=42)
            
            # Sort by nutritional value based on BMI and activity
            if bmi_category.lower() in ['underweight']:
                filtered_foods = filtered_foods.sort_values('calories', ascending=False)
            elif bmi_category.lower() in ['overweight', 'obese']:
                filtered_foods = filtered_foods.sort_values('calories')
            
            if 'active' in activity_level.lower():
                filtered_foods = filtered_foods.sort_values('protein', ascending=False)
            
            # Format recommendations
            recommendations = []
            for _, row in filtered_foods.head(n_recommendations).iterrows():
                recommendations.append({
                    'food': row['food'],
                    'meal_type': row['meal_type'],
                    'nutrition': {
                        'calories': row['calories'],
                        'protein': f"{row['protein']}g",
                        'carbs': f"{row['carbs']}g",
                        'fat': f"{row['fat']}g",
                        'fiber': f"{row['fiber']}g"
                    }
                })
            
            return {
                'recommendations': recommendations,
                'summary': {
                    'bmi_category': bmi_category,
                    'activity_level': activity_level,
                    'diet_preference': diet_preference
                }
            }
            
        except Exception as e:
            print(f"Error in get_recommendations: {str(e)}")
            # Return some default recommendations in case of error
            return self._get_default_recommendations()
    
    def _get_default_recommendations(self):
        """Provide default recommendations in case of errors"""
        default_foods = self.food_data.sample(n=3, random_state=42)
        return {
            'recommendations': [
                {
                    'food': row['food'],
                    'meal_type': row['meal_type'],
                    'nutrition': {
                        'calories': row['calories'],
                        'protein': f"{row['protein']}g",
                        'carbs': f"{row['carbs']}g",
                        'fat': f"{row['fat']}g"
                    }
                }
                for _, row in default_foods.iterrows()
            ],
            'summary': {
                'bmi_category': 'normal',
                'activity_level': 'moderate',
                'diet_preference': 'vegetarian'
            }
        }
