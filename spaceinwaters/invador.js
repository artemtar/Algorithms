class Invador{
    constructor(_x, _y){
        this.x = _x;
        this.y = _y;
        this.r = 64;
        this.speed = 1;
        this.direction = 1;
    }
    show(){
        stroke(0);
        fill(100, 150, 30, 50);
        ellipse(this.x, this.y, this.r, this.r / 2);
    }
    update(){
        this.x += this.speed * this.direction;
    }
    changeDir(){
        this.direction = this.direction * -1;
        this.y += this.speed * 10;
        // this.x = this.speed * this.direction;
    }
    collision(){
        if(this.x - 40 < 0 || this.x + 40 > width){
           return true;
        }
        else return false;
    }
}