import zipfile
import sys
import os

def search_and_extract(zip_path, keyword, output_dir="extracted"):
    # Crée le dossier de sortie si nécessaire
    os.makedirs(output_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as z:
        for file_name in z.namelist():
            # On ignore les répertoires
            if file_name.endswith('/'):
                continue

            with z.open(file_name) as f:
                try:
                    text = f.read().decode("utf-8", errors="ignore")
                except Exception as e:
                    print(f"Impossible de lire {file_name}: {e}")
                    continue

                if keyword in text:
                    print(f"Mot-clé '{keyword}' trouvé dans: {file_name}")
                    
                    # Extraire le fichier dans le répertoire de sortie
                    out_path = os.path.join(output_dir, file_name)
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    with open(out_path, "wb") as out_f:
                        out_f.write(text.encode("utf-8"))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <zip_path> <keyword>")
        sys.exit(1)

    zip_path = sys.argv[1]
    keyword = sys.argv[2]
    search_and_extract(zip_path, keyword)
