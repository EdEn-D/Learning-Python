class Girl:

    gender = 'female'           #class variable

    def __init__(self,name):
        self.name = name        #instance variable


r = Girl('Tanya')
s = Girl ('Sharkisha')
print(r.gender)
print(s.gender)
print(r.name)