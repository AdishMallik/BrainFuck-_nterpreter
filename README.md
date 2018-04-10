# BrainFuck_Interpreter
A simple brainfuck interpreter written in Python. Brainfuck is an esoteric programming language created in 1993 by Urban Müller, and notable for its extreme minimalism. It only uses 8 simple commands and is a Turing complete langaunge. For more information, see [here](https://en.wikipedia.org/wiki/Brainfuck)

## Getting Started

Clone this repository using 
```
  git clone https://github.com/AdishMallik/BrainFuck_Interpreter.git
```

Navigate to the directory using
```
  cd BrainFuck_Interpreter
```

Interprete your BrainFuck program using
```
  python BrainFuck_Interpreter.py [your brainfuck file here]
```

### Prerequisites
Python 2.7 should be installed in your computer. The code is written for python 2.7.

## The BrainFuck syntax
BrainFuck only uses 8 commands.

|  Command   |  Usage                                    |
|------------|-------------------------------------------|
|     *      |increments the byte at the data pointer    |
|     -      |decrements the byte at the data pointer    |
|     >      |moves the data pointer to the next cell    |
|     <      |moves the data pointer to the previous cell|
|     \[     |if the byte at the data pointer is 0, the program instead of moving forward,jumps to the command after matching \] command|
|     \]     |if the byte at the data pointer is not 0, the program instead of moving forward,jumps to the command after matching \[ command|
|      .     |prints the byte at the data pointer|
|      ,     |takes a byte of data as input and stores it value in the byte of data pointer|

### Example Program:
The following program prints Hello World!
```BrainFuck
>+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-]
<.#>+++++++++++[<+++++>-]<.>++++++++[<+++>-]<.+++.------.--------.[-]>++++++++[
<++++>-]<+.[-]++++++++++.
```

Two test programs are provided : helloworld.bf and mandelbrot.bf
Time taken by the interpreter to interpret mandelbrot.bf and to create the mandelbrot set is  7294.171278 seconds (around 2.02 hours).


## License
The repository is under [WTPFL](http://www.wtfpl.net/) License - see the [LICENSE](LICENSE) file for details

## Acknowledgments
Although the interpreter was written by me, all the BrainFuck code was taken from [here](http://esoteric.sange.fi/brainfuck/bf-source/prog/). 

