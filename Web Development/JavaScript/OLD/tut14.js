let x = "Hello\" ";
console.log(x.length);
console.log(x.toUpperCase());
console.log(x.toLowerCase());
console.log(x.slice(1,4));
console.log(x.replace("ll", "ck"));
let y = "        JavaScript       ";
console.log(x.concat(y, " World "));
y = y.trim();
console.log(x.concat(y, " World "));

for(let i=0;i<y.length;i++){
    x = x.concat(y[i]);
}

console.log(x);