# Część 3 - implementacja klasy `TaskManager`
W tej części zaimplementujesz funkcjonalności klasy `TaskManager`.

1. Stwórz klasę `TaskManager` wraz z jej konstruktorem. Niech klasa posiada następujące atrybuty:
- name (`str`)
- spaces (`dict[str, Space]`)

a jako argument niech przyjmuje nazwę aplikacji.

Słowników space'ów niech zostanie przechwycony z wywołania metody `_load_spaces()`.

Użyj *type annotations*.


2. Stwórz metody `__str__()` i `__repr__`, które będą zwracać stringi zawierające reprezentację i stringifikację.

Przykładowa reprezentacja: `TaskManager(name=<nazwa>)`

Przykładowa stringifikacja: `<nazwa>`


3.  Napisz metodę statyczną `_load_spaces()`. Powinna ona:
- wylistować zawartość folderu z danymi space'ów
- na tej podstawie stworzyć listę nazw space'ów
- na tej podstawie stworzyć listę ścieżek do plików reprezentujących poszczególne space'y
- zainicjować pusty słownik wynikowy
- przeiterować **jednocześnie** po liście nazw space'ów oraz liście ścieżek do nich
- w każdej iteracji należy wczytać dane z właściwego pliku, przygotować je odpowiednio a następnie utworzyć obiekt klasy `Space`

Niech funkcja zwraca utworzony wcześniej słownik, do którego w pętli zostały dodawane na bieżąco tworzone space'y.


4. Napisz metodę `add_space()`, która przyjmie nazwę space'a, utworzy odpowiedni obiekt i doda go do słownika w atrybucie `spaces`.


5. Napisz metodę `_validate_space_name()`, która sprawdzi czy nazwa space'a, którego próbujesz dodać, nie została zajęta. Niech funkcja ta zwraca `True` albo `False`, w zależności od tego, czy operacja zakończy się sukcesem.

Zastosuj nową metodę wewnątrz `add_space()`.


6. W folderze `scripts/` utwórz plik, w którym przetestujesz działanie klasy `TaskManager`.
