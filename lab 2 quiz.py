#1. class - bimay
binusmaya = binusmaya()

binusmaya.add_lecturer("zhandos pookie", "scicom", "A2005")
binusmaya.add_lecturer("jude whateverhislastnameis", "algoprolec", "A2004")

binusmaya.add_class("L1AC")
binusmaya.add_class("L2BC")

binusmaya.add_schedule("L1AC", "10:00", "scicom")
binusmaya.add_schedule("L2BC", "11:00", "algoprolec")

print(binusmaya.lecturers)
print(binusmaya.classes)
print(binusmaya.schedules)

#2. methods thing

#check if lecturer with the same subject alr exists if not adds a new lecturer to the list
def add_lecturer(self, name, subject, lecturerID):
        for lecturer in self.lecturers:
            if lecturer['subject'] == subject:
                print("lecturer for this subject already exists")
                return
        self.lecturers.append({'name': name, 'subject': subject, 'lecturerID': lecturerID})

#find n remove lecturer by id
def remove_lecturer(self, lecturerID):
        for lecturer in self.lecturers:
            if lecturer['lecturerID'] == lecturerID:
                self.lecturers.remove(lecturer)
                return
        print("lecturer not found")

#check if class code alr exists if not adds it to the list
def add_class(self, class_code):
        if class_code in self.classes:
            print("class code alr exists")
            return
        self.classes.append(class_code)

#find n remove class code from the list
def remove_class(self, class_code):
        if class_code in self.classes:
            self.classes.remove(class_code)
            return
        print("class code not found")

#find lecturer by their subject n if found add a new schedule tuple to the list
def add_schedule(self, class_code, time, subject):
        for lecturer in self.lecturers:
            if lecturer['subject'] == subject:
                self.schedules.append((time, class_code, subject, lecturer['name']))
                return
        print("lecturer for this subject not found")

    #iwanttopasspls4.0gpa