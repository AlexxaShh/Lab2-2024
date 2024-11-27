money_capital = 0
salary = 100000
spend = 130000
increase = 0.03
mounths = 10
for i in range(mounths):
    money_capital += (spend-salary)
    spend *= (1+increase)
print('Подушка безопасности, чтобы протянуть 10 месяцев без долгов:', round(money_capital, 2))
