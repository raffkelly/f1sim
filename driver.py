class Driver:
    def __init__(self, driver_name, team, driver_quality):
        self.driver_name = driver_name
        self.driver_quality = driver_quality
        self.team = team
        team.drivers.append(self)



