function callBuilding(){
    let valueToSend = "";
    let target = "/player_info";
    let goal = 4;
    ajaxCall(valueToSend, target, goal);
}

function getBuilding(jsonRes){
    let building = jsonRes['syst_details'];
    console.log(ressources);
    for (let building in building){
        setRessource(ressources[ressource], ressource);
    }
}
