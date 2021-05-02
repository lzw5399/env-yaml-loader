#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- author: lzw5399 -*-

from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        endpoint="http://172.16.129.169:39900/",
        access_key="415WK7QG60FJHUGCE3TO",
        secret_key="904nqDB1kcmPrzLWTNkjA4n3t77AU2JRJyqAKkNo",
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("help-center-hana")
    if not found:
        client.make_bucket("help-center-hana")
    else:
        print("Bucket 'help-center-hana' already exists")

    objects = client.list_objects("help-center")
    for obj in objects:
        # client.fput_object('help-center-hana', )
        print(obj)

    print(
        "'/home/user/Photos/asiaphotos.zip' is successfully uploaded as "
        "object 'asiaphotos-2015.zip' to bucket 'asiatrip'."
    )


if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
