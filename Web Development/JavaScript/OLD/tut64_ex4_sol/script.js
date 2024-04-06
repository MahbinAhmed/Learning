// Time Functions
let get_hour = () =>{
    let get_hour = new Date().getHours();
    let return_value;
    if(get_hour>12){
        document.getElementById("session").innerText = "PM";
        return_value = get_hour-12;
    }
    else{
        return_value =  get_hour;
    }
    return (return_value<10)? "0"+return_value:return_value;
}

let get_minute = () =>{
    let get_minute = new Date().getMinutes();
    return (get_minute<10)? "0"+get_minute:get_minute;
}

let get_second = () =>{
    let get_second = new Date().getSeconds();
    return (get_second<10)? "0"+get_second:get_second;
}

// DOM Objects
let second = document.getElementById("second");
let minute = document.getElementById("minute");
let hour = document.getElementById("hour");

// Time Initializer
second.innerText = get_second();
minute.innerText = get_minute();
hour.innerText = get_hour();

//Main Clock
setInterval(()=>{
    second.innerText = get_second();
    if(second.innerText==0){
        minute.innerText = get_minute();
    };

    if(minute.innerText==0){
        hour.innerText = get_hour();
    };
}, 1000);