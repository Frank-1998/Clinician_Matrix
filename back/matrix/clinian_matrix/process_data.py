SKILLS = []
PATIENTS = {}
NURSES = {}

def process(patients, nurses, skills):
    for i in skills:
        SKILLS.append(i.id)
    for i in patients:
        skills_needed = i['skills_needed']
        pt_name = i['name']
        is_stable = i['is_stable']
        is_complex = 0 if is_stable else 1 
        result_array = [1 if element in skills_needed else 0 for element in SKILLS]
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
        is_sr = 0 if is_jr else 1
        nurse_result = []
        for element in SKILLS:
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
        nurse_value = [is_sr, nurse_result]
        NURSES[nurse_name]=nurse_value
    return SKILLS, PATIENTS, NURSES

