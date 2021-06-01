
function ajaxCall(valueToSend, target, goalIndex){
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', target, true);
    httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    httpRequest.onreadystatechange = function(){
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            let text = httpRequest.responseText;
            console.log(text);
            reactAjax(goalIndex);
        }
        else{
            console.log("Fail with the connection to server");
        }
    };
    httpRequest.send(valueToSend);
}

//Function launching next part after AJAX response
function reactAjax(index){
    if(index == null)
        index=-1;

    switch (index){
        case 1:
            console.log('Only example');
            break;
        case -1:
            break;
        default:
            console.log('Error with the index transmitted');
    }
}