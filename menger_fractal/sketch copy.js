let width = 400;
let height = 400;
var delta = 0

function setup(){
createCanvas(width, height, WEBGL);

}

function draw(){
background(50);
stroke(255);
// translate(width / 2, height / 2);
rotateX(delta);
box(200);
delta +=  0.01;
}