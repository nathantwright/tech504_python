# WORKING WITH DICTIONARIES

student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables",
                               "data_types",
                               "set up"],
}

"""
Dictionaries save data as key-value pairs, where 
  the key is a string and the value is any other 
  data type.
"""

print(student_1)
print(type(student_1))
print(student_1["stream"])
print(student_1["completed_lesson_names"])
print(type(student_1["completed_lesson_names"]))
print(student_1["completed_lesson_names"][0])
student_1["completed_lessons"] = 3
print(student_1)
student_1["completed_lesson_names"].remove(
    "data_types")
print(student_1.keys())