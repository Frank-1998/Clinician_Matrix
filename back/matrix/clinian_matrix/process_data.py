SKILLS = []
PATIENTS = {}
SR_NURSES = {}
JR_NURSES = {}
sks = []
def process(patients, nurses, skills):
    for i in skills:
        sks.append(i.id)
    for i in patients:
        skills_needed = i['skills_needed']
        pt_name = i['name']
        is_stable = i['is_stable']
        is_complex = 0 if is_stable else 1 
        result_array = [1 if element in skills_needed else 0 for element in sks]
        value = [is_complex, result_array]
        PATIENTS[pt_name] = value
    for i in nurses:
        level1 = i['level1']
        level2 = i['level2']
        level3 = i['levle3']
        level4 = i['levle4']
        level5 = i['levle5']
        nurse_name = i['name']
        is_jr = i['is_jr']
        nurse_result = []
        for element in sks:
            if element in level1:
                nurse_result.append(1)
            elif element in level2:
                nurse_result.append(2)
            elif element in level3:
                nurse_result.append(3)
            elif element in level4:
                nurse_result.append(4)
            elif element in level5:
                nurse_result.append(5)
        if is_jr:
            JR_NURSES[nurse_name] = nurse_result
        else:
            SR_NURSES[nurse_name] = nurse_result
        for i in skills:
            SKILLS.append(i.name)
    return SKILLS, PATIENTS, JR_NURSES, SR_NURSES

def assign_nurses_to_complex_patients(patient_data, senior_nurses, junior_nurses):
    assignments = {}
    unassigned_complex_patients = {}

    for patient_id, (is_complex, skills_required) in patient_data.items():
        if is_complex == 1:
            assigned = False

            # Assign to junior nurses first
            for nurse_id, skill_ratings in junior_nurses.items():
                required_skills_indices = [i for i, skill_required in enumerate(skills_required) if skill_required == 1]
                if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 1:
                    assignments.setdefault(nurse_id, []).append(patient_id)
                    assigned = True
                    break

            # Assign to senior nurses next
            if not assigned:
                for nurse_id, skill_ratings in senior_nurses.items():
                    required_skills_indices = [i for i, skill_required in enumerate(skills_required) if skill_required == 1]
                    if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 2:
                        assignments.setdefault(nurse_id, []).append(patient_id)
                        assigned = True
                        break

            # Keep track of unassigned complex patients
            if not assigned:
                unassigned_complex_patients[patient_id] = required_skills_indices

    return assignments, unassigned_complex_patients

def assign_remaining_non_complex_patients(patient_data, assignments, senior_nurses, junior_nurses):
    remaining_non_complex_patients = [patient_id for patient_id, (is_complex, _) in patient_data.items() if is_complex == 0]
    unassigned_non_complex_patients = {}
    # Assign remaining non-complex patients to senior nurses first
    for patient_id in remaining_non_complex_patients:
        assigned = False

        # Assign to junior nurses first
        for nurse_id, skill_ratings in junior_nurses.items():
            required_skills_indices = [i for i, skill_required in enumerate(patient_data[patient_id][1]) if skill_required == 1]
            if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 4:
                assignments.setdefault(nurse_id, []).append(patient_id)
                assigned = True
                break

        # Assign to senior nurses next
        if not assigned:
            for nurse_id, skill_ratings in senior_nurses.items():
                required_skills_indices = [i for i, skill_required in enumerate(patient_data[patient_id][1]) if skill_required == 1]
                if all(skill_ratings[i] >= 3 for i in required_skills_indices) and len(assignments.get(nurse_id, [])) < 4:
                    assignments.setdefault(nurse_id, []).append(patient_id)
                    assigned = True
                    break

        # Keep track of unassigned non-complex patients
        if not assigned:
            unassigned_non_complex_patients[patient_id] = required_skills_indices

    return assignments, unassigned_non_complex_patients

