import enum


class Lexer:
    def __init__(self, source) -> None:
        self.source = source + '\n' # Source code to lex as a string. Append a newline to simplify lexing/parsing the last toeken/statement.
        self.cur_char = '' # Current character in the string.
        self.cur_pos = -1 # Current position in the string.
        self.next_char()
    
    # process the next token
    def next_char(self):
        self.cur_pos += 1
        if self.cur_pos >= len(self.source):
            self.cur_char = '\0' # EOF
        else:
            self.cur_char = self.source[self.cur_pos]
    
    # Return the lookahead character.
    def peek(self):
        if self.cur_pos + 1 >= len(self.source):
            return '\0'
        return self.source[self.cur_pos + 1]
    
    # Invalid token found, print error message and exit.
    def abort(self, message):
        pass
    
    # Skip whitespace except  for newlines, which we will indicate the end
    #   end of a statement.
    def skip_whitespace(self):
        pass
    
    # Skip comments in code.
    def skip_comment(self):
        pass
    
    # Return the next token.
    def get_token(self):
        # Check the first character of this token to see if we can decide what it is.
        # If it is a multiple character operator (e.g., !=), number, identifier, or keyword, then we will process the rest.
        if self.cur_char == '+':
            pass # plus token
        elif self.cur_char == '-':
            pass # minus token
        elif self.cur_char == '*':
            pass # asterisk token
        elif self.cur_char == '/':
            pass # divide token
        elif self.cur_char == '\n':
            pass # newline token
        elif self.cur_char == '\0':
            pass # EOF token
        else:
            # unknown token
            pass
        
        self.next_char()
        
        
# Token contains the original text and the type of token.
class Token:
    def __init__(self, token_text, token_kind) -> None:
        self.text = token_text # the token's actual text. used for identifiers, strings, and numbers.
        self.kind = token_kind # the token's type. used for keywords, operators, etc. classified as.
        
class Token_Type(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # operators
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211