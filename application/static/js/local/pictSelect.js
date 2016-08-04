function pictSelect(element) //Is called when a hazard pictogram is clicked
{
    if (document.getElementById(element).class == 'selectedPict'){
        document.getElementById(element).removeClass('selectedPict'); //If pictogram was selected, remove select styling  
    }else{
        document.getElementById(element).addClass('selectedPict'); //If pictogram was not selected, add select styling
    }    
}
