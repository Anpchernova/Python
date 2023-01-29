def write(some_str, result):
    with open('log_cash.txt', 'a') as l:
        l.write(f'{some_str} = {result}' + '\n')