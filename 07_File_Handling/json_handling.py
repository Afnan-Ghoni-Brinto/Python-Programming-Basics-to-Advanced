import json
from pathlib import Path
student = {"name": "Rahim", "age": 20, "skills": ["Python", "HTML"]}
file_path = Path(__file__).with_name("student.json")
file_path.write_text(json.dumps(student, indent=4), encoding="utf-8")
loaded = json.loads(file_path.read_text(encoding="utf-8"))
print("Loaded:", loaded)