def assign(sr_nurses, jr_nurses, patients):
    '''
    nurse_file_path = 'nurse_data_D.json'
    with open(nurse_file_path, 'r') as file:
        nurse_data = json.load(file)
    nurse_data = {
        "N1": [1,[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 5, 5, 4, 5, 5]], # Sr. nurse, with atleast one skill-rating 5
        "N2": [1,[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 5, 5, 5, 4, 5, 5]], # Sr. nurse, with atleast one skill-rating 5
        "N3": [1,[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 4, 5, 4]], # Sr. nurse, with atleast one skill-rating 5
        #"N3": [1,[5, 5, 5, 2, 5, 5, 3, 5, 5, 4, 5, 4]], # Sr. nurse, with atleast one skill-rating 5
        "N4": [0,[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 3, 2, 3, 3, 2, 4, 2]], # Jr. nurse, no skill-rating 5
        "N5": [0,[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 1, 2, 3, 3, 4, 4]] # Jr. nurse, no skill-rating 5
    }
    '''
    #senior_nurses = {nurse_id: skill_ratings for nurse_id, (is_senior, skill_ratings) in nurse_data.items() if is_senior == 1}
    senior_nurses = sr_nurses#junior_nurses = {nurse_id: skill_ratings for nurse_id, (is_senior, skill_ratings) in nurse_data.items() if is_senior == 0}
    junior_nurses = jr_nurses 
    patient_data = patients 

    # Run the algorithm
    assignments, unassigned_complex_patients = assign_nurses_to_complex_patients(patient_data, senior_nurses, junior_nurses)
    assignments, unassigned_non_complex_patients = assign_remaining_non_complex_patients(patient_data, assignments, senior_nurses, junior_nurses)
    '''
    # Display the assignments
    for nurse_id, assigned_patients in assignments.items():
        print(f"Nurse {nurse_id} assigned to patients: {', '.join(assigned_patients)}")

    # Display unassigned complex patients
    print("\nUnassigned Complex Patients:")
    for patient_id, required_skills_indices in unassigned_complex_patients.items():
        required_skills = [SKILLS[i] for i in required_skills_indices if 18 <= i < 30] # only level 3 skills are considered
        print(f"Patient {patient_id} required skill(s): {', '.join(required_skills)}")

    # Display unassigned non-complex patients
    print("\nUnassigned Non-Complex Patients:")
    for patient_id, required_skills_indices in unassigned_non_complex_patients.items():
        required_skills = [SKILLS[i] for i in required_skills_indices if 18 <= i < 30] # only level 3 skills are considered
        print(f"Patient {patient_id} required skill(s): {', '.join(required_skills)}")
    '''
    # Combine the required skillsets for suggested training plan
    suggested_training_plan = set()
    for patient_id, required_skills_indices in unassigned_complex_patients.items():
        suggested_training_plan.update(required_skills_indices)

    for patient_id, required_skills_indices in unassigned_non_complex_patients.items():
        suggested_training_plan.update(required_skills_indices)

    #print("\nSuggested Training Plan:")
    nurses_to_be_trained = {}
    for skill_index in suggested_training_plan:
        #print(f"skill: {SKILLS[skill_index]}")
        for nurse_id, skill_ratings in senior_nurses.items():
            if skill_ratings[skill_index] < 3:
                #print(f"Train nurse {nurse_id} in skill: {SKILLS[skill_index]}")
                nurses_to_be_trained.setdefault(nurse_id, []).append(SKILLS[skill_index])
        for nurse_id, skill_ratings in junior_nurses.items():
            if skill_ratings[skill_index] < 3:
                #print(f"Train nurse {nurse_id} in skill: {SKILLS[skill_index]}")
                nurses_to_be_trained.setdefault(nurse_id, []).append(SKILLS[skill_index])

    return assignments, unassigned_complex_patients, unassigned_non_complex_patients, nurses_to_be_trained