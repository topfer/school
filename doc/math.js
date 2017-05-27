function loaded() {
    alert("Loaded !");
}

function checkChange(widget, type, idxParam) {
    //var checkName = widget.name;
    //var idx = checkName[checkName.length-1];

    var hiddenWidgetId = "math." + type
    
    if ( idxParam ) {
        hiddenWidgetId += "." + idxParam
    }
    
    //var hiddenWidget = document.getElementById("math." + type + "." + idxParam);
    var hiddenWidget = document.getElementById(hiddenWidgetId)
    //alert("id : " + hiddenWidgetId)

    if (widget.checked) {
        hiddenWidget.value = "on"; 
    }
    else {
        hiddenWidget.value = "off"; 
    }
}

function checkComplete() {
    var items = document.getElementsByClassName("workcell");
    var allComplete = 1
    for(var i = 0; i < items.length; i++) {
        var nodeItem = items.item(i);
        nodeItem.className = "workcell"; 
        if (!nodeItem.childNodes[1].value.replace(/\s/g, '').length) {
            nodeItem.className = "workcell incomplete_cell";
            allComplete = 0
        }
    }
    if (allComplete == 1){
        checkResults()
    }
}

function checkResults() {
    var items = document.getElementsByClassName("workcell");
    for(var i = 0; i < items.length; i++) {
        var nodeItem = items.item(i);
        nodeItem.childNodes[1].className = "rezuser";
        if (parseInt(nodeItem.childNodes[1].value) == parseInt(nodeItem.childNodes[2].value)) {
            //nodeItem.childNodes[1].style.color = "green"
            nodeItem.childNodes[1].className += " rezuser_ok";
        } else {
            //nodeItem.childNodes[1].style.color = "red"
            nodeItem.childNodes[1].className += " rezuser_nok";
        }

        $.ajax({
            url: "/rekenscr/sendRez.py",
            type: "post",
            data: $('form').serialize(),
            success: function(response) {
            }
        });

    }
}
