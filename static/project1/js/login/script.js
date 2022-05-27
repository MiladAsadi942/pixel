$('.sign').show(1000)


$('#s-login').click(function(event){
    $('.Login').show(500);
    $('.Login').css('z-index' , '4');
    $('.sign').hide();
    event.preventDefault();
})


$('#l-sign').click(function(event){
    $('.sign').show(500);
    $('.sign').css('z-index' , '4');
    $('.Login').hide();
    event.preventDefault();
})

