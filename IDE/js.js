// Oscar Guevara  A01281577
// Gerardo Ponce  A00818934


$("#form1").val("begin\n\tmain{\n\t\n\t}\nend");
$("#run").click(function(){
    //String que se mandará al compilador.
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
    //String del form1.
    var str = $("#form1").val();
    //Substring hasta donde está el cursor.
    var strN = str.substring(0, cursorPosition);
    //Substring desde donde está el cursor hasta el final.
    var strRest = str.substring(cursorPosition, str.length);
    //Inserta el código entre los 2 substrings y los pone en el form.
    var strF = strN + "\n\t"+ getIf() + strRest;
    $("#form1").val(strF);
});

$("#else").click(function(){
    var str = $("#form1").val();
    var strN = str.substring(0, cursorPosition);
    var strRest = str.substring(cursorPosition, str.length);
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
