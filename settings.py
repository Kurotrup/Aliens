class Settings:
    """class that stores all game settings"""

    def __init__(self):
        """Initialize game settings """
        # display param
        self.scn_wth = 1200
        self.scn_hth = 675
        self.bg = "pic/bg.jpg"
        self.start_x = 10
        self.start_y = 35

        # ship settings
        self.ship_sp_f = 1.8
