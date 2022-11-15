### UnitBuilding class - Subclass of Building
#
#
#

from building import Building


class UnitBuilding(Building):

    def __init__(self,hud,SCREEN,button_list,image,exec_string,cost,unit_list=[]):
        super().__init__(hud,SCREEN,button_list,image,exec_string,cost)
        self.unit_list = unit_list
    
    def get_unit_list(self)->list:
        return self.unit_list


