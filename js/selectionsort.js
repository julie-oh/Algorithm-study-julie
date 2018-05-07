function selectionsort(arr) {
  // change array index
  let swap = (arr, i, j) => {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  };

  for (let i = 0; i < arr.length; i++) {
    // remember minimum index
    let minidx = i;

    for (let j = i; j < arr.length; j++) {
      // capture minimum index
      if (arr[minidx] > arr[j]) {
        minidx = j;
      }
    }

    // if i is not minimum index
    if (i !== minidx) {
      swap(arr, i, minidx);
    }
  }

  return arr;
}

const toSort = [2,192,1,29,10,22,93,77];
console.log(selectionsort(toSort));