function character_count() {
  var total=document.getElementById("id_post_title").value;
  document.getElementById("title-length").innerHTML="Title Length: "+total.length+"/60";
};
