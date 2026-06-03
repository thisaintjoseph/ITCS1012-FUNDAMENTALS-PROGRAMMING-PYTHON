import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active


sheet ['A1'] = "ID"
sheet ['B1'] = "Name"
sheet['C1'] = "Room Number"
sheet['D1'] = "Date"
sheet['E1'] = "Nights"


workbook.save("Afable_Database.xlsx")
