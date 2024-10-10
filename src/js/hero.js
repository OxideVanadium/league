export default class Hero{
    constructor(data){
        this.name = data.name;
        this.title = data.title;
        this.image = data.image.full;
        this.attack = data.info.attack;
        this.defense = data.info.defense;
        this.magic = data.info.magic;
        this.difficulty = data.info.difficulty;
        this.partype = data.partype;
        this.id = data.id;
    }
}