# Część 0 - przygotowanie projektu

1. Przygotuj projekt w PyCharmie o następującej strukturze:
```
|
|__src/
    |_classes/
    |   |_ space.py
    |   |_ task.py
    |   |_ task_manager.py
    |   |_ user.py
    |
    |_data/
    |   |_spaces/
    |   |_ users/
    |
    |_scripts/
    |
    |_utils/
        |_file_operations.py
```

Stwórz również środowisko wirtualne.


2. W folderze `utils/` stwórz plik `file_operations.py` i napisz w nim dwie funkcje:
- `write_to_json()`, która przyjmie listę/słownik oraz ścieżkę do pliku i zapisze obiekt w pliku pod daną ścieżką
- `read_from_json()`, która przyjmie ścieżkę do pliku, wczyta podany plik oraz zwróci jego zawartość

Przetestuj powyższe funkcje, najlepiej wywołując je wewnątrz folderu `scripts/` a zapisując dane wewnątrz folderu `data/`.