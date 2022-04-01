import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BErETTOV6sVyJtTOqxNVrTlgBMr8wZXLgMvU6jcGe85n4SVmpk80Vl7kiZuf0QOZh55pTdnAC7O6j6nxT2O6LDvtJDq6rLkdJoBRV7sMxbKPT0PXkEsUUq8d2ZadhSdku0LrU9PMWwMO'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer")
    file_to =   input("enter the full path to upload to dropbox")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()