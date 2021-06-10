callRessources();

function callRessources(){
    let valueToSend = "";
    let target = "/player_info";
    let goal = 4;
    ajaxCall(valueToSend, target, goal);
}

function getRessources(jsonRes){
    let ressources = jsonRes['ressources'];
    console.log(ressources);
    return null;
}