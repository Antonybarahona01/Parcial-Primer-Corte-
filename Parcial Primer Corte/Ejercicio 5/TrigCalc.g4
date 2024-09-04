grammar TrigCalc;

// Definición de las expresiones principales
expr: sin_expr | cos_expr | tan_expr;

// Definición de expresiones trigonométricas
sin_expr: 'Sin' '(' number ')';
cos_expr: 'Cos' '(' number ')';
tan_expr: 'Tan' '(' number ')';

// Definición de números
number: DIGIT+ ('.' DIGIT+)?;

// Definición de dígitos
fragment DIGIT: '0'..'9';

// Definición de espacio en blanco
WS: [ \t\r\n]+ -> skip;
