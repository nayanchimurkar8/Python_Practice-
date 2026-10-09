
students= { 
    1:{"Name": "Aditi","score":[20,3,40]},
    2:{"Name": "Nayan","score":[780,60,70]},
    3:{"Name": "Aryan","score":[90,68,70]},
    4:{"Name": "Harsh","score":[60,70,60]}
}
for sid, details in students.items():
    avg = sum(details["score"])/len(details["score"])
    details["Average"] = avg
    details["Passed"] = avg>=30
    
print("Student who passed: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["Name"])