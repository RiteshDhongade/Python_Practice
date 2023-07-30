class data_science:
    def syllabus(self):
        print("this is method for data science syllabus")
class web_dev:
    def syllabus(self):
        print("this is method for web dev syllabus")
def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()
obj_data_science=data_science()
obj_web_dev=web_dev()
class_obj=[obj_data_science,obj_web_dev]
class_parcer(class_obj)                        