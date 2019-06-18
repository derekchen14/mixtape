var song_count = 0;
var music = document.getElementById("player-0");

$( document ).ready(function() {
  $("div.well.id-" + song_count.toString()).show();
});

$("img.forward").click( function(){
  $("div.well.id-" + song_count.toString()).hide();
  music.pause();
  song_count = (song_count+1) % 11;
  $("div.well.id-" + song_count.toString()).show();
});

$("img.backward").click( function(){
  $("div.well.id-" + song_count.toString()).hide();
  music.pause();
  song_count = (song_count == 0) ? 10 : (song_count-1) % 11;
  $("div.well.id-" + song_count.toString()).show();
});


$(".radio").bind("ended", function(){
  $("div.well.id-" + song_count.toString()).hide();
  song_count = (song_count+1) % 11;
  $("div.well.id-" + song_count.toString()).show();

  music = document.getElementById("player-" + song_count.toString());
  music.load();
  music.play();
});
