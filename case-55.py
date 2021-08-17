from scipy import optimize

class miner:
    def __init__(self, computational_power, attack_fraction):
        self.cp = computational_power
        self.af = attack_fraction
        pass

class PowerSplittingGames:
    def __init__(self, miner1, miner2, whom):
        self.miner1 = miner1
        self.miner2 = miner2
        self.whom = whom
        pass

    def generate_reward_1(self, af1):
        cp1 = self.miner1.cp; cp2 = self.miner2.cp
        af1 = af1; af2 = self.miner2.af

        r1_p1 = 1 / (1 - af1 - af2)
        r1_p2 = ((cp1 - af1) ** 2) / (cp1 - af1 + af2)
        r1_p3 = (af1 * (cp2 - af2)) / (cp2 - af2 + af1)
        Reward1 = r1_p1 * (r1_p2 + r1_p3)
        return Reward1

    def generate_reward_2(self, af2):
        cp1 = self.miner1.cp; cp2 = self.miner2.cp
        af1 = self.miner1.af; af2 = af2

        r2_p1 = 1 / (1 - af1 - af2)
        r2_p2 = ((cp2 - af2) ** 2) / (cp2 - af2 + af1)
        r2_p3 = (af2 * (cp1 - af1)) / (cp1 - af1 + af2)
        Reward2 = r2_p1 * (r2_p2 + r2_p3)
        return Reward2

    def main(self):
        if self.whom == 1:
            af1 = optimize.fminbound(lambda af1: self.generate_reward_1(af1), 0, self.miner1.cp)
            strategy = [self.miner1.cp - af1, af1]
            print("The best strategy for miner1 is: ", strategy)
            return

        elif self.whom == 2:
            af2 = optimize.fminbound(lambda af2: self.generate_reward_2(af2), 0, self.miner2.cp)
            strategy = [self.miner2.cp - af2, af2]
            print("The best strategy for miner2 is: ", strategy)
            return

if __name__ == '__main__':
    miner1 = miner(0.35, 0.2)
    miner2 = miner(0.65, 0.4)
    whom = 2
    PSG = PowerSplittingGames(miner1, miner2, whom)
    best_attack_fraction = PSG.main()
