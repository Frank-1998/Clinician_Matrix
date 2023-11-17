#V3: also returning the skill matched.

import numpy as np
SKILLS = ['surgery', 'empathy', 'general care', 'pediatric care', 'postoperative care']

def match_score(skill_ratings_1, skill_ratings_2):
    """
    Calculate a match score based on the dot product of skill ratings.
    You might want to replace this with a more sophisticated scoring function.
    """
    return np.dot(skill_ratings_1, skill_ratings_2)

def assign_patients_to_nurses(nurse_skills, patient_skills):
    assignments = {}
    assigned_nurses = set()

    for patient_id, patient_skill_ratings in patient_skills.items():
        available_nurses = list(set(nurse_skills.keys()) - assigned_nurses)  # Exclude already assigned nurses

        while available_nurses:
            # Calculate match scores for each available nurse
            match_scores = {nurse_id: match_score(nurse_skills[nurse_id], patient_skill_ratings) for nurse_id in available_nurses}

            # Find the nurse(s) with the highest match score
            best_nurses = [nurse_id for nurse_id, score in match_scores.items() if score == max(match_scores.values())]

            # Randomly choose one nurse in case of ties
            best_nurse = np.random.choice(best_nurses)

            # Find the specific skill that led to the highest match score
            best_skill_index = np.argmax(nurse_skills[best_nurse])

            # Assign the patient to the nurse along with the matched skill index
            assignments[patient_id] = (best_nurse, best_skill_index)

            # Update assigned_nurses set
            assigned_nurses.add(best_nurse)

            break  # Exit the loop after the first assignment

    return assignments

# Example data represented as skill ratings (1 to 5) in a matrix
nurse_skills_data = { # [surgery, empathy, general care, pediatric care, postoperative care]
    "Nurse1": np.array([4, 3, 5, 2, 4]), # Top-skill(s): General care
    "Nurse2": np.array([5, 4, 3, 4, 5]), # Top-skill(s): surgery, postoperative care
    "Nurse3": np.array([3, 2, 4, 5, 3]) # Top-skill(s): pediatric care
}

patient_skills_data = { # 
    "Patient1": np.array([5, 5, 1, 1, 5]), # post-surgery patient
    "Patient2": np.array([1, 5, 5, 1, 1]), # OPD patient
    "Patient3": np.array([1, 5, 5, 5, 1]), # child patient
    "Patient4": np.array([1, 5, 5, 5, 1]) # child patient
}

# Run the algorithm
assignments = assign_patients_to_nurses(nurse_skills_data, patient_skills_data)

# Display the assignments along with matched skill index
for patient_id, (nurse_id, skill_index) in assignments.items():
    print(f"Patient {patient_id} assigned to Nurse {nurse_id} based on skill {SKILLS[skill_index]}")
