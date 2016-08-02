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
    if (barInput.value.length == 8){
        changeForm(false);
        getData(barInput);
    }else{
        changeForm(true);
    }
}

function getData(barcodeId){
    $.ajax({
        url: "/checkInData/",
        data: {barId : barcodeId.value},
        type: "GET",
        success: function(data) {
            document.getElementById("chemId").value = data['chemName'];
            document.getElementById('prevStorageId').value = data['storage'];
            document.getElementById('prevQuantity').value = data['quantity'] + " " + data['unit'];
        },
        error: function() {
            console.log("Error: There are no containers with that barcode in the system.")
        }
    });
    }