function drawBg(cw,ch) {
  ctx.clearRect(0, 0, cw, ch);
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, cw, ch);
}

function systemPrev(canvasId) {
  const canvas = document.getElementById(canvasId);
  const ctx = canvas.getContext("2d");

  const cw = canvas.width;
  const ch = canvas.height;

  ctx.strokeStyle = "white"; // color of orbits

  const canvasPercentage = canvas.width / 100 / 2;
  drawBg(cw,ch);
  var key = sha256(canvasId);
  var usedSurface = 0; // when it reaches 100, stop plotting.
  var index = 0;

  // drawing star
  var starColor = parseInt(key[index]);
  if (starColor < 6) {
    ctx.fillStyle = "#fe2e00"; // red
  } else if (starColor < 8) { // orange
    ctx.fillStyle = "#ff6700";
  } else if (starColor < 9) { // white
    ctx.fillStyle = "#fff7c8";
  } else { // blue
    ctx.fillStyle = "#a4c4ff";
  }
  index += 1;
  while (parseInt(key[index]) < 2) {
    index += 1;
  }
  ctx.beginPath();
  ctx.arc(cw/2,ch/2,parseInt(key[index]) * canvasPercentage, 0, 2*Math.PI, false);
  ctx.fill();
  usedSurface += parseInt(key[index]);
  //console.log(`usedSurface : ${usedSurface}`);
  index += 1;


  var planetSpace = 0, planetColor = 0, planelSize = 0, planetPosition = 0, planetSizeMultiplier, isTelluric;
  // drawing planets

  while (true) {
    if (usedSurface < 60) {
      planetSizeMultiplier = 0.5;
      isTelluric = true;
    } else {
      planetSizeMultiplier = 1;
      isTelluric = false;
    }
    // planet space
    while (parseInt(key[index]) < 5) {
      index += 1;
    }
    planetSpace = 2*parseInt(key[index]);
    //console.log(`planetSpace : ${planetSpace}`);
    index += 1;

    // planet size
    while (parseInt(key[index]) < 5) {
      index += 1;
    }
    planetSize = planetSizeMultiplier * parseInt(key[index]);
    //console.log(typeof planelSize);
    //console.log(`planetSize : ${planetSize}`);
    index += 1;

    planetPosition = parseInt(key[index] + key[index + 1]);
    //console.log(`planetPosition : ${planetPosition}`);
    index += 2;

    // planet color
    planetColor = parseInt(key[index]);
    //console.log(`planetColor : ${planetColor}`);
    if (isTelluric) {
      if (planetColor == 0) {
        ctx.fillStyle = "#579ED4"; // blue
      } else if (planetColor < 4) {
        ctx.fillStyle = "#e87347"; // red
      } else if (planetColor < 7) {
        ctx.fillStyle = "#fbd79e"; // yellow
      } else {
        ctx.fillStyle = "#a9a8a8"; // grey
      }
    } else {
      if (planetColor < 3) {
        ctx.fillStyle = "#3a60c1"; // blue
      } else if (planetColor < 6) {
        ctx.fillStyle = "#acdee6"; // light blue
      } else {
        ctx.fillStyle = "#f3c158"; // yellow
      }
    }

    index += 1;

    if (usedSurface + 2*planelSize + planetSpace > 100) {
      break;
    } else {

      // first draw orbit
      ctx.beginPath();
      ctx.arc(cw/2,ch/2,(usedSurface + planetSpace) * canvasPercentage, 0, 2*Math.PI, false);
      ctx.stroke();

      // then draw planet
      ctx.beginPath();
      ctx.arc(cw/2 + (usedSurface + planetSpace + planelSize) * canvasPercentage * Math.cos(Math.PI/50 * planetPosition),ch/2 + (usedSurface + planetSpace + planelSize) * canvasPercentage * Math.sin(Math.PI/50 * planetPosition), planetSize * canvasPercentage, 0, 2*Math.PI, false);
      //ctx.arc(cw/2 + (usedSurface + planetSpace + planelSize) * canvasPercentage, ch/2 + (usedSurface + planetSpace + planelSize) * canvasPercentage, planetSize * canvasPercentage, 0, 2*Math.PI, false);
      ctx.fill();

      // then update usedSurface
      usedSurface = usedSurface + planetSize + planetSpace*2;
      //console.log(`planetSize : ${planetSize}`);
      //console.log(`planetSpace : ${planetSpace}`);
      //console.log(`usedSurface : ${usedSurface}`);
    }
  }

}

