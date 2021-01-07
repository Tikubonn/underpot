
# UnderPot 

![](https://img.shields.io/badge/python-v3.6-blue)
![](https://img.shields.io/badge/license-MIT-green)

\| English \| [Japanese](README.ja.md) \|

UnderPot is a small cipher library.
it provide some cipher functions that encrypt and decrypt without key, because it make cipher key from machine identifier, user-name and file path.
so if you used this, you don't have to save secret key into another file or source code.

be careful, author is not a security professional, so you should use another library if you could.

## Usage

after installed, you could use some cipher functions from this package.
you could encrypt any data with `encrypt` function.
you could decrypt encrypted data with `decrypt` function.

```py
import underpot 

encrypted = underpot.encrypt(b"your secret!")
underpot.decrypt(encrypted) # b"your secret!"
```

if you want to save any data with encryption, you could use `save` and `load` functions.

```py
import underpot 

underpot.save("secrets/password", b"my password!")
underpot.load("secrets/password") # b"my password!"
```

underpot provide `get_hashed_path` function that transform a filename to obfuscated.

```py
import underpot 

underpot.get_hashed_path("secrets/password") # secrets/KsvJ-9_MErflf_-K0eU4qaW8QVZJBArxR6KIMfjyDZA=
```

## Requirement

* [pycryptodomex](https://www.pycryptodome.org)

## License 

UnderPot is released under the [MIT License](LICENSE.txt).

* [pycryptodomex](https://www.pycryptodome.org) is released under the [BSD, Public Domain and Apache Licenses](license/pycryptodomex/LICENSE.rst).
