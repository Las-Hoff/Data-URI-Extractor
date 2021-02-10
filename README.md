# Data-URI Extractor
テキストファイルからData URI部分(RFC3986に準拠したものに限る)を抜き出し、埋め込まれたファイルを復元するスクリプトです。

A small script for extracting and decoding data URIs following RFC3986 inside a text file, then saving them as individual files.

# 使い方 / Usage
```python:usage
python extractor.py <file>
```
対象とするファイルが存在するディレクトリに`<file>_saved`というディレクトリを作成し、その中に`file_<number>.<ext>`というファイル名で復号したファイルを連番で保存していきます。MIMEタイプから拡張子を判別できないファイルが存在した場合は、`.dat`として保存した上で、`unknown_bin.txt`というファイルに、**ファイルの番号**と**ヘッダー**(URIのdata部分を取り除いたもの)をログとして出力します。

This command makes a directory named `<file>_saved` in the directory where `<file>` exists, and saves decoded files as `file_<number>.<ext>`. If the extension of a file is unable to be guessed from the MIME type, the file is saved as `.dat` and a log file named `unknown_bin.txt` is generated. The log file contains the **file's number** and the **header(the non-data part)**.

# メモ / Notes
- `mimetypes.guess_type()`は余り用いられない拡張子を返す場合があったり(`image/jpeg`に対し`.jpe`など)、非標準のMIMEタイプ(けれどそれなりに用いられている)に対応してなかったりする(`image/jpg`など)ので、人力で用意した辞書に存在しない場合の最終手段としてのみ利用

  Since `mimetypes.guess_type()` does not necessarily output the most common extension (e.g. `image/jpeg` → `.jpe`)
and non-standard MIME types (yet in use) are ignored (e.g. `image/jpg`), this program use the original dictionary prior to `mimetypes.guess_type()`.

- 画像を抽出するために書いたものなので、今のところ用意した辞書は画像に関する小規模なもの

  Because I wrote this for extracting images, the prepared dictionary is a small one about image extensions now.
