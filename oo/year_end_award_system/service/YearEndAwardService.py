from functools import reduce


class YearEndAwardService:
    def giveAwardToColleague(self, person):
        person.setSalary(30)
        pass

    def calculateTotalAward(self, *persons):
        # count = 0
        # for m in persons:
        #     count += m.getSalary()
        # return count
        return reduce(lambda x, y: x + y, map(lambda p: p.getSalary(), persons))
