//my code
function solution(arr) {
  var answer = [];
  var j = -1;
  for (var i = 0; i < arr.length; i++) {
    if (arr[i] != j) {
      j = arr[i];
      answer.push(j);
    } else continue;
  }
  return answer;
}

console.log(solution([1, 1, 3, 3, 0, 1, 1]));

//short code
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
}
console.log(solution([1, 1, 3, 3, 0, 1, 1]));
