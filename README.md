# Manual de usuario del lenguaje EZ-PZ
___


## Primeros pasos

El lenguaje EZ-PZ se compone de una estructura sencilla la cual sea amigable con el usuario, por esto, para empezar a codificar en el lenguaje, es necesario la declarion de las palabras reservadas `begin` y `end`, las cuales indicaran el inicio y el final del codigo.

Entre las palabras reservadas se debe de declarar la estructura `main`, la cual sera la principal encargada de la ejecucion del codigo, y de la cual atraves de esta se realizara la ejecucion del mismo, de esta manera el codigo principal consta de la siguiente estructura
```
begin

main {

}

end
```

## Declarando variables

Ahora que tenemos la estructura principal de nuestro lenguaje ya podemos empezar a realizar nuestro codigo, de esta manera el primer paso es poder declara una variable.

Para lograr esto se tiene que primero declarar el tipo de la variable que deseamos y luego el id de la misma, al final de toda declaracion se debera terminar con un `;`

Los tipos de datos que son aceptados son los siguientes

* int
* float
* string
* bool
  * true
  * false

De esta manera para declarar nuestras primerass variables el codigo quedaria asi:

```
begin

main {
  int variable1;
  float variable2;
  string variable3;
  bool variable4;
}

end

```

El lenguaje de igual manera es capaz de soportar declaraciones multiples dentro de la misma linea de codigo

```
begin

main {
  int variable1, variableInt2, variableInt3;
  float variable2, variableFlt2, variableFlt3;
  string variable3, variableStr2, variableStr3;
  bool variable4, variableBool2, variableBool3;
}

end

```

## Asignacion de variables

Ahora el siguiente paso es darle un valor a nuestras variables, Para esto tomaremos de ejemplo las variables anteriormente declaradas y le daremos un valor correspondiendo al tipo de variable, para esto usaremos el operando `=`, con el cual asignaremos el valor a la variable deseada

```
begin

main {
  int variable1, variableInt2, variableInt3;
  float variable2, variableFlt2, variableFlt3;
  string variable3, variableStr2, variableStr3;
  bool variable4, variableBool2, variableBool3;

  variable1 = 345;
  variableInt2 = variable1 * 3;
  variable2 = 3.1416;
  variableFlt3 = variable2 /23.2;
  variable3 = "Hola mundo";
  variable4 = false;


}

end
```

## Operadores permitidos

Las operaciones permitidas en el lenguaje son la siguientes:

* Suma (+)
* Resta (-)
* Multiplicacion ( * )
* Division (/)

De igual manera el lenguaje acepta los siguientes operadores logicos

* "<"
* ">"
* "<="
* ">="
* "=="
* "<>"
* and
* or

# Lectura y Escritura

El lenguaje soporta los estatutos `input` y `output`, los cuales son los encargados de que el usuario pueda imprimir en pantalla y almacenar datos introducidos por el mismo

## Lectura
La lectura se realiza a traves de la palabra `input`, con la cual el usuario podra almacenar un valor ingresado por el en su variable correspondiente, la estructura de la misma es:

```
input(variable);
```
El input solo puede tener una variable previamente declarada dentro del parentesis, en la cual se almacenara el valor introducido

## Escritura
La escritura se realiza a traves de la palabra `output`, con la cual el usuario sera capaz de imprimir en pantalla el valor de una variable o un string, la estructura de la misma es:

```
int a;
a = 42;
output("Esto imprime un string");
output(a);
```

Ejemplo de lo impreso:

```
Esto imprime un string
42
```


# Estructuras

Para complementar lo anterior, y continuar con el desarrollo de nuestro primer codigo EZ-PZ, comenzaremos con la creacion de diferentes estructuras, las cuales seran las encargadas de que podamos desarrollar codigos mas completos.

## if..else

Esta estructura es la encargada de que si una condicion se cumple se tome un camino correspondiente

para la codificacion de esta estructura es necesario la utilizacion de las palabras `if` y en su caso `else` de ser necesario, un ejemplo:

```
if  (a > b){
  output("A ES MAYOR");
}
else {
  output("B ES MAYOR")
}
```

## loop

Esta estructura es un ciclo que se repite hasta que cierta condicion se cumpla para salir

Para la creacion de esta estructura es necesario la utilizacion de la palabra `loop`, Un ejemplo para esta estructura es el siguiente:

```
a = 0;
loop (a < 6){
  output(a);
  a = a + 1;
}
```

# Funciones y llamadas

Las funciones y llamadas son herramientras de gran utilidad para la simplificacion de nuestro codigo, ya que sirven para generar un codigo mas limpio y entendible

## Funciones

El siguiente paso para avanzar en nuestro lenguaje, es la creacion de funciones que seran las encargadas de realizar pedazos de codigo que no deseamos tener en el main o codigo que utilizaremos varias veces y queramos simplificar, para la declaracion de la misma se realiza primero declarando la palabra reservada `func`, seguido por su tipo y sus correspondientes parametros, en caso de que tenga, la declaracion general de la misma es la siguiente:

```
func tipo ID_funcion(parametros){


  return variable;
}
```

al contrario del tipo de las variables, el tipo de las funciones consta por los siguientes:

* int
* float
* string
* bool
* void

void es un tipo de funcion en la cual es imposible retornar un valor dentro de la misma funcion, un ejemplo seria:

```
func void imprimir(int a){
  output(a);
}
```

Se debe aclarar que las funciones deben ser declaradas antes del main
```
begin

int globalVar;

func int facto(int num){
  int i, fact;
  fact = 1;
  i = 1;
    loop(i < num + 1){
      fact = fact * i;
      i = i + 1;
    }
     return fact;
}

main {
  int n, respu;
  int res;
  n = 0;
}

end
```

## Llamadas a funcion

Ahora si queremos llamar una funcion para que realice el codigo dentro de la misma es necesario seguir la siguiente estructura:

```
id_funcion(parametros);
```

de igual manera si una funcion tiene un valor de return, este valor puede ser asignado a una variable.

```
begin

int globalVar;

func int facto(int num){
  int i, fact;
  fact = 1;
  i = 1;
    loop(i < num + 1){
      fact = fact * i;
      i = i + 1;
    }
     return fact;
}

main {
  int n, respu;
  int res;
  n = 1;
  facto(n);
  res = facto(n);
  output(res);
}

end
```
De esta forma se puede retornar el valor calculado en la funcion llamada y usarlo dentro del main

# Arreglos

El lenguaje EZ-PZ soporta la creacion de arreglos, los cuales nos sirven para almacenar diferentes datos, para la declaracion de estos se hace mediante la siguiente forma
```
int arreglo[n];
```

donde n es el tamaño del arreglo declarado, para acceder el valor dentro de un arreglo se hace a traves de la siguiente forma

```
arr[1];
```
