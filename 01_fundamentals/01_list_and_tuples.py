"""
Topic: Lists & Tuples
Concepts: Slicing, List Comprehensions, Immutability
"""

numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = tuple(x for x in numbers_list)
numbers_gen = (x for x in numbers_list)


def generate_squares(numbers, data_structure):
    if data_structure == "list":
        return [x**2 for x in numbers]
    elif data_structure == "tuple":
        return tuple(x**2 for x in numbers)
    elif data_structure == "generator":
        return (x**2 for x in numbers)


def get_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


if __name__ == "__main__":
    # ------------------------------------------------------------------
    # 1. basic Printing & Generators
    # ------------------------------------------------------------------
    # print(numbers_list)
    # print(numbers_tuple)
    # numbers_gen_list = list(numbers_gen)
    # for num in numbers_gen_list:
    #     print(num)
    # print("Squaring the numbers")

    # ------------------------------------------------------------------
    # 2. Comprehensions & Data Structure Tests
    # ----------------------------------------------------------------
    # square_list = generate_squares(numbers_list, "list")
    # print(square_list)
    # assert square_list == [1, 4, 9, 16, 25], "Square Test Failed"
    # print("List Square test passed!")

    # square_tuple = generate_squares(numbers_list, "tuple")
    # print(square_tuple)
    # assert square_tuple == (1, 4, 9, 16, 25), "Square Test Failed"
    # print("Tuple Square test passed!")

    # square_gen = generate_squares(numbers_list, "generator")
    # square_gen_list = list(square_gen)
    # for num in square_gen_list:
    #     print(num)
    # assert list(square_gen_list) == [1, 4, 9, 16, 25], "Square Test Failed"
    # print("Generator Square test passed!")

    # even_num = get_even_numbers(numbers_list)
    # print("Even numbers are: ", even_num)
    # assert even_num == [2, 4], "Even number Test Failed"
    # print("Even Number assertions passed!")

    # ------------------------------------------------------------------
    # 3. Slicing Examples [start:stop:step]
    # ------------------------------------------------------------------
    # sample_data = [10, 20, 30, 40, 50, 60, 70, 80]
    # first_three = sample_data[:3]
    # print(first_three)
    # assert first_three == [10, 20, 30], "Slicing First Three Test Failed"

    # every_second = sample_data[::2]
    # print(every_second)
    # assert every_second == [10, 30, 50, 70], "Slicing Every Second item Test Failed"

    # reverse_list = sample_data[::-1]
    # print(reverse_list)
    # assert reverse_list == [80, 70, 60, 50, 40, 30, 20, 10], (
    #     "Slicing Reverse Test Failed"
    # )
    # print("All assertions are successfull")

    # ------------------------------------------------------------------
    # 4. Immutability Examples
    # ------------------------------------------------------------------
    # mutable_list = [10, 20, 30, 40]
    # mutable_list[0] = 50
    # print(mutable_list)

    # immutable_tuple = (10, 20, 30, 40)
    # try:
    #     immutable_tuple[0] = 50
    # except TypeError as e:
    #     print("Caught immutability error for tuple", e)
    #     assert True

    # new_tuple = (50,) + immutable_tuple[1:]
    # assert new_tuple == (50, 20, 30, 40)
    # print("Created new tuple", new_tuple)
