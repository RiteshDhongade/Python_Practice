import abc

class pwskills:

    @abc.abstractmethod
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass
class data_science(pwskills):
    def student_details(self):
        return "it will return details of data science student"
    def student_assignment(self):
        return "it will return assignments of data science student"
class web_dev(pwskills):
    def student_details(self):
        return "it will give details of web dev student"
    def student_marks(self):
        return "this will return marks of web dev student"
ds = data_science()
ds.student_details()
wd = web_dev()
wd.student_marks()