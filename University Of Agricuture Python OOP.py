name = input("Enter Name : ")
semester = int(input("Enter Your Semester In Number : "))
ag = input("Enter Your Ag No : ")
cgpa = input("Enter Your CGPA : ")


class University:
    uni = "University Of Agriculture"
    def __init__(self,name,ag,cgpa,semester):
        self.name = name
        self.semester = semester
        self.ag = ag
        self.cgpa = cgpa
    @staticmethod
    def getInfo():
        print("\t\t---Welcome---")
        print(f"{universityy.uni} Is Present In Toba Tek Singh ")
        print(f"Location = Keekha Bangla Road Near 149 Village ")
        print(f"{universityy.uni} Is Popular For BS Poetry Science Degree")
    def totalDegrees(self):
        print(f"Total Degrees In {universityy.uni} = 16")
    def degreesName(self):
        print("\t*Degress*")
        lst = ["BS Computer Science","BS IT","BS Math","BS Chemistry"
        ,"BS Animal Science","BS Poetry Science",
        "BS English","Bachelor In Bussines Art",
        "BS Bio Chemistry","BS Zology"]
        for i in range(0,len(lst)):
            # print(f"{i+1} - "+ lst[i])
            print(f"{i+1} - {lst[i]}")
    def teachers(self):
        print("\t\*****Teachers*****")
        print("\n\tMale ")
        lst1 = ["Sir Shan Afzal","Mr Khalil Ur Rehman","Dr Umer Farooq","Dr Farooq Khalid"
        ,"Mr Muhammad Auon","Mr Usman","Dr Bahare Mustafa","Dr Riaz Mustafa","Dr Muhammad Tariq"
        ,"Mr Muhammad Wasif Shafeeq","Mr Muhammad Abdul Wahab","Dr Salman Latif Butt","Mr Muhammad Umair"
        ,"Mr Muhammad Ashraf","Dr Zia Ur Rehman","Miss Maliha Sarfaraz","Mr Waseem Tariq","Mr Waseem Malik"
        ,"Mr Ayyaz Rafi"
        ]
        for i in range(0,len(lst1)):
            print(f"{i+1} - {lst1[i]}")
        print(f"\n\tFemales")
        lst2 = ["Miss Madiha Tabassum","Miss Rimsha Zulfqar","Miss Fatima Shehzadi",
        "Miss Sidra Chatha","Miss Sidra Ramzan"," Miss Hina ","Miss Mehmona"
        ,"Miss Maliha Sarfaraz","Miss Noor Ul Huda"," Miss Saba "
        ]
        for j in range(0,len(lst2)):
            print(f"{j+1} - {lst2[j]}")
        

class Degree(University):
    def bsCS(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Computer Science")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsIT(self):
        print(f"\n{self.uni}")
        print(f"{self.name} Is A Studet Of BS IT")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"CGPA Is {self.cgpa}")
    def bsPoetryscience(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Poetry Science")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsChemistry(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Chemistry")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsAnimalscience(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Animal Science")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsBiochemistry(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Bio Chemistry")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsEnglish(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS English")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bba(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of Bachelor In Bussiness Art")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsMath(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Math")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    def bsZology(self):
        print(f"\n{self.uni}")
        print(f"\n{self.name} Is A Student Of BS Zology")
        if semester==3:
            print(f"Semester = {semester}rd")
        elif semester>3:
            print(f"Semester = {semester}Th")
        elif semester==2:
            print(f"Semester = {semester}nD")
        elif semester==1:
            print(f"Semester = {semester}sT")
        print(f"\nAG No = {self.ag}")
        print(f"\nCGPA Of {self.name} Is {self.cgpa}")
    
    
        
# a = University(name,ag,cgpa)
# a.getInfo()
universityy = Degree(name,ag,cgpa,semester)
# universityy.getInfo()
# universityy.bsCS()
universityy.degreesName()
# universityy.totalDegrees()
# universityy.bsIT()
# universityy.teachers()
# universityy.bsBiochemistry()
# universityy.bsPoetryscience()

