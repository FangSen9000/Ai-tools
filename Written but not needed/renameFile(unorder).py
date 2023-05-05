import os
import glob

count = 1
for file in glob.glob("*.*"):
    if file.endswith('.json') or file.endswith('.mp4'):
        new_filename = str(count).zfill(6) + os.path.splitext(file)[1]
        with open(file, 'rb') as f:
            with open(new_filename, 'wb') as nf:
                nf.write(f.read())
        os.remove(file)
        count +=1
print("所有文件已重命名完毕！")
