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
  let content = `
        <div class="b_1">
            <div class="b_11">
                <canvas id="c${windowID}" class="systemPreview" width="250" height="250">
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
            <div class="b_21">`;
  let defaufltbutton1 = `
                <select onclick="replace_image(this.id`;

  let defaufltbutton2 = `)"  id= "b_selector`;

  let defaufltbutton3=                    ` " class="b_select">
                  <option value="">Construire un batiment</option>
                  <option value="ferme">Ferme</option>
                  <option value="habitations">Habitations</option>
                  <option value="mine">Mine</option>
                  <option value="rafinerie">Rafinerie</option>
                  <option value="usine">Usine</option>
                  <option value="laboratoire">Laboratoire</option>
                  <option value="spatioport">Spatioport</option>
                 </select>
  `;

  let cntr = 0;
  /*
  for( let i = 0; i < buildings.length; i++){
    if (buildings(id_system) = 1 ){
      cntr++;
    }
  } */

  for(cntr;cntr < 6; cntr++){
    content=content + defaufltbutton1 + defaufltbutton2 + cntr + defaufltbutton3;
  }


  return content + `
            </div>
        </div>
  `;
}

function unitWindowContent(windowIndex,location) {
  return `
        <div class="u_div1">
            <div class="u_div11">
                <p>Exploration</p>
                <button type="button" class="u_button u_but11">Vaisseau 11</button>
            </div>
            <div class="u_div12">
                <p>Colonisation</p>
                <button type="button" class="u_button u_but12">Vaisseau 12</button>
            </div>
        </div>
        <div class="u_div2">
            <div class="u_div21">
                <p>Destroyer</p>
                <button type="button" class="u_button u_but211">I</button>
                <button type="button" class="u_button u_but212">II</button>
                <button type="button" class="u_button u_but213">III</button>
            </div>

            <div class="u_div22">
                <p>Cuirassé</p>
                <button type="button" class="u_button u_but221">I</button>
                <button type="button" class="u_button u_but222">II</button>
                <button type="button" class="u_button u_but223">III</button>
            </div>
            <div class="u_div23">
                <p>Tardigrade</p>
                <button type="button" class="u_button u_but231">I</button>
                <button type="button" class="u_button u_but232">II</button>
                <button type="button" class="u_button u_but233">III</button>
            </div>
        </div>
        <div class="u_div3">
            <p>Spatioports</p>
                <button type="button" class="u_button u_but31">Spatioport 1</button>
                <button type="button" class="u_button u_but32">Spatioport 2</button>
                <button type="button" class="u_button u_but33">Spatioport 3</button>
                <button type="button" class="u_button u_but34">Spatioport 4</button>
                <button type="button" class="u_button u_but35">Spatioport 5</button>
                <button type="button" class="u_button u_but36">Spatioport 6</button>
        </div>
  `;
}

function  replace_image(selector_id){
  let torepalce=document.getElementById(selector_id);
  if(torepalce != null){
    let id_image=torepalce.value;
    switch (id_image) {
      case "ferme":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/ferme.png"
       >`
        break;
      case "habitations":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/city.png"
       >`
        break;
      case "mine":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/mine.png"
       >`
        break;
      case "rafinerie":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/fondrie.png"
       >`
        break;
      case "usine":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/usine.png"
       >`
        break;
      case "laboratoire":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/labo.png"
       >`
        break;
      case "spatioport":
        torepalce.outerHTML = `<img class="b_image"
       src="get_img/Spatioport.png"
       >`
        break;
      default:
        break;
    }
  }else(console.log("nothing selected"));
}
