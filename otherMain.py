# Example 1

# try:
#     print("Start code")
#     print(error)
#     print("No errors")
# except:
#     print("We have an error")
#
# print("Code after capsule")
#

# Example 2

# try:
#     print("Start code")
#     print(10/0)
#     print("No errors")
# except ZeroDivisionError:
#     print("We have an Zero Division Error")
# except NameError:
#     print("We have Name Error")
#
# print("Code after capsule")

# Example 3

# try:
#     print("Start code")
#     print(10/0)
#     print("No errors")
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print("Code after capsule")


# Example 4

try:
    x = int(input("Введіть число: "))
    res = 10 / x
    print(res)
except ZeroDivisionError:
    print("На нуль ділити не можна")
except ValueError:
    print("Потрібно було ввести саме число!!!")
