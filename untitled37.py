class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Age: "+str(self.citizen_age))
        print("Date of birth: "+self.citizen_dob)
        print("Citizen Id: "+self.citizen_id)
        print("Citizen Added")
        
        
citizen1 = Citizen("Prithviraaj",13,"10th june 2011","0001")
citizen1.add_citizen()

citizen2 = Citizen("Sophia",10,"19th october 2010","0000")
citizen2.add_citizen()


    