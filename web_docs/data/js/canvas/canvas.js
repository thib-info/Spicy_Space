const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;


// loading images
const starImage = new Image();
starImage.addEventListener('load', function() {
  loadedImages += 1;
}, false);
starImage.src ="../data/images/star.png";

const hoverStarImage = new Image();
hoverStarImage.addEventListener('load', function() {
  loadedImages += 1;
}, false);
hoverStarImage.src ="../data/images/hoverStar.png";

var loadedImages = 0
// CONSTANTS
var n = 1000;
var starSize = 48;
var maxZoom = 1, minZoom = 0.05, zoomFactor = 1.05, zoomLimit = 0.3;
var topCanvas, leftCanvas;
var galaxySize = 10000;

var X = [], Y = [];
for (let i = 0 ; i < n ; i++) {
  X.push(Math.floor(Math.random() * galaxySize));
  Y.push(Math.floor(Math.random() * galaxySize));
}

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
    event.preventDefault();
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
  var rect = canvas.getBoundingClientRect();
  //starImage.addEventListener('load',function() {
    for (let i = 0 ; i < n ; i++) {
        if (displayTransform.scale > zoomLimit) {
          ctx.beginPath();
          ctx.rect(X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
          if (ctx.isPointInPath(mouse.x,mouse.y)) {
              ctx.drawImage(hoverStarImage, X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
              if (mouse.oldX !== undefined && (mouse.buttonRaw & 1) === 1)
                addPanel(1,'i',true);
          } else {
              ctx.drawImage(starImage, X[i]-(starSize/displayTransform.scale)/2,Y[i]-(starSize/displayTransform.scale)/2,starSize/displayTransform.scale,starSize/displayTransform.scale);
          }
        }
        else {
            ctx.beginPath();
            ctx.arc(X[i], Y[i], 10, 10, 2 * Math.PI, true);
            ctx.fillStyle = "red";
            ctx.fill();
        }
      }
  //}, false);
}

function update() {
  //console.log(displayTransform.mouseX);
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
    drawStars();
  }

  /*if (mouse.buttonRaw === 4) {
    // right click to return to home
    displayTransform.x = 0;
    displayTransform.y = 0;
    displayTransform.scale = 1;
    displayTransform.rotate = 0;
    displayTransform.ox = 0;
    displayTransform.oy = 0;
  }*/
  // reaquest next frame
  requestAnimationFrame(update);
}

update(); // start it happening
