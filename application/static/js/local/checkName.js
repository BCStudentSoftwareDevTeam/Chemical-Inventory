function checkName(){
    /*Checks the input name, to see if it exists in the database.
    If the name is there, require user to enter a concentration as a way to prohibit repeated chemical names.*/
    var chemVal = document.getElementById('name').value;
    $.ajax({
        url: "/checkName/",
        data: {value : chemVal},
        type: "GET",
        success: function(data) {
            console.log(data)
            document.getElementById('concentration').required = data['required']; //url will return a json object with either true or false as the value to this key.
        },
        error: function() {
            document.getElementById('concentration').required = true;
            //If the request failed for some reason, don't take chances for duplicate chemical names with no concentration
        }
    });
}

var concentrate = document.getElementById('concentration');
concentrate.addEventListener("change", checkConc());

function checkConc() {
    var chemName = document.getElementById('name').value;
    if (concentrate.required === true) {
        $.ajax({
            url: "/checkConc/",
            data: {chemName:chemName, concentration:concentrate.value},
            type:"GET",
            success: function(data) {
                console.log(data);
            },
            error: function() {
                console.log("Error");
            }
        });
    };
}