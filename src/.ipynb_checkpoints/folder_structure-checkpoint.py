import os
import argparse

def get_args():
    '''
    Gets arguments from command line interface
    '''
    #declare argument parser
    parser = argparse.ArgumentParser("Create Git project folder structure")
    #Describe commands
    p_desc = "Project name / Desired folder name"
    
    #Define as optional argument
    optional = parser.add_argument_group("optional arguments")
    optional.add_argument("-p", help=p_desc, default="project")
    args = parser.parse_args()
    
    return args


def make_folders(args):
    root = "."    
    
    project = args.p
    src = "src"
    data = "data"
    notebooks = "notebooks"    
    
    src_path = f"{root}/{project}/{src}"
    data_path = f"{root}/{project}/{data}"
    notebooks_path = f"{root}/{project}/{notebooks}"    
    
    os.makedirs(src_path)
    os.makedirs(data_path)
    os.makedirs(notebooks_path)    

def main():
    args = get_args()
    make_folders(args)
    
if __name__ == "__main__":
    main()
    
