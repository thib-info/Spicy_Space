var leftPanel = 0, rightPanel = 0;

function panelConstructor(panelIndex, location,isRight) {
  // panelIndex est un entier qui indique ce qu'affiche le panel :
  // interface pour vaisseaux, apercu système,etc.
  // location permet de renseigner le système visé ou actuel
  // isRight décrit la position du panel
  function panelBase() {
    if (isRight) {
      document.body.insertAdjacentHTML('beforeend',`
        <div id="panel${panelIndex}" class="panel" side="right">
          <div class="panelHeader"></div>
          <div class="panelBody">
          </div>
        </div>
      `);
    } else {
      document.body.insertAdjacentHTML('beforeend',`
        <div id="panel${panelIndex}" class="panel" side="left">
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
    var panelHeader = document.querySelector(`[id="panel${panelIndex}"] .panelHeader`);
    panelHeader.insertAdjacentHTML('afterbegin',title);
  }
  function panelContent() {
    var content;
    switch (panelIndex) {
      case 0: // Apercu général du système
        content = `
        <p>Ici il y aura tous les éléments relatifs au système ${location}</p>
        <button type="button" onclick="addWindow(3,${location})">Bâtiments...</button>
        <button type="button" onclick="addWindow(4,${location})">Unités...</button>
        `;
        break;
      case 1: // Vaisseaux / flottes
        content = `<p>Ici il y aura tous les éléments relatifs aux Vaisseaux du système ${location}</p>`;
        break;
      default:
        content = '<h2>Default_Content</h2>';
        break;
    }
    var panelBody = document.querySelector(`[id="panel${panelIndex}"] .panelBody`);
    panelBody.insertAdjacentHTML('afterbegin',content);
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

  var panelElement = document.getElementById(`panel${panelIndex}`);
  if (isRight)
    rightPanel = panelElement;
  else
    leftPanel = panelElement;

  function detect(e) {
    let targetElement = e.target; // clicked element
    do {
        //console.log(targetElement);
        if (targetElement == panelElement // click inside the panel
          || targetElement == document.getElementById("windowMenu") // click inside the bar
          || windows.includes(targetElement) // click inside a window
          || clickingOnStar) { // clicking right now on the star
            console.log("inside");
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
}
