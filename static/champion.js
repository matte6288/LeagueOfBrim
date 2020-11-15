
$(document).ready(function(){
  $('.championMasteryImage').click(function () {
    var clicks = $(this).data('clicks');
    var $this = $(this);
    var num = $this.attr('id')
    var LoadingArt = LoadingArt0;
    var ChampArt = ChampArt0;
    var ChampMas = ChampMas0;
    if($this.hasClass('stalled')){
      return false;
    }
    if (num==1){
      LoadingArt=LoadingArt1;
      ChampArt=ChampArt1;
      ChampMas = ChampMas1;

    }
    else if (num==2){
      LoadingArt=LoadingArt2;
      ChampArt=ChampArt2;
      ChampMas = ChampMas2;
    }
    else if (num==3){
      LoadingArt=LoadingArt3;
      ChampArt=ChampArt3;
      ChampMas = ChampMas3;
    }
    else if (num==4){
      LoadingArt=LoadingArt4;
      ChampArt=ChampArt4;
      ChampMas = ChampMas4;
    }
    if (clicks) {
      // odd clicks
      $this.html("<div class='' align='center'><img src="+LoadingArt+" alt='Champ0' class='cmi'></div>");
      $this.removeClass('col-md-6').addClass('col-md-2');
      $this.siblings('.championMasteryImage').removeClass('col-md-1').addClass('col-md-2').removeClass('stalled');
    }else{
      // even clicks
      $this.html("<div class='' align='center'><img src="+ChampArt+" alt='Champ0' class='cmi'><img src="+ChampMas+" alt='' class=''></div>");
      $this.removeClass('col-md-2').addClass('col-md-6');
      $this.siblings('.championMasteryImage').removeClass('col-md-2').addClass('col-md-1').addClass('stalled');
   }
   $(this).data("clicks", !clicks);
  });
});

