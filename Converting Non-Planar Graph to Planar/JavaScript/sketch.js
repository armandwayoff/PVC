let p = [];
let o = [];
const nbrPtn = 20;
const vitesseAffichage = 20;
const bord = 20;
const rayon = 20;

function setup() {
  createCanvas(windowWidth, windowHeight);
  textSize(rayon);
  for (let i = 0; i < nbrPtn; i++) {
    p[i] = new Point();
  }
  o = [...p];
}

function draw() {
  background(255);
  let nbrInter = 0;

  if (frameCount % vitesseAffichage == 0) {
    for (let i = 0; i < p.length - 2; i++) {
      for (let j = i + 2; j < p.length - 1; j++) {
        if (i !== j && (i + 1) !== j) {
          let inter = intersection(p[i], p[i + 1], p[j], p[j + 1]);
          if (inter) {
            [p[i + 1], p[j]] = [p[j], p[i + 1]];
            nbrInter++;
          }
        }
      }
    }
    if (nbrInter == 0) {
      print("Done");
      noLoop();
    }
  }

  for (let i = 0; i < p.length; i++) {
    p[i].affichage();
    noStroke();
    fill("red");
    text(i, o[i].x + rayon / 2, o[i].y + rayon);
  }

  for (let i = 0; i < p.length - 1; i++) {
    stroke(0);
    strokeWeight(rayon / 5);
    line(p[i].x, p[i].y, p[i + 1].x, p[i + 1].y);
  }

}

function intersection(p1, p2, q1, q2) {
  let det = (p2.x - p1.x) * (q2.y - q1.y) - (q2.x - q1.x) * (p2.y - p1.y);
  if (det == 0) {
    return false
  } else {
    let lambda = ((q2.y - q1.y) * (q2.x - p1.x) + (q1.x - q2.x) * (q2.y - p1.y)) / det;
    let gamma = ((p1.y - p2.y) * (q2.x - p1.x) + (p2.x - p1.x) * (q2.y - p1.y)) / det;
    return (0 < lambda && lambda < 1) && (0 < gamma && gamma < 1);
  }
}

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
