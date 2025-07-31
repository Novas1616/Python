class Robot:

    #constructor
    def __init__(self, baterie,delka_rukou):
        self.baterie = baterie
        self.delka_rukou = delka_rukou
        #self predstavuje ten konkretni objekt

#objekt tvoříme podle classy
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5 )
robot_3 = Robot(14, 0.3)
robot_4 = Robot(58, 0.7 )



print(f"Výdrž baterie:{robot_1.baterie}")
print(f"Délka rukou:{robot_1.delka_rukou}")

print(f"Výdrž baterie:{robot_2.baterie}")
print(f"Délka rukou:{robot_2.delka_rukou}")

print(f"Výdrž baterie:{robot_3.baterie}")
print(f"Délka rukou:{robot_3.delka_rukou}")

print(f"Výdrž baterie:{robot_4.baterie}")
print(f"Délka rukou:{robot_4.delka_rukou}")