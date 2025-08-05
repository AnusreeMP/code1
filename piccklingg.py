import pickle
students=[{"name":"Alice","age":20},{"name":"Bob","age":22}] 
with open("students.pkl","wb")as file:
    pickle.dump(students,file)