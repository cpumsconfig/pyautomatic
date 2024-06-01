import zipfile

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

