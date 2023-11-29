#  Merge two files into one 

def merge_files(f1_path, f2_path, of_path):
  with open(f1_path, 'r') as f1:
    f1_data = f1.read()
  with open(f2_path, 'r') as f2:
    f2_data = f2.read()
  
  with open(of_path, 'w') as of:
    of.write(f1_data)
    of.write(f2_data)


merge_files("a.txt", "b.txt", "c.txt")
