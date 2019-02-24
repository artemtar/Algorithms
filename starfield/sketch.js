let width = 800;
let height = 800;

let starfield = []

function setup(){
createCanvas(width, height);
for (var i = 0; i < 400; i++){
    starfield.push(new Star);
}
}

function draw(){
background(0);
translate(width / 2, height / 2);
for (var i = 0; i < starfield.length; i++){
    starfield[i].show();
    starfield[i].update();
}
}