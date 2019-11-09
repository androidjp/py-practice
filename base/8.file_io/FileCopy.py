import os
import time
import shutil

sourceDir = r"D:\test\from"
targetDir = r"D:\test\to"
copyFileCounts = 0


def CopyFiles1(sourceDir, targetDir):
    # 完全连子目录也会复制好，美观
    global copyFileCounts
    print(sourceDir)
    print("%s, 当前处理文件夹:%s, 已处理 %s 个文件" % (
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), sourceDir, copyFileCounts))
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)
        if os.path.isfile(sourceF):
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
                copyFileCounts += 1
            if not os.path.exists(targetF) or (
                    os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                open(targetF, "wb").write(open(sourceF, "rb").read())
                print("%s, %s 复制完毕" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF))
            else:
                print("%s %s 已存在，不重复复制" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), targetF))
        if os.path.isdir(sourceF):
            CopyFiles1(sourceF, targetF)


def CopyFiles2(sourceDir, targetDir):
    # 会将目录下所有文件都复制在一起，速度快，可以筛选文件 (最终得到的targetDir 中，目录结构全部打平)
    for root, dir1, filename in os.walk(sourceDir):
        # print(filename)
        for index in range(len(filename)):
            print(os.path.splitext(filename[index])[1])
            if os.path.splitext(filename[index])[1][0] == '.':  # 这里注意filename是个元组，splitext方法的时候只能是字符串
                old_path = os.path.join(root, filename[index])
                new_path = os.path.join(targetDir, filename[index])
                print("准备复制:", old_path, ", 到:", new_path)
                shutil.copyfile(old_path, new_path)


if __name__ == "__main__":
    time_start = time.time()
    # CopyFiles1(sourceDir, targetDir)
    CopyFiles2(sourceDir, targetDir)
    time_end = time.time()
    print('totally cost', time_end - time_start)
