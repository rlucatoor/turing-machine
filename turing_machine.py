class TuringMachine:
    
    def __init__(self, instructions_table, initial_tape, initial_state, initial_cursor):
        self.state = initial_state
        # cursor position relative to tape's length (first position is 0)
        self.cursor = initial_cursor
        self.tape = initial_tape
        # list of instructions to be executed based on current_state and current_symbol; 
        # consists of a list of lists, where each sublist is an entry in the instructions 
        # table and must have the following format:
        # [ current_state, current_symbol, write_instruction, move_instruction, new_state ]
        self.instructions_table = instructions_table
        
    def move_tape_right(self):
        # move tape to the right by subtracting one to the cursor's position; 
        # simulate an infinitely long tape by adding a blank symbol at the beginning 
        # of the tape once cursor == 0 and this function is called
        if self.cursor == 0:
            self.tape.insert(0, ' ')
        else:
            self.cursor -= 1
            
    def move_tape_left(self):
        # move tape to the left by adding one to cursor's position; simulates
        # an infinitely long tape by adding a blank symbol at the end of the tape 
        # once cursor == len(tape) and this function is called;
        self.cursor += 1
        if self.cursor >= len(self.tape):
            self.tape.append(' ')
            
    def get_current_instruction(self):
        # get the instructions to be executed based on the current_state 
        # (first sublist element in inst_table) and current_symbol 
        # (second sublist element in inst_table)
        current_instruction = next(( inst for inst in self.instructions_table
            if inst[0] == self.state and inst[1] == self.tape[self.cursor]
        ), None)
        
        return current_instruction
        
    def __call__(self):
        while self.state != 'stop':
            # get the instructions to execute based on current state and symbol
            current_instruction = self.get_current_instruction()
            # replace the current symbol with the one specified in the instruction
            self.tape[self.cursor] = current_instruction[2]
            # move cursor to the direction specified in the instruction
            if current_instruction[3] == 'R':
                self.move_tape_right()
            elif current_instruction[3] == 'L':
                self.move_tape_left()
            # change state to the one specified in the instruction
            self.state = current_instruction[4]
                    
        # delete blanks, if any, from the output tape and return it
        return [ item for item in self.tape if item != ' ' ]