from pathlib import Path
file_path = Path(__file__).with_name("example.txt")
if file_path.exists():
    print(file_path.read_text(encoding="utf-8"))
else:
    print("File missing. Run write_file.py first.")
