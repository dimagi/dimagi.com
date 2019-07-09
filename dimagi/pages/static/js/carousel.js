requirejs.config({
  paths: {
    jquery: "lib/jquery/jquery.min",
    lodash: "lib/lodash/lodash.min",
    knockout: "lib/knockout/knockout-latest"
  }
});

require([
  'jquery',
], function (
  $
) {
    'use strict';
    var slideIndex = 1;
    showSlides(slideIndex);

    $('.build').click(function(e) {
      showSlides(slideIndex = 1);
    })
    $('.collect').click(function(e) {
      showSlides(slideIndex = 2);
    })
    $('.analyze').click(function(e) {
      showSlides(slideIndex = 3);
    })
    $('.next').click(function(e) {
      showSlides(slideIndex += 1);
    })
    $('.prev').click(function() {
      showSlides(slideIndex -= 1);
    })

    function showSlides(n) {
      var i;
      var slides = document.getElementsByClassName("slide");
      var slideNumbers = document.getElementsByClassName("slide-number-section");
      var dots = document.getElementsByClassName("dot");
      if (n > slides.length) {slideIndex = 1}    
      if (n < 1) {slideIndex = slides.length}
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
      }
      for (i = 0; i < slideNumbers.length; i++) {
        slideNumbers[i].className = slideNumbers[i].className.replace(" active", "");
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].setAttribute("data-active", false);
      }
      slides[slideIndex-1].style.display = "block";  
      slideNumbers[slideIndex-1].className += " active";
      dots[slideIndex-1].setAttribute("data-active", true);
    }
  }
);
