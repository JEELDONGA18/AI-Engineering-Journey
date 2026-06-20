# NOTE: Instance attributes, take preference over class attributes during assignment and retrieval.  means Instance attributes' preference is more compare to class attributes.
class Employee:
    language='Java'
    salary=120000000
Jeel=Employee()
Jeel.salary=20000000
print(Jeel.language,Jeel.salary)