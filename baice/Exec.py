import Hero
import Enemy

turn = 0
hero = Hero.Hero("ルルーシュ",25,3,False)
enemy = Enemy.Enemy("スザク",20,4,False)
print("{} vs {}".format(hero.getName(),enemy.getName()))
while(not(hero.isDead()) and enemy.isDead() == False):
    turn += 1
    print("{}ターン目開始".format(turn))
    hero.Attack(enemy)
    enemy.Attack(hero)
print("戦闘終了")
