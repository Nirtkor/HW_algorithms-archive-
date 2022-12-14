# В коде подсчитываем количество сыгранных матчей между n командами при условии того, что если кол-во
# команд нечетное, одна из них сразу считается победителем. Считаем k просто фиксируя кол-во команд,
# поделенное на 2 (матчи проходят с 2 командами). При условии, что n == 1 (определилась команда-победитель),
# выводим k. Чисто в теории можно было бы вывести просто k = n-1, т.к. с учетом следующих раундов, будет
# кол-во матчей равно кол-ву команд за исключением победителя, но мы не ищем простых путей.
#
# Сложность алгоритма: есть вложенный цикл if, поэтому O(N) ¯\_(ツ)_/¯

def numberOfMatches(n):
    k = 0                       # k - кол-во сыгранных матчей
    while n > 1:                # при n == 1 определился победитель и матчей не будет
        if n % 2 == 0:          # если кол-во команд четное, делим на 2 (кол-во победителей) и фиксируем матчи в k
            n = n // 2
            k += n
        else:                   # если n - нечет., то учитываем, что команда проходит в следующий раунд, но матча с ней не было
            n += 1
            n = n // 2
            k += n - 1
    return k

print (numberOfMatches(7))
print (numberOfMatches(14))