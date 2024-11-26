# AI Health & Fitness Planner 🏋️‍♂️

The **AI Health & Fitness Planner** is a personalized health and fitness app powered by Phidata's AI Agent framework. This app generates tailored dietary and fitness plans based on user inputs such as age, weight, height, activity level, dietary preferences, and fitness goals.

---

## Features

- **Health Agent and Fitness Agent**
    - The app has two phidata agents that are specialists in giving Diet advice and Fitness/workout advice respectively.

- **Personalized Dietary Plans**:
  - Generates detailed meal plans (breakfast, lunch, dinner, and snacks).
  - Includes important considerations like hydration, electrolytes, and fiber intake.
  - Supports various dietary preferences like Keto, Vegetarian, Low Carb, etc.

- **Personalized Fitness Plans**:
  - Provides customized exercise routines based on fitness goals.
  - Covers warm-ups, main workouts, and cool-downs.
  - Includes actionable fitness tips and progress tracking advice.

- **Interactive Q&A**:
  - Allows users to ask follow-up questions about their plans.
  - Provides AI-generated responses for personalized guidance.

---

## Requirements

The application requires the following Python libraries:

- `phidata`
- `google-generativeai`
- `anthropic`
- `streamlit`

Ensure these dependencies are installed via the `requirements.txt` file.

---

## How to Run

Follow the steps below to set up and run the application:

<<<<<<< HEAD
Before anything else, Please get a free Gemini API Key provided by Google AI here: https://aistudio.google.com/apikey

=======
    Before anything else, Please get a free Gemini API Key provided by Google AI here: https://aistudio.google.com/apikey
>>>>>>> 0e9b896 (Added new Diet-Fitness Agent)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
<<<<<<< HEAD
   cd ai_agent_tutorials

=======
   cd ai_agent_tutorials```
>>>>>>> 0e9b896 (Added new Diet-Fitness Agent)
2. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run the Streamlit App(s)**
    If you want to learn and take a look at the basic implementation:
    ```bash
    streamlit run ai_health-fitness_agent/health_agent.py
    ```
    If you want to use the actual app (better UI):
    ```bash
    streamlit run ai_health-fitness_agent/dub.py
    ```


