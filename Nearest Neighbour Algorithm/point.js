class Point {
  constructor() {
    this.x = floor(random(width - espacement));
    this.y = floor(random(height - espacement));
  }

  affichage() {
    fill(0);
    circle(this.x, this.y, rayon);
  }
}
