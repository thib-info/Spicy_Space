const containerMenu = document.querySelector('.container-menu');
const btnMenu = document.querySelector('.btn-menu');

btnMenu.addEventListener('click', function(){
    containerMenu.classList.toggle('active');
});

const itemsMenu = document.getElementsByClassName('menu-item');
for(const item of itemsMenu){
    item.addEventListener('click', function(element){
        let idElement = element.target.parentElement.id;
        setWindow(idElement);
    });
}

function setWindow(idElement){
    if(idElement==='statistique')
        addWindow(3);
    else if(idElement==='diplomatie')
        addWindow(1);
    else if(idElement==='arbre-tech') {
        addWindow(4);
    }
}