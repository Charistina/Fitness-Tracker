import pandas as pd

def get_food_recommendations(bmi_category, activity_level, diet_preference):

    bmi_recommendations = {
        "Underweight": {
            "focus": "Calorie-dense, nutrient-rich foods",
            "foods": ["nuts and seeds", "avocados", "whole milk dairy", "whole grains", "healthy oils"],
            "tips": "Eat frequent, smaller meals throughout the day"
        },
        "Normal weight": {
            "focus": "Balanced nutrition for maintenance",
            "foods": ["lean proteins", "whole grains", "fruits and vegetables", "healthy fats"],
            "tips": "Maintain variety in your diet"
        },
        "Overweight": {
            "focus": "High-fiber, low-calorie density foods",
            "foods": ["leafy greens", "lean proteins", "legumes", "whole fruits", "whole grains"],
            "tips": "Focus on portion control and mindful eating"
        },
        "Obese": {
            "focus": "Nutrient-dense, low-calorie foods",
            "foods": ["non-starchy vegetables", "lean proteins", "low-sugar fruits", "whole grains in moderation"],
            "tips": "Consult a nutritionist for personalized guidance"
        }
    }

    activity_recommendations = {
        "No activity": {
            "pre-workout": "Not applicable",
            "post-workout": "Not applicable",
            "general": "Focus on lighter meals that are easy to digest",
            "hydration": "2-2.5 liters of water daily"
        },
        "Light walking": {
            "pre-workout": "Light snack with complex carbs (e.g., banana, whole grain toast)",
            "post-workout": "Protein + carb combo (e.g., yogurt with berries)",
            "general": "Moderate protein intake with balanced carbs",
            "hydration": "2.5-3 liters of water daily"
        },
        "Regular exercise": {
            "pre-workout": "Carbohydrates for energy (e.g., oatmeal, fruit)",
            "post-workout": "Protein-rich recovery meal (e.g., chicken with quinoa)",
            "general": "Higher protein intake for muscle recovery",
            "hydration": "3+ liters with electrolytes during workouts"
        }
    }

    diet_recommendations = {
        "Vegetarian": {
            "proteins": ["paneer", "lentils", "chickpeas", "dairy", "soy products"],
            "meals": ["dal with rice", "vegetable stir-fry with tofu", "cheese sandwich with whole grain bread"]
        },
        "Vegan": {
            "proteins": ["tofu", "tempeh", "legumes", "quinoa", "nuts and seeds"],
            "meals": ["chickpea curry", "lentil soup", "vegetable stir-fry with quinoa"]
        },
        "Non-Vegetarian": {
            "proteins": ["chicken", "fish", "eggs", "lean meat", "dairy"],
            "meals": ["grilled chicken with vegetables", "fish with brown rice", "omelette with whole grain toast"]
        },
        "Eggitarian": {
            "proteins": ["eggs", "dairy", "plant proteins"],
            "meals": ["vegetable omelette", "scrambled eggs with toast", "egg curry with rice"]
        },
        "Gluten-Free": {
            "proteins": ["meat", "fish", "eggs", "legumes", "dairy"],
            "carbs": ["rice", "quinoa", "potatoes", "gluten-free oats"],
            "meals": ["grilled fish with rice", "stir-fried vegetables with quinoa"]
        },
        "Keto": {
            "foods": ["avocados", "cheese", "nuts", "meat", "leafy greens", "olive oil"],
            "meals": ["cheese omelette with avocado", "grilled chicken with broccoli", "salmon with asparagus"]
        },
        "Paleo": {
            "foods": ["lean meats", "fish", "fruits", "vegetables", "nuts and seeds"],
            "meals": ["grilled steak with sweet potato", "salmon with roasted vegetables"]
        },
        "Mediterranean": {
            "foods": ["olive oil", "fish", "whole grains", "nuts", "legumes", "vegetables"],
            "meals": ["grilled fish with quinoa salad", "hummus with whole grain pita"]
        },
        "Other": {
            "advice": "Focus on whole, unprocessed foods and balanced macronutrients"
        }
    }

    meal_timing = {
        "Breakfast": {
            "Underweight": "Dense smoothie (milk, banana, peanut butter, oats)",
            "Normal weight": "Whole grain toast with eggs and avocado",
            "Overweight": "Greek yogurt with berries and nuts",
            "Obese": "Vegetable omelette with small portion of whole grains"
        },
        "Lunch": {
            "Underweight": "Rice with dal and ghee + protein portion",
            "Normal weight": "Balanced plate with protein, carbs, and vegetables",
            "Overweight": "Salad with lean protein and healthy fats",
            "Obese": "Vegetable soup with lean protein"
        },
        "Dinner": {
            "Underweight": "Protein + carb combo (e.g., chicken with rice)",
            "Normal weight": "Lighter protein with vegetables",
            "Overweight": "Lean protein with non-starchy vegetables",
            "Obese": "Small portion of protein with vegetables"
        },
        "Snacks": {
            "Underweight": "Nuts, cheese, dried fruits",
            "Normal weight": "Fruits, yogurt, handful of nuts",
            "Overweight": "Vegetables with hummus, small portion of nuts",
            "Obese": "Raw vegetables, small portion of protein-rich snacks"
        }
    }

    sample_plans = {
        "Indian": {
            "Underweight": ["Poha with nuts", "Dal rice with ghee", "Chapati with paneer curry"],
            "Normal weight": ["Idli with sambar", "Rotli with dal and sabzi", "Grilled fish with quinoa"],
            "Overweight": ["Vegetable upma", "Dal with rotli and salad", "Grilled chicken with vegetables"],
            "Obese": ["Vegetable soup", "Dal with small portion of rotli", "Stir-fried vegetables with tofu"]
        },
        "Western": {
            "Underweight": ["Oatmeal with nuts and honey", "Pasta with meat sauce", "Grilled chicken with mashed potatoes"],
            "Normal weight": ["Greek yogurt with granola", "Quinoa salad with chicken", "Salmon with roasted vegetables"],
            "Overweight": ["Scrambled eggs with spinach", "Grilled chicken salad", "Vegetable stir-fry with tofu"],
            "Obese": ["Vegetable omelette", "Lentil soup", "Grilled fish with steamed vegetables"]
        }
    }
    
    return {
        "BMI Analysis": {
            "Category": bmi_category,
            "Focus Area": bmi_recommendations[bmi_category]["focus"],
            "Recommended Foods": bmi_recommendations[bmi_category]["foods"],
            "Nutrition Tips": bmi_recommendations[bmi_category]["tips"]
        },
        "Activity Recommendations": {
            "Pre-Workout": activity_recommendations[activity_level]["pre-workout"],
            "Post-Workout": activity_recommendations[activity_level]["post-workout"],
            "General Advice": activity_recommendations[activity_level]["general"],
            "Hydration Guide": activity_recommendations[activity_level]["hydration"]
        },
        "Diet-Specific Guidance": diet_recommendations.get(diet_preference, 
            {"advice": "Focus on whole, unprocessed foods appropriate for your dietary needs"}),
        "Meal Timing Suggestions": {
            "Breakfast": meal_timing["Breakfast"][bmi_category],
            "Lunch": meal_timing["Lunch"][bmi_category],
            "Dinner": meal_timing["Dinner"][bmi_category],
            "Snacks": meal_timing["Snacks"][bmi_category]
        },
        "Sample Meal Plans": {
            "Indian": sample_plans["Indian"][bmi_category],
            "Western": sample_plans["Western"][bmi_category]
        },
        "Additional Tips": [
            "Eat mindfully and chew slowly",
            "Stay hydrated throughout the day",
            "Include a variety of colorful vegetables",
            "Limit processed foods and added sugars"
        ]
    }