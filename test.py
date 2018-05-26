"Use three double quotes for docstrings"


def very_bad():
    """
    Very bad practices
    """
    print('Executing list comprehension: ')
    print([x for x in range(10)])

    print('Using lambda: ')
    value = (lambda x: x**2)(5)

    print('About to return nothing: ')

    if not value:
        # This should not be caught
        return

    return
