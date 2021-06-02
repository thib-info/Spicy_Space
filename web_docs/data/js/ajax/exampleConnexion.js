let buttonSubmit = document.getElementById('ajax-test');
if(buttonSubmit!= null){
    buttonSubmit.addEventListener('click', function(){
        let valueToSend = "a=10";
        let target = "/api/rendu";
        let goal = 100;
        ajaxCall(valueToSend, target, goal);
    });
}

function justeTest(value){
    value = JSON.parse(value);
    console.log(value);
}