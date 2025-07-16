
menu = document.querySelector('#menu')

menu_state = false
menu_btn = document.querySelector('#menu_btn').addEventListener('click', ()=>{
    if (menu_state){
        menu.style.top = '100px'
        menu_state = !menu_state
    }else {
        menu.style.top = '-250%'
        menu_state = !menu_state
    }
})