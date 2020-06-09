let p = [];
const nbrPtn = 20;
const vitesseAffichage = 10;

function setup() {
  createCanvas(750, 550);
  textSize(20);
  for (let i = 0; i < nbrPtn; i++) {
    p[i] = new Point();
  }
}

function draw() {
  background(220);
  comparaison();
}

function comparaison() {
  let nbrInter = 0;

  for (let i = 0; i < p.length; i++) {
    p[i].affichage();
    // noStroke();
    // text(i + 1, p[i].x + 10, p[i].y + 10);
  }

  for (let i = 0; i < p.length - 1; i++) {
    stroke(0);
    strokeWeight(1);
    line(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y);
  }


  if (frameCount % vitesseAffichage == 0) {
    for (let i = 0; i < p.length - 2; i++) {
      for (let j = i + 2; j < p.length - 1; j++) {
        if (i !== j && (i + 1) !== j) {
          let inter = intersection(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y, p[j].x, p[j].y, p[j + 1].x, p[j + 1].y);
          if (inter) {
            swap(p, i + 1, j);
            nbrInter++;
          }
        }
      }
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

class Point {
  constructor() {
    this.x = random(width);
    this.y = random(height);
  }

  affichage() {
    stroke(0);
    strokeWeight(5);
    point(this.x, this.y);
  }
}
