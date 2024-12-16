import random
from driver import Driver
from team import Team

class RaceSimulator:
    def __init__(self, DRIVERS):
        self.field = DRIVERS
    
    
    def get_order(self):
        finishing_order = []
        for driver in self.field:
            position_factor = driver.driver_quality * driver.team.team_quality * random.uniform(.75, 1.0)
            finishing_order.append((position_factor, driver))
        finishing_order.sort(reverse=True)
        for finisher in finishing_order:
            print(f"{finishing_order.index(finisher) +1}. {finisher[1].driver_name}")