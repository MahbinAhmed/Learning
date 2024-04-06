async function hello(){
    return 5;
}

let func1 = async() =>{
    let p1 = new Promise((resolve, reject)=>{
        setTimeout(()=>{
            resolve("First Promise");
        }, 3000);
    })

    let p2 = new Promise((resolve, reject)=>{
        setTimeout(()=>{
            resolve("Second Promise");
        }, 5000);
    })

    console.log("Promise 1 will be printed...");
    let first = await p1;
    console.log(first);
    console.log("Promise 1 Printed")
    
}

// hello().then((value)=>{
//     console.log(value);
// });

// let a = hello();
// a.then((value)=>{
//     console.log(value);
// });

// let a = await hello();
// a.then((value)=>{
//     console.log(value);
// });

// func1();