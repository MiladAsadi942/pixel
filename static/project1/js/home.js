let red = document.getElementsByClassName('red');
let white = document.getElementsByClassName('white');
let gren = document.getElementsByClassName('gren');
let gray = document.getElementsByClassName('gray');
let img = document.getElementsByClassName('img');

for(let j=0;j<red.length;j++){
    

    red[j].addEventListener('mouseover' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'red'

})



    white[j].addEventListener('mouseover' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'white'
    

})


gren[j].addEventListener('mouseover' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = '#b3ffff'

})

gray[j].addEventListener('mouseover' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = '#f2f2f2'

})






red[j].addEventListener('mouseout' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'white'

})



    white[j].addEventListener('mouseout' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'white'
    

})


gren[j].addEventListener('mouseout' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'white'

})

gray[j].addEventListener('mouseout' , function(){
    img[j].style.transition = 'all 0.5s'
    img[j].style.background = 'white'

})
}

