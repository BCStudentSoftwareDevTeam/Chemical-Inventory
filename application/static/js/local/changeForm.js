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
    $.getJSON("/checkInData/", {
        barId: $('input[name="barcodeId"]').val()
    },
        function(data) {
            console.log(data);
            for (var contKey in data){
                var cont = data[contKey];
                window.chemId = "{{ group.id['" + cont.chemId + "']|safe }}";
                window.storageId = "{{ group.id['" + cont.storageId + "'] | safe }}";
                window.currentQuantity = cont.currentQuantity + " " + cont.currentQuantityUnit;
            }
        });
}
