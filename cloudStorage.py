import os
import shutil
import random
import dropbox

class TransferData(object):
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken

    def transferFiles(self,pathFrom,pathTo):
        dropboxbruh = dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(fileFrom):
            relative_path = os.path.relpath(local_path,fileFrom)
            dropbox_path = os.path.join(file_to, relative_path)
def main():
    IRDKWHATTOTRANSFER = TransferData("sl.Aywum4fGFcsrq5fBefozBpDcNWGbsellFTgV5ToDUViUHt-h74ih3wgEBV_su7u7jheCyHxbRMzAvy0A3hNNeS7_3acDBFw9Mr9LjfUTYbBYAyt5rLyaBK47yQffX_ccD0xQJQkU")
    fileFrom = input("ENTER THE FILE PATH TO TRANSFER > ")
    fileTo = input("ENTER THE FILE PATH TO UPLOAD TO DROPBOX > ")
    IRDKWHATTOTRANSFER.transferFiles(fileFrom,fileTo)
    print("FILE HAS BEEN TRANSFERRED")

main()