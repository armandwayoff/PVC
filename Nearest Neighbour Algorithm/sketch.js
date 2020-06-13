let p = [];
let i_suppr = [];

let nombre_points = 15;
let bord = 20;
let rayon = 10;
let espacement = rayon;

let i_encours = 0;

let distanceTotale = 0;

let vitesseAffichage = 1;

function setup() {
  createCanvas(600, 600);
  background(255);
  strokeWeight(rayon / 4);
  textSize(rayon * 2);

  for (let i = 0; i < nombre_points; i++) {
    p[i] = new Point();
    p[i].affichage();
    fill("red");
    text(i + 1, p[i].x + espacement, p[i].y + espacement);
    print((i + 1) + " : (" + p[i].x + " ; " + p[i].y + ")");
  }
}

function draw() {
  if (frameCount % vitesseAffichage == 0) {
    calculDistanceMinimale();
  }
  if(i_suppr.length == p.length - 1) {
    print("Distance totale : " + distanceTotale);
    noLoop();
  }
}

function calculDistanceMinimale() {
  let distances = [];

  for (let i = 1; i < p.length; i++) {
    if (!i_suppr.includes(i)) {
      let d = dist(p[i_encours].x, p[i_encours].y, p[i].x, p[i].y);
      distances.push(d);
    }
  }

  for (let i = 1; i < p.length; i++) {
    if (dist(p[i_encours].x, p[i_encours].y, p[i].x, p[i].y) == min(distances)) {
      distanceTotale += min(distances);
      line(p[i_encours].x, p[i_encours].y, p[i].x, p[i].y);
      i_encours = i;
      i_suppr.push(i_encours);
      break;
    }
  }
}
