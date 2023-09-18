document.getElementById('add_item').addEventListener('click', function(){
    var element = document.createElement('li');
    
    element.textContent = "Item";

    document.querySelector('.my_list').appendChild(element)
})