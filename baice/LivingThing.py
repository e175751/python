import random
class LivingThing:
    #dead = False
    def __init__(self,name,maximumHP,attack):
        self.name = name
        self.hitPoint = maximumHP
        self.attack = attack
        print("{}のHPは{}で,攻撃力は{}です".format(name,maximumHP,attack))

    def isDead(self):
        return self.dead

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getHitPoint(self):
        return self.hitPoint

    def setHitPoint(self,hitPoint):
        self.hitPoint = hitPoint

    def getAttack(self):
        return self.attack

    def setAttack(self,attack):
        self.attack = attack

    def getIsdead(self):
        return self.dead

    def setIsdead(self,dead):
        self.dead = dead

    def Attack(self,oppoenent):
        if(self.isDead() == False):
            damage = random.randint(1,4) * self.attack
            print("{}の攻撃!{}に{}のダメージを与えた!!".format(self.name,oppoenent.getName(),damage))
            oppoenent.Wounded(damage)

    def Wounded(self,damage):
        pass
