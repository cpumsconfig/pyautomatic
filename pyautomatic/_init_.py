import requests
import time
import os
from tqdm import tqdm
from tkinter import Tk, Label, StringVar
import zipfile
import patoolib

def jieya_file(file_path, mode):
    try:
        if mode == 1:
            # 解压到解压名字的文件夹
            patoolib.extract_archive(file_path, outdir=None)
        elif mode == 0:
            # 直接解压到当前文件夹
            patoolib.extract_archive(file_path)
        else:
            print("输入错误，解压模式只能为'1'或'0'")
    except patoolib.util.PatoolError:
        print("无效的压缩文件")
def jieya_zip(file_path, mode):
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            if mode == 1:
                # 解压到解压名字的文件夹
                zip_ref.extractall()
            elif mode == 0:
                # 直接解压到当前文件夹
                zip_ref.extractall('.')
            else:
                print("输入错误，解压模式只能为'1'或'0'")
    except zipfile.BadZipFile:
        print("无效的压缩文件")
class Downloader:
    def __init__(self):
        self.root = Tk()
        self.root.title("Download Progress")
        self.progress_var = StringVar()
        self.progress_label = Label(self.root, textvariable=self.progress_var)
        self.progress_label.pack()
    
    def download_putong(self, url):
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    print("\r[%s%s]" % ('=' * done, ' ' * (50-done)), end='', flush=True)
        print("\nDownload Complete")

    def download_tk(self, url):
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    self.progress_var.set("Downloading: [{}{}]".format('=' * done, ' ' * (50-done)))
                    self.root.update()
        print("Download Complete")

    def download_teshu(self, url):
        filename = url.split('/')[-1]
        with open(filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    print("\rDownloading: [{}{}]".format('=' * done, ' ' * (50-done)), end='', flush=True)
        print("\nDownload Complete")

def putong(url):
    downloader = Downloader()
    downloader.download_putong(url)

def tk(url):
    downloader = Downloader()
    downloader.download_tk(url)

def teshu(url):
    downloader = Downloader()
    downloader.download_teshu(url)

if __name__ == "__main__":
    # 示例用法
    putong("https://www.example.com/file.zip")
    tk("https://www.example.com/file.zip")
    teshu("https://www.example.com/file.zip")
class colors:
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

def print(text):
    print(text)
