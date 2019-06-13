from builtins import str
import openpyxl


class Model():
    wb, ws = None, None
    def loadBase(self, name):
        self.wb = openpyxl.load_workbook(name + ".xlsx")
        self.ws = self.wb.active;

    def getTA(self, num):
        TA = (self.ws["A" + str(num):"E"+str(num)])[0]
        values = TA[1].value, TA[2].value, TA[3].value, TA[4].value
        return values

