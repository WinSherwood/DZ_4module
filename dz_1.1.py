Str = str(input("введите слово: "))


def palindrom(Str):
    x = Str
    if Str == x[::-1]:
        return True
    else:
        return False


print(palindrom(Str))
