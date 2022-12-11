import openpyxl

wb=openpyxl.load_workbook("data.xlsx")
sheets=wb.sheetnames
# print(sheets)
print(wb.active.title)