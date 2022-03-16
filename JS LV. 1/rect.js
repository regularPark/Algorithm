const data = "5 3";
const n = data.split(" ");
const a = Number(n[0]),
  b = Number(n[1]);
for (let i = 0; i < b; i++) {
  let str = "";
  for (let j = 0; j < a; j++) {
    str = str + "*";
  }
  console.log(str);
}
