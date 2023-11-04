import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/Users/billoncho/MEGA/MEGAsyncUploads/0001_Python_Mega_Course/app1/Bonus/compressed.zip",
                    "/Users/billoncho/MEGA/MEGAsyncUploads/0001_Python_Mega_Course/app1/Bonus/files")