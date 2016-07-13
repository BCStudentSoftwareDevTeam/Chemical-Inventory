function createBarcode(elementId, lastBar){
    var d = new Date();
    var year = d.getFullYear();
    var month = (d.getMonth()+1).toString();
    year = year.toString().substr(2,2);
    
    if (month.length == 1){
        month = "0" + month;
    }
    
    var barYear = lastBar.substr(0,2);
    var barMonth = lastBar.substr(2,2);
    var barNum = lastBar.substr(4,8);

    if (year == barYear){
        if (month == barMonth){
            barNum = (parseInt(barNum)+1).toString();
            barNum = checkbarNumLen(barNum);
            var newBar = year + month + barNum;
        }
    }else{
        var newBar = year + month + '0000';
    }
    
    // Need to build code that creates barcodes based on the last barcode created
    document.getElementById(elementId).value=newBar;
}

function checkbarNumLen(barNum){
    if (barNum.length == 4){
        return barNum;
    }else{
            return checkbarNumLen('0' + barNum);
        }
}