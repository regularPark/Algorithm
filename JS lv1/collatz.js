function solution(n) {
  var cnt = 0;
  while (n !== 1 || cnt > 500) {
    if (n % 2 === 0) {
      n /= 2;
      cnt++;
    } else if (cnt > 500) {
      cnt = -1;
      return cnt;
    } else {
      n = n * 3 + 1;
      cnt++;
    }
  }
  return cnt;
}

console.log(solution(6));

//others code
function collatz(n) {
  var answer = 0;
  while (n != 1 && answer != 500) {
    n % 2 == 0 ? (n = n / 2) : (n = n * 3 + 1);
    answer++;
  }
  return n == 1 ? answer : -1;
}

console.log(collatz(6));
