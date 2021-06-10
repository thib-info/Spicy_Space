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
    for (let ressource in ressources){
        setRessource(ressources[ressource], ressource);
    }
}

function setRessource(ressource, name){
    let currentQt = ressource['qt'];
    let nextQt = ressource['qt_t'];

    let currentQtPrint = document.getElementById(name + '_q');
    let nextQtPrint = document.getElementById(name + '_qt');

    currentQtPrint.innerText = currentQt;
    nextQtPrint.innerText = "+" + nextQt;
}