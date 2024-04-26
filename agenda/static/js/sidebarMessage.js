'use strict'

const individual_message = document.querySelector('#individual_message');
const sidebar = document.querySelector("#sidebar");

var ancho_mensaje = individual_message.offsetWidth;

sidebar.style.width = ancho_mensaje + 'px';