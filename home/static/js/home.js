
menu = document.querySelector('#menu')

menu_state = true
menu_btn = document.querySelector('#menu_btn').addEventListener('click', ()=>{
    if (menu_state){
        menu.style.top = '100px'
        menu_state = !menu_state
    }else {
        menu.style.top = '-300%'
        menu_state = !menu_state
    }
})