let width = 1000;
let height = 1000;
let drops = [];

function setup(){
createCanvas(width, height);
    for(var i = 0; i < 800; i++){
        drops.push(new Drop(random(-300, width)));
    }
}

function draw(){
background(50);
drops.forEach(drop => {
    drop.update();
    drop.show();
});

}