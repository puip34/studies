import random


class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team

    def follow_hero(self, hero):
        print(f"Soldier {self.number} is following Hero {hero.number}")


class Hero:
    def __init__(self, number, team):
        self.number = number
        self.team = team
        self.level = 1

    def increase_level(self):
        self.level += 1


# создание героев и списков солдат
hero1 = Hero(1, random.choice(["A", "B"]))
hero2 = Hero(2, "A" if hero1.team == "B" else "B")

soldiers_team1 = []
soldiers_team2 = []

# генерация солдат
for i in range(10):
    team = random.choice(["A", "B"])
    number = i + 1
    soldier = Soldier(number, team)

    if team == "A":
        soldiers_team1.append(soldier)
    else:
        soldiers_team2.append(soldier)

# определение команды с наибольшим числом солдат
if len(soldiers_team1) > len(soldiers_team2):
    hero1.increase_level()
else:
    hero2.increase_level()

# отправка первого солдата первой команды за первым героем
if hero1.team == "A":
    soldiers_team1[0].follow_hero(hero1)
else:
    soldiers_team2[0].follow_hero(hero1)

# вывод идентификационных номеров героя и солдата, который следует за ним
print(f"Hero {hero1.number} is leading Soldier {soldiers_team1[0].number}")
