let buttonSubmit = document.getElementById('ajax-test');
if(buttonSubmit!= null){
    buttonSubmit.addEventListener('click', function(){
        let valueToSend = "a=10";
        let target = "localhost:8080/api/user";
        let goal = null;
        ajaxCall(valueToSend, target, goal);
    });
}