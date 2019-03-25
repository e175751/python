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


class Hero(LivingThing):
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
        if(Hp < 0):
            Dead = True
            self.setIsdead(Dead)
            print("勇者{}は道半ばで力尽きてしまった".format(Name))



class Enemy(LivingThing):
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



turn = 0
hero = Hero("ルルーシュ",25,3,False)
enemy = Enemy("スザク",20,4,False)
print("{} vs {}".format(hero.getName(),enemy.getName()))
while(not(hero.isDead()) and enemy.isDead() == False):
    turn += 1
    print("{}ターン目開始".format(turn))
    hero.Attack(enemy)
    enemy.Attack(hero)
print("戦闘終了")
