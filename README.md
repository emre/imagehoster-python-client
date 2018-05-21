[Imagehoster](https://github.com/steemit/imagehoster) is the project powers the images you upload at Steemit. It's an interesting project because **only** STEEM accounts can upload files here by signing the image content with their posting key. You can get more [details](https://github.com/steemit/imagehoster) on the ImageHoster README.

***

[imagehoster-python-client](https://github.com/emre/imagehoster-python-client) is the python client of the steemitimages. You can upload images to steemitimages in your python applications.

##### Installation

```
$ (sudo) pip install imagehoster
```

##### Usage

```
image_uploader = ImageUploader(
	steem_username,
   private_posting_key,
)
resp = image_uploader.upload("/path/to/image.png)
if 'url' in resp:
    print("File uploaded: %s" % resp["url"])
else:
    print(resp)
```

##### Using the CLI APP

<img src="https://steemit-production-imageproxy-upload.s3.amazonaws.com/DQmdws8Jofne1WEds361YJhqNDhNUidhQuGuucqbhRdavAL">
<center><sup><i>imagehosterception</i></sup></center>

Once you have installed the package via pip, you have also a CLI app installed.

Make sure you have set environment variables first:

```
export IMAGEHOSTER_USERNAME=emrebeyler
export IMAGEHOSTER_POSTING_WIF=PRIVATE_POSTING_WIF
```

Then...

```
$ imagehoster qq.jpeg
File uploaded: https://steemitimages.com/DQmZNzWiHHSJGdPjTXDAmeZEW5G84z47uSKbR9shABJRRaL/image
```