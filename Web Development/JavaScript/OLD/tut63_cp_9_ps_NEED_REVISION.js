// Question-1
// Question-2
// Question-3

// const rejecter = () =>{
//     return new Promise((resolve, reject)=>{
//         setTimeout(()=>{
//             reject(new Error("Request Rejected"));
//         },3000);
//     })
// }
// let func1 = async()=>{
// try{
//     let a = await rejecter();
// }
// catch(error){
//     console.log(error.message);
// }}

// func1();

// Question-4
let p1 = new Promise((resolve, reject)=>{
    resolve("Resolve 1");
})

let p2 = new Promise((resolve, reject)=>{
    resolve("Resolve 2");
})

let p3 = new Promise((resolve, reject)=>{
    resolve("Resolve 3");
})

let func1 = async()=>{
    let time1_start = new Date().getMilliseconds();
    let result = await Promise.all([p1, p2, p3]);
    // result.then((value)=>{
    //     console.log(value);
    // })
    console.log(result);
    let time1_end = new Date().getMilliseconds();
    let total_time = time1_end-time1_start
    console.log("Total time for Function 1:- " + total_time +" ms");
    return total_time;
}

let func2 = async()=>{
    let time2_start = new Date().getMilliseconds();
    let process1 = await p1;
    let process2 = await p2;
    let process3 = await p3;
    let time2_end = new Date().getMilliseconds();
    let total_time = time2_end-time2_start
    console.log("Total time for Function 2:- " + total_time +" ms");
}

let method1 = func1();
let method2 = func2();