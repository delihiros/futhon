start: sexpr;

@sexpr: atom | sequence | quoted;

@atom: string | regex_string | symbol;
@sequence: vector | list | hashmap | set;

quoted: '\'' sexpr;

symbol: '[\w.\-><\+\-\*\/\?!:=]+';
string: '".*?(?<!\\)(\\\\)*?"';
regex_string: '\#' string;

vector: '\[' sexpr* '\]';
list: '\(' sexpr* '\)';
hashmap: '{' (sexpr sexpr)* '}';
set: '\#{' sexpr* '}';

WS: '[ \t\n,]+' (%ignore) (%newline);