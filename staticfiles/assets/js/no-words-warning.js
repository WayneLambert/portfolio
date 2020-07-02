function IsEmpty(){
  if(document.forms['frm'].fulltext.value === "")
{
    document.getElementById('no-words-msgbox').innerHTML =
      "ATTENTION: Please enter some text in the box above, then click the 'Analyse' button.";
  return false;
}
  return true;
}
