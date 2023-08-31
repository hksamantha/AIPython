def check_power_even(a, b, c=2):
    if a**b % c == 0:
        return True
    else:
        return False


print(check_power_even(a=4, b=3))
