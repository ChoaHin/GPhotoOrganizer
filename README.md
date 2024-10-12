# GPhotoOrganizer

GPhotoOrganizer is a desktop application designed to help users organize photos, videos, and metadata files in a chosen folder. It separates files by type and allows users to easily categorize and sort them. The application features both a command-line interface (CLI) for backend operations and a graphical user interface (GUI) for user-friendly interactions.

## Features

- **File Sorting:**
  - Automatically separates photos, edited photos, videos, and metadata into respective folders.
- **File Types Supported:**
  - Photos: `.png`, `.jpg`, `.webp`
  - Edited Photos: `-edited.png`, `-edited.jpg`, `-edited.webp`
  - Videos: `.mp4`, `.mkv`, `.avi`
  - Metadata: `.json`, `.xml`, `.csv`
- **Command-Line and GUI Support:**
  - Run as a command-line tool for advanced users.
  - Use a graphical interface for ease of use.
  
## Project Structure

```plaintext
GPhotoOrganizer/
│
├── backend/
│   ├── __init__.py
│   ├── main.py            # Backend entry point for CLI operations
│   ├── services/
│   │   └── organizing.py   # File organizing logic
│   ├── utils/
│   │   └── file_ops.py     # File operations (e.g., scanning, copying files)
│   └── classes/
│       └── photoMetadata.py # Handles photo metadata
│
├── gui/
│   ├── __init__.py
│   ├── main.py            # GUI entry point
│   └── organizer_gui.py   # GUI logic
│
├── data/
│   └── sample_photos/      # Folder for sample photos used in testing
│
└── tests/
    └── test_organizer.py   # Test cases for backend logic
```

## Requirements

- Python 3.8+
- Tkinter (for the GUI)
- PyInstaller (for packaging the application into an executable)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/GPhotoOrganizer.git
   cd GPhotoOrganizer
   ```

2. **Set up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies:**
   Install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Tests (Optional):**
   You can run tests to ensure everything is working as expected:
   ```bash
   pytest
   ```

## Running the Application

### Command-Line Interface (CLI)

To use the backend organizer functionality from the command line:
```bash
python backend/main.py
```

### Graphical User Interface (GUI)

To launch the GUI version of the application:
```bash
python gui/main.py
```

## Building an Executable

If you want to create a standalone executable of the application:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller to package the GUI version:
   ```bash
   pyinstaller --onefile --windowed gui/main.py
   ```

The executable will be created in the `dist/` folder.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For any questions, feel free to reach out or open an issue on GitHub.

---
