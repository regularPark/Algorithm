// my code
function solution(phone_number) {
  var answer = "";
  for (var i = 0; i < phone_number.length; i++) {
    if (i < phone_number.length - 4) {
      answer += "*";
    } else answer += phone_number[i];
  }
  return answer;
}

console.log(solution("01033334444"));

// short code
function hide_numbers(s) {
  var result = "*".repeat(s.length - 4) + s.slice(-4);
  return result;
}

console.log("결과 : " + hide_numbers("01033334444"));

//normal code
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}

console.log("정규식 결과 : " + hide_numbers("01033334444"));
