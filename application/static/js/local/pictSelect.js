function pictSelect(element)
{
    if (document.getElementById(element).class == 'selectedPict'){
        document.getElementById(element).removeClass('selectedPict');  
    }else{
        document.getElementById(element).addClass('selectedPict');
    }    
    document.getElementById("addChemSubmit").disabled = false;
    document.getElementById("addChemSubmit").className = "btn btn-success btn";
}
