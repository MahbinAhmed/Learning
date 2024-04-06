let p1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        console.log("First promise done");
        resolve(1);
    }, 2000);
})

let p2 = p1.then((value)=>{
    console.log(value);
    return new Promise((resolve, reject)=>{
        console.log("Second promise done");
        resolve(2);
    });
})

p2.then((value)=>{
    console.log(value);
    return new Promise((resolve, reject)=>{
        console.log("Third promise done");
        resolve(3);
    })
}).then((value)=>{
    console.log(value);
});