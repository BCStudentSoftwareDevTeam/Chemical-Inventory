function highlightTab(tabId) {
    clearPastStyles();
    var curTab = document.getElementById(tabId);
    clearPastStyles();
    if (curTab.classList.contains('panel-closed')){
            // curTab.style.background = "dimgrey";
            // curTab.style.color = "white";
            curTab.classList.remove("panel-closed");
            curTab.classList.add("panel-open");
        }
    else{
        curTab.classList.remove("panel-open");
        curTab.classList.add("panel-closed");
        // curTab.style.background = '';
        // curTab.style.color = '';
    }
}

function clearPastStyles() {
    var elementList = document.getElementsByClassName("panel-change");
    for (var i = 0; i < elementList.length; i++){
        elementList[i].classList.remove("panel-open");
        elementList[i].classList.add("panel-closed");
    }
}