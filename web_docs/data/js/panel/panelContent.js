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
  return `
  dfkuvhfd
  `;
}
