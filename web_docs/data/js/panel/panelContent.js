function systemPanelContent(location) {
  return `
  <canvas id="c${location}" width=100%></canvas>
  <div class="container-button">
  <button type="button" class="btn-pannel" onclick="addWindow(3,${location})">Bâtiments...</button>
  <button type="button" class="btn-pannel" onclick="addWindow(4,${location})">Unités...</button>
  <button type="button" class="btn-pannel" onclick="addPanel(1,${location},true)">Vaisseaux sur ce système...</button>
  </div>  
  `;
}

function shipPanelContent(location) {
    var tempCode = "<div id='nav1'><ul>";
    ships[location].forEach(ship =>{
        if(ship["owner"]==5) tempCode+=`<li class="unselectedShip">${ship["ship_t"]}</li>`;
    });
    tempCode+= '</ul></div> <button type="button">Attaquer</button>';
    tempCode+= "<div id='nav2'><ul>"
    ships[location].forEach(ship =>{
        if(ship["owner"]!=5) tempCode+=`<li class="unselectedShip">${ship["ship_t"]} joueur ${ship["owner"]}</li>`;
    });
    tempCode+= '</ul></div>';
  return tempCode;
}
