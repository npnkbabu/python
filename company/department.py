'''
Created on 31 Mar 2018

@author: kishore
'''
class department:
    def __init__(self,dept_no,dept_name):
        self.dept_no=dept_no
        self.dept_name=dept_name
        
    def printdepartment(self):
        str = 'dept_no = {0} \n dept_name = {1} '.format(self.dept_no,self.dept_name)
        print str
        

        
