let points = [];

let X = [];
let Y = [];

let coef = 5;

let M = 50;

function setup() {
  createCanvas(100 * coef, 100 * coef);
}

function draw() {
  background(220);
  for (let i = 0; i < points.length; i++) {
    points[i].display();
  }

  if (points.length >= M) {
    print(X);
    print(Y);
    noLoop();
  }
}

function mousePressed() {
  let new_point = new Point(mouseX, mouseY)
  points.push(new_point);
  X.push(new_point.x / coef);
  Y.push(new_point.y / coef);
}

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  display() {
    fill(0);
    circle(this.x, this.y, 10);
  }
}
