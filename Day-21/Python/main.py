boss_hp = int(input().split()[-1])
boss_dmg = int(input().split()[-1])
boss_arm = int(input().split()[-1])

def simulate(boss_dmg, boss_arm, boss_hp, your_dmg, your_arm, your_hp=100):
    while your_hp > 0 and boss_hp > 0:
        boss_hp -= max(1, your_dmg - boss_arm)
        if boss_hp <= 0:
            break
        your_hp -= max(1, boss_dmg - your_arm)
    return your_hp > 0

def cost(dmg, arm, maximize):
    dmg_shop = {4: 8, 5: 10, 6: 25, 7: 40, 8: 74}
    arm_shop = {0: 0, 1: 13, 2: 31, 3: 53, 4: 75, 5: 102}
    dmg_ring = {0: 0, 1: 25, 2: 50, 3: 100}
    arm_ring = {0: 0, 1: 20, 2: 40, 3: 80}
    cost = [float('inf'), 0][int(maximize)]
    f = [min, max][int(maximize)]
    for d in dmg_shop:
        for d2 in dmg_ring:
            for d3 in dmg_ring:
                for a in arm_shop:
                    for a2 in arm_ring:
                        for a3 in arm_ring:
                            if d + d2 + d3 == dmg and a + a2 + a3 == arm and [d2, d3, a2, a3].count(0) >= 2 and (d2 != d3 or d2 == 0) and (a2 != a3 or a2 == 0):
                                cost = f(cost, dmg_shop[d] + dmg_ring[d2] + dmg_ring[d3] + arm_shop[a] + arm_ring[a2] + arm_ring[a3])
    return cost

win_condition, lose_condition = [], []
for dmg in range(15):
    for arm in range(12):
        if simulate(boss_dmg, boss_arm, boss_hp, dmg, arm):
            win_condition.append((dmg, arm))
        else:
            lose_condition.append((dmg, arm))
print("Part 1:", min(map(lambda x: cost(*x, False), win_condition)))
print("Part 2:", max(map(lambda x: cost(*x, True), lose_condition)))