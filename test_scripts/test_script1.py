from generic.base_setup import BaseSetup
from generic.excel import Excel

class TestScript1(BaseSetup):
    def test_script1(self):
        print("This is test script 1")
        print(self.driver.title)
        Excel.get_data("../test_data/input.xlsx",'login',2,2)
        print("hello world")