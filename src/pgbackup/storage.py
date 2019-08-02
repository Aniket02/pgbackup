def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def google_storage(storage_client, source_name, bucket_name, dest_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(dest_name)
    blob.upload_from_filename(source_name)
