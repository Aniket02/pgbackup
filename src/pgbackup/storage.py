def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()


def google_storage(storage_client, source_file, bucket_name, dest_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(dest_name)
    dest_file = open(dest_name, 'wb')
    local(source_file, dest_file)
    blob.upload_from_filename(dest_name)
