#!/usr/bin/node

// Exercise 6:
// Update the HTML 'header' tag's content with
// 'New Header!!!', using JQuery.

const update_header_div = $('DIV#update_header');

update_header_div.click(
    function () {
        $('header').html('New Header!!!');
    }
);
