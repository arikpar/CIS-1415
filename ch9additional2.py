class Employee:
    def __init__(self,name = '',id_number ='' ,department = '',job_title = ''):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def print_employee_info(self):
        print('Name:',self.name,'\nID Number:',self.id_number,'\nDepartment:',
              self.department,'\nJob Title:', self.job_title,'\n')


instancelist = [Employee('Susan Meyers','47899','Accounting','Vice President'),
                Employee('Mark Jones','39119','IT','Programmer'),
                Employee('Joy Rogers','81774','Manufacturing','Engineer')]

for x in range(len(instancelist)):
    print('Employee %d: ' % (x + 1))
    instancelist[x].print_employee_info()
