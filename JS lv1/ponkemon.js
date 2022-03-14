function solution(nums) {
  var set_nums = new Set(nums);
  if (parseInt(nums.length / 2) >= set_nums.size) {
    return set_nums.size;
  } else return parseInt(nums.length / 2);
}

console.log(solution([3, 3, 3, 2, 2, 2]));

// 삼항연산자
function solution(nums) {
  var set_nums = new Set(nums);
  return set_nums.size > nums.length / 2 ? nums.length : set_nums.size;
}

console.log("삼항연산자 : " + solution([3, 3, 3, 2, 2, 2]));
