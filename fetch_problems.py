import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import time
import re

BASE_URL = "https://cses.fi/problemset/"

def fetch_all_problems():
    print("🚀 Scanne CSES Hauptseite (ohne General)...")
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        content = soup.find('div', class_='content')
        current_category = None
        cat_counter = 1

        # Kategorien, die wir ignorieren wollen
        blacklist = ["General", "Common", "Introduction"]

        for element in content.find_all(['h2', 'a']):
            if element.name == 'h2':
                title = element.text.strip()

                # Prüfen, ob die Kategorie ignoriert werden soll
                if any(x in title for x in blacklist):
                    current_category = None
                    continue

                # Namen säubern und "Problems" am Ende entfernen
                clean_name = title.replace(" Problems", "").replace(" ", "_").replace("/", "_")
                current_category = f"{cat_counter:02d}_{clean_name}"
                cat_counter += 1
                print(f"\n📂 Starte Kategorie: {current_category}")

            # Nur fetchen, wenn wir uns in einer gültigen Kategorie befinden
            elif element.name == 'a' and current_category and '/problemset/task/' in element.get('href', ''):
                problem_name = element.text.strip().lower().replace(" ", "_")
                problem_id = element['href'].split('/')[-1]

                target_dir = os.path.join("src", current_category)
                os.makedirs(target_dir, exist_ok=True)

                save_problem(problem_id, target_dir, problem_name)
                time.sleep(0.4)

    except Exception as e:
        print(f"❌ Fehler: {e}")

def save_problem(problem_id, folder, name):
    md_path = os.path.join(folder, f"{name}.md")

    # Auskommentiert, damit deine alten Dateien überschrieben werden!
    # if os.path.exists(md_path):
    #     print(f"⏩ Überspringe (existiert bereits): {name}")
    #     return

    url = f"https://cses.fi/problemset/task/{problem_id}"
    try:
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'html.parser')
        task_content = soup.find('div', class_='content')

        # HTML zu Markdown
        markdown_text = md(str(task_content), heading_style="ATX", bullets="-")

        # --- MATHJAX FIX START ---
        # Wandelt LaTeX-Befehle in echte Zeichen für CLion um
        markdown_text = markdown_text.replace(r"\rightarrow", "→")
        markdown_text = markdown_text.replace(r"\leftarrow", "←")
        markdown_text = markdown_text.replace(r"\le", "≤")
        markdown_text = markdown_text.replace(r"\ge", "≥")
        markdown_text = markdown_text.replace(r"\dots", "…")
        markdown_text = markdown_text.replace(r"\times", "×")
        markdown_text = markdown_text.replace(r"\cdot", "·")
        markdown_text = markdown_text.replace(r"\neq", "≠")

        # Formeln wie 10^6 oder 2^n in HTML-Superscript verwandeln
        markdown_text = re.sub(r"(\d+|[a-zA-Z])\^([a-zA-Z0-9]+)", r"\1<sup>\2</sup>", markdown_text)
        # --- MATHJAX FIX END ---

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"# {name.replace('_', ' ').title()}\n\n")
            f.write(markdown_text)
            f.write(f"\n\n---\n**Source:** [{url}]({url})")
        print(f"✅ {name}")
    except Exception as e:
        print(f"⚠️ Fehler bei {name}: {e}")

if __name__ == "__main__":
    if not os.path.exists("src"):
        os.makedirs("src")
    fetch_all_problems()