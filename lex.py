


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
        pass