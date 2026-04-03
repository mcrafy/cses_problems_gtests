import os

# Konfiguration
SRC_ROOT = "src"
IDEA_DIR = ".idea/runConfigurations"
PROJECT_NAME = "CSES_AutoTest"

# Vorlage für die XML-Datei
XML_TEMPLATE = """<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="{name}" type="CMakeGoogleTestRunConfigurationType" factoryName="Google Test" REDIRECT_INPUT="false" ELEVATE="false" USE_EXTERNAL_CONSOLE="false" EMULATE_TERMINAL="false" PASS_PARENT_ENVS_2="true" PROJECT_NAME="{project}" TARGET_NAME="{target}" CONFIG_NAME="Debug" RUN_TARGET_PROJECT_NAME="{project}" RUN_TARGET_NAME="{target}" TEST_MODE="SUITE_TEST">
    <method v="2">
      <option name="com.jetbrains.cidr.execution.CidrBuildBeforeRunTaskProvider$BuildBeforeRunTask" enabled="true" />
      <option name="BeforeTestRunTask" enabled="true" />
    </method>
  </configuration>
</component>"""

def generate():
    # Stelle sicher, dass der Zielordner existiert
    if not os.path.exists(IDEA_DIR):
        os.makedirs(IDEA_DIR)
        print(f"Ordner {IDEA_DIR} wurde erstellt.")

    count = 0
    # Gehe durch alle Kategorien (z.B. 01_Introductory)
    for category in os.listdir(SRC_ROOT):
        cat_path = os.path.join(SRC_ROOT, category)
        if os.path.isdir(cat_path):
            # Gehe durch alle .cpp Dateien im Kategorie-Ordner
            for file in os.listdir(cat_path):
                if file.endswith(".cpp"):
                    problem_name = file.replace(".cpp", "")
                    target_name = f"{problem_name}_test"

                    # Erstelle den Inhalt der XML
                    xml_content = XML_TEMPLATE.format(
                        name=target_name,
                        project=PROJECT_NAME,
                        target=target_name
                    )

                    # Dateipfad für die XML
                    xml_path = os.path.join(IDEA_DIR, f"{target_name}.xml")

                    # XML schreiben
                    with open(xml_path, "w") as f:
                        f.write(xml_content)

                    print(f"Erstellt: {xml_path}")
                    count += 1

    print(f"\nFertig! {count} Konfigurationen wurden generiert.")

if __name__ == "__main__":
    generate()