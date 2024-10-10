import Hero from "./hero.js";

const heroes_content = document.querySelector('#heroes_content');
const league_button = document.querySelector('.header');

const heroes = [];

league_button.addEventListener('click', () => {
    console.log('addEventListener');
    
    league_button.style.transform = 'translateY(0px)';
    league_button.style.transition = '2s';
    league_button.style.height = '200px';
    heroes_content.style.opacity = '100%';
    heroes_content.style.transition = '3s';
});

async function getHeroes(url) {
    console.log('getHeroes');
    const data = await fetch(url);
    if (data.ok) {
        var heroes_json = await data.json();
        for (var hero in heroes_json.data) {
            hero = new Hero(heroes_json.data[hero]);
            heroes.push(hero);
        }
    } else {
        showError();
    };
    console.log('getHeroesEND');
};

async function showHeroes(heroes_list) {
    console.log('showHeroes');
    await getHeroes('https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion.json');
    heroes_list.forEach((hero) => {
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
        }
    )
    console.log('showHeroesEND');
}
showHeroes(heroes);

document.querySelectorAll(".img_hero").forEach((img) => {
    img.addEventListener('mouseover', () => {
        img.style.width = '150px';
        img.style.transition = '1s';
    });
    img.addEventListener('mouseout', () => {
        img.style.width = '100px';
        img.style.transition = '50ms';
    })
})

function showError() {
    heroes_content.innerHTML += 
    `<div class='hero' id='error'>error 8(</div>`
};

