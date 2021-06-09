let data = null;
let checkAjax = false;
let isLoading = false;

var url = window.location.href; url = url.split('/');
url = url[2].split(':');

var units = [
  {"id" : 0, "id_system" : 5, "ship_t" : "Cuirassé", "pv_max" : 100, "pv" : 37, "at" : 20, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 3, "tier" : 1, "precision" : 9},
  {"id" : 1, "id_system" : 6, "ship_t" : "Tardigrade", "pv_max" : 100, "pv" : 57, "at" : 20, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 2, "tier" : 2, "precision" : 9},
  {"id" : 2, "id_system" : 5, "ship_t" : "Cuirassé", "pv_max" : 100, "pv" : 64, "at" : 20, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 1, "tier" : 3, "precision" : 9},
  {"id" : 3, "id_system" : 1, "ship_t" : "Tardigrade", "pv_max" : 100, "pv" : 37, "at" : 40, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 5, "tier" : 1, "precision" : 9},
  {"id" : 4, "id_system" : 1, "ship_t" : "Tardigrade", "pv_max" : 100, "pv" : 37, "at" : 40, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 5, "tier" : 3, "precision" : 9},
  {"id" : 5, "id_system" : 17, "ship_t" : "Cuirassé", "pv_max" : 100, "pv" : 37, "at" : 40, "mp" : 5, "cost" : 2000, "maint_cost" : 150, "owner" : 5, "tier" : 1, "precision" : 9},
];


