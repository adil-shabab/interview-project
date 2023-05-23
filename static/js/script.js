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