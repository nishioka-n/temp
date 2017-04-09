$('td').click(function(){
  if ($(this).attr('bg') && $(this).attr('bg').length > 0){
    $(this).css('background', $(this).attr('bg'));
    $(this).removeAttr('bg');
  } else {
    $(this).attr('bg', $(this).css('background'));
    $(this).css('background','lightblue');
  }
});void(0);