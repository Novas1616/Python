class Robot:

    #constructor
    def __init__(self, baterie,delka_rukou,):
        self.baterie = baterie
        self.delka_rukou = delka_rukou
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print("Robot udelal krok vpred ")
        self.ukony_do_kontroly -= 1
        print(f"Úkonů do kontroly:{self.ukony_do_kontroly}")

    def krok_vzad(self):
        print("Robot udelal krok vzad ")
        self.ukony_do_kontroly -= 1
        print(f"Úkonů do kontroly:{self.ukony_do_kontroly}")


robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5 )
robot_3 = Robot(14, 0.3)
robot_4 = Robot(58, 0.7 )



print(f"Výdrž baterie:{robot_1.baterie}")
print(f"Délka rukou:{robot_1.delka_rukou}")
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vzad()
robot_1.krok_vzad()


