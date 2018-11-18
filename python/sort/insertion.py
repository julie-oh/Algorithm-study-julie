def insertion(arr):
  for i in range(1, len(arr)):
      for j in range(i, 0, -1):
          if arr[j] < arr[j - 1]:
              arr[j], arr[j - 1] = arr[j - 1], arr[j]
          elif arr[j] == arr[i]:
              continue
          else:
              break

  print(arr)


if __name__ == '__main__':
    test_fname = 'test-set/sort_test_set.txt'
    with open(test_fname, 'r') as testf:
        lines = testf.readlines()
        for line in lines:
            int_arr = [int(s) for s in line.strip().split(',')]
            insertion(int_arr)