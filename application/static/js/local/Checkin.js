function CheckInModal(name,barcode,lastroom,newQuanity,newroom){
   var list = [name,barcode,lastroom,newQuanity,newroom];
   var check = checkValues(list);
   if (check == true) {
     $("#myModal").modal();
     
     
   }
   showModal()
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
 function print(name,barcode,lastroom,newQuanity,newroom){
     var Name = document.getElementById(name).textContent;
     var Barcode = document.getElementById(barcode).textContent;
     var Lastroom = document.getElementById(lastroom).textContent;
     var Quanity = document.getElementById(newQuanity).textContent;
      $('.share_list_popup ul').append(Name);
      $('.share_list_popup ul').append(Barcode);

  function showModal($) {
      $('#myModal').modal('show');
      //still need to fix this I have no idea how to print this on the modal
  }
 }