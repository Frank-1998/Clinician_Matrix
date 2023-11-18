#Cur Ver (V3): added training recommendation functionality for unassigned nurses

import json

LEVEL_3_SKILLS = ['Recognizing/Managing Anaphylaxis',
'Intravenous infusion Therapy peripheral',
'Intravenous infusion Therapy central',
'Medication Administration simple',
'Medication Administration complex',
'Blood Administration (complex)',
'Tracheostomy care (complex)',
'Urinary Catheterization',
'Drains - simple',
'Drains - complex',
'Wound Care - simple',
'Wound Care - complex']

def assign_nurses_to_complex_patients(patient_data, senior_nurses, junior_nurses):
    assignments = {}
    unassigned_complex_patients = {}
    unassigned_non_complex_patients = {}

    # Assign complex patients to senior nurses first
    for patient_id, (is_complex, skills_required) in patient_data.items():
        if is_complex == 1:
            assigned = False

            # Assign to senior nurses first
            for nurse_id, skill_ratings in senior_nurses.items():
                required_skills_indices = [i for i, skill_required in enumerate(skills_required) if skill_required == 1]
                if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 2:
                    assignments.setdefault(nurse_id, []).append(patient_id)
                    assigned = True
                    break

            # Assign to junior nurses if no senior nurse is available
            if not assigned:
                for nurse_id, skill_ratings in junior_nurses.items():
                    required_skills_indices = [i for i, skill_required in enumerate(skills_required) if skill_required == 1]
                    if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 1:
                        assignments.setdefault(nurse_id, []).append(patient_id)
                        assigned = True
                        break

            # Keep track of unassigned complex patients
            if not assigned:
                unassigned_complex_patients[patient_id] = required_skills_indices

    return assignments, unassigned_complex_patients, unassigned_non_complex_patients

def assign_remaining_non_complex_patients(patient_data, assignments, senior_nurses, junior_nurses):
    remaining_non_complex_patients = [patient_id for patient_id, (is_complex, _) in patient_data.items() if is_complex == 0]
    non_complex_assignments = {}
    # Assign remaining non-complex patients to senior nurses first
    for patient_id in remaining_non_complex_patients:
        assigned = False

        # Assign to senior nurses first
        for nurse_id, skill_ratings in senior_nurses.items():
            required_skills_indices = [i for i, skill_required in enumerate(patient_data[patient_id][1]) if skill_required == 1]
            if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(non_complex_assignments.get(nurse_id, [])) < 2:
                non_complex_assignments.setdefault(nurse_id, []).append(patient_id)
                assignments.setdefault(nurse_id, []).append(patient_id)
                assigned = True
                break

        # Assign to junior nurses if no senior nurse is available
        if not assigned:
            for nurse_id, skill_ratings in junior_nurses.items():
                required_skills_indices = [i for i, skill_required in enumerate(patient_data[patient_id][1]) if skill_required == 1]
                if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(non_complex_assignments.get(nurse_id, [])) < 3:
                    non_complex_assignments.setdefault(nurse_id, []).append(patient_id)
                    assignments.setdefault(nurse_id, []).append(patient_id)
                    assigned = True
                    break

        # Keep track of unassigned non-complex patients
        if not assigned:
            unassigned_non_complex_patients[patient_id] = required_skills_indices

    return non_complex_assignments, assignments, unassigned_non_complex_patients

# Example data represented as skill ratings (1 to 5) in a matrix
nurse_data = {
    "N1": [1,[5, 5, 5, 5, 4, 4, 5, 5, 5, 4, 5, 5]], # Sr. nurse, with atleast one skill-rating 5
    "N2": [1,[5, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, 5]], # Sr. nurse, with atleast one skill-rating 5
    "N3": [1,[5, 5, 5, 3, 5, 5, 3, 5, 5, 4, 5, 4]], # Sr. nurse, with atleast one skill-rating 5
    #"N3": [1,[5, 5, 5, 2, 5, 5, 3, 5, 5, 4, 5, 4]], # Sr. nurse, with atleast one skill-rating 5
    "N4": [0,[4, 4, 4, 4, 4, 3, 2, 3, 3, 2, 4, 2]], # Jr. nurse, no skill-rating 5
    "N5": [0,[4, 4, 4, 4, 3, 3, 1, 2, 3, 3, 4, 4]] # Jr. nurse, no skill-rating 5
}
senior_nurses = {nurse_id: skill_ratings for nurse_id, (is_senior, skill_ratings) in nurse_data.items() if is_senior == 1}
junior_nurses = {nurse_id: skill_ratings for nurse_id, (is_senior, skill_ratings) in nurse_data.items() if is_senior == 0}

# Load patient data from file (replace 'your_patient_file_path.json' with the actual file path)
patient_file_path = 'patient_data_D.json'
with open(patient_file_path, 'r') as file:
    patient_data = json.load(file)

# Run the algorithm
assignments, unassigned_complex_patients, unassigned_non_complex_patients = assign_nurses_to_complex_patients(patient_data, senior_nurses, junior_nurses)
non_complex_assignments, assignments, unassigned_non_complex_patients = assign_remaining_non_complex_patients(patient_data, assignments, senior_nurses, junior_nurses)

# Display the assignments
for nurse_id, assigned_patients in assignments.items():
    print(f"Nurse {nurse_id} assigned to patients: {', '.join(assigned_patients)}")

# Display unassigned complex patients
print("\nUnassigned Complex Patients:")
for patient_id, required_skills_indices in unassigned_complex_patients.items():
    required_skills = [LEVEL_3_SKILLS[i] for i in required_skills_indices]
    print(f"Patient {patient_id} required skill(s): {', '.join(required_skills)}")

# Display unassigned non-complex patients
print("\nUnassigned Non-Complex Patients:")
for patient_id, required_skills_indices in unassigned_non_complex_patients.items():
    required_skills = [LEVEL_3_SKILLS[i] for i in required_skills_indices]
    print(f"Patient {patient_id} required skill(s): {', '.join(required_skills)}")

# Combine the required skillsets for suggested training plan
suggested_training_plan = set()
for patient_id, required_skills_indices in unassigned_complex_patients.items():
    suggested_training_plan.update(required_skills_indices)

for patient_id, required_skills_indices in unassigned_non_complex_patients.items():
    suggested_training_plan.update(required_skills_indices)

print("\nSuggested Training Plan:")
for skill_index in suggested_training_plan:
    #print(f"skill: {LEVEL_3_SKILLS[skill_index]}")
    for nurse_id, (is_senior, skill_ratings) in nurse_data.items():
        if skill_ratings[skill_index] < 3:
            print(f"Train nurse {nurse_id} in skill: {LEVEL_3_SKILLS[skill_index]}")
