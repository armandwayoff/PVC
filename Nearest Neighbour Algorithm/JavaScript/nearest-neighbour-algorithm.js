const NUMBER_VERTICES = 100;
const RAD = 5;

let vertices = [];
let visited_vertices = [0]; // By default, the graph starts with the first vertex
let current_vertex = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(255);
  strokeWeight(RAD / 2);
  textSize(RAD * 2);
  for (let i = 0; i < NUMBER_VERTICES; i++) {
    vertices[i] = new Vertex();
    vertices[i].display();
    text(i, vertices[i].x + RAD * 2, vertices[i].y + RAD * 2);
  }
}

function draw() {
  let record_distance = Infinity;
  let nearest_vertex;
  for (let i = 0; i < vertices.length; i++) {
    if (!visited_vertices.includes(i)) {
      let d = dist(vertices[i].x, vertices[i].y, vertices[current_vertex].x, vertices[current_vertex].y);
      if (d < record_distance) {
        nearest_vertex = i;
        record_distance = d;
      }
    }
  }
  line(vertices[nearest_vertex].x, vertices[nearest_vertex].y, vertices[current_vertex].x, vertices[current_vertex].y);
  visited_vertices.push(nearest_vertex);
  current_vertex = nearest_vertex;

  if (visited_vertices.length == vertices.length) {
    noLoop();
  }
}

class Vertex {
  constructor() {
    this.x = random(width);
    this.y = random(height);
  }

  display() {
    fill(0);
    circle(this.x, this.y, RAD * 2);
  }
}
