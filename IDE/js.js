
$("#form1").val("begin\n\tmain{\n\t\n\t}\nend");
$("#run").click(function(){
    //str que se mandara al compi
    var str = $("#form1").val();

    alert("HOLA");
});

$("textarea").keydown(function(e) {
    if(e.keyCode === 9) {
        var start = this.selectionStart;
        var end = this.selectionEnd;

        var $this = $(this);
        var value = $this.val();
        $this.val(value.substring(0, start)
                    + "\t"
                    + value.substring(end));


        this.selectionStart = this.selectionEnd = start + 1;

        e.preventDefault();
    }
});

var cursorPosition = 0;

function getIf(){
    return "if (expresion) {\n\t\n\t}";
}

function getElse(){
    return "else {\n\n\t}";
}

function getIfElse(){
    return getIf() +"\n\t"+ getElse();
}

function getLoop(){
    return "loop(expresion) {\n\t\t\n\t}"
}

function getDeclaracion(){
    return "tipo id_Variable = expresion;"
}

function getModulo(){
    return "\tfunc tipo id_funcion (tipo id_Variable) {\n\t}"
}

$("#form1").click( function(){
    cursorPosition = $('#form1').prop("selectionStart");
});

$("#if").click(function(){
    //string del primer form
    var str = $("#form1").val();
    //un substring hasta donde esta el cursor
    var strN = str.substring(0, cursorPosition);
    //substring desde donde esta el cursor hasta el final
    var strRest = str.substring(cursorPosition, str.length);
    //inserta el codigo entre los 2 substrings y los pone en el form
    var strF = strN + "\n\t"+ getIf() + strRest;
    $("#form1").val(strF);
});

$("#else").click(function(){
    //string del primer form
    var str = $("#form1").val();
    //un substring hasta donde esta el cursor
    var strN = str.substring(0, cursorPosition);
    //substring desde donde esta el cursor hasta el final
    var strRest = str.substring(cursorPosition, str.length);
    //inserta el codigo entre los 2 substrings y los pone en el form
    var strF = strN + "\n\t"+ getElse() + strRest;
    $("#form1").val(strF);
});

$("#ifelse").click(function(){

    var str = $("#form1").val();

    var strN = str.substring(0, cursorPosition);

    var strRest = str.substring(cursorPosition, str.length);

    var strF = strN + "\n\t"+ getIfElse() + strRest;
    $("#form1").val(strF);
});

$("#loop").click(function(){

    var str = $("#form1").val();

    var strN = str.substring(0, cursorPosition);

    var strRest = str.substring(cursorPosition, str.length);

    var strF = strN + "\n\t"+ getLoop() + strRest;
    $("#form1").val(strF);
});

$("#declaracion").click(function(){

    var str = $("#form1").val();

    var strN = str.substring(0, cursorPosition);

    var strRest = str.substring(cursorPosition, str.length);

    var strF = strN + getDeclaracion() + strRest;
    $("#form1").val(strF);
});

$("#modulo").click(function(){

    var str = $("#form1").val();

    var strN = str.substring(0, cursorPosition);

    var strRest = str.substring(cursorPosition, str.length);

    var strF = strN + "\n"+ getModulo() + strRest;
    $("#form1").val(strF);
});
