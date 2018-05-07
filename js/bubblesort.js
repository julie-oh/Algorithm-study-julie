function bubbleSort(arr) {
  // change current index and the next
  // arrow function practice
  const swap = (array, arrLen, idx) => {
    if (arrLen - 1 > idx) {
      let rem = array[idx + 1];
      array[idx + 1] = array[idx];
      array[idx] = rem;
    }

    return array;
  };

  // for-loop until fix index
  for (let i = arr.length; i > 0; i--) {
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, i, j);
      }
    }

  }

  return arr;
}

function bubbleSort2(arr) {
  const swap = (array, i, j) => {
    let tmp = array[j];
    array[j] = array[i];
    array[i] = tmp;
  };

  for (let i = arr.length - 1; i > 0; i--) {
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        swap(arr, j, j + 1);
      }
    }
  }

  return arr;
}

const toSort = [4, 2, 6, 9, 11, 2, 1, 5, 6, 10];
console.log(bubbleSort2(toSort));
