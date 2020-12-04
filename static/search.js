
$(document).ready(function() {
    fade1();
    setTimeout(fade2, 3000);
});

function fade1(){
    $('.title').animate({'opacity':'1'},3500);
}

function fade2(){
    $('.search').animate({'opacity':'1'},3500);
}