#!/usr/nin/node

// Exercise 9: fetch the value of 'hello'
// from the JSON object from this URL:
// https://stefanbohacek.com/hellosalut/?lang=fr,
// and display the value in
// the 'div' tag with its id='hello'.

// This script must also work when linked
// from the <head> tag.

// Courtesy of Liz :)

const hello_div = $('DIV#hello');

function getHello() {
$.ajax({
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  success: function (data) {
    hello.text(data.hello);
  }
});
}

$(document).ready(getHello);
