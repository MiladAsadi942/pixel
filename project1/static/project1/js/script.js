






var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });



  var swipers = new Swiper(".swiper2", {
    slidesPerView: 1,
    spaceBetween: 10,
    
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },

    breakpoints: {
      "@0.00": {
        slidesPerView: 1,
        spaceBetween: 10,
      },
      "@0.75": {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      "@1.00": {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      "@1.50": {
        slidesPerView: 4,
        spaceBetween: 50,
      },
    },
  });

  
  let nav = document.getElementById('navjs');
  let menu = document.getElementById('menu');
  let closee = document.getElementById('close');
  let header = document.getElementById('header');

  let img = document.querySelectorAll('.swiper-slide img');
  let search = document.getElementById('search');
  let input_s = document.getElementById('input-search')
  input_s.style.display = 'none';
  

  
  // menu.addEventListener('click' , function(e){
  //   nav.style.right = "0";
  //   menu.style.display = 'none';
  //   closee.style.display = 'block';
    
  // })

  // closee.addEventListener('click' , function(e){
  //   nav.style.right = "-40%";
  //   closee.style.display = 'none';
  //   menu.style.display = 'block';
    
  // })

  $('.menue').click(function(){
    $('nav').toggle('300');
  })


  $("#search").click(function(){
    $('#input-search').toggle('slow');
  })

//   function wth() {
//     let xx = document.querySelector('.mmm');
    

// 
// xx.innerHTML = x3;
// if(x3 < 700){
//   xx.style.display = 'none';
// }else{
//   xx.style.display = 'block'
// }


//   }


function sized(){
  let bodys = document.querySelector('body').clientWidth;
  if (bodys > 912) {
    menu.style.display = 'none';
    closee.style.display = 'none';
  }else{
    menu.style.display = 'block';
    closee.style.display = 'block';
  }
}


  
  
  



