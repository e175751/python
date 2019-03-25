import LivingThing
class Enemy(LivingThing.LivingThing):
    def __init__(self,name,maximumHP,attack,dead):
        super().__init__(name,maximumHP,attack)
        self.hitPoint = maximumHP
        self.dead = dead

    def Wounded(self,damage):
        Hp = self.getHitPoint()
        Name = self.getName()
        Dead = self.getIsdead()
        Hp -= damage
        self.setHitPoint(Hp)
        if(Hp<0):
            Dead = True
            self.setIsdead(Dead)
            print("敵{}は倒された".format(Name))
