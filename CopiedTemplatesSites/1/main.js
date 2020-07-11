
$(function (){
    $('.tap_menu').click(function tap(){
        $('.tap_menu_ExiteBlock').css('display','block');
        $('.tap_menu_block').css('width','250px');
    });

    $('.tap_menu_ExiteBlock').click(function(){
        $('.tap_menu_ExiteBlock').css('display','none');
        $('.tap_menu_block').css('width','0');
    });

    
});


