def str_print_recursion_1(i, str):
    if len(str) < i:
        print(str)
        return str

    print(str[0:i])
    str_print_recursion_1(i, str[i:])


def str_print_recursion_2(i, str, arr = None):
   if arr == None:
       arr = []
       arr.append(str[0:i])
       str_print_recursion_2(i, str[i:], arr)

       return

   if len(str) < i:
       arr.append(str)
       for i in range(0, len(arr)):
           print(arr[i])

       return

   arr.append(str[0:i])
   str_print_recursion_2(i, str[i:], arr)


if __name__ == '__main__':
    str_print_recursion_1(3, 'lll')
    str_print_recursion_2(3, 'abcdefgwwqqqqqqqqqqp')