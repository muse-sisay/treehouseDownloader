# Treehouse Downloader

* Download [**Treehouse**](https://teamtreehouse.com/) track for personal offline use.
* You will need teamtreehouse.com account to download a track or workshop.

* **NOTE** Your library might have partnered with teamtreehouse.com to offer you free teamtreehouse.com account.

## Requirements

* Python3
* ChromeWeb Driver
* youtube_dl
* BeautifulSoup
* selenium

# Course Folder Structure

```
- Treehouse          (Here goes all your downloaded courses)
---- Course1
---- Course2
---- Course3
---- Course4
```

## Course Folder Structure

```
- Course1 Folder
---- content.md
---- 00 - Chapter A     // chapter folder
---- 01 - Chapter B     // ...
---- 02 - Chapter C
-- 0 - Video A          // video file
-- 1 - Video B          // video file
-- 2 - Video C          // ...

```

## Usage

* In order to begin download you have to edit settings.json file first. Add your email, password and course download path.

```javascript
{
  "email": "",
  "password": "",
  "EXTERNAL_DL": "  --external-downloader aria2c --external-downloader-args '-j1 -x16 -s16 -k1M' ",
  "courses_folder_path": ""
}

```

## Run treehouseDownloader

```bash
# open terminal or commandline
$ python path/to/treehouseDownloader/downloader.py
```

## Acknowledgement

* Thanks to [**ankitsejwal**](https://github.com/ankitsejwal), for inspiration.
