function solution(numbers) {
  num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  const reducer = (a, b) => a + b;
  return num.reduce(reducer) - numbers.reduce(reducer);
}

console.log(solution([1, 2, 3, 4, 6, 7, 8, 0]));

// short code
function solution(numbers) {
  return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}
