
function getTreeTech(){
    let valueToSend = "";
    let target = "/treeTech";
    let goal = 2;
    ajaxCall(valueToSend, target, goal);
}

function createHTMLCodeTreeTech(){
    return null;
}

function askUpdateTech(idTech){
    let valueToSend = "idTech=" + idTech;
    let target = "/treeTech";
    let goal = 3;
    ajaxCall(valueToSend, target, goal);
}

function redrawTreeTech(){
    // Changer la classe pour modifier son visuel à la limite
    return null;
}