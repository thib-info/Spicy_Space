let markupArray = ["<ul>"];
let jsonTreeTech = null;

getTreeTech();

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
const createList = (items) => {
    switch (typeof items) {
        case "object":
            getItems(items);
            break;
    }
};

// get items in the object
const getItems = (items) => {
    for (const item in items) {
        //markupArray.push(`<li> ${item}`);
        let details = items[item];
        getDetails(details);
        markupArray.push("</li>");
    }
};

const getDetails = (details) => {
    // iterate over the detail items of object
    let id = details['name'].replace(/ /g, '_');
    if(details['researched'] === true)
        markupArray.push(`<li id=${id} class="researched"><span class="tf-nc"> ${details['name']} </span>`);
    else
        markupArray.push(`<li id=${id} class="no-researched"><span class="tf-nc"> ${details['name']} </span>`);

    if(Object.entries(details['children']).length !== 0){
        markupArray.push("</div><ul>");
        getItems(details['children'][0]);
        markupArray.push("</ul>");
    }
};

function drawTreeTech(){
    createList(jsonTreeTech);
    markupArray.push("</ul>");
    let htmlCode = markupArray.join("");
    return htmlCode;
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