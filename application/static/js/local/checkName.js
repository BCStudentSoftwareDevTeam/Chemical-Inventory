function checkName(){
    var chemName = document.getElementById('name');
    $.getJSON("/checkName/", {
        barId: $('input[name="chemName"]').val()
    },
        function(data) {
            console.log(data);
        });
}