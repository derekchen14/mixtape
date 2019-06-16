var song_count = 0;

$( document ).ready(function() {
  $("div.well.id-" + song_count.toString()).show();
});

$("h1").click( function(){
  $("div.well.id-" + song_count.toString()).hide();
  song_count = (song_count+1) % 11;
  $("div.well.id-" + song_count.toString()).show();
});