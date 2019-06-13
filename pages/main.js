function thesa(){
    sendRequest(th);
}
function athesa(){
    sendRequest(ath);
}

function back(){
    seq = seq.slice(0,-1);
    a = seq.pop();
    sendRequest(a);
}

function sendRequest(num){
    var thesa = document.getElementById("thesa");
    var athesa = document.getElementById("athesa");
    var xhr = new XMLHttpRequest();
    xhr.responseType = "json";
    xhr.open("GET", "/ta/" + base + "/"+num, true);
    xhr.send();
    xhr.onreadystatechange = function() { // (3)
        if (xhr.readyState != 4) return;
        json = xhr.response;
        console.log(json);
        thesa.textContent = json[0];
        athesa.textContent = json[2];
        th = json[1];
        ath = json[3];
        seq.push(num);
    }
}

seq = [];
num = 1;
th=-1
ath = -1
sendRequest(1);
