#!/usr/bin/env python3

import csv

def read_employees(x):
        with open(x,'r') as f:
                csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
                file = csv.DictReader(f,dialect='empDialect')
                employee_list = []
                for data in file:
                        employee_list.append(data)
                return employee_list

employee_list = read_employees('/home/student-03-aaf8b67d7aa5/data/employees.csv')

def process_data(x):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data

dictionary = process_data(employee_list)


def write_report(dictionary, report_file):
        with open(report_file,'w+') as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')

write_report(dictionary, '/home/student-03-aaf8b67d7aa5/test_report.txt')


