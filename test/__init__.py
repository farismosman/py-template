import sys, os

parent_dir = os.path.pardir
full_path = os.path.join(os.path.dirname(__file__), parent_dir)

sys.path.append(os.path.abspath(full_path))
