function solution(left, right) {
  var nums = [];
  var result = [];
  var divisor = [];
  var answer = 0;
  for (let i = left; i < right + 1; i++) {
    nums.push(i);
  }
  for (let i = 0; i < nums.length; i++) {
    for (let j = 1; j < nums[i] + 1; j++) {
      if (nums[i] % j == 0) {
        divisor.push(j);
      }
    }
    result.push(divisor.length);
    divisor = [];
  }
  for (let i = 0; i < nums.length; i++) {
    result[i] % 2 == 0 ? (answer += nums[i]) : (answer -= nums[i]);
  }
  return answer;
}

console.log(solution(24, 27));

// using sqrt
function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    if (Number.isInteger(Math.sqrt(i))) {
      answer -= i;
    } else {
      answer += i;
    }
  }
  return answer;
}
