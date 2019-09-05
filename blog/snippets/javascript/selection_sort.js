// Selection sort algorithm

function selectionSort(array) {
  for (var i = 0; i < array.length; i++) {
    var minIndex = i;
    for (var j = i + 1; j < array.length; j++) {
      if(array[j] < array[minIndex]) {
        minIndex = j;
      }
    }
    if (minIndex != i) {
      var temp = array[i];
      array[i] = array[minIndex];
      array[minIndex] = temp;
    }
  }
  return array;
}

randomArray = [13,25,26,17,48,78,34,78,12,56,89,45]

sortedList = selectionSort(randomArray);
console.log(`The sorted list is ${sortedList}`);
