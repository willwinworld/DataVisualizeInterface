$(document).ready(function () {
    $(".list1").hide();
    $(".list2").hide();
   $(".city").click(function(){
       $(".list1").toggle();
   });
   $(".graph").click(function(){
       $(".list2").toggle();
   });
});
