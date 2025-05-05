def health_chatbot():
    print("HealthBot: Hi! I'm your virtual wellness assistant.")
    print("Ask me about symptoms, wellness tips, or common conditions.")
    print("Type 'exit' to end the conversation.\n")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("HealthBot:Take care! Stay healthy!")
            break
        elif any(symptom in user_input for symptom in ["fever", "temperature", "hot", "chills"]):
            print("HealthBot:A fever could be a sign of infection. Make sure to rest, stay hydrated, and monitor your temperature. Consult a doctor if it goes above 102°F.")

        elif any(symptom in user_input for symptom in ["cough", "sore throat", "throat pain"]):
            print("HealthBot:A sore throat or cough can be caused by a cold or allergies. Warm liquids and rest can help. If it lasts more than a week, see a doctor.")

        elif any(symptom in user_input for symptom in ["headache", "migraine"]):
            print("HealthBot:Try resting in a dark, quiet room and drink plenty of water. Persistent headaches should be discussed with a healthcare provider.")
        elif any(cond in user_input for cond in ["diabetes", "blood sugar"]):
            print("HealthBot:Diabetes is a condition where blood sugar levels are too high. A healthy diet, exercise, and monitoring are key. Talk to your doctor for proper care.")


        elif any(cond in user_input for cond in ["bp", "blood pressure", "hypertension"]):
            print("HealthBot:High blood pressure can lead to heart problems. Limit salt, manage stress, and check your BP regularly.")

        elif "tips" in user_input or "wellness" in user_input:
            print("HealthBot:Here are some wellness tips:\n"
                  "- Drink at least 8 glasses of water a day\n"
                  "- Get 7–8 hours of sleep\n"
                  "- Eat fruits and veggies\n"
                  "- Exercise for 30 mins daily\n"
                  "- Take breaks from screens")

        elif "stress" in user_input or "anxiety" in user_input:
            print("HealthBot:Try deep breathing, meditation, or going for a walk. Talking to someone you trust can also help.")
        elif "covid" in user_input or "corona" in user_input:
            print("HealthBot:Common COVID-19 symptoms include fever, cough, fatigue, and loss of taste or smell. Get tested if you suspect infection.")
        else:
            print("HealthBot: I’m not sure how to help with that.")
# Run the chatbot
health_chatbot()

