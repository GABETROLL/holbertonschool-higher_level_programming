#!/usr/bin/node

const toggle_header = $('DIV#toggle_header');

toggle_header.addClass('red');
// The header had no class to begin with,
// so I added the red one first.

toggle_header.click(
    function () {
        toggle_header.toggleClass('red');
        toggle_header.toggleClass('green');
    }
);
