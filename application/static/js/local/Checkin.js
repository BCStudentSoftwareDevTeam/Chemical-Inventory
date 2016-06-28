function CheckInModal(name,barcode,lastroom,newQuanity,newroom){
   var list = [name,barcode,lastroom,newQuanity,newroom];
   var check = checkValues(list);
   if (check == true) {
     $("#myModal").modal();
     //console.log("opened modal");
   }
}

function checkValues(list){
  for (x = 0; x < list.length; x++){
    var string = list[x];
    var val = document.getElementById(string).value;
    if (val == "" || val == null){
      return false;
    }
  }
  return true;
}