import os

SRC_DIR = "src"
TEST_DIR = "tests"

# --- DEINE MINIMALISTISCHEN VORLAGEN ---

CPP_TEMPLATE = """#include <iostream>
#include <vector>

#ifndef RUNNING_TESTS
int main() {
    
    return 0;
}
#endif
"""

TEST_TEMPLATE = """#include <gtest/gtest.h>
#include <vector>

TEST({suite_name}, {test_name}_BaseCase) {{
    
}}
"""

def generate_files():
    print("🧹 Erstelle leere C++ und Test-Dateien für alle Aufgaben...")
    count_src = 0
    count_test = 0

    # Gehe durch alle Kategorien in src/
    for category in os.listdir(SRC_DIR):
        cat_path = os.path.join(SRC_DIR, category)

        if not os.path.isdir(cat_path):
            continue

        # Test-Ordner für diese Kategorie sicherstellen
        test_cat_path = os.path.join(TEST_DIR, category)
        os.makedirs(test_cat_path, exist_ok=True)

        # Suche nach allen .md Dateien
        for file in os.listdir(cat_path):
            if file.endswith(".md"):
                problem_name = file.replace(".md", "")

                # Namen für GTest formatieren
                # Aus "01_Introductory" wird "Introductory"
                suite_name = category.split("_", 1)[-1]
                # Aus "apple_division" wird "AppleDivision"
                test_name = problem_name.replace("_", " ").title().replace(" ", "")

                # 1. Studenten .cpp Datei erstellen
                cpp_path = os.path.join(cat_path, f"{problem_name}.cpp")
                if not os.path.exists(cpp_path):
                    with open(cpp_path, "w", encoding="utf-8") as f:
                        f.write(CPP_TEMPLATE)
                    count_src += 1

                # 2. Test .cpp Datei erstellen
                test_cpp_path = os.path.join(test_cat_path, f"{problem_name}_test.cpp")
                if not os.path.exists(test_cpp_path):
                    with open(test_cpp_path, "w", encoding="utf-8") as f:
                        f.write(TEST_TEMPLATE.format(suite_name=suite_name, test_name=test_name))
                    count_test += 1

    print(f"✅ Fertig! {count_src} leere Source-Dateien und {count_test} leere Test-Dateien wurden erstellt.")

if __name__ == "__main__":
    generate_files()