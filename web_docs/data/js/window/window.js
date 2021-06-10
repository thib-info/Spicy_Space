var windows = []; // array of all window class instances

function windowConstructor(windowIndex,location) {
  // windowIndex is an integer
  // location is the id of the system (=null if window represents diplomacy, stats, etc.)
  var windowID = `${windowIndex}-${location}`;
  function windowBase() { // what all windows contain
    document.body.insertAdjacentHTML('beforeend',`
    <div id="${windowID}" class="window" selected="true">
      <div class="windowHeader">
        <button type="button" class="windowCloseButton" onclick="closeWindow('${windowID}')"></button>
      </div>
      <div class="windowBody">
      </div>
    </div>
    `);
  }
  function windowTitle() {
    var title;
    switch (windowIndex) {
      case 0: // Technologies
        title = '<h2>Technologie</h2>';
        break;
      case 1: // Diplomatie
        title = '<h2>Diplomatie</h2>';
        break;
      case 2: // Statistiques de partie
        title = '<h2>Diplomatie</h2>';
        break;
      case 3: // Construire un bâtiment sur un système
        title = `<h2>Système ${location} - Bâtiments</h2>`;
        break;
      case 4: // Construire une unité sur un système
        title = `<h2>Système ${location} - Unités</h2>`;
        break;
      case 3: // Statistiques de la partie
        title = '<h2>Statistique</h2>';
        break;
      case 5:
        title = '<h2>Arbre de technologie</h2>';
        break;
      default:
        title = '<h2>Default_Title</h2>';
        break;
    }
    var windowHeader = document.querySelector(`[id="${windowID}"] .windowHeader`);
    windowHeader.insertAdjacentHTML('afterbegin',title);
  }
  function windowContent() {
    var content;
    switch (windowIndex) {
      case 0: // Technologies
        content = techWindowContent();
        break;
      case 1: // Diplomatie
        content = diplomacyWindowContent();
        break;
      case 2: // Statistiques de partie
        content = statsWindowContent();
        break;
      case 3: // Construire un bâtiment sur un système
        content = buildingWindowContent(windowIndex,location);
        break;
      case 4:
        content = unitWindowContent(windowIndex,location);
        break;
      case 5: // Arbre de technologie
        content = printPartTree();
        break;
      default:
        content = '<h2>Default_Content</h2>';
        break;
    }
    var windowBody = document.querySelector(`[id="${windowID}"] .windowBody`);
    windowBody.insertAdjacentHTML('afterbegin',content);

      if (windowIndex === 3)
        systemPrev(`c${windowID}`);

      if(windowIndex === 5)
        animateArrow();
  }

  windowBase();
  windowTitle();
  windowContent();
}

function windowFocus(windowElement) {
  windowElement.attributes.selected.value = true;
  windows.forEach(function(windowEl){
    if (windowEl != windowElement) {
      windowEl.attributes.selected.value = false;
    }
  });
}

function windowUnfocusAll() {
  windows.forEach(function(windowEl){
    windowEl.attributes.selected.value = false;
  });
}

function addWindow(windowIndex,location) { // windowIndex is an integer
  if (document.querySelector(`[id="${windowIndex}-${location}"]`)) { // if window already exists,
    windowFocus(document.querySelector(`[id="${windowIndex}-${location}"]`)); // just focus on it
    return 0;
  }

   // constructing window
  windowConstructor(windowIndex,location);

  var windowElement = document.getElementById(`${windowIndex}-${location}`);
  windows.push(windowElement);

  // window focus managment
  windowFocus(windowElement); // always focus the new window
  windowElement.onmousedown = function() {
    windowFocus(windowElement); // focus if window is clicked on
  }

  dragElement(windowElement);
  return 0;
}

function closeWindow(windowID) {
  document.getElementById(`${windowID}`).remove();
}

// Make the DIV element draggable:
function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.querySelector(`[id="${elmnt.id}"] .windowHeader`)) {
    // if present, the header is where you move the DIV from:
    document.querySelector(`[id="${elmnt.id}"] .windowHeader:not(.windowCloseButton)`).onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
