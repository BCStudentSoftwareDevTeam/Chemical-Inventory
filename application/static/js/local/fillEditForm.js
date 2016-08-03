function fillEditForm(chemId, config){
    $.ajax({
        url: "/getEditData/",
        data: {chemId : chemId},
        type: "GET",
        success: function(data) {
            config = config.replace(/'/g, '"');
            config = config.replace(/u"/g, '"');
            config = JSON.parse(config);
            console.log(config);
            for (var section in config){
                for (var element in config[section]){
                    var curElement = config[section][element];
                    if (curElement.type == "text" || curElement.type == "number"){
                        document.getElementById(curElement.id).value = data[curElement.id];
                    }
                    else if (curElement.type == "dropdown"){
                        var dropdownList = document.getElementById(curElement.id);
                        dropdownList.value = data[curElement.id]
                    }
                    else if (curElement.type == "checkbox"){
                        var checkbox = document.getElementById(curElement.id);
                        if (data[curElement.id] == 'True'){
                            checkbox.checked = true;
                        }
                        else {
                            checkbox.checked = false;
                        }
                    }
                }
            }
        },
        error: function(){
            console.log("Error: Could not retrieve data for requested chemical");
        }
    });
}