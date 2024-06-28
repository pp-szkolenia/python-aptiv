# Część 1 - implementacja klasy `Task`
W tej części zaimplementujesz podstawowe funkcjonalności klasy `Task`. Później zostanie ona rozbudowana o kolejne.

1. Stwórz klasę `Task` wraz z jej konstruktorem. Niech posiada następujące atrybuty:
- description (`str`)
- assignee (`str`)
- due_date (`datetime.date`)
- priority (`int`)
- time_logged (`datetime.timedelta`)
- is_complete (`bool`)
- tags (`list[str]`)
- comments (`list[dict[str, str]]`)

Parametrem konstruktora niech będzie `task_data` (typu `dict`). Będzie to słownik wczytany z pliku `.json` a więc nie może zawierać obiektów typu `datetime.timedelta` czy `datetime.date`.

Użyj *type annotations*. 

2. Stwórz metodę `__str__()`, która będzie zwracać stringa zawierającego w kolejnych liniach informacje o:
- description
- status ("Done", "To do")
- assignee
- due_date
- priority
- tags
- liczbie komentarzy

W celu wyświetlenia informacji o statusie może przydać się zdefiniowanie *class attribute* z odpowiednim słownikiem mapującym wartości logiczne na status.

3. Napisz metodę `jsonify()`, która nie przyjmie żadnych argumentów oprócz *self* i zwróci słownik z danymi możliwymi do zapisania w pliku `.json` (czyli obiekty związane z datą i czasem powinny zostać zapisane jako stringi lub liczby). 

Niech liczba określająca ilość zalogowanego czasu będzie wyrażona w godzinach.

Dane w słowniku powinny obejmować:
- description
- assignee
- due_date
- priority
- time_logged
- is_complete
- tags
- comments

4. Napisz metodę `edit_description()`, która przyjmie jako argument *new_description*. Metoda ta powinna sprawdzić, czy przekazana wartość jest stringiem i w takim wypadku nadpisać nim atrybut *description*. W przeciwnym wypadku powinna wyprintować odpowiednie ostrzeżenie.

5. Napisz metodę `mark_as_complete()`. Niech sprawdzi ona czy zadanie zostało już ukończone. Jeżeli nie, to status powinien zostać zmieniony na ukończony. Jeżeli zadanie już było ukończone, należy wyprintować odpowiednie ostrzeżenie.

6. Napisz metodę `change_priority()`, która zmieni priorytet zadania, sprawdzając najpierw czy przekazana wartość jest dozwolona (należy do zbioru {1, 2, 3}). W celu sprawdzenia, może przydać się odpowiedni *class attribute*.

7. Napisz metodę `log_time()`, która doda przekazaną do niej timedeltę do dotychczas zalogowanego czasu. Powinno odbyć się najpierw sprawdzenie czy przekazano argument odpowiedniego typu.

8. Napisz dwie metody: `add_comment()` oraz `_validate_comment()`. Ich działanie wynika z ich nazw, a jako poprawny komentarz należy uznać taki, który jest słownikiem o kluczach "author" oraz "text" pod którymi znajdą się obiekty typu *str*.

9. W folderze `scripts/` utwórz plik, w którym przetestujesz działanie klasy `Task`.