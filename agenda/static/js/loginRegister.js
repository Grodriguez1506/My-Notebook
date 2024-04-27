'use strict'

const registerButton = document.querySelector('.to_register');
const loginButton = document.querySelector('.to_login');
const registerForm = document.querySelector('.register_form');
const loginForm = document.querySelector('.login_form');
const registerImg = document.querySelector('.register_img');
const loginImg = document.querySelector('.login_img');

function showRegister(){
    registerForm.style.transition = 'all 500ms';
    registerForm.style.transform = 'translateX(0%)';
    registerImg.style.transition = 'all 500ms';
    registerImg.style.transform = 'translateX(0%)';
}

function hideRegister(){
    registerForm.style.transition = 'all 500ms';
    registerForm.style.transform = 'translateX(-100%)';
    registerImg.style.transition = 'all 500ms';
    registerImg.style.transform = 'translateX(120%)';
}

function hideLogin(){
    loginForm.style.transition = 'all 500ms';
    loginForm.style.transform = 'translateY(-100%)';
    loginImg.style.transition = 'all 500ms';
    loginImg.style.transform = 'translateY(160%)';
}

function showLogin(){
    loginForm.style.transition = 'all 500ms';
    loginForm.style.transform = 'translateY(0%)';
    loginImg.style.transition = 'all 500ms';
    loginImg.style.transform = 'translateY(-20%)';
}

registerButton.addEventListener('click', function(){
    hideLogin();
    setTimeout(function(){
        showRegister();
    },200);
})

loginButton.addEventListener('click', function(){
    hideRegister();
    setTimeout(function(){
        showLogin();
    },200);
})