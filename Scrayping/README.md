# Scraping

scraping practice using python

## book title

* [Pythonクローリング＆スクレイピング―データ収集・解析のための実践開発ガイド―」
加藤 耕太. Pythonクローリング＆スクレイピング[増補改訂版] -データ収集・解析のための実践開発ガイド-](http://gihyo.jp/book/2019/978-4-297-10738-3)

## content

* keywords
  * クローリング
  * スクレイピング
  * 正規表現
* サードパーティ
  * wget
  * Xpath, CSSセレクター
  * lxml
  * Beautiful Soup
* フレームワーク
  * Scrapy

## Note

Instead of "brew install mongodb"

```sh
rm -fr $(brew --repo homebrew/core)
brew tap homebrew/core
brew tap mongodb/brew
brew install mongodb-community@4.4
brew services start mongodb/brew/mongodb-community@4.4
brew services stop mongodb/brew/mongodb-community@4.4
```
