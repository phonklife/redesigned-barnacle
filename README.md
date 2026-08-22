# Suno-Archive-Automator

Zautomatyzowane archiwum motywów muzycznych opartych na bazie tematów muzycznych artysty **virtualluser**.

Projekt ten stanowi kompletny, modularny i automatyczny system służący do katalogowania, archiwizowania oraz analizy motywów muzycznych w utworach stworzonych za pomocą serwisu Suno przez artystę **virtualluser**.

## 🚀 Główne Funkcje Systemu

1. **Automatyczny Generator Archiwum (`generator.py`)**:
   - Skrypt napisany w czystym Pythonie 3, który automatycznie buduje całą strukturę plików i folderów archiwum oraz interaktywny pulpit nawigacyjny.
   - Posiada wbudowaną bazę wysokiej jakości przeanalizowanych utworów wraz z tekstami, gatunkami muzycznymi oraz powtarzającymi się motywami.
   - Obsługuje mechanizm automatycznego sprawdzania i pobierania aktualizacji z publicznych kanałów Suno (z zachowaniem pełnej odporności na błędy sieciowe/blokady zapory sieciowej).

2. **Integracja z Obsidian Vault (`/archive`)**:
   - Generuje w pełni funkcjonalny, zgodny z Obsidianem folder wiedzy.
   - **Tracks (`archive/Tracks/`)**: Indywidualne notatki markdown dla każdego utworu zawierające szczegółowe metadane (YAML frontmatter), opisy, teksty piosenek oraz dwukierunkowe linki do motywów.
   - **Motifs (`archive/Motifs/`)**: Notatki dla każdego z motywów muzycznych (np. *TR-808 Cowbell*, *Slavic Noir Atmosphere*, *Melancholic Guitar Riff*), wymieniające powiązane z nimi utwory.
   - **Obsidian Canvas Map (`archive/virtualluser_music_map.canvas`)**: Interaktywny, automatycznie pozycjonowany graf powiązań między utworami a ich motywami, do wyświetlenia bezpośrednio w aplikacji Obsidian.

3. **Interaktywny Pulpit Web (`index.html`)**:
   - Piękny, nowoczesny panel wdrożony bezpośrednio na GitHub Pages za pomocą GitHub Actions.
   - **Zintegrowany Odtwarzacz Audio**: Pozwala na odsłuch utworów bezpośrednio z CDN serwisu Suno.
   - **Wyszukiwarka i Filtrowanie**: Dynamiczne filtrowanie utworów po tytule, tekście, gatunku lub konkretnym motywie muzycznym.
   - **Interaktywny Graf 2D (HTML5 Canvas)**: Renderowany w czasie rzeczywistym graf powiązań sieciowych. Kliknięcie w węzeł utworu automatycznie ładuje go do odtwarzacza, a kliknięcie w motyw filtruje powiązane utwory.

4. **Automatyzacja CI/CD (GitHub Actions)**:
   - Zintegrowany workflow `.github/workflows/static.yml` automatycznie uruchamia generator przy każdym pushu do gałęzi `main` i publikuje wygenerowaną stronę na GitHub Pages.

---

## 📂 Struktura Projektu

```text
├── .github/
│   └── workflows/
│       └── static.yml          # Skonfigurowany przepływ pracy wdrożenia GitHub Pages
├── archive/                    # Wygenerowane archiwum Obsidian Vault
│   ├── Tracks/                 # Notatki o utworach
│   ├── Motifs/                 # Notatki o motywach muzycznych
│   ├── Artist - virtualluser.md # Profil artysty
│   └── virtualluser_music_map.canvas # Interaktywna mapa powiązań (Obsidian Canvas)
├── generator.py                # Główny skrypt silnika generującego
├── index.html                  # Wygenerowany interaktywny interfejs webowy
└── README.md                   # Niniejsza dokumentacja
```

---

## 🛠️ Uruchomienie Lokalne i Użycie

Aby ręcznie wygenerować archiwum oraz zaktualizować stronę internetową, upewnij się, że masz zainstalowany Python 3, a następnie uruchom:

```bash
python3 generator.py
```

### Import do Obsidian:
1. Pobierz lub sklonuj folder `archive/` z tego repozytorium.
2. Otwórz aplikację **Obsidian**.
3. Wybierz opcję **"Open folder as vault"** (Otwórz folder jako sejf).
4. Wskaż pobrany katalog `archive/`.
5. Upewnij się, że masz włączoną wbudowaną wtyczkę **Canvas**, a następnie otwórz plik `virtualluser_music_map.canvas`, aby cieszyć się interaktywną mapą motywów muzycznych!
