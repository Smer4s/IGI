import zipfile

def archive_result(filename, result_filename, archive_filename):
    """
    Archives the result file using zipfile.
    """
    with zipfile.ZipFile(archive_filename, 'w') as zipf:
        zipf.write(filename, result_filename)