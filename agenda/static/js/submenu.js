'use strict'

if (document.querySelector('.notification')){

    document.addEventListener('DOMContentLoaded', function(){
        
        const menu = this.querySelector('.notification');

        menu.addEventListener('mouseover', function(){
            const submenu = document.querySelector('.ul_notification');
        
            var ancho_menu = menu.offsetWidth;
        
            submenu.style.width = `${ancho_menu}px`;}
        )
    }

    )

};
