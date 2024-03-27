import re


def check_equal_elements(lst):
    return all(elem == lst[0] for elem in lst)

def main():
    lst = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy : ").split(',')))
    print(check_equal_elements(lst))

if __name__ == "__main__":
    main()
