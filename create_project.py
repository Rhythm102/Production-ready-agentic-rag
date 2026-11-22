from pathlib import Path
# current working directory
root = Path(".")

# making folders 
folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data", 
    "template",
    "static",
    "upload",
    "test",
]

# files to create

files =[
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]

#create folders
for folder in folders:
    (root/folder).mkdir(parents=True, exist_ok=True)

# create files
for file in files:
    (root/file).touch(exist_ok=True)

print("project files created succesfully")