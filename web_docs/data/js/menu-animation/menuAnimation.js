const containerMenu = document.querySelector('.container-menu');
const btnMenu = document.querySelector('.btn-menu');

btnMenu.addEventListener('click', function(){
    containerMenu.classList.toggle('active');

    //visibleName();
});

function visibleName(){
    let names = document.getElementsByClassName('name-item');
    for(var i=0; i<names.length; i++) {
        let name = names[i];
        let classes = name.className;
        if (classes.includes('visible')) {
            name.classList.remove("visible");
            name.classList.add("hidden");
        } else {
            name.classList.remove("hidden");
            name.classList.add("visible");
        }
    }
}