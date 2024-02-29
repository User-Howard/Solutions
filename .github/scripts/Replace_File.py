import os
import shutil

def move_files(source_dir):
    """
    将指定目录下的特定文件移动到另一个指定目录
    """
    
    filenames = os.listdir(source_dir)
    print('filenames', filenames)
    for filename in filenames:
        if filename.find('-') == -1:
            continue

        judge = filename.split('-')[0]
        print(filename)
        src_path = os.path.join(source_dir, filename)
        
        problem = filename.replace(f"{judge}-", "")
        problem_store_folder = f"./Solutions/{judge.upper()}/{os.path.splitext(problem)[0]}"
        if not os.path.exists(problem_store_folder):
           os.makedirs(problem_store_folder)
        dst_path = os.path.join(problem_store_folder, os.path.splitext(problem)[0]+f"-{len(os.listdir(problem_store_folder))}"+os.path.splitext(problem)[1])
        shutil.move(src_path, dst_path)
                

if __name__ == "__main__":
    source_dir = "."
    move_files(source_dir)
