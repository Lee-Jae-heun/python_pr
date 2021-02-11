# 일반 유닛
class Unit:
    def __init__(self, name , hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상유닛이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛 (상속)
class AttackUnit(Unit):
    def __init__(self, name , hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("%s : %s 방향으로 적군이 공격 합니다. [공격력 %d]" % (self.name, location, self.damage))

    def damaged(self, damage):
        print("%s : %d 데미지를 입었습니다." % (self.name, damage))
        self.hp -= damage
        print("%s : 현재 체력은 %d 입니다." % (self.name, self.hp))
        if self.hp <= 0:
            print("%s : 파괴되었습니다." % (self.name))

# 비행 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 비행 공격 유닛 (다중 상속)
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 메소드 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass