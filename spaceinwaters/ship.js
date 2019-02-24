class Ship{
    constructor(){
    this.x = width / 2;
    this.direction = 0;
    this.speed = 5;
    
    }
    show(){
        stroke(0)
        fill(200, 150, 50);
        rect(this.x, height - 45, 20, 40);
    }
    update(){
        this.x += this.direction * this.speed;
    }
    dir(_d){
        this.direction = _d;
    }
}