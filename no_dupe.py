student_data={
"my_dict1":{"ID":"194823","name":"sunny","grade":"7th grade","subject integration":"english, math"},
"my_dict2":{"ID":"194848","name":"daniel","grade":"7th grade","subject integration":"english, science"},
"my_dict3":{"ID":"194883","name":"vihaan","grade":"5th grade","subject integration":"computer science, math"},
"my_dict4":{"ID":"194894","name":"arjun","grade":"7th grade","subject integration":"english, math"},
"my_dict1":{"ID":"194823","name":"sunny","grade":"7th grade","subject integration":"english, math"}
}
result={}
seen=set()
for student_ID, details in student_data.items():
    unique_key=(details["ID"],details["name"],details["grade"],details["subject integration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_ID]=details
for k,v, in result.items():
    print(k,":",v)