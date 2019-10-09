
# UnderPot 

![](https://img.shields.io/badge/Python-3.6-blue)
![](https://img.shields.io/badge/License-MIT-green)

UnderPot は鍵を用意せずに共通鍵暗号方式で暗号化を行う機能を提供するライブラリです。
このライブラリは暗号化の際に秘密鍵をマシンの識別子とユーザ名から自動生成し、その鍵を使用して暗号化を行います。
なので、鍵をソースコードに直書きしたり、配布するファイルに同封したりするよりかは安全に情報を保存することができます。
もしもデータだけ盗まれたとしても、ユーザ名とマシンの識別子がわからなければ解読しづらいだろうという算段です。

ただ、これを書いている人はセキュリティの専門家でもないただの素人なので、
高いセキュリティが求められるような製作物に使用するのはお勧めしません。
もっと良いライブラリをご存知ならば、そちらを使うことを推奨します。

## Usage

単純にデータを暗号化・復号したい場合には `underpot` パッケージが提供している
`encrypt` 関数と `decrypt` 関数を利用することで、データの暗号化・復号を行うことができます。

```py
import underpot 

encrypted = underpot.encrypt(b"your secret!")
underpot.decrypt(encrypted) # b"your secret!"
```

<!--
暗号化したデータをファイルに書き出したい・読み込みたい場合には同パッケージにて提供されている `save` 関数と `load` 関数が利用できます。
これらの関数は第一引数にファイルパスを受け取りますが、ファイル名からそれがどのようなファイルなのかを判別しづらいようにするために、
そのままのファイルパスは使わずに、ハッシュ化されたファイル名でファイルを保存・読み込みします。
-->

暗号化したデータをファイルに書き出したい・読みだしたい場合には同パッケージにて提供されている `save` 関数と `load` 関数が利用できます。
この関数でデータを保存する場合、この関数は「ユーザ名・マシンの識別子」に加えて「保存先のファイルの絶対パス」も鍵生成に利用されます。
それ以外ではファイルを開き `encrypt` 関数で暗号化したデータを書き込む、または開いたファイルから読み込んだデータを `decrypt` 関数で復号することと変わりありません。

```py
import underpot 

underpot.save("cachedir/password-cache.cache", b"my password!")
underpot.load("cachedir/password-cache.cache") # b"my password!"
```

`save` 関数 `load` 関数はともにファイルの種類の判別を困難にするために保存先・読み込み元のファイル名をハッシュ化してくれる機能があります。
この機能は FTP のホスト名とそれに関するパスワードなどといった複数の秘密情報を管理する際に有効です。
この機能を有効にするにはオプショナル引数の `use_hashed_path` に `True` を与えてください。

```py
underpot.save("cachedir/password-cache.cache", b"my password!", use_hashed_path=True)
underpot.load("cachedir/password-cache.cache", use_hashed_path=True) # b"my password!"
```

## Installation

UnderPot は [setup.py](setup.py) が同梱されているため下記のコマンドからインストールすることができます。

```shell
$ python setup.py install
```

## Requirement

* [pycryptodomex](https://www.pycryptodome.org)

## Installation

* UnderPot は [MIT License](LICENSE.txt) の許諾の下で公開されています。
* UnderPot は [pyencryptdomex](https://www.pycryptodome.org) を利用しています。[pycryptodomex](https://www.pycryptodome.org) は [BSD, Public Domain and Apache Licenses](license/pycryptodomex/LICENSE.rst) の許諾の下で公開されています。詳細は [license/pycryptodomex/LICENSE.rst](license/pycryptodomex/LICENSE.rst) を参照ください。
