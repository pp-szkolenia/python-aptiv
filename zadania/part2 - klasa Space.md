# Część 2 - implementacja klasy `Space`
W tej części zaimplementujesz funkcjonalności klasy `Space`. 

1. Stwórz klasę `Space` wraz z jej konstruktorem. Niech klasa posiada następujące atrybuty:
- name (`str`)
- created_at (`datetime`)
- tasks (`list[Task]`)

Parametrami konstruktora niech będą:
- space_name (`str`) - nazwa space'a
- created_at (`datetime`) - data i czas utworzenia
- tasks_json (`list[dict]`) - lista słowników reprezentujących zadania
- already_in_db (`bool`) - ten parametr będzie określał, czy space znajduje się już w bazie, czy jeszcze nie. Ta informacja przyda się później

Atrybut `tasks` utwórz wykorzystując informacje zawarte w `tasks_json`.

Użyj *type annotations*.


2. Stwórz metody `__str__()` i `__repr__`, które będą zwracać stringi zawierające informacje o nazwie space'a oraz liczbie zadań. 

Przykładowa reprezentacja: `Space(name=<nazwa>, n_tasks=<n>)`

Przykładowa stringifikacja: `Space: <nazwa> (<n> tasks)`


3. Napisz metodę `_convert_tasks_to_json()`, która na podstawie atrybutu `tasks` wyznaczy listę słowników reprezentującą wszystkie zadania. Zwróć tę listę słowników. Podpowiedź: użyj `list comprehension`.


4. Napisz metodę `save_to_database()`, która użyje `_convert_tasks_to_json()`, aby przypisać do zmiennej JSONa reprezentującego listę zadań. Następnie utwórz słownik o następujących kluczach:
- `name`
- `created_at`
- `tasks`

którego wartościami będą odpowiednio: nazwa space'a, jego data i czas utworzenia oraz lista zadań w nim zawartych. Informacje do tego potrzebne znajdują się w atrybutach obiektu lub zostały zwrócone przez `_convert_tasks_to_json()`.

Pamiętaj, że cała zawartość utworzonego w ten sposób słownika musi być możliwa do zapisania w pliku .json, a więc nie wszystkie typy obiektów mogą się w takim słowniku znajdować.

Na koniec wywołaj funkcję `write_to_json()` i zapisz utworzony słownik do pliku w folderze `data/spaces/`. Nazwa pliku .json powinna odpowiadać nazwie space'a.


5. Napisz metodę `add_task()`, która:
- przyjmie jako argument słownik reprezentujący jedno zadanie
- zamieni go na obiekt klasy `Task`
- doda ten obiekt do listy zadań (skorzystaj z właściwego atrybutu) 
- zapisze space do "bazy danych" (użyj odpowiedniej metody)


6. Napisz metodę `add_task_from_input()`, wewnątrz której pojawią się wywołania funkcji `input()`, które pobiorą od użytkownika wszystkie potrzebne informacje na temat dodawanego zadania. Będzie to alternatywny dla `add_task()` sposób dodawania zadań.


7. W folderze `scripts/` utwórz plik, w którym przetestujesz działanie klasy `Space`.
