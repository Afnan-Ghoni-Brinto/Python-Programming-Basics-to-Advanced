from pathlib import Path
file_path = Path(__file__).with_name("example.txt")
file_path.write_text("Hello Python!\nThis is a sample file.\n", encoding="utf-8")
print("Written:", file_path)
