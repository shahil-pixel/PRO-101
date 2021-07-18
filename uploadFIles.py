import dropbox
import os

from dropbox.files import WriteMode

class TransferData():
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to,local_path):
        dbx = dropbox.Dropbox(self.access_token)

         # enumerate local files recursively
        for root, dirs, files in os.walk(file_from):
            # construct the full dropbox path
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

        f = open(local_path, 'rb')
        dbx.files_upload(f.read(), dropbox_path,mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.A0qcyQ9rjuyrss5Y2xAjXrWQkcuDbWEPikuJyMB00onq84l5Bbw1fRXbPcKUTahb6WTwCq_96RtC_TB2pgjKB287-ukd57PkvVDzOsWa1MdYXl1wM89uEsVIQu9beSjEj6U3fW0'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()