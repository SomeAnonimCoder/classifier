import openpyxl
wb = openpyxl.load_workbook("base.xlsx")
ws = wb.active

def getTA(num):
    TA = (ws["A" + str(num):"E"+str(num)])[0]
    values = TA[1].value, TA[2].value, TA[3].value, TA[4].value
    return values

