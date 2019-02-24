let width = 600;
let height = 400;
var ship;
var bullets = [];
var invadors = [];
var num_inv = 5;

function setup(){
createCanvas(width, height);
ship = new Ship();
for (var i = 0; i < num_inv; i++){
    invadors.push(new Invador(i * 80 + 40, 50));
}
}

function draw(){
background(50);
invadors.forEach(inv =>{
    inv.show();
    inv.update();
});

invadors.forEach(inv =>{
    if(inv.collision()){
        invadors.forEach(inv =>{
            inv.changeDir();
        });
    }
});

ship.show();
ship.update();
bullets.forEach(b => {
   b.show();
   b.update();
});
}

function keyPressed(){
     if (keyCode === RIGHT_ARROW){
         ship.dir(1);
     }
     if (keyCode === LEFT_ARROW){
         ship.dir(-1);
     }
     if (keyCode == 32){
         bullets.push(new Bullet(ship.x + 10, height + 5));
         console.log(bullets.length);
     }
 }

function keyReleased(){
    if (keyCode !== 32){
        ship.dir(0);
    }
 }