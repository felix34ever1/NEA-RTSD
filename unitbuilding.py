### UnitBuilding class - Subclass of Building
#
#
#

from building import Building
from unit import Unit


class UnitBuilding(Building):

    def __init__(self,grid,SCREEN,building_list:list,name: str,health:int=100,image:str="images/default.png",pos:list=[0,0],exec_string="",cost=1,unit_list=[]):
        super().__init__(grid,SCREEN,building_list,name,health,image,pos)
        self.unit_list = unit_list
        self.exec_string = exec_string

    def get_unit_list(self)->list:
        return self.unit_list

    def on_click(self):
        exec(self.exec_string)



