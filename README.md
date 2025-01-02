![Wordscapes Icon](https://github.com/user-attachments/assets/71c18749-e617-403f-a892-a5f7fa80b0cd)

# Wordscapes Solver 



For when a Wordscapes level is just too hard

## How to Use
### Command Line Arguments
#### No Arguments
```python3 main.py```
- You will be prompted for both ALLOWED_LETTERS and MIN_LENGTH

#### 1 Argument
```python3 main.py ALLOWED_LETTERS```

- Providing 1 argument (not including the name of the python file) specifies the letters that can be used to create words (e.g. `python3 main.py dgo`)
- The default value of the minimum length of a valid words is 3


#### 2 Arguments
```python3 main.py ALLOWED_LETTERS MIN_LENGTH```

Ex. ```python3 main.py dgo 4```
- Providing 2 arguments (not including the name of the python file) specifies the letters that can be used to create words and the minimum length of a valid word
