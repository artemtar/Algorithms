var n = 0;
class Snake{
    constructor(){
        this.speedX = 1;
        this.speedY = 0;
        this.lastX = 0;
        this.lastY = 0;
        this.lastXX = 0;
        this.lastYY = 0;
        this.tottal = 1;
        this.tail = [];
        var head = new Segment(width / 2, height / 2);
        this.tail.push(head);
    }
    update(){
        this.lastYY = this.lastY;
        this.lastXX = this.lastX;
        this.lastX = this.tail[this.tottal - 1].x;
        this.lastY = this.tail[this.tottal - 1].y;
        var head = new Segment(this.speedX * scl + this.tail[0].x,
             this.speedY * scl + this.tail[0].y)
        for(var i = this.tottal - 1; i > 0; i--){
            this.tail[i].update(this.tail[i - 1].x, this.tail[i - 1].y);
        }       
        this.tail[0] = head;
    }
    show(){
        this.tail.forEach(e => {
            e.show();
        });
    }
    direction(_x, _y){
        this.speedX = _x;
        this.speedY = _y;
    }
    eat(food){
        var d = dist(this.tail[0].x, this.tail[0].y, food.x, food.y);
        return d < 1;
    }
    grow(food){
       this.tottal++;
       var body = new Segment (this.lastX, this.lastY);
       body.setColor(food.c);
       this.tail.push(body);
       this.lastX = this.lastXX;
       this.lastY = this.lastYY;
    }
    collision(){
        var head = this.tail[0];
        var collision = false;
        for(var i = 0; i < this.tail.length; i++){
            var d = dist(head.x, head.y, this.tail[i].x, this.tail[i].y);
            if (d < 1){ collision = true; }
        }
        return collision;
    }

}

class Segment{
    constructor(_x, _y){
        this.x = _x;
        this.y = _y;
        this.c = color(random(255), random(255), random(255));
    }
    update(_x, _y){
        this.x = _x;
        this.y = _y;
    }
    show(){
        fill(this.c);
        stroke(0)
        rect(this.x, this.y, scl, scl);
    }
    setColor(_c){
        this.c = _c
    }
}