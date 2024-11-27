money_capital = 200000
salary = 100000
spend = 130000
increase = 0.05
mounths = 0
while money_capital+salary >= spend:
    money_capital = money_capital + salary - spend
    mounths += 1
    spend = spend * (1+increase)
print('Количество месяцев, которое можно протянуть без долгов:', mounths)