if(url[1] !== '8080'){
  data = {"systems": [{"name": "syst_nul", "pos": [38, 562]}, {"name": "syst_nul", "pos": [72, 531]}, {"name": "syst_nul", "pos": [126, 513]}, {"name": "syst_nul", "pos": [40, 496]}, {"name": "syst_nul", "pos": [16, 509]}, {"name": "syst_nul", "pos": [59, 552]}, {"name": "syst_nul", "pos": [23, 546]}, {"name": "syst_nul", "pos": [84, 491]}, {"name": "syst_nul", "pos": [44, 579]}, {"name": "syst_nul", "pos": [49, 224]}, {"name": "syst_nul", "pos": [79, 226]}, {"name": "syst_nul", "pos": [77, 287]}, {"name": "syst_nul", "pos": [158, 268]}, {"name": "syst_nul", "pos": [109, 278]}, {"name": "syst_nul", "pos": [89, 319]}, {"name": "syst_nul", "pos": [124, 219]}, {"name": "syst_nul", "pos": [143, 307]}, {"name": "syst_nul", "pos": [114, 245]}, {"name": "syst_nul", "pos": [122, 318]}, {"name": "syst_nul", "pos": [264, 488]}, {"name": "syst_nul", "pos": [289, 524]}, {"name": "syst_nul", "pos": [214, 568]}, {"name": "syst_nul", "pos": [274, 584]}, {"name": "syst_nul", "pos": [222, 537]}, {"name": "syst_nul", "pos": [248, 586]}, {"name": "syst_nul", "pos": [231, 519]}, {"name": "syst_nul", "pos": [472, 509]}, {"name": "syst_nul", "pos": [491, 539]}, {"name": "syst_nul", "pos": [453, 564]}, {"name": "syst_nul", "pos": [483, 448]}, {"name": "syst_nul", "pos": [430, 487]}, {"name": "syst_nul", "pos": [411, 551]}, {"name": "syst_nul", "pos": [485, 570]}, {"name": "syst_nul", "pos": [466, 477]}, {"name": "syst_nul", "pos": [456, 524]}, {"name": "syst_nul", "pos": [439, 538]}, {"name": "syst_nul", "pos": [380, 503]}, {"name": "syst_nul", "pos": [549, 244]}, {"name": "syst_nul", "pos": [593, 253]}, {"name": "syst_nul", "pos": [587, 219]}, {"name": "syst_nul", "pos": [499, 213]}, {"name": "syst_nul", "pos": [505, 291]}, {"name": "syst_nul", "pos": [572, 322]}, {"name": "syst_nul", "pos": [580, 304]}, {"name": "syst_nul", "pos": [542, 311]}, {"name": "syst_nul", "pos": [468, 327]}, {"name": "syst_nul", "pos": [560, 295]}, {"name": "syst_nul", "pos": [385, 140]}, {"name": "syst_nul", "pos": [316, 136]}, {"name": "syst_nul", "pos": [403, 174]}, {"name": "syst_nul", "pos": [323, 78]}, {"name": "syst_nul", "pos": [312, 184]}, {"name": "syst_nul", "pos": [388, 184]}, {"name": "syst_nul", "pos": [336, 159]}, {"name": "syst_nul", "pos": [430, 136]}, {"name": "syst_nul", "pos": [352, 170]}, {"name": "syst_nul", "pos": [338, 115]}, {"name": "syst_nul", "pos": [168, 84]}, {"name": "syst_nul", "pos": [224, 131]}, {"name": "syst_nul", "pos": [258, 44]}, {"name": "syst_nul", "pos": [219, 76]}, {"name": "syst_nul", "pos": [251, 79]}, {"name": "syst_nul", "pos": [258, 13]}, {"name": "syst_nul", "pos": [175, 62]}, {"name": "syst_nul", "pos": [294, 70]}, {"name": "syst_nul", "pos": [240, 111]}, {"name": "syst_nul", "pos": [165, 26]}, {"name": "syst_nul", "pos": [227, 93]}, {"name": "syst_nul", "pos": [378, 290]}, {"name": "syst_nul", "pos": [377, 334]}, {"name": "syst_nul", "pos": [362, 374]}, {"name": "syst_nul", "pos": [343, 375]}, {"name": "syst_nul", "pos": [402, 289]}, {"name": "syst_nul", "pos": [302, 313]}, {"name": "syst_nul", "pos": [337, 353]}, {"name": "syst_nul", "pos": [401, 389]}, {"name": "syst_nul", "pos": [406, 345]}, {"name": "syst_nul", "pos": [328, 318]}, {"name": "syst_nul", "pos": [224, 220]}, {"name": "syst_nul", "pos": [230, 264]}, {"name": "syst_nul", "pos": [297, 287]}, {"name": "syst_nul", "pos": [304, 241]}, {"name": "syst_nul", "pos": [214, 192]}, {"name": "syst_nul", "pos": [302, 183]}, {"name": "syst_nul", "pos": [276, 261]}, {"name": "syst_nul", "pos": [210, 252]}, {"name": "syst_nul", "pos": [213, 292]}, {"name": "syst_nul", "pos": [151, 427]}, {"name": "syst_nul", "pos": [203, 418]}, {"name": "syst_nul", "pos": [111, 476]}, {"name": "syst_nul", "pos": [145, 471]}, {"name": "syst_nul", "pos": [112, 425]}, {"name": "syst_nul", "pos": [162, 481]}, {"name": "syst_nul", "pos": [212, 492]}, {"name": "syst_nul", "pos": [165, 443]}, {"name": "syst_nul", "pos": [144, 402]}, {"name": "syst_nul", "pos": [79, 107]}, {"name": "syst_nul", "pos": [0, 96]}, {"name": "syst_nul", "pos": [108, 138]}, {"name": "syst_nul", "pos": [34, 112]}, {"name": "syst_nul", "pos": [91, 52]}, {"name": "syst_nul", "pos": [47, 67]}, {"name": "syst_nul", "pos": [16, 62]}], "sectors": [{"name": "nom_nul", "pos": [67, 532]}, {"name": "nom_nul", "pos": [103, 259]}, {"name": "nom_nul", "pos": [261, 535]}, {"name": "nom_nul", "pos": [435, 505]}, {"name": "nom_nul", "pos": [538, 281]}, {"name": "nom_nul", "pos": [369, 138]}, {"name": "nom_nul", "pos": [228, 75]}, {"name": "nom_nul", "pos": [351, 334]}, {"name": "nom_nul", "pos": [245, 234]}, {"name": "nom_nul", "pos": [162, 441]}, {"name": "nom_nul", "pos": [60, 104]}], "links": [{"start": [38, 562], "end": [59, 552]}, {"start": [38, 562], "end": [23, 546]}, {"start": [38, 562], "end": [44, 579]}, {"start": [72, 531], "end": [126, 513]}, {"start": [72, 531], "end": [40, 496]}, {"start": [126, 513], "end": [84, 491]}, {"start": [126, 513], "end": [44, 579]}, {"start": [40, 496], "end": [72, 531]}, {"start": [16, 509], "end": [40, 496]}, {"start": [59, 552], "end": [38, 562]}, {"start": [59, 552], "end": [72, 531]}, {"start": [59, 552], "end": [126, 513]}, {"start": [59, 552], "end": [44, 579]}, {"start": [23, 546], "end": [16, 509]}, {"start": [84, 491], "end": [72, 531]}, {"start": [84, 491], "end": [89, 319]}, {"start": [44, 579], "end": [38, 562]}, {"start": [49, 224], "end": [79, 226]}, {"start": [49, 224], "end": [77, 287]}, {"start": [79, 226], "end": [77, 287]}, {"start": [79, 226], "end": [114, 245]}, {"start": [77, 287], "end": [79, 226]}, {"start": [77, 287], "end": [89, 319]}, {"start": [77, 287], "end": [114, 245]}, {"start": [158, 268], "end": [143, 307]}, {"start": [109, 278], "end": [77, 287]}, {"start": [109, 278], "end": [89, 319]}, {"start": [109, 278], "end": [122, 318]}, {"start": [89, 319], "end": [84, 491]}, {"start": [89, 319], "end": [49, 224]}, {"start": [89, 319], "end": [77, 287]}, {"start": [89, 319], "end": [122, 318]}, {"start": [124, 219], "end": [79, 226]}, {"start": [124, 219], "end": [114, 245]}, {"start": [124, 219], "end": [108, 138]}, {"start": [143, 307], "end": [158, 268]}, {"start": [143, 307], "end": [109, 278]}, {"start": [114, 245], "end": [79, 226]}, {"start": [114, 245], "end": [77, 287]}, {"start": [114, 245], "end": [109, 278]}, {"start": [122, 318], "end": [109, 278]}, {"start": [122, 318], "end": [89, 319]}, {"start": [122, 318], "end": [143, 307]}, {"start": [264, 488], "end": [289, 524]}, {"start": [264, 488], "end": [231, 519]}, {"start": [264, 488], "end": [343, 375]}, {"start": [289, 524], "end": [274, 584]}, {"start": [214, 568], "end": [222, 537]}, {"start": [274, 584], "end": [222, 537]}, {"start": [274, 584], "end": [248, 586]}, {"start": [222, 537], "end": [289, 524]}, {"start": [222, 537], "end": [231, 519]}, {"start": [248, 586], "end": [214, 568]}, {"start": [231, 519], "end": [212, 492]}, {"start": [472, 509], "end": [483, 448]}, {"start": [491, 539], "end": [453, 564]}, {"start": [491, 539], "end": [485, 570]}, {"start": [453, 564], "end": [439, 538]}, {"start": [483, 448], "end": [430, 487]}, {"start": [483, 448], "end": [401, 389]}, {"start": [430, 487], "end": [472, 509]}, {"start": [430, 487], "end": [411, 551]}, {"start": [430, 487], "end": [466, 477]}, {"start": [430, 487], "end": [380, 503]}, {"start": [411, 551], "end": [439, 538]}, {"start": [485, 570], "end": [453, 564]}, {"start": [466, 477], "end": [472, 509]}, {"start": [466, 477], "end": [483, 448]}, {"start": [466, 477], "end": [430, 487]}, {"start": [456, 524], "end": [472, 509]}, {"start": [456, 524], "end": [439, 538]}, {"start": [439, 538], "end": [453, 564]}, {"start": [439, 538], "end": [411, 551]}, {"start": [380, 503], "end": [289, 524]}, {"start": [549, 244], "end": [593, 253]}, {"start": [549, 244], "end": [587, 219]}, {"start": [549, 244], "end": [499, 213]}, {"start": [549, 244], "end": [560, 295]}, {"start": [593, 253], "end": [549, 244]}, {"start": [587, 219], "end": [549, 244]}, {"start": [587, 219], "end": [593, 253]}, {"start": [499, 213], "end": [549, 244]}, {"start": [499, 213], "end": [587, 219]}, {"start": [499, 213], "end": [505, 291]}, {"start": [505, 291], "end": [542, 311]}, {"start": [505, 291], "end": [468, 327]}, {"start": [505, 291], "end": [560, 295]}, {"start": [572, 322], "end": [580, 304]}, {"start": [572, 322], "end": [468, 327]}, {"start": [580, 304], "end": [572, 322]}, {"start": [580, 304], "end": [560, 295]}, {"start": [542, 311], "end": [572, 322]}, {"start": [542, 311], "end": [560, 295]}, {"start": [468, 327], "end": [505, 291]}, {"start": [468, 327], "end": [542, 311]}, {"start": [560, 295], "end": [572, 322]}, {"start": [560, 295], "end": [580, 304]}, {"start": [560, 295], "end": [542, 311]}, {"start": [385, 140], "end": [336, 159]}, {"start": [385, 140], "end": [430, 136]}, {"start": [316, 136], "end": [336, 159]}, {"start": [316, 136], "end": [338, 115]}, {"start": [403, 174], "end": [385, 140]}, {"start": [403, 174], "end": [388, 184]}, {"start": [323, 78], "end": [430, 136]}, {"start": [323, 78], "end": [338, 115]}, {"start": [312, 184], "end": [316, 136]}, {"start": [312, 184], "end": [336, 159]}, {"start": [312, 184], "end": [352, 170]}, {"start": [312, 184], "end": [302, 183]}, {"start": [388, 184], "end": [385, 140]}, {"start": [388, 184], "end": [403, 174]}, {"start": [388, 184], "end": [352, 170]}, {"start": [388, 184], "end": [402, 289]}, {"start": [336, 159], "end": [316, 136]}, {"start": [336, 159], "end": [312, 184]}, {"start": [336, 159], "end": [352, 170]}, {"start": [430, 136], "end": [499, 213]}, {"start": [430, 136], "end": [403, 174]}, {"start": [352, 170], "end": [385, 140]}, {"start": [338, 115], "end": [385, 140]}, {"start": [338, 115], "end": [323, 78]}, {"start": [168, 84], "end": [165, 26]}, {"start": [224, 131], "end": [124, 219]}, {"start": [224, 131], "end": [168, 84]}, {"start": [224, 131], "end": [240, 111]}, {"start": [224, 131], "end": [227, 93]}, {"start": [224, 131], "end": [214, 192]}, {"start": [258, 44], "end": [251, 79]}, {"start": [258, 44], "end": [258, 13]}, {"start": [219, 76], "end": [168, 84]}, {"start": [219, 76], "end": [165, 26]}, {"start": [219, 76], "end": [227, 93]}, {"start": [251, 79], "end": [258, 44]}, {"start": [251, 79], "end": [294, 70]}, {"start": [251, 79], "end": [240, 111]}, {"start": [251, 79], "end": [227, 93]}, {"start": [258, 13], "end": [294, 70]}, {"start": [175, 62], "end": [168, 84]}, {"start": [175, 62], "end": [219, 76]}, {"start": [175, 62], "end": [165, 26]}, {"start": [294, 70], "end": [323, 78]}, {"start": [294, 70], "end": [224, 131]}, {"start": [294, 70], "end": [258, 44]}, {"start": [294, 70], "end": [251, 79]}, {"start": [240, 111], "end": [294, 70]}, {"start": [165, 26], "end": [258, 44]}, {"start": [165, 26], "end": [219, 76]}, {"start": [165, 26], "end": [258, 13]}, {"start": [165, 26], "end": [175, 62]}, {"start": [227, 93], "end": [168, 84]}, {"start": [227, 93], "end": [219, 76]}, {"start": [227, 93], "end": [240, 111]}, {"start": [378, 290], "end": [402, 289]}, {"start": [378, 290], "end": [328, 318]}, {"start": [377, 334], "end": [378, 290]}, {"start": [377, 334], "end": [362, 374]}, {"start": [377, 334], "end": [406, 345]}, {"start": [362, 374], "end": [377, 334]}, {"start": [362, 374], "end": [343, 375]}, {"start": [362, 374], "end": [337, 353]}, {"start": [362, 374], "end": [401, 389]}, {"start": [343, 375], "end": [362, 374]}, {"start": [343, 375], "end": [302, 313]}, {"start": [343, 375], "end": [337, 353]}, {"start": [402, 289], "end": [377, 334]}, {"start": [302, 313], "end": [378, 290]}, {"start": [302, 313], "end": [328, 318]}, {"start": [302, 313], "end": [297, 287]}, {"start": [337, 353], "end": [343, 375]}, {"start": [337, 353], "end": [302, 313]}, {"start": [337, 353], "end": [328, 318]}, {"start": [401, 389], "end": [483, 448]}, {"start": [401, 389], "end": [362, 374]}, {"start": [401, 389], "end": [343, 375]}, {"start": [406, 345], "end": [468, 327]}, {"start": [406, 345], "end": [377, 334]}, {"start": [406, 345], "end": [362, 374]}, {"start": [406, 345], "end": [401, 389]}, {"start": [328, 318], "end": [378, 290]}, {"start": [328, 318], "end": [302, 313]}, {"start": [328, 318], "end": [337, 353]}, {"start": [224, 220], "end": [214, 192]}, {"start": [224, 220], "end": [276, 261]}, {"start": [230, 264], "end": [224, 220]}, {"start": [230, 264], "end": [276, 261]}, {"start": [230, 264], "end": [210, 252]}, {"start": [230, 264], "end": [213, 292]}, {"start": [297, 287], "end": [302, 313]}, {"start": [297, 287], "end": [213, 292]}, {"start": [214, 192], "end": [224, 220]}, {"start": [214, 192], "end": [302, 183]}, {"start": [302, 183], "end": [224, 220]}, {"start": [276, 261], "end": [230, 264]}, {"start": [276, 261], "end": [297, 287]}, {"start": [276, 261], "end": [304, 241]}, {"start": [210, 252], "end": [158, 268]}, {"start": [210, 252], "end": [224, 220]}, {"start": [210, 252], "end": [230, 264]}, {"start": [210, 252], "end": [214, 192]}, {"start": [213, 292], "end": [230, 264]}, {"start": [213, 292], "end": [276, 261]}, {"start": [213, 292], "end": [203, 418]}, {"start": [151, 427], "end": [203, 418]}, {"start": [151, 427], "end": [145, 471]}, {"start": [151, 427], "end": [165, 443]}, {"start": [203, 418], "end": [151, 427]}, {"start": [203, 418], "end": [165, 443]}, {"start": [111, 476], "end": [84, 491]}, {"start": [111, 476], "end": [145, 471]}, {"start": [111, 476], "end": [112, 425]}, {"start": [145, 471], "end": [151, 427]}, {"start": [145, 471], "end": [111, 476]}, {"start": [145, 471], "end": [162, 481]}, {"start": [145, 471], "end": [165, 443]}, {"start": [112, 425], "end": [151, 427]}, {"start": [162, 481], "end": [212, 492]}, {"start": [162, 481], "end": [165, 443]}, {"start": [165, 443], "end": [212, 492]}, {"start": [144, 402], "end": [122, 318]}, {"start": [144, 402], "end": [151, 427]}, {"start": [79, 107], "end": [108, 138]}, {"start": [79, 107], "end": [91, 52]}, {"start": [0, 96], "end": [16, 62]}, {"start": [108, 138], "end": [79, 107]}, {"start": [108, 138], "end": [34, 112]}, {"start": [34, 112], "end": [79, 107]}, {"start": [34, 112], "end": [0, 96]}, {"start": [34, 112], "end": [47, 67]}, {"start": [34, 112], "end": [16, 62]}, {"start": [91, 52], "end": [79, 107]}, {"start": [91, 52], "end": [108, 138]}, {"start": [91, 52], "end": [47, 67]}, {"start": [47, 67], "end": [79, 107]}, {"start": [47, 67], "end": [34, 112]}, {"start": [16, 62], "end": [34, 112]}, {"start": [16, 62], "end": [47, 67]}], "map_size": 600};
}else{
  isLoading = true;
  checkAjax = true;
}

