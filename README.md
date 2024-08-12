# Turing Machine

<p align='center'>
    <img src='./figures/proof.png' width='800'>
</p>

A very simple, pure-Python implementation of a [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine), created for educational purposes and to show that Python is [Turing-complete](https://en.wikipedia.org/wiki/Turing_completeness). The implementation is designed to be as straightforward as possible, with the core component consisting of just about 60 lines of code (20 of which being comments 🤓).

## What is a Turing Machine?

A Turing Machine is an idealized computational device first described by Alan Turing in 1936 which, despite its simplicity, can simulate any algorithm and therefore compute any algorithmically specifiable series of numbers. By serving as a model of what is theoretically computable, the Turing Machine underpins the functioning and design of modern digital computers.

## How does a Turing Machine work?

A Turing Machine constists of four components:

- An arbitrarily long tape devided into cells. Each cell contains a symbol taken from a finitely-long list of symbols
- A pointer which identifies the currently selected cell (and therefore the currently selected symbol)
- A <i>machine state</i> selected from a finitely-long list of possible machine states
- An <i>instructions table</i> which, given a current symbol - current state pair, instructs the machine to do the following:
    - substitute the currently selected symbol with a different symbol 
    - move the tape either left or right
    - modify the current machine state.

<p align='center'>
    <img src='./figures/tape.png' width='700'>
</p>

Given an <i>initial state</i>, an <i>initial tape configuration</i> and an <i>instructions table</i>, the Turing Machine performs the following steps until it reaches a <i>halting</i> state:

1. Read the currently selected symbol
2. From the instruction table, get the instruction associated with the current symbol-state pair
3. Substitute the current symbol with the one specified in the instruction
4. Move the tape in the direction specified in the instruction
5. Substitute the current machine state with the one specified in the instruction

## How to use it

The Turing Machine defined in this work makes use of three symbols: `0`, `1` and `" "` (meaning <i>blank</i>). It can therefore perform arbitrary computation on binary-encoded numbers.

In order to run your computation, instantiate a `TuringMachine` by passing it four parameters:

- `instructions_table`: a `list` of `list`'s, containing one list per instruction; each instruction should be a `list` containing exactly 5 elements, in the following order:
    - `current_state`: the machine state that needs to be present for this instruction to be executed, must be either `int` or `str`
    - `current_symbol`: the symbol that needs to be selected for this instruction to be executed, must be one of `0`, `1` and `" "`
    - `write_instruction`: the new symbol that should replace `current_symbol`, must be one of `0`, `1` and `" "`
    - `move_instruction`: the direction in which the tape should be moved; should be `"L"` for 'left' and `"R"` from 'right'.
    - `new_state`, the new state that should replace `current_state`, must be either `int` or `str`.
- `initial_tape`: a `list` defining the initial tape; must only contain one of the three allows symbols, i.e. `0`, `1` or `" "`.
- `initial_state`: the initial machine state, must be either `int` or `str`
- `initial_cursor`: the initial position of the cursor; must be an `int` such that `o <= initial_cursor <= len(initial_tape)`.

