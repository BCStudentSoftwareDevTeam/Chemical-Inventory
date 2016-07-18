function changeForm(status){
    var inputList = document.getElementsByClassName("d");
    for (var i = 0; i < inputList.length; i++){
        if (status == true){
           inputList[i].value = '';   
        }
        inputList[i].disabled = status;
    }
}

function checkBar(){
    var barInput = document.getElementById('barcodeId');
    if (barInput.value != ''){
        changeForm(false)
    }else{
        changeForm(true);
    }
}