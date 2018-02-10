# name = "1ppp"
# if name[0].isnumeric():
#     raise NameError("alyarm")


# while True:
#     a = input("Enter less 10 symbols: ")
#     if len(a)<10:break
# assert len(a)<10
# print(a)
#


class Employer:

    def __init__(self,name = str(), surname = str(), pos=str(),salary=int()):
        self.name = name.title()
        self.surname = surname.title()
        self.position = pos
        self.salary = int(salary)

    def set_name(self,name):
        self.name = name

    def getter_name (self):
        return self.name+" "+self.surname

    def income (self,months):
        return months*int(self.salary)

    def increase_salary(self,howMuch):
        self.salary=self.salary*howMuch

if __name__=="__main__":
    e = Employer("Vasya","pupkin","megachel",3)
    print(e.income(2))
    # e.increase_salary(5)
    print(e.income(12))
    # el = Employer("Noname","Nonamovich")
    # #el.set_name("test")
    # #print(el.name)
    # print(el.name,el.surname)
    # el2 = Employer()
    # print(el2.name,el2.surname)
    # el3 = Employer(name="fameforEL3")
    # print(el3.name,el3.surname)
    # el4 = Employer(surname="Goga")
    # print(el4.name,el4.surname)
    # el5 = Employer(pos="CTO")
    # print(el5.surname,el5.name,el5.position)