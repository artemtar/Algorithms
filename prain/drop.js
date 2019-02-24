
class Drop{
    constructor(_x){
        this.x = _x;
        this.y = random(-500, -50);
        this.z = random(0,20);
        this.length = map(this.z, 0, 20, 0, 20);
        this.speedY = map(this.z, 0, 20, 3, 8);
        this.ac = map(this.z, 0, 20, 0.01, 2);
        this.speedX = 0.7;
    }

    show(){
        stroke(250);
        fill(238, 43, 226);
        // thick(3);
        line(this.x, this.y, this.x + this.speedX, this.y + this.length);
        // rect(this.x, this.x + 20, this.x, this.x + 20);
    }

    update(){
        this.y += this.speedY + this.ac;
        this.x += this.speedX
        if(this.y > height){
            this.y = -10;
            this.x = random(-300, width);
        }
    }
}