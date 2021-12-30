boss_hp = int(input().split()[-1])
boss_dmg = int(input().split()[-1])

spending = {
    'magic_missile': 53,
    'drain': 73,
    'shield': 113,
    'poison': 173,
    'recharge': 229
}

class Player:
    def __init__(self, hp, mana):
        self.hp, self.mana = hp, mana

    def get_moves(self):
        valid = []
        if self.mana >= 53:
            valid.append('magic_missile')
        if self.mana >= 73:
            valid.append('drain')
        if self.mana >= 113:
            valid.append('shield')
        if self.mana >= 173:
            valid.append('poison')
        if self.mana >= 229:
            valid.append('recharge')
        return valid

    def magic_missile(self, boss):
        boss.hp -= 4
        self.mana -= 53
        boss.tick()

    def drain(self, boss):
        boss.hp -= 2
        self.hp += 2
        self.mana -= 73
        boss.tick()

    def shield(self, boss):
        self.mana -= 113
        boss.tick()
        boss.effect['shield'] += 6

    def poison(self, boss):
        self.mana -= 173
        boss.tick()
        boss.effect['poison'] += 6

    def recharge(self, boss):
        self.mana -= 229
        boss.tick()
        boss.effect['recharge'] += 5

class Boss:
    def __init__(self, hp, dmg, ply):
        self.hp, self.dmg = hp, dmg
        self.player = ply
        self.effect = {'shield': 0, 'poison': 0, 'recharge': 0}

    def attack(self):
        self.tick()
        if self.hp > 0:
            self.player.hp -= max(1, self.dmg - 7 * int(self.effect['shield'] != 0))

    def tick(self):
        if self.effect['poison']:
            self.hp -= 3
        if self.effect['recharge']:
            self.player.mana += 101
        
        for eff in self.effect:
            self.effect[eff] = max(0, self.effect[eff] - 1)

def simulate(hp, dmg, mana, decay):
    def check_state(p_hp, p_mana, b_hp, b_dmg, b_eff, spend):
        if spend >= 1242: # too high for both parts
            return [False, 0]
        
        if p_hp <= 0:
            return [False, spend]
        elif p_hp > 0 and b_hp <= 0:
            return [True, spend]
        p_dummy = Player(p_hp, p_mana)
        res = []
        for move in p_dummy.get_moves():
            p = Player(p_hp, p_mana)
            b = Boss(b_hp, b_dmg, p)
            b.effect = b_eff.copy()
            if decay:
                p.hp -= 1
            exec(f'p.{move}(b);b.attack()')
            check = check_state(p.hp, p.mana, b.hp, b.dmg, b.effect, spend + spending[move])
            if check[0]:
                res.append(check)
        if res:
            return min(res)
        return [False, spend]
    
    default_eff = {'shield': 0, 'poison': 0, 'recharge': 0}
    res = check_state(50, mana, hp, dmg, default_eff, 0)
    return res

print("Part 1:", simulate(boss_hp, boss_dmg, 500, False)[1])
print("Part 2:", simulate(boss_hp, boss_dmg, 500, True)[1])