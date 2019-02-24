class Bullet{
    constructor(_x, _y){
        this.x = _x;
        this.y = _y;
        this.r = 8;
        this.speed = 15;
        this.toDelete = false;
    }
    show(){
        stroke(0);
        fill(150, 200, 0);
        ellipse(this.x, this.y, this.r, this.r);
    }
    update(){
        this.y -= this.speed;
    }
    remove(){
        if(this.y < 0){
            this.toDelete = true;
        }
    }
}