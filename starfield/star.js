let speed = 15;
let dividor = 8;
let boxx = width / dividor;
let boxy = height / dividor;

class Star{

    constructor(){
       this.x = random(- width / 2, width / 2);
       this.y = random(- height / 2, height / 2);      
       this.z = random(0, width);
       this.mult = random(0, 2.5);
       this.pz = this.z;
    } 

    show(){
        fill(200);
        noStroke();
        var xs = map(this.x / this.z, 0, 1, 0, width)
        var ys = map(this.y / this.z, 0, 1, 0, height)
        // print(this.x > boxx * 2 && this.x < boxx * 3);
        if( this.x > 0 && this.x > dividor * 0.4 * boxx &&
            this.y > 0 && this.y > dividor * 0.4 * boxy &&
            this.x > 0 && this.x < dividor * 0.5 * boxx &&
            this.y > 0 && this.y < dividor * 0.5 * boxy)
            {
            var d = map(this.z, width, 1,  0, 50) * this.mult;
            }
        else if
           (this.x > 0 && this.x > dividor * 0.3 * boxx &&
            this.y > 0 && this.y > dividor * 0.3 * boxy &&
            this.x > 0 && this.x < dividor * 0.7 * boxx &&
            this.y > 0 && this.y < dividor * 0.7 * boxy)
            {
            var d = map(this.z, width, 1,  0, 30) * this.mult;
            }
        else{
            var d = map(this.z, width, 1,  0, 12) * this.mult;
            }
        var px = map(this.x / this.pz, 0, 1, 0, width);
        var py = map(this.y / this.pz, 0, 1, 0, height);
        stroke(50);
        line(px, py, xs, ys);
        ellipse(xs, ys, d, d);


        
        
        // px - map(xs, 0, width, 100, 0),
        //     py - map(ys, 0, height, 100, 0));
    }

    update(){
        this.z -= speed;
        if (this.z < 1){
           this.z = width;
           this.pz = this.z;
           this.mult = random(0, 2.5);
           this.x = random(- width / 2, width / 2);
           this.y = random(- height / 2, height / 2);   
        }
    }
}