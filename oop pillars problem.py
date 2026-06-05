class staff:
    def __init__(self,Name,staff_id,department):
        self.name=Name
        self.id=staff_id
        self.dept=department
        

    def get_details(self):
        # print("ID   : ",self.id)
        # print("NAME : ",self.name)
        # print("DEPT :  ",self.dept)
        return f"NAME : {self.name}\nID   : {self.id}\nDEPT : {self.dept}"

    def cal_salary(self):
        raise

class doctor(staff):
    def __init__(self,Name,staff_id,department,specialization,consultation_fee,patients_per_day):
        self.spec=specialization
        self.cons=consultation_fee
        self.patients=patients_per_day
        super().__init__(Name,staff_id,department)
        

    def cal_salary(self):
        salary=self.cons*self.patients*30
        return salary


class nurse(staff):
    def __init__(self,Name,staff_id,department,shift,base_salary,ot_hours):
        self.shift=shift
        self.base_salary=base_salary
        self.ot_hours=ot_hours
        super().__init__(Name,staff_id,department)
        

    def cal_salary(self):
        salary=self.base_salary+(self.ot_hours*750)
        return salary
        


class technician(staff):
    def __init__(self,Name,staff_id,department,equipment,hourly_rate,hours):
        self.equipment=equipment
        self.hours=hours
        self.hourly_rate=hourly_rate
        super().__init__(Name,staff_id,department)
        

    def cal_salary(self):
        salary=self.hours*self.hourly_rate
        return salary

# liki=
# liki.cal_salary()
# riya=
# riya.cal_salary()
# john=
# john.cal_salary()

staff_members=[doctor("likitha",99,"bio","zoology",200,20),
               nurse("riya",674,"bio","morning shift",35000,14),
               technician("john",89,"mechanical","compresser",640,50),
               doctor("ruby",65,"bio","microbiology",250,20),
               technician("alexa",29,"scanning","x-ray machine",700,50)]


for i in staff_members:
    # print(staff.get_details(i))  details can be accesses in 2 ways
    print(i.get_details())
    print("SALARY : ",i.cal_salary())
    print()