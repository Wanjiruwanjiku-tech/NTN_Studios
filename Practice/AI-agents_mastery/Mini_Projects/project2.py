# Mini project 2: Tropical diseases symptom checker
# Contains predefined responsses
# Goal => A chatbot that asks for user symptoms, compares them against, a dictionary of diseases and their symptoms and returns a possible match. 

# project2.py

def check_disease(user_symptoms):
    # Disease dictionary
    disease_data = {
        "malaria": ["fever", "chills", "sweating", "headache", "nausea"],
        "dengue": ["fever", "rash", "joint pain", "muscle pain", "headache"],
        "typhoid": ["fever", "abdominal pain", "diarrhea", "weakness", "headache"],
        "cholera": ["diarrhea", "dehydration", "vomiting", "leg cramps"],
        "yellow fever": ["fever", "jaundice", "muscle pain", "nausea", "fatigue"]
    }

    # Store possible matches
    possible_matches = {}

    # Compare symptoms
    for disease, symptoms in disease_data.items():
        matches = len(set(user_symptoms) & set(symptoms))
        if matches > 0:
            possible_matches[disease] = matches

    # Find best match
    if possible_matches:
        best_match = max(possible_matches, key=possible_matches.get)
        print(f"\n🩺 Based on your symptoms, you might have: {best_match.capitalize()}")
        print("⚠️ Please seek professional medical advice for confirmation.\n")
    else:
        print("\n❌ No matching disease found. Please consult a doctor.\n")
        
# Main program
if __name__ == "__main__":
    print("🌴 Tropical Disease Symptom Checker 🤖")

    while True:
        user_input = input("Enter your symptoms (comma-separated) or type 'exit' to quit: ").strip().lower()
        if user_input == "exit":
            print("Exiting the Tropical Disease Symptom Checker. Stay healthy!")
            break

        user_symptoms = [sym.strip() for sym in user_input.split(",")]
        check_disease(user_symptoms)