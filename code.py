from checker import MyChecker


def register(linter):
    print('Hello Plugin!')

    linter.register_checker(MyChecker(linter))

    print('Cya around!')
