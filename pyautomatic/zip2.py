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

