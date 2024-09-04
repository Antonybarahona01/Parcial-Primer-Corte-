grammar Trig;

prog: expr+ ;

expr:   SIN '(' NUM ')'      # sinExpr
      | COS '(' NUM ')'      # cosExpr
      | TAN '(' NUM ')'      # tanExpr
      ;

SIN: 'Sin' ;
COS: 'Cos' ;
TAN: 'Tan' ;

NUM: [0-9]+ ('.' [0-9]+)? ;  // Número entero o decimal

WS: [ \t\r\n]+ -> skip ; // Espacios en blanco
