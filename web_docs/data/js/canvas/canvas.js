// canvas creation
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var canvasWidth = window.innerWidth;
var canvasHeight = window.innerHeight;
console.log(canvasWidth,canvasHeight);
var topCanvas = 0;
var leftCanvas = 0;
n = 2000;

const starSize = 48;

canvas.width = canvasWidth;
canvas.height = canvasHeight;
//ctx.beginPath();
//ctx.rect(0, 0, canvasWidth, canvasHeight);
//ctx.fillStyle = "#C6B2AF";
//ctx.fill();

var starImage = new Image();
starImage.src = '../data/images/star.png';
//starImage.addEventListener('load', function() {
//  ctx.drawImage(starImage, 50,50);
//}, false);

var X = [], Y = [];
for (let i = 0 ; i < n ; i++) {
  X.push(Math.floor(Math.random() * 10000));
  Y.push(Math.floor(Math.random() * 10000));
}

function drawStars() {
  //starImage.addEventListener('load',function() {
    for (let i = 0 ; i < n ; i++) {
      if (X[i] > leftCanvas && X[i] < leftCanvas + 1000 && Y[i] > topCanvas && Y[i] < topCanvas + 1000) {
        ctx.drawImage(starImage, X[i]-starSize/2 - leftCanvas ,Y[i]-starSize/2 - topCanvas);
      }
    }
  //}, false);
}

setInterval(function(){
  console.log("hello");
  leftCanvas += 3;
  topCanvas += 3;
  ctx.clearRect(0,0,canvasWidth,canvasHeight);
  //ctx.rect(leftCanvas, leftCanvas, 30, 30);
  //ctx.fillStyle = "#FF0000";
  //ctx.fill();
  drawStars();
}, 17);