window.onresize = function()
{
    var canvas = document.getElementById('canvas');
    canvas.width = window.innerWidth;
    canvas.style.width = window.innerWidth;
    canvas.height = window.innerHeight;
    canvas.style.height = window.innerHeight;
}

document.addEventListener('contextmenu', event => event.preventDefault()); // disable right click

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// loading images
const starImage = new Image();
starImage.addEventListener('load', function() {
  loadedImages += 1;
}, false);
if(!checkAjax)
  starImage.src ="../data/images/star2.png";
else
  starImage.src ="../data/images/stazr2.png";

const hoverStarImage = new Image();
hoverStarImage.addEventListener('load', function() {
  loadedImages += 1;
}, false);
hoverStarImage.src ="../data/images/hoverStar2.png";

var clickingOnStar = false, starHovered = false;

var loadedImages = 0
// CONSTANTS
var n = 1000;
var starSize = 48;
var galaxySize = 600;
var maxZoom = 5, minZoom = (canvas.width/galaxySize)/3, zoomFactor = 1.05, zoomLimit = 0.3;
var topCanvas, leftCanvas;


var X = [], Y = [], links = [];
data["systems"].forEach((system) => {
  X.push(system["pos"][0]);
  Y.push(system["pos"][1]);
});
data["links"].forEach((link) => {
  links.push([link["start"],link["end"]]);
});
console.log(X.length);


