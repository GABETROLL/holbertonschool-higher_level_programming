#!/usr/bin/node

const add_item_div = $('DIV#add_item');

add_item_div.click(
    function () {
        $('UL.my_list').append('<li>Item</li>');
    }
);
