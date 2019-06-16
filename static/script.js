// $( "#arrow" ).click(function() {
//   $(".player#open").fadeOut("slow", function() {
//     $(this).load(function() {
//       $(this).fadeIn( function() {
//         setTimeout(function(){ $(location).attr('href', "/"); }, 1400);
//         $(this).css('cursor', 'progress');
//       });
//     });
//     $(this).attr("src", "static/images/close_player.png");
//   });
// });

$("#mixtape").draggable({
  containment: "window"
});

$(".player").droppable({
  drop: function( event, ui ) {
    $("#mixtape").addClass("disappear", function(){
      $(".player#open").fadeOut("slow", function() {
        // only show closed player after fading out the open one
        $(this).load(function() {
          $(this).fadeIn( function() {
            // only change the page after the closed CD player is displayed
            setTimeout(function(){ $(location).attr('href', "/"); }, 1400);
            $(this).css('cursor', 'progress');
          });
        });
        $(this).attr("src", "static/images/close_player.png");
      });
    });
  }
})