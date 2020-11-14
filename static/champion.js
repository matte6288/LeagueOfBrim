$(document).ready(function(){
  $('.championMasteryImage').hover(function () {
    var $this = $(this);
    $this.removeClass('col-md-2').addClass('col-md-10');
    $this.siblings('.col-md-2').hide();
  }, function () {
  var $this = $(this);
    $this.removeClass('col-md-10').addClass('col-md-2');
    $this.siblings('.col-md-2').show();
  });
});