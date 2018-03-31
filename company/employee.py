'''
Created on 31 Mar 2018

@author: kishore
'''
class employee:
    def __init__(self,emp_no,birth_date,first_name,last_name,gender,hire_date,dept_no):
        self.emp_no=emp_no
        self.birth_date=birth_date
        self.first_name=first_name
        self.last_name=last_name
        self.gender=gender
        self.hire_date=hire_date
        self.dept_no=dept_no
        
    def printemployee(self):
        msg = 'emp_no = {0} \n birth_date = {1} \n first_name = {2} \n last_name={3} \n gender = {4} \n hire_date = {5} \n' .format(self.emp_no,self.birth_date, self.first_name,self.last_name,self.gender,self.hire_date)
        print msg