function showSideMenu(){
    document.getElementById("Show-nav").style.display="block";
}
function hideSideNav(){
    document.getElementById("Show-nav").style.display="none";
}

// Owl-Carousel------
$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        items:5,
        autoplay:true,
        loop:true,
        autoplayHoverPause:true,
        center:true
    });
  });