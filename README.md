
# UnderPot 

![](https://img.shields.io/badge/Python-3.6-blue)
![](https://img.shields.io/badge/License-MIT-green)

\| [日本語](README.ja.md) \| English \|

UnderPot is a small library that provide some routines for encryption with auto-generated key.
when encryption and decrypt, this library generate a secret key with user-name and machine identifier.
so it is more safer than wrote secret key in the source code or include secret key in the package.
even if an encrypted data was stolen, decrypting is difficult without knowing username and machine identifier.

but, I'm a not professional for security. 
so I recommend other library if you know the better library than this.

## Usage

if you want to encrypt and decrypt, you can use `encrypt` and `decrypt` functions in the `underpot` package.

```py
import underpot 

encrypted = underpot.encrypt(b"your secret!")
underpot.decrypt(encrypted) # b"your secret!"
```

if you want to save the encrypted data or load encrypted data then decrypt it, you can use `save` and `load` functions from same package.
when generate a secret key on encryption, those functions add absolute path name to source for generating secret key.
in the other, those functions are same what open file then write encrypted data or open file then read data then decrypt it.

```py
import underpot 

underpot.save("cachedir/password-cache.cache", b"my password!")
underpot.load("cachedir/password-cache.cache") # b"my password!"
```

`save` and `load` functions has a function that save and load to hashed file name.
it is useful for hiding the file name for protection from Infer the file kind from filename.
if you want to use this function, give a optional parameter of `use_hashed_path` a `True`.

```py
underpot.save("cachedir/password-cache.cache", b"my password!", use_hashed_path=True)
underpot.load("cachedir/password-cache.cache", use_hashed_path=True) # b"my password!"
```

## Installation

UnderPot has a [setup.py](setup.py) so you can install this package with this command.

```shell
$ python setup.py install
```

## Requirement

* [pycryptodomex](https://www.pycryptodome.org)

## Installation

* UnderPot has released under the [MIT License](LICENSE.txt).
* UnderPot has required [pyencryptdomex](https://www.pycryptodome.org).  
  it has released under the [BSD, Public Domain and Apache Licenses](license/pycryptodomex/LICENSE.rst).  
  please read detail to [license/pycryptodomex/LICENSE.rst](license/pycryptodomex/LICENSE.rst).
