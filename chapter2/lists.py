"""
"List and tuples" section examples of list comprehension usage

"""


def evens_using_for_loop(count):
    """ Calculate evens using for loop """
    evens = []
    for i in range(count):
        if i % 2 == 0:
            evens.append(i)
    return evens


def evens_using_list_comprehension(count):
    """ Calculate evens using list comprehension """
    # list comprehension 不需要在每次循环的时候做判断，append也额外需要时间，上面的方法还需要维护一个计数器，所以这样快过上面的方法
    # 所以在很多需要if或者函数调用的时候，用list comprehension 会比for loop高效很多
    return [i for i in range(count) if i % 2 == 0]


def enumerate_elements(elements):
    for index, element in enumerate(elements):
        print(index, element)


if __name__ == "__main__":
    print(
        "0-10 evens calculated in for loop:",
        evens_using_for_loop(11)
    )
    print()

    print(
        "0-10 evens calculated in list comprehension:",
        evens_using_list_comprehension(11)
    )
    print()

    print("0-10 evens enumerated:")
    enumerate_elements(evens_using_list_comprehension(11))
    print()

