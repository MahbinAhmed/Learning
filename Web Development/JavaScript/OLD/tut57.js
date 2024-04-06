let p1 = new Promise((resolve, reject)=>{
    setTimeout(()=>{
        console.log("SetTimeOut");
        resolve();
    }, 2000);
});

p1.then(()=>{
    console.log("First Then");
})

p1.then(()=>{
    console.log("Second Then");
})