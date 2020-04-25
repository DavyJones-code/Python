profit = int(input('Сколько была выручка: '))
costs = int(input('Сколько было издержек: '))
if profit > costs:
    profit_mounth = profit - costs
    print('Компания работает в плюс! Прибыль составила: ' + str(profit_mounth))
    personal = input('Сколько человек работает в вашей фирме? : ')
    personal_profit = int(profit_mounth) / int(personal)
    print('Каждый сотрудник принес вашей фирме: ' + str(personal_profit))
elif profit == costs:
    print('Компания не приносит прибыль.')
else:
    print('Компания работает в убыток!')
