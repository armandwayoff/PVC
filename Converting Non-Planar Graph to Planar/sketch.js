let p = [];
let originalP = [];
let o = [];
const nbrPtn = 5;
const vitesseAffichage = 20;
const bord = 20;
const rayon = 10;

let iter = 0;

function setup() {
  createCanvas(750, 550);
  textSize(20);
  // p[0] = new Point();
  // for (let i = 1; i < nbrPtn; i++) {
  //   let newPoint = new Point();
  //   if (!overlay(newPoint, p)) {
  //     p[i] = newPoint;
  //   }
  //   originalP.push(i);
  // }
  for (let i = 0; i < nbrPtn; i++) {
    p[i] = new Point();
    originalP.push(i);
  }
  o = [...p];
}

function draw() {
  background(255);

  for (let i = 0; i < p.length; i++) {
    p[i].affichage();
    noStroke();
    text(i + 1, o[i].x + 10, o[i].y + 10);
  }

  for (let i = 0; i < p.length - 1; i++) {
    stroke(0);
    strokeWeight(2);
    line(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y);
  }
  
  if (iter == 0) {
   // saveCanvas();
  }
  
  iter = 1;
  
  comparaison();
}

function comparaison() {
  let nbrInter = 0;

  if (frameCount % vitesseAffichage == 0) {
    for (let i = 0; i < p.length - 2; i++) {
      for (let j = i + 2; j < p.length - 1; j++) {
        if (i !== j && (i + 1) !== j) {
          let inter = intersection(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y, p[j].x, p[j].y, p[j + 1].x, p[j + 1].y);
          if (inter) {
            swap(p, i + 1, j);
            swap(originalP, i + 1, j);
            nbrInter++;
          }
        }
      }
    }
    if (nbrInter == 0) {
      adjacencyMatrix(originalP);
      noLoop();
    }
  }
}

function swap(a, i, j) {
  let copie = a[i];
  a[i] = a[j];
  a[j] = copie;
}

function intersection(a, b, c, d, p, q, r, s) {
  var det, gamma, lambda;
  det = (c - a) * (s - q) - (r - p) * (d - b);
  if (det === 0) {
    return false;
  } else {
    lambda = ((s - q) * (r - a) + (p - r) * (s - b)) / det;
    gamma = ((b - d) * (r - a) + (c - a) * (s - b)) / det;
    return (0 < lambda && lambda < 1) && (0 < gamma && gamma < 1);
  }
}

function adjacencyMatrix(arr) {
  let matrix = [];
  for (let i = 0; i < arr.length; i++) {
    matrix.push([]);
    for (let j = 0; j < arr.length; j++) {
      matrix[i].push(0);
    }
  }

  for (let i = 0; i < arr.length - 1; i++) {
    matrix[arr[i]][arr[i + 1]] = 1;
    matrix[arr[i + 1]][arr[i]] = 1;
  }

  for (let i = 0; i < arr.length; i++) {
    print(matrix[i]);
  }
}


// function overlay(obj, list) {
//   const minDistBetweenVertices = rayon * 3;
//   for (let i = 0; i < list.length; i++) {
//     if (dist(obj.x, obj.y, list[i].x, list[i].y) <= minDistBetweenVertices) {
//       return true;
//     }
//   }
//   return false;
// }

class Point {
  constructor() {
    this.x = random(bord + rayon, width - rayon - bord);
    this.y = random(bord + rayon, height - rayon - bord);
  }

  affichage() {
    stroke(0);
    strokeWeight(rayon);
    point(this.x, this.y);
  }
}
