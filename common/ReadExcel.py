import xlrd, json, re

from common.ReadConfig import ReadConfig

class ReadExcel():
    def __init__(self):
        self.readConfig = ReadConfig()
        self.table = xlrd.open_workbook('./testfile/二维码支付.xlsx')
        self.sheet = self.table.sheet_by_index(0)

    def get_rows(self):
        return self.sheet.nrows

    def get_cell_value(self, row, session, option):
        col = int(self.readConfig.get(session, option))
        return self.sheet.cell_value(row, col)

    def getCol(self, session, option):
        return int(self.readConfig.get(session, option))

    def get_col_values(self, col_id=None):
        if col_id is None:
            return self.sheet.col_values(0)
        else:
            return self.sheet.col_values(col_id)

    def get_row_num(self, case_id):
        num = 0
        col_data = self.get_col_values()
        for data in col_data:
            if case_id == data:
                return num
            num = num + 1


if __name__ == '__main__':
    res = ReadExcel()
    ID = res.get_cell_value(1, 'qrCode', 'url')
    print(ID)
