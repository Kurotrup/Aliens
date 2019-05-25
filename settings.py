class Settings:
    """class that stores all game settings"""

    def __init__(self):
        """Initialize game settings """
        # display param
        self.scn_wth = 1200
        self.scn_hth = 675
        self.bg = "pic/bg.jpg"
        self.start_x = 250
        self.start_y = 250
        # ship settings
        self.ship_sp_f = 1.8

        # bullet settings
        self.bul_sp_f = 5
        self.bul_w = 3
        self.bul_h = 12
        self.bul_col = 135, 226, 242
        self.bul_allowed = 10


# 87, 127, 178