var sha256 = function sha256(ascii) {
    function rightRotate(value, amount) {
        return (value>>>amount) | (value<<(32 - amount));
    };

    var mathPow = Math.pow;
    var maxWord = mathPow(2, 32);
    var lengthProperty = 'length'
    var i, j; // Used as a counter across the whole file
    var result = ''

    var words = [];
    var asciiBitLength = ascii[lengthProperty]*8;

    //* caching results is optional - remove/add slash from front of this line to toggle
    // Initial hash value: first 32 bits of the fractional parts of the square roots of the first 8 primes
    // (we actually calculate the first 64, but extra values are just ignored)
    var hash = sha256.h = sha256.h || [];
    // Round constants: first 32 bits of the fractional parts of the cube roots of the first 64 primes
    var k = sha256.k = sha256.k || [];
    var primeCounter = k[lengthProperty];
    /*/
    var hash = [], k = [];
    var primeCounter = 0;
    //*/

    var isComposite = {};
    for (var candidate = 2; primeCounter < 64; candidate++) {
        if (!isComposite[candidate]) {
            for (i = 0; i < 313; i += candidate) {
                isComposite[i] = candidate;
            }
            hash[primeCounter] = (mathPow(candidate, .5)*maxWord)|0;
            k[primeCounter++] = (mathPow(candidate, 1/3)*maxWord)|0;
        }
    }

    ascii += '\x80' // Append Ƈ' bit (plus zero padding)
    while (ascii[lengthProperty]%64 - 56) ascii += '\x00' // More zero padding
    for (i = 0; i < ascii[lengthProperty]; i++) {
        j = ascii.charCodeAt(i);
        if (j>>8) return; // ASCII check: only accept characters in range 0-255
        words[i>>2] |= j << ((3 - i)%4)*8;
    }
    words[words[lengthProperty]] = ((asciiBitLength/maxWord)|0);
    words[words[lengthProperty]] = (asciiBitLength)

    // process each chunk
    for (j = 0; j < words[lengthProperty];) {
        var w = words.slice(j, j += 16); // The message is expanded into 64 words as part of the iteration
        var oldHash = hash;
        // This is now the undefinedworking hash", often labelled as variables a...g
        // (we have to truncate as well, otherwise extra entries at the end accumulate
        hash = hash.slice(0, 8);

        for (i = 0; i < 64; i++) {
            var i2 = i + j;
            // Expand the message into 64 words
            // Used below if
            var w15 = w[i - 15], w2 = w[i - 2];

            // Iterate
            var a = hash[0], e = hash[4];
            var temp1 = hash[7]
                + (rightRotate(e, 6) ^ rightRotate(e, 11) ^ rightRotate(e, 25)) // S1
                + ((e&hash[5])^((~e)&hash[6])) // ch
                + k[i]
                // Expand the message schedule if needed
                + (w[i] = (i < 16) ? w[i] : (
                        w[i - 16]
                        + (rightRotate(w15, 7) ^ rightRotate(w15, 18) ^ (w15>>>3)) // s0
                        + w[i - 7]
                        + (rightRotate(w2, 17) ^ rightRotate(w2, 19) ^ (w2>>>10)) // s1
                    )|0
                );
            // This is only used once, so *could* be moved below, but it only saves 4 bytes and makes things unreadble
            var temp2 = (rightRotate(a, 2) ^ rightRotate(a, 13) ^ rightRotate(a, 22)) // S0
                + ((a&hash[1])^(a&hash[2])^(hash[1]&hash[2])); // maj

            hash = [(temp1 + temp2)|0].concat(hash); // We don't bother trimming off the extra ones, they're harmless as long as we're truncating when we do the slice()
            hash[4] = (hash[4] + temp1)|0;
        }

        for (i = 0; i < 8; i++) {
            hash[i] = (hash[i] + oldHash[i])|0;
        }
    }

    for (i = 0; i < 8; i++) {
        for (j = 3; j + 1; j--) {
            var b = (hash[i]>>(j*8))&255;
            result += ((b < 16) ? 0 : '') + b.toString(16);
        }
    }
    return result.replace(/\D+/g, '');
};
