function printBarcode(barId){
    var barcode = document.getElementById(barId);
    var openWindow = window.open("", "", "width=800, height=700");
    openWindow.document.write("<title>Print Barcode</title>");
    openWindow.document.write(barcode.innerHTML);
    openWindow.document.close();
    openWindow.focus();
    openWindow.print();
    openWindow.close();
}

$(document).ready(function(){
    $('#containers tr').on('click', function(e){
        if ( $(e.target).is('span') ){ 
            printBarcode($(e.target.id).selector)
        }
        else { //If anywhere else in the row was clicked
            var href = $(this).find("a").attr("href"); //Set the link to the correct one
            if(href){
                window.location = href; //And change the window location to that link
            }
        }
    })
})