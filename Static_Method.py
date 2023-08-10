#Staic_Method
class pwskills:
    def student_details(self , name , mail_id , number) :
        print(name , mail_id , number)

pw = pwskills()
pw.student_details("rit" , "rit@gmail.com" , 97979797)

class pwskills1:
    def student_details(self , name , mail_id , number):
        print(name , mail_id , number)

    @staticmethod
    def mentor_class(list_mentor) :
        print(list_mentor)

    def mentor(self , mentor_list) :
        print(mentor_list)

pw1 = pwskills1()

pw1.mentor(["rit" , "D37"])

pw1.mentor_class(["Sum" , "Sud"])

