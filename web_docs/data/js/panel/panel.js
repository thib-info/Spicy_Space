var panels = [];

function panelConstructor(panelIndex, typeValue,isRight) {
  // panelIndex est un entier qui indique ce qu'affiche le panel :
  // interface pour vaisseaux, apercu système,etc.
  // typeValue permet de renseigner le système visé ou actuel
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
      case 0: // Vaisseaux / flottes
        title = `<h2>Vaisseaux - Système ${typeValue}</h2>`;
        break;
      case 1: // Apercu général du système
        title = `<h2>Système ${typeValue}</h2>`;
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
      case 0: // Vaisseaux / flottes
        content = `<p>Ici il y aura tous les éléments relatifs aux Vaisseaux du système ${typeValue}</p>`;
        break;
      case 1: // Apercu général du système
        content = `<p>Ici il y aura tous les éléments relatifs au système ${typeValue}</p>`;
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

function addPanel(panelIndex,typeValue,isRight) {
  panelConstructor(panelIndex,typeValue,isRight);

  var panelElement = document.getElementById(`panel${panelIndex}`);
  panels.push(panelElement);

  function detect(e) {
    let targetElement = e.target; // clicked element
    do {
        console.log(targetElement);
        if (targetElement == panelElement // click inside the panel
          || targetElement == document.getElementById("windowMenu") // click inside the bar
          || windows.includes(targetElement)) { // click inside a window
            console.log("inside");
            return;
        }
        targetElement = targetElement.parentNode;
    } while (targetElement);

    // click outside.
    closePanel(panelElement);
    console.log("outside");
  }

  // when clicking outside of panel and bar, remove the panel.
  document.addEventListener("click", detect);

  function closePanel(panelElement) {
    document.removeEventListener("click",detect);
    panelElement.remove();
  }
}
