class pwskills:
    def __init__(self, name , email):

        self.name = name
        self.email = email
    
    def student_detail(self):
        print(self.name , self.email)

pw = pwskills("ritesh", "ritesh@gmail.com")

pw.name