/*for (let i = 0 ; i < n ; i++) {
  X.push(Math.floor(Math.random() * galaxySize));
  Y.push(Math.floor(Math.random() * galaxySize));
}*/

const mouse = {
  x: 0,
  y: 0,
  w: 0,
  alt: false,
  shift: false,
  ctrl: false,
  buttonLastRaw: 0, // user modified value
  buttonRaw: 0,
  over: false,
  buttons: [1, 2, 4, 6, 5, 3] // masks for setting and clearing button raw bits;
};

function mouseMove(event) {
  mouse.x = event.offsetX;
  mouse.y = event.offsetY;
  if (mouse.x === undefined) {
    mouse.x = event.clientX;
    mouse.y = event.clientY;
  }
  mouse.alt = event.altKey;
  mouse.shift = event.shiftKey;
  mouse.ctrl = event.ctrlKey;
  if (event.type === "mousedown") {
    //event.preventDefault();
    mouse.buttonRaw |= mouse.buttons[event.which - 1];
  } else if (event.type === "mouseup") {
    mouse.buttonRaw &= mouse.buttons[event.which + 2];
  } else if (event.type === "mouseout") {
    mouse.buttonRaw = 0;
    mouse.over = false;
  } else if (event.type === "mouseover") {
    mouse.over = true;
  } else if (event.type === "mousewheel") {
    event.preventDefault();
    mouse.w = event.wheelDelta;
  } else if (event.type === "DOMMouseScroll") {
    // FF you pedantic doffus
    mouse.w = -event.detail;
  }
}

