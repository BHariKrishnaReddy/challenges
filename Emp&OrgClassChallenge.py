#!/bin/python3

import math
import os
import random
import re
import sys

 class Employee:

    def __init__(self,name,Id,age,gender):

        self.name = name

        self.Id   = Id

        self.age  = age

        self.gender = gender



class Organisation:

    def __init__(self,organizationName,employee_list):

        self.organizationName = organizationName

        self.employee_list = employee_list

   

    def addEmployee(self,name,Id,age,gender):

        empObj = Employee(name,Id,age,gender)

        self.employee_list.append(empObj)



    def getEmployeeCount(self):

        count = len(self.employee_list)

        return count

   

    def findEmployeeAge(self,Id):

        for i in self.employee_list:

            if(i.Id == Id):

                return i.age

        return -1

   

    def countEmployees(self,Age):

        countEmp = 0

        for i in self.employee_list:

            if(i.age > Age):

                countEmp = countEmp + 1

        return countEmp





if __name__ == '__main__':

    employees=[]

    o = Organisation('XYZ',employees)

    n=int(input())

    for i in range(n):

        name=input()

        id=int(input())

        age=int(input())

        gender=input()

        o.addEmployee(name,id,age,gender)



    id=int(input())

    age=int(input())

    print(o.getEmployeeCount())

    print(o.findEmployeeAge(id))

    print(o.countEmployees(age))
