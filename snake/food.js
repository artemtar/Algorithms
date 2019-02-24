class Food{
    constructor(){
        var loc = this.picklocation();
        this.x = loc[0];
        this.y = loc[1];
        this.newColor();
    }
    
    show(){
        stroke(0)
        fill(this.c);
        rect(this.x, this.y, scl, scl);
    }

    update(){
        var loc = this.picklocation();
        this.x = loc[0];
        this.y = loc[1];
        this.newColor();
    }

    newColor(){
        this.c = [random(255), random(255), random(255)];
    }
    
    picklocation(){
    var posX = floor(random(width) / scl);
    var posY = floor(random(height) / scl);
    return [posX * scl, posY * scl];
}
}