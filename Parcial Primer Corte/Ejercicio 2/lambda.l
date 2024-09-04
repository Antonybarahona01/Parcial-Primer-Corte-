%{
#include <stdio.h>
#include <stdlib.h>

int found_lambda = 0;

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int yylex(void);
%}

%%
lambda      { found_lambda = 1; }
[ \t\n]     { }
.           { }
%%

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file>\n", argv[0]);
        return 1;
    }
    
    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }
    
    yyin = file;
    yylex();
    fclose(file);
    
    if (found_lambda) {
        printf("ACEPTA\n");
    } else {
        printf("NO ACEPTA\n");
    }
    return 0;
}
