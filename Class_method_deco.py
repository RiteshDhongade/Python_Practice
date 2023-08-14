class pwskills1:
    def __init__(self, name , email):

        self.name = name
        self.email = email
    
    @classmethod
    def details(cls , name1 , email1):
        return cls(name1 , email1)
    def student_detail(self):
        print(self.name , self.email)

pw = pwskills1.details("riteshDh", "riteshDh@gmail.com")


pw.email
pw.name
pw.student_detail()
