import argparse
import hashlib
import os
import struct
import sys
from binascii import hexlify

import ecdsa
import requests
from steem.commit import PrivateKey


class ImageUploader:
    API_BASE_URL = "https://steemitimages.com"
    CHALLENGE = b"ImageSigningChallenge"

    def __init__(self, username, posting_wif):
        self.username = username
        self.posting_wif = posting_wif

    def checksum(self, filename, ):
        sha256 = hashlib.sha256()
        image_data = open(filename, 'rb').read()
        sha256.update(self.CHALLENGE)
        sha256.update(image_data)
        return sha256.digest(), image_data

    def upload(self, image_path, image_name=None):
        private_key = PrivateKey(self.posting_wif)
        sk = ecdsa.SigningKey.from_string(bytes(private_key),
                                          curve=ecdsa.SECP256k1)

        digest, image_content = self.checksum(image_path)
        signature = sk.sign_digest(digest)
        signature_in_hex = hexlify(
            struct.pack("<B", 31) + signature
        ).decode("ascii")

        files = {image_name or 'image': image_content}
        url = "%s/%s/%s" % (
            self.API_BASE_URL,
            self.username,
            signature_in_hex
        )
        r = requests.post(url, files=files)
        return r.json()


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", help="Image file (Absolute path)")
    args = parser.parse_args()

    # check the existance of required environment variables
    if not os.getenv("IMAGEHOSTER_USERNAME"):
        sys.exit("You need to set environment variable IMAGEHOSTER_USERNAME")

    if not os.getenv("IMAGEHOSTER_POSTING_WIF"):
        sys.exit(
            "You need to set environment variable IMAGEHOSTER_POSTING_WIF")

    image_uploader = ImageUploader(
        os.getenv("IMAGEHOSTER_USERNAME"),
        os.getenv("IMAGEHOSTER_POSTING_WIF")
    )

    resp = image_uploader.upload(args.image_path)
    if 'url' in resp:
        print("File uploaded: %s" % resp["url"])
    else:
        print(resp)


if __name__ == '__main__':
    cli()
