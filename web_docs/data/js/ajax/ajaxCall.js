
function ajaxCall(valueToSend, target, goalIndex){
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', target, true);
    httpRequest.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    httpRequest.onreadystatechange = function(){
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            let response = httpRequest.responseText;
            //console.log(response);
            reactAjax(goalIndex, response);
        }
    };
    httpRequest.send(valueToSend);
}

//Function launching next part after AJAX response
function reactAjax(index, response){
    if(index == null)
        index=-1;

    switch (index){
        case 1:
            let jsonMap = JSON.parse(response);
            setData(jsonMap);
            break;
        case 2:
            let jsonTreeTech = JSON.parse(response);
            defineJsonTreeTech(jsonTreeTech);
            addWindow(5, null);
            defWindowTree();
            break;
        case 3:
            if(response===true)
                redrawTreeTech();
            break;
        case 100:
            justeTest(response);
            break;
        case -1:
            break;
        default:
            console.log('Error with the index transmitted');
    }
}