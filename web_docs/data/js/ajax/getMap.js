// return the value of the initial Map

getInitialMap();

function getInitialMap(){
    let valueToSend = "";
    let target = "/map";
    let goal = 1;
    ajaxCall(valueToSend, target, goal);
}