function setupMouse(e) {
  e.addEventListener("mousemove", mouseMove);
  e.addEventListener("mousedown", mouseMove);
  e.addEventListener("mouseup", mouseMove);
  e.addEventListener("mouseout", mouseMove);
  e.addEventListener("mouseover", mouseMove);
  e.addEventListener("mousewheel", mouseMove);
  e.addEventListener("DOMMouseScroll", mouseMove); // fire fox

  e.addEventListener(
    "contextmenu",
    function(e) {
      e.preventDefault();
    },
    false
  );
}
setupMouse(canvas);

// terms.
// Real space, real, r (prefix) refers to the transformed canvas space.
// c (prefix), chase is the value that chases a requiered value
const displayTransform = {
  x: 0,
  y: 0,
  ox: 0,
  oy: 0,
  scale: 1,
  rotate: 0,
  cx: 0, // chase values Hold the actual display
  cy: 0,
  cox: 0,
  coy: 0,
  cscale: 1,
  crotate: 0,
  dx: 0, // deltat values
  dy: 0,
  dox: 0,
  doy: 0,
  dscale: 1,
  drotate: 0,
  drag: 0.1, // drag for movements
  accel: 0.7, // acceleration
  matrix: [0, 0, 0, 0, 0, 0], // main matrix
  invMatrix: [0, 0, 0, 0, 0, 0], // invers matrix;
  mouseX: 0,
  mouseY: 0,
  ctx: ctx,
  setTransform: function() {
    const m = this.matrix;
    let i = 0;
    this.ctx.setTransform(m[i++], m[i++], m[i++], m[i++], m[i++], m[i++]);
  },
  setHome: function() {
    this.ctx.setTransform(1, 0, 0, 1, 0, 0);
  },
  update: function() {
    // smooth all movement out. drag and accel control how this moves
    // acceleration
    this.dx += (this.x - this.cx) * this.accel;
    this.dy += (this.y - this.cy) * this.accel;
    this.dox += (this.ox - this.cox) * this.accel;
    this.doy += (this.oy - this.coy) * this.accel;
    this.dscale += (this.scale - this.cscale) * this.accel;
    this.drotate += (this.rotate - this.crotate) * this.accel;

    if((-displayTransform.matrix[4] / displayTransform.scale)<-galaxySize && this.dx<0) {
        this.dx=0;
    }
    if((-displayTransform.matrix[5] / displayTransform.scale)<-(galaxySize*0.5) && this.dy<0) {
        this.dy=0;
    }
    if(((-displayTransform.matrix[4] +canvas.width)/ displayTransform.scale)>2*galaxySize && this.dx>0) {
        this.dx=0;
    }
    if(((-displayTransform.matrix[5] +canvas.height)/ displayTransform.scale)>1.5*galaxySize && this.dy>0) {
        this.dy=0;
    }


    // drag
    this.dx *= this.drag;
    this.dy *= this.drag;
    this.dox *= this.drag;
    this.doy *= this.drag;
    this.dscale *= this.drag;
    this.drotate *= this.drag;
    // set the chase values. Chase chases the requiered values
    this.cx += this.dx;
    this.cy += this.dy;
    this.cox += this.dox;
    this.coy += this.doy;
    this.cscale += this.dscale;
    this.crotate += this.drotate;

    // create the display matrix
    this.matrix[0] = Math.cos(this.crotate) * this.cscale;
    this.matrix[1] = Math.sin(this.crotate) * this.cscale;
    this.matrix[2] = -this.matrix[1];
    this.matrix[3] = this.matrix[0];

    // set the coords relative to the origin
    this.matrix[4] =
      -(this.cx * this.matrix[0] + this.cy * this.matrix[2]) + this.cox;
    this.matrix[5] =
      -(this.cx * this.matrix[1] + this.cy * this.matrix[3]) + this.coy;

    // create invers matrix
    const det =
      this.matrix[0] * this.matrix[3] - this.matrix[1] * this.matrix[2];
    this.invMatrix[0] = this.matrix[3] / det;
    this.invMatrix[1] = -this.matrix[1] / det;
    this.invMatrix[2] = -this.matrix[2] / det;
    this.invMatrix[3] = this.matrix[0] / det;

    // check for mouse. Do controls and get real position of mouse.
    if (mouse !== undefined) {
      // if there is a mouse get the real canvas coordinates of the mouse
      if (mouse.oldX !== undefined && (mouse.buttonRaw & 4) === 4) {
        // check if panning (middle button)
        const mdx = mouse.x - mouse.oldX; // get the mouse movement
        const mdy = mouse.y - mouse.oldY;
        // get the movement in real space
        const mrx = mdx * this.invMatrix[0] + mdy * this.invMatrix[2];
        const mry = mdx * this.invMatrix[1] + mdy * this.invMatrix[3];

        this.x -= mrx;
        this.y -= mry;
      }
      // do the zoom with mouse wheel
      if (mouse.w !== undefined && mouse.w !== 0) {
        this.ox = mouse.x;
        this.oy = mouse.y;
        this.x = this.mouseX;
        this.y = this.mouseY;
        /* Special note from answer */
        // comment out the following is you change drag and accel
        // and the zoom does not feel right (lagging and not
        // zooming around the mouse
        /*
        this.cox = mouse.x;
        this.coy = mouse.y;
        this.cx = this.mouseX;
        this.cy = this.mouseY;
        */
        if (mouse.w > 0) {
          // zoom in
          if (displayTransform.scale * 1.05 <= maxZoom)
            this.scale *= 1.05;
          mouse.w -= 20;
          if (mouse.w < 0) {
            mouse.w = 0;
          }
        }
        if (mouse.w < 0) {
          // zoom out
          if (displayTransform.scale *  1 / 1.05 >= minZoom)
            this.scale *= 1 / 1.05;
          mouse.w += 20;
          if (mouse.w > 0) {
            mouse.w = 0;
          }
        }
      }
      // get the real mouse position
      const screenX = mouse.x - this.cox;
      const screenY = mouse.y - this.coy;
      this.mouseX =
        this.cx + (screenX * this.invMatrix[0] + screenY * this.invMatrix[2]);
      this.mouseY =
        this.cy + (screenX * this.invMatrix[1] + screenY * this.invMatrix[3]);
      mouse.rx = this.mouseX; // add the coordinates to the mouse. r is for real
      mouse.ry = this.mouseY;
      // save old mouse position
      mouse.oldX = mouse.x;
      mouse.oldY = mouse.y;
    }
  }
};

