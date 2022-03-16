// my code
function solution(absolutes, signs) {
  var answer = 0;
  for (var i = 0; i < absolutes.length; i++) {
    signs[i] ? (answer += absolutes[i]) : (answer -= absolutes[i]);
  }
  return answer;
}

console.log(solution([4, 7, 12], [true, false, true]));

// short code, using reduce()
function solution(absolutes, signs) {
  return absolutes.reduce((acc, val, i) => acc + val * (signs[i] ? 1 : -1));
}

console.log("using reduce() : " + solution([4, 7, 12], [true, false, true]));
