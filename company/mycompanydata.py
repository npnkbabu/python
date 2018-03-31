'''
Created on 31 Mar 2018

@author: kishore
'''

import pymysql
from mysql.connector import cursor
from company.employee import employee
from company.department import department

class mycompanydata:
    employees = list()
    departments = list()
    
    def __init__(self):
        self.LoadData()
        
    
    def LoadData(self):
        connection = pymysql.connect(host='localhost',user='root',passwd='',db='employees')
        print 'connected to database'
        try:
            with connection.cursor() as cursor:
                sql = 'select * from employees'
                cursor.execute(sql)
                result_set = cursor.fetchall()
                for row in result_set:
                    self.employees.append(employee(row[0], row[1], row[2], row[3], row[4], row[5],1))
                    
                '''for emp in self.employees:
                    emp.printemployee()'''
                    
                sql = 'select * from  departments'
                cursor.execute(sql)
                result_set = cursor.fetchall()
                
                for row in result_set:
                    self.departments.append(department(row[0],row[1]))
                    
                '''for dep in self.departments:
                    dep.printdepartment()'''
                        
                    
        except:
            print 'Error in getting data'
            
        finally:
            connection.close()
        

                
        
    