function drawStars() {
  starHovered = false;
  var rect = canvas.getBoundingClientRect();
  //starImage.addEventListener('load',function() {
  for (let i = 0 ; i < links.length ; i++) {
    ctx.beginPath();
    ctx.moveTo(links[i][0][0],links[i][0][1]);
    ctx.lineTo(links[i][1][0],links[i][1][1]);
    ctx.strokeStyle = "green";
    ctx.stroke();
  }

  for (let i = 0 ; i < n ; i++) {
      if (displayTransform.scale > zoomLimit) {
        ctx.beginPath();
        ctx.rect(X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
        if (ctx.isPointInPath(mouse.x,mouse.y) && !starHovered) {
          starHovered = true;
            ctx.drawImage(hoverStarImage, X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
            if (mouse.oldX !== undefined && (mouse.buttonRaw & 1) === 1) {
              clickingOnStar = true;
              addPanel(0,i,true);
            } else {
              clickingOnStar = false;
            }
        } else {
            ctx.drawImage(starImage, X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
        }
        ctx.textAlign = 'center';
        ctx.fillStyle = "white"
        ctx.fillText(`Système ${i}`,X[i],Y[i]+(starSize/displayTransform.scale)/2);
      }
      else {
          ctx.beginPath();
          ctx.arc(X[i], Y[i], 10, 10, Math.PI, true);
          ctx.fillStyle = "red";
          ctx.fill();
      }
    }
}

function update() {
  topCanvas = -displayTransform.matrix[5] / displayTransform.scale;
  leftCanvas = -displayTransform.matrix[4] / displayTransform.scale;

  // update the transform
  displayTransform.update();
  // set home transform to clear the screem
  displayTransform.setHome();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  // if the image loaded show it
  if (loadedImages == 2) {
    displayTransform.setTransform();
    if(!isLoading){
    drawStars();
    }
  }

  // reaquest next frame
  requestAnimationFrame(update);
}

update(); // start it happening

function setData(jsonMap){
  data = jsonMap;
  isLoading=false;
}
