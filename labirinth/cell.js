class Cell{
    constructor(_x, _y){
        this.x = _x;
        this.y = _y;
        this.visited = false;
        this.walls = [true, true, true, true];
    }

    show(){
        stroke(255);
        var posX = this.x * SCL;
        var posY = this.y * SCL;

        if(this.walls[0] == true){
            line(posX,       posY,       posX + SCL, posY);
        }
        if(this.walls[1] == true){
            line(posX + SCL, posY + SCL, posX + SCL, posY + SCL);
        }
        if(this.walls[2] == true){
            line(posX,       posY + SCL, posX + SCL, posY + SCL);
        }
        if(this.walls[3] == true){
            line(posX,       posY,       posX,       posY + SCL);
        }

        if(this.visited){
            fill(150, 0, 150, 100);
            noStroke();
            rect(posX, posY, SCL, SCL);
        }
    }
}

class Grid{
    constructor(raw, col){
        this.g = [];
        this.next = 0;
        for(var i = 0; i < raw; i++){
            for(var j = 0; j < col; j++){
                this.g.push(new Cell(i, j));
            }
        }
    }
    show(){
        this.g.forEach(c =>{
            c.show();
        })
    }
    index(i, j){
        if (i >= RAW || i < 0 || j >= COL || j < 0){
            return -1;
        }
        else{
            return i * RAW + j;
        }
    }
    neibours(cell){
        var n = [];
        var t = this.g[this.index(cell.x,     cell.y - 1)];
        var r = this.g[this.index(cell.x + 1, cell.y)];
        var b = this.g[this.index(cell.x,     cell.y + 1)];
        var l = this.g[this.index(cell.x - 1, cell.y)];
        if(t && !t.visited){
            n.push(t);
        }
        if(r && !r.visited){
            n.push(r);
        }
        if(b && !b.visited){
            n.push(b);
        }
        if(l && !l.visited){
            n.push(l);
        }
        return n;
    }
    removeWalls(c1, c2){
        if (c1.x - c2.x == -1){
            c1.walls[1] = false;
            c2.walls[3] = false;
        }
        if (c1.x - c2.x == 1){
            c1.walls[3] = false;
            c2.walls[1] = false;
        }
        if (c1.y - c2.y == -1){
            c1.walls[2] = false;
            c2.walls[0] = false;
        }
        if (c1.y - c2.y == 1){
            c1.walls[0] = false;
            c2.walls[2] = false;
        }
    }

}