function loadScript(src, callback){
    let script = document.createElement("script");
    script.src = src;
    script.onload = function(){
        callback(null, src);
    }
    script.onerror = function(){
        callback(new Error("An error has occured!"), src);
    }
    document.body.appendChild(script);
    return;
}

function output(error, src){ // output() is a callback function
    if(error){
        console.log("Couldn't load the file! URL:- ", src);
        console.log(error);
        return;
    }
    console.log("File loaded succesfully! URL:- ", src);
}

loadScript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js", output);