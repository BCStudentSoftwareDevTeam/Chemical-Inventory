var quantityUnit = document.getElementById('currentQuantityUnit');
var capacityUnit = document.getElementById('capacityUnit');
var quantity = document.getElementById('currentQuantity')
var capacity = document.getElementById('capacity');

quantityUnit.addEventListener('change', function(){checkVals(quantity, quantityUnit, capacityUnit, "quantitymL")});
capacityUnit.addEventListener('change', function(){checkVals(capacity, capacityUnit, quantityUnit, "capacitymL")});
function checkVals(from, subject, compare, saveAs) {
    window[saveAs] = (window.conversionObject.functions.converter("Volume", subject[subject.selectedIndex].text, "milliliter (mL)", from.value))
    capacity.min = window.conversionObject.functions.converter("Volume", 'milliliter (mL)', capacityUnit[capacityUnit.selectedIndex].text, quantity.value)
    console.log(window['capacitymL'])
    console.log(window['quantitymL'])
};
