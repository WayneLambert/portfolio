function IsEmpty(){
  if(document.forms['frm'].fulltext.value === "")
{
    document.getElementById('no-words-msgbox').innerHTML =
      "Please enter some text in the box above, then click the 'Count Words' button.";
  return false;
}
  return true;
}
