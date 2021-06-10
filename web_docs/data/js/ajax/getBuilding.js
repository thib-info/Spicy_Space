function callBuilding(){
    let valueToSend = "";
    let target = "/player_info";
    let goal = 4;
    ajaxCall(valueToSend, target, goal);
}

function getBuilding(jsonRes){
    let buildings = jsonRes['syst_details'];
    console.log(ressources);
    for (let building in buildings){

    }
}
