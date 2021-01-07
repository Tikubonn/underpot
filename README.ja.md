
# UnderPot 

![](https://img.shields.io/badge/python-v3.6-blue)
![](https://img.shields.io/badge/license-MIT-green)

\| [English](README.md) \| Japanese \|

UnderPot はちいさな暗号化ライブラリです。
このライブラリは暗号化のための幾つかの関数を提供します。
これらの関数はデータ暗号化時に、「コンピュータの識別子」「ユーザ名」「保存先ファイル名」等の情報から秘密鍵を動的に生成し使用します。
そのため、これらの関数はデータ暗号化時に秘密鍵を要求しません。
このライブラリを使用することで、パスワードなどの機密情報を保存するソフトウェアで、
秘密鍵を別途ファイルやソースコード内に保持するよりも、安全に暗号化を行うことができるでしょう。

ただし注意してください。
このライブラリの作者はセキュリティの専門家ではありません。
そのため、類似する高品質なライブラリがあるならば、そちらの利用を検討したほうが良いでしょう。

## Usage

導入後、暗号化のための幾つかの関数が提供されます。
任意のバイト列を暗号化するには `encrypt` 関数を使用します。
暗号化されたバイト列を復号するには `decrypt` 関数を使用します。

```py
import underpot 

encrypted = underpot.encrypt(b"your secret!")
underpot.decrypt(encrypted) # b"your secret!"
```

もし、任意のデータを暗号化して保存したい場合には `save` 関数と `load` 関数が利用できます。

```py
import underpot 

underpot.save("secrets/password", b"my password!")
underpot.load("secrets/password") # b"my password!"
```

UnderPot はファイル名から内容を推察されることを防ぐため、ファイル名を難読化する機能も用意されています。
ファイル名を難読化したい場合には `get_hashed_path` 関数が利用できます。

```py
import underpot 

underpot.get_hashed_path("secrets/password") # secrets/KsvJ-9_MErflf_-K0eU4qaW8QVZJBArxR6KIMfjyDZA=
```

## Requirement

* [pycryptodomex](https://www.pycryptodome.org)

## License 

UnderPot は [MIT License](LICENSE.txt) で公開されています。

* [pycryptodomex](https://www.pycryptodome.org) は [BSD, Public Domain and Apache Licenses](license/pycryptodomex/LICENSE.rst) で公開されています。
