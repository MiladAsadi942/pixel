$('.top-img').mouseenter(function(){
    $(this).find('.more').show(500);
})

$('.top-img').mouseleave(function(){
    $(this).find('.more').hide(200);
})



$(window).scroll(function(){
    if ($(window).scrollTop() > 150) {
       
        

      $('header').addClass('top');
     }

     else if($(window).scrollTop() < 130){
        $('header').removeClass('top');
     }
     
  });


  $('.menu').click(function(){
      $('nav').toggle(300);
  })

