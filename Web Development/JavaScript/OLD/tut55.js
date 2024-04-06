let p = new Promise((resolve, reject)=>{
    let rand = Math.floor(Math.random()*(1-0+1)+0);
    if(rand==0){
        reject("False");
    }
    else if(rand==1){
        resolve("True");
    }
});

p.then((message)=>{
    console.log("Then :- "+message);
});
p.catch((message)=>{
    console.log("Catch :- "+message);
})