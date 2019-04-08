str = 'Ласковый Литра Кейс Лимит Лимитировать cout Лига Личный Л'
str = str.split(' ')
for i in range(0, len(str)-1):
    if str[i][0] == 'Л' and str[i][1] == 'и':
        print(str[i])
