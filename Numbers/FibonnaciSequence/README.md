# Fibonnaci Sequence Generation

* [Explanation](#Sequence-Explained)
* [How to use](#Usage)
* [Warnings](#Warnings)
* [Planned Changes](#Planned-Changes)

## Sequence Explained

The Fib sequence is probably one of the most iconic in mathematics. It's no secret to how the sequence is created since it follows the simple formula:

<p align="center" style="font-family:Arev; font-size:18pt;">
s<sub>k</sub> = s<sub>k-1</sub> + s<sub>k-2</sub>
</p>

with the start of the sequence seeded with: 

<p align="center" style="font-family: Arev; font-size:18pt;">
x = [ 0 , 1 ]
</p>

So in other words, every subsequent value in the sequence will just be the sum of the previous two elements. The ratio between values approaches the [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio) (φ).

## Usage

#### Function

The `Fib()` function is contained in [**fib.py**](fib.py) and takes a single argument **n**, which is the desired length of the sequence. You can call it inside your own script by including the file in your local directory.
```python
from fib import fib

print(fib(12))
```

#### Program

If you wish to run from the terminal, you should call [**run.py**](run.py) with your interpreter. If no arguments are provided then the default sequence length is 10. Two flags are available to call:
```
   <flag>   :  <name>  :  <type>

[-h,--help] :  <help>  :  <none>
[-l]        : <length> :  <int>
```
Example:
```python
$python3 -l 7
```
Output:
```
$[0, 1, 1, 2, 3, 5, 8]
```

#### WARNINGS!

If you try to supply a very large integer value from the terminal there will be a warning message asking if you wish to continue. If you choose to continue printing you may encounter memory issues. It will likely break down at 1 million iterations but the warning is generated if you enter anything larger than 10,000. 

## Planned Changes

* June 2020
    - [ ] Increase sequence size
    - [ ] Reduce memory errors for larger sequences
* July 2020
    - [ ] Improve speed performance for sizes above 1 million