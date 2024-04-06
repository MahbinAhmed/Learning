let p1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("First Promise");
        // reject("First Promise");
    },1000);
});

let p2 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("Second Promise");
    },2000);
});

let p3 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        resolve("Third Promise");
    },3000);
});

// let promise_list = Promise.all([p1, p2, p3]);
// let promise_list = Promise.allSettled([p1, p2, p3]);
// let promise_list = Promise.race([p1, p2, p3]);
// let promise_list = Promise.any([p1, p2, p3]);
// let promise_list = Promise.resolve("Promise Resolved");
let promise_list = Promise.reject(new Error("Promise Rejected"));
promise_list.then((value)=>{
    console.log(value);
});