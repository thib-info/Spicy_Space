function techWindowContent() {
  return '<p>Ici il y aura tous les éléments relatifs aux Technologies</p>';
}

function diplomacyWindowContent() {
  return `
  <div class="d_1">
      <img src="https://iddeo.ca/wp-content/uploads/2015/03/p_iddeo_10_03_2015_900x400_01.jpg" class="d_img1">
      <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Poster-sized_portrait_of_Barack_Obama.jpg/450px-Poster-sized_portrait_of_Barack_Obama.jpg" class="d_img2">
      <img src="https://www.letudiant.fr/static/uploads/mediatheque/ETU_ETU/1/5/2358415-portrait-anthony-003-300x507.jpeg" class="d_img3">
  </div>
  <div class="d_2">
      <button type="button" class="d_button">Déclarer la guerre</button>
      <button type="button" class="d_button">Proposer la paix</button>
      <button type="button" class="d_button">Proposer l'alliance</button>
      <button type="button" class="d_button">Se retirer de l'alliance</button>
  </div>
  `;
}

function statsWindowContent() {
  return '<p>Ici il y aura tous les éléments relatifs aux statistiques de la partie</p>';
}

function buildingWindowContent(windowIndex,location) {
  var windowID = `${windowIndex}-${location}`;
  return `
  <div class="b_1">
      <div class="b_11">
          <canvas id="c${windowID}" class="systemPreview" width="250" height="250"></canvas>
      </div>
      <div class="b_12">
          <p class="b_sysname">Nom du système</p>
          <p class="b_ressource">Population : 10</p>
          <p class="b_ressource">Ressource 1 : 50</p>
          <p class="b_ressource">Ressource 2 : 60</p>
          <p class="b_ressource">Ressource 3 : 60</p>
      </div>
  </div>
  <div class="b_2">
      <div class="b_22">
          <button type="button" class="b_button">Bâtiment 1</button>
          <button type="button" class="b_button">Bâtiment 2</button>
          <button type="button" class="b_button">Bâtiment 3</button>
      </div>
      <div class="b_23">
          <button type="button" class="b_button">Bâtiment 4</button>
          <button type="button" class="b_button">Bâtiment 5</button>
          <button type="button" class="b_button">Bâtiment 6</button>
      </div>
  </div>
  `;
}

function unitWindowContent(windowIndex,location) {
  return `
   <div class="u_div1 u_divp u_diva">
      <p>Militaire</p>
      <div>
          <p>Exploration</p>
          <button type="button" class="u_button">Vaisseau 11</button>
      </div>
      <div>
          <p>Colonisation</p>
          <button type="button" class="u_button">Vaisseau 12</button>
      </div>
  </div>
  <div class="u_div1 u_divg u_divb">

      <div>
          <p>Destroyer</p>
          <button type="button" class="u_button">I</button>
          <button type="button" class="u_button">II</button>
          <button type="button" class="u_button">III</button>
      </div>

      <div>
          <p>Cuirassé</p>
          <button type="button" class="u_button">I</button>
          <button type="button" class="u_button">II</button>
          <button type="button" class="u_button">III</button>
      </div>
      <div>
          <p>Tardigrade</p>
          <button type="button" class="u_button">I</button>
          <button type="button" class="u_button">II</button>
          <button type="button" class="u_button">III</button>
      </div>
  </div>
  <div class="u_div1 u_divp u_divc">
      <p>Spacioports</p>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>
      <div>
          <button type="button" class="u_button">Spacioport 1</button>
      </div>

  </div>
  `;
}
