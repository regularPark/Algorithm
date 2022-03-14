function solution(numbers) {
  var answer = [];
  for (var i = 0; i < numbers.length - 1; i++) {
    for (var j = i + 1; j < numbers.length; j++) {
      num = numbers[i] + numbers[j];
      if (answer.includes(num) == false) {
        answer.push(num);
      }
    }
  }
  answer.sort((a, b) => a - b);
  return answer;
}

console.log(solution([5, 0, 2, 7]));

// using Set
function solution(numbers) {
  const temp = [];

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      temp.push(numbers[i] + numbers[j]);
    }
  }
  const answer = [...new Set(temp)];

  return answer.sort((a, b) => a - b);
}

console.log("Using Set : " + solution([5, 0, 2, 7]));
