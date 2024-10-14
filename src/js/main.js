import Hero from "./hero.js";

const heroes_content = document.querySelector('#heroes_content');
const league_button = document.querySelector('.header');

const heroes = [];

league_button.addEventListener('click', () => {   
    league_button.style.transform = 'translateY(0px)';
    league_button.style.transition = '2s';
    league_button.style.height = '200px';
    league_button.style.cursor = 'default';
    heroes_content.style.opacity = '100%';
    heroes_content.style.transition = '3s';
});

async function getHeroes(url) {
    const data = await fetch(url);
    if (data.ok) {
        var heroes_json = await data.json();
        for (var hero in heroes_json.data) {
            hero = new Hero(heroes_json.data[hero]);
            heroes.push(hero);
            showHero(hero);
        }
    } else {
        showError();
    };
};

function showHero(hero) {
        heroes_content.innerHTML +=
        `<div class='hero'>
                <div class='name'>${hero.name}</div>
                <div class='info'>
                    <img class='img_hero' id='${hero.id}' src='https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/${hero.image}'>
                    <div class='stat'>
                        <div>Attack: ${hero.attack}</div>
                        <div>Defense: ${hero.defense}</div>
                        <div>Magic: ${hero.magic}</div>
                        <div>Dificulty: ${hero.difficulty}</div>
                    </div>
                </div>
                <div class='title'>${hero.title}</div>
            </div>`;
};

function showError() {
    heroes_content.innerHTML += 
    `<div class='hero' id='error'>error 8(</div>`
};

// parcel no deja usar await fuera del cuerpo de funcion asincrona 8(

async function auxFunc()  {
    await getHeroes('https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion.json');
    document.querySelectorAll(".img_hero").forEach((img) => {   
        img.addEventListener('mouseover', () => {
            img.style.width = '150px';
            img.style.transition = '1s';
        });
        img.addEventListener('mouseout', () => {
            img.style.width = '100px';
            img.style.transition = '50ms';
        })
    });
};

auxFunc();


