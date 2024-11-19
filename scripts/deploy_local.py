import os
import shutil

def deploy():
    src_dir = os.getcwd()
    
    # destination directory for deployment
    dest_dir = "C:/deployed_app"
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # copy all files from source to destination
    for file_name in os.listdir(src_dir):
        full_file_name = os.path.join(src_dir, file_name)
        
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest_dir)

    print(f"Application deployed to {dest_dir}")


if __name__ == "__main__":
    deploy()
