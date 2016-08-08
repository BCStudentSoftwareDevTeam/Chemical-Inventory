function changeForm(status){
    var inputList = document.getElementsByClassName("d");
    for (var i = 0; i < inputList.length; i++){ //For all elements with class "d"
        if (status == true){
           inputList[i].value = ''; //If status is true, change values of all fields to an empty string. When barcode is removed, values don't remain in text boxes.
        }
        inputList[i].disabled = status; //change disabled value to whatever is passed in. If true, they are disabled. If false, they are not.
    }
}

function checkBar(){
    var barInput = document.getElementById('barcodeId').value;
    if (barInput.length == 8){ //Only runs after user has entered 8 digits into barcode field (all barcodes will be 8 digits)
        getData(barInput); //Fill enabled fields
    }else{
        changeForm(true); //Disable and clear fields when there are less than 8 digits in the field
    }
}

function getData(barcodeId){
    $.ajax({ //AJAX call to url "/checkInData/" to get info with barcodeId that is passed in from checkBar function
        url: "/checkInData/",
        data: {barId : barcodeId},
        type: "GET",
        success: function(data) { //fill values of elements: 'chemId', 'prevStorageId', and 'prevQuantity' with info from database
            if (data['status'] === 'OK') {
                document.getElementById("chemId").value = data['chemName'];
                document.getElementById('prevStorageId').value = data['storage'];
                document.getElementById('prevQuantity').value = data['quantity'] + " " + data['unit'];
                changeForm(false); //Enable fields
            } else {
                changeForm(true); //Disable and clear fields when there are no containers with matching barcode
                console.log(data['status'])
            }
        },
        error: function() {
            console.log(data['status']) //TODO: change to write to a log file as well as console.
        }
    });
}