var leftPanel = 0, rightPanel = 0;

function panelConstructor(panelIndex, location,isRight) {
  // panelIndex est un entier qui indique ce qu'affiche le panel :
  // interface pour vaisseaux, apercu système,etc.
  // location permet de renseigner le système visé ou actuel
  // isRight décrit la position du panel
  var panelID = `${panelIndex}-${location}`;
  function panelBase() {
    if (isRight) {
      document.body.insertAdjacentHTML('beforeend',`
        <div id="${panelID}" class="panel" side="right">
          <div class="panelHeader"></div>
          <div class="panelBody">
          </div>
        </div>
      `);
    } else {
      document.body.insertAdjacentHTML('beforeend',`
        <div id="${panelID}" class="panel" side="left">
          <div class="panelHeader"></div>
          <div class="panelBody">
          </div>
        </div>
      `);
    }

  }
  function panelTitle() {
    var title;
    switch (panelIndex) {
      case 0: // Apercu général du système
        title = `<h2>Système ${location}</h2>`;
        break;
      case 1: // Vaisseaux / flottes
        title = `<h2>Vaisseaux - Système ${location}</h2>`;
        break;
      default:
        title = '<h2>Default_Title</h2>';
        break;
    }
    var panelHeader = document.querySelector(`[id="${panelID}"] .panelHeader`);
    panelHeader.insertAdjacentHTML('afterbegin',title);
  }
  function panelContent() {
    var content;
    switch (panelIndex) {
      case 0: // Apercu général du système
        content = systemPanelContent(location);
        break;
      case 1: // Vaisseaux / flottes
        content = shipPanelContent(location);
        break;
      default:
        content = '<h2>Default_Content</h2>';
        break;
    }
    var panelBody = document.querySelector(`[id="${panelID}"] .panelBody`);
    panelBody.insertAdjacentHTML('afterbegin',content);
    if (panelIndex == 0)
      systemPrev(`c${location}`);
  }
  panelBase();
  panelTitle();
  panelContent();
}

function addPanel(panelIndex,location,isRight) {
  if (isRight == true) {
    if (rightPanel != 0) {
      closePanel(rightPanel);
    }
  }
  panelConstructor(panelIndex,location,isRight);

  var panelElement = document.getElementById(`${panelIndex}-${location}`);
  if (isRight)
    rightPanel = panelElement;
  else
    leftPanel = panelElement;

  function detect(e) {
    console.log("detecting");
    let targetElement = e.target; // clicked element
    do {
        if (targetElement == panelElement // click inside the panel
          || targetElement == document.getElementById("windowMenu") // click inside the bar
          || windows.includes(targetElement) // click inside a window
          || clickingOnStar // clicking right now on the star
          || clickingOnShip) { // clicking right now on the ship
            return;
        }
        targetElement = targetElement.parentNode;
    } while (targetElement);

    // click outside.
    closePanel(panelElement);
  }

  // when clicking outside of panel and bar, remove the panel.
  canvas.addEventListener("click", detect);

  function closePanel(panelElement) {
    document.removeEventListener("click",detect);
    if (panelElement.attributes.side.value == "right")
      rightPanel = 0;
    else
      leftPanel = 0;
    panelElement.remove();
  }
  var list_ship = document.querySelectorAll('#nav1>ul>li');

  for (var i = 0; i < list_ship.length; i++) {
    list_ship[i].addEventListener("click", toggle);
}
  var list_ennemy_ship = document.querySelectorAll('#nav2>ul>li');

  for (var i = 0; i < list_ennemy_ship.length; i++) {
    list_ennemy_ship[i].addEventListener("click", toggle);
    

}


}

function toggle() {
  this.classList.toggle("unselectedShip");
  this.classList.toggle("selectedShip");
}


