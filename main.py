#!/usr/bin/env python3

print("f")

from openpyxl import load_workbook

wb = load_workbook('config.xlsx') 
print(wb.sheetnames)

print(wb['page1']['A1'].value)
