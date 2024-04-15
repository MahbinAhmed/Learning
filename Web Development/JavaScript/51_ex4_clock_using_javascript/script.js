// TIME FUNCTIONS
const get_hours = () =>{
    let time = new Date();
    if(time.getHours()>12){
        let result = time.getHours()-12;
        if(result<10){
            return `0${result}`;
        }
        return result;
    }
    else if(time.getHours()<10){
        return `0${time.getHours()}`;
    }
    return time.getHours()
}

const get_minutes = () =>{
    let time = new Date();
    if(time.getMinutes()<10){
        return `0${time.getMinutes()}`;
    }
    return time.getMinutes();
}

const get_seconds = () =>{
    let time = new Date();
    if(time.getSeconds()<10){
        return `0${time.getSeconds()}`;
    }
    return time.getSeconds();
}

// DOM OBJECTS
let scr_hr = document.getElementsByClassName("hours")[0];
let scr_min = document.getElementsByClassName("minutes")[0];
let scr_sec = document.getElementsByClassName("seconds")[0];

// INITIAL TIME
scr_hr.innerHTML = get_hours();
scr_min.innerHTML = get_minutes();
scr_sec.innerHTML = get_seconds();

// TIME UPDATE
setInterval(function(){
    let hours = get_hours();
    let minutes = get_minutes();
    let seconds = get_seconds();
    
    let scr_hr = document.getElementsByClassName("hours")[0];
    let scr_min = document.getElementsByClassName("minutes")[0];
    let scr_sec = document.getElementsByClassName("seconds")[0];
    scr_hr.innerHTML = hours;
    scr_min.innerHTML = minutes;
    scr_sec.innerHTML = seconds;
},1000);
