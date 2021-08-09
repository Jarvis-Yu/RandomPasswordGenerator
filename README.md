# RandomPasswordGenerator

A python program that generates a random string of length n, n ∈ ℕ.

## How to use it

### Prerequisite

First make sure python is installed in your computer and is added to path. If you are not sure about it, enter `python` in your terminal to see if python is called.

### Using Examples

```shell
$ python randomPassword.py %d
```

Where `%d` is supposed to be the length of the password.

if your default python is not python3, use `python3` instead of `python`

---

You may choose the type of symbols that appears in the password

```shell
$ python randomPassword.py 15 -lc -n
```

This means you want a password of length 15 that is composed of lower-case letters and numbers only.

```
-lc : lower-case letters | a-z
-uc : upper-case letters | A-Z
-n  : numbers            | 0-9
-s  : symbols            | ~`! @#$%^&*()_-+={[}]|\:;"'<,>.?
```

## Extra Details

The more same args you enter, the more weight it has in the password.

Default weight of all types of symbols

```
lc: 260
uc: 260
n : 400
s : 200
```
