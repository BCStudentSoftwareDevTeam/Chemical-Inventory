function pictSelect(element)
{
    $(".hazardRadio").removeClass('selectedPict');
    $(element).addClass('selectedPict');
    document.getElementById("addChemSubmit").disabled = false;
    document.getElementById("addChemSubmit").className = "btn btn-success btn";
}
