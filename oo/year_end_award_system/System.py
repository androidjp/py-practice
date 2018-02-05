from oo.year_end_award_system.model.Person import Person
from oo.year_end_award_system.service.YearEndAwardService import YearEndAwardService

yearEndAwardService = YearEndAwardService()

ming = Person('Ming', 18)
fang = Person('Fang', 19)

print('===================================')
print('[toString 看看我们的员工]')
print('------')

ming.toString()
fang.toString()

print('===================================')
print('[Ming get Award！]')
print('------')

yearEndAwardService.giveAwardToColleague(ming)
print('%s , 今年%d岁 , 年中奖只有他自己知道：%d元' % (ming.name, ming.age, ming.getSalary()))

print('===================================')
print('[Ming get Award！]')
print('------')

yearEndAwardService.giveAwardToColleague(fang)
print('%s , 今年%d岁 , 年中奖只有他自己知道：%d元' % (fang.name, fang.age, fang.getSalary()))

print('===================================')
print('[获得所有员工的年终奖总和：]')
print('------')

yearEndAwardService.calculateTotalAward(ming, fang)
