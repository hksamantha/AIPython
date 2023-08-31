def arb_kwards(**kwargs):
    total = 0
    average = 0

    for key, value in kwargs.items():
        total += value
        print(f'{key}={value}')
    average = total/len(kwargs)
    print(f'Total:{total}')
    print(f'Average:{average}')


arb_kwards(Eng=80, Sci=67, Math=90)
