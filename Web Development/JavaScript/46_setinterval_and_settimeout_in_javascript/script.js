const nothing = (a, b) => {
    console.log("Starter");
}


// let starter = setTimeout(function(){
let starter = setTimeout(nothing, 5000, 5, 6);

let confirmation = confirm("Wanna see the starter?");
if (confirmation == false) {
    clearTimeout(starter);
}

let interval = setInterval(hello = () => {
    console.log("Interval");
}, 5000);

function a(interval) {
    let value;
    setTimeout(function(){
        value = confirm("Wanna see the interval?");
        if(value==false){
            clearInterval(interval)
        }
    }, 15000);
}
// if (a(value) == false) {
//     clearInterval(interval);
// }
// console.log(a(value));
a(interval);