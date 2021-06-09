function systemPanelContent(location) {
  return `
  <canvas id="c${location}" width=100%></canvas>
  <button type="button" onclick="addWindow(3,${location})">Bâtiments...</button>
  <button type="button" onclick="addWindow(4,${location})">Unités...</button>
  <button type="button" onclick="addPanel(1,${location},true)">Vaisseaux sur ce système...</button>
  `;
}

function shipPanelContent(location) {
  return `
  dfkuvhfd
  `;
}
