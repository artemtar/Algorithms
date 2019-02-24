let SCL = 20;
let width = 400;
let height = 400;
let RAW = width / SCL;
let COL = height / SCL;
var grid;
var first = 0;
var current;
var visited = []

function setup(){
frameRate(60);
createCanvas(width, height);
grid = new Grid(RAW, COL);
current = grid.g[first];
current.visited = true;
visited.push(current);
createCanvas(width, height); 
}

function draw(){
    background(50);
    fill(250, 0, 100);
    noStroke();
    rect(current.x * SCL, current.y * SCL, SCL, SCL);
    var n = grid.neibours(current);
    grid.show();
    randn = floor(random(0, n.length));
    var next;
    if(n.length > 0){
        next = n[randn];
        grid.removeWalls(current, next);
        current = next; 
        current.visited = true;
        visited.push(current);
    }
    else{
        current = visited.pop();
    }
}