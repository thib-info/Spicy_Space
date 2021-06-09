let markupArray = [];
let jsonTreeTech = null;
let indexTree = 0;
let keyTreeVal = ["colonisateur", "mine", "ferme", "labo", "habitation", "eclaireur"];

function getTreeTech(){
    let valueToSend = "";
    let target = "/treeTech";
    let goal = 2;
    ajaxCall(valueToSend, target, goal);
}

function defineJsonTreeTech(jsonTT){
    jsonTreeTech = jsonTT;
}

// evaluate expressions
const createList = (items, nameValue) => {
    switch (typeof items) {
        case "object":
            getItems(items, nameValue);
            break;
    }
};

// get items in the object
const getItems = (items, nameValue) => {
    for (const item in items) {
        if(item === nameValue || nameValue === null) {
            let details = items[item];
            getDetails(details);
            markupArray.push("</li>");
        }
    }
};

const getDetails = (details) => {
    // iterate over the detail items of object
    let id = details['name'].replace(/ /g, '_');
    if(details['researched'] === true)
        markupArray.push(`<li id=${id} class="researched"><span class="tf-nc tree-tech-researched-color"> ${details['name']} </span>`);
    else
        markupArray.push(`<li id=${id} class="no-researched"><span class="tf-nc tree-tech-no-researched-color"> ${details['name']} </span>`);

    if(Object.entries(details['children']).length !== 0){
        markupArray.push("</div><ul>");
        getItems(details['children'][0], null);
        markupArray.push("</ul>");
    }
};

function drawTreeTech(nameValue){
    markupArray = ["<div class=\"arrow\"><div class=\"arrow-top\"></div><div class=\"arrow-bottom\"></div></div>"];
    markupArray.push("<ul class='tf-tree'>");
    createList(jsonTreeTech, nameValue);
    markupArray.push("</ul>");
    return markupArray.join("");
}

function askUpdateTech(idTech){
    let valueToSend = "idTech=" + idTech;
    let target = "/treeTech";
    let goal = 3;
    ajaxCall(valueToSend, target, goal);
}

function redrawTreeTech(element){
    // Changer la classe pour modifier son visuel à la limite
    let windowContainer = element.parentElement;
    windowContainer.innerHTML = "";
    windowContainer.innerHTML = drawTreeTech(keyTreeVal[indexTree]);
    animateArrow();
}

function animateArrow(){
    let arrow = document.getElementsByClassName('arrow')[0];
    arrow.addEventListener('click', function(){
        indexTree+=1;
        if(indexTree === keyTreeVal.length)
            indexTree = 0;
        redrawTreeTech(this);
    });
}

function printPartTree(){
    let nameToPrint = keyTreeVal[indexTree];
    return drawTreeTech(nameToPrint);
}