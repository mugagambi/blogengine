  $('body').scrollspy({
      target: '.navbar-fixed-top'
  });
  $('.navbar-collapse ul li a').click(function(event) {
      $('.navbar-toggle:visible').click();
  });