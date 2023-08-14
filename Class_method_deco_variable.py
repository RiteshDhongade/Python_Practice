class pwskills2:

    mobile_number = 9898989898

    def __init__(self, name , email):

        self.name = name
        self.email = email
    
    @classmethod
    def details(cls , name1 , email1):
        return cls(name1 , email1)
    def student_detail(self):
        print(self.name , self.email)

pw = pwskills2.details("riteshDh", "riteshDh@gmail.com")


pw.email
pw.name
pw.student_detail()
pwskills2.mobile_number
pw_obj = pwskills2.mobile_number
