let password_input = document.querySelectorAll('.input_div.password')
if(password_input!=null){
    password_input.forEach((item)=>item.querySelector('i').addEventListener('click', function(){
        if(item.querySelector('input').type === 'password'){
            item.querySelector('i').classList.remove('fa-eye')
            item.querySelector('i').classList.add('fa-eye-slash')
            item.querySelector('input').type = 'text'
        }else{
            item.querySelector('i').classList.remove('fa-eye-slash')
            item.querySelector('i').classList.add('fa-eye')
            item.querySelector('input').type = 'password'
        }
    }))
}



function myFunction() {
    var input, filter, parent, childs, name, i, txtValue;
    input = document.getElementById("search__input");
    filter = input.value.toUpperCase();
    parent = document.querySelectorAll(".parent_product");
    childs = document.querySelectorAll(".each-product");
      
    for (i = 0; i < childs.length; i++) {
        name = childs[i].querySelector('.name');
        txtValue = name.textContent || name.innerText;
        
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            childs[i].style.display = "";
        } else {
            childs[i].style.display = "none";
        }
    }
}


if(document.getElementById('search__input') != null){
  document.getElementById('search__input').addEventListener('input', myFunction)
}