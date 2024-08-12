from turing_machine import TuringMachine


instructions_table_1 = [ 
    [ 0, ' ', ' ', ' ', 'stop' ],
    [ 0, 0, 1, 'R', 0 ],
    [ 0, 1, 0, 'R', 0 ]
]
tape_1 = [ 1, 1, 0 ]
state_1 = 0
cursor_1 = 2

instructions_table_2 = [ 
    [ 0, ' ', ' ', 'L', 1 ],
    [ 0, 0, 1, 'R', 1 ],
    [ 0, 1, 0, 'R', 0 ],
    
    [ 1, ' ', ' ', 'R', 'stop' ],
    [ 1, 0, 1, 'L', 1 ],
    [ 1, 1, 0, 'L', 1 ]
]
tape_2 = [ ' ', 0, 0, 1 ]
state_2 = 0
cursor_2 = 0

t = TuringMachine(instructions_table_1, tape_1, state_1, cursor_1)
final_tape = t()
assert final_tape == [ 0, 0, 1 ]

t = TuringMachine(instructions_table_2, tape_2, state_2, cursor_2)
final_tape = t()
assert final_tape == [ 1, 1, 0 ]

print('All tests passed')