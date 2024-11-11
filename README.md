
# Cyberpunk Countdown Timer

Welcome to the Cyberpunk Countdown Timer, a sleek and modern desktop application designed to provide a visually appealing countdown experience with optional sound effects.

<img width="302" alt="Screenshot 2024-11-12 004729" src="https://github.com/user-attachments/assets/cec2006d-a397-4663-9655-81331cb79be0">

## Features

- **User-Friendly Interface**: Input hours, minutes, and seconds effortlessly.
- **Start, Stop, and Reset Controls**: Manage the countdown with intuitive buttons.
- **Cyberpunk Aesthetics**: Enjoy a dark-themed interface with neon green accents.
- **Optional Sound Effects**: Enable or disable tick-tock sounds and an alarm upon countdown completion.
- **Custom Icon**: Personalized icon to enhance the application's visual appeal.

## Project Structure

The project is organized as follows:

```
Metronome_Desktop_App/
├── assets/
│   ├── images/
│   │   └── Icon.png
│   └── sounds/
│       ├── tick.wav
│       ├── tock.wav
│       └── alarm.wav
├── documentation/
├── venv/
├── .gitignore
├── build_exe.bat
├── metronome.py
├── metronome.spec
├── README.md
├── requirements.txt
└── setup_env.bat
```

- **assets/**: Contains all asset files used in the application.
  - **images/**: Stores image files.
    - `Icon.png`: Custom icon for the application window.
  - **sounds/**: Stores sound files.
    - `tick.wav`: Sound played for the "tick" effect.
    - `tock.wav`: Sound played for the "tock" effect.
    - `alarm.wav`: Alarm sound played when the countdown reaches zero.
- **documentation/**: Contains project documentation and design diagrams.
- **venv/**: Virtual environment for managing project dependencies.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **build_exe.bat**: Batch script to build the application into a standalone .exe file using PyInstaller.
- **metronome.py**: Main Python script for the countdown timer application.
- **metronome.spec**: PyInstaller spec file generated during the build process.
- **README.md**: This readme file.
- **requirements.txt**: Lists Python packages required for the project.
- **setup_env.bat**: Batch script to set up the virtual environment.

## Setup Instructions

Follow these steps to set up and run the Cyberpunk Countdown Timer application on your local machine.

1. **Clone the Repository**  
   Clone the project repository to your local machine using Git.
   ```bash
   git clone https://github.com/heathbrew/Metronome_Desktop_App.git
   ```

2. **Navigate to the Project Directory**  
   Change to the project directory.
   ```bash
   cd Metronome_Desktop_App
   ```

3. **Set Up the Virtual Environment**  
   Run the setup script to create and activate the virtual environment.
   ```bash
   setup_env.bat
   ```

4. **Activate the Virtual Environment**  
   Activate the virtual environment. If you haven't run the setup script, you can activate it manually.
   ```bash
   # On Windows
   venv\Scriptsctivate.bat

   # On Unix or MacOS
   source venv/bin/activate
   ```

5. **Install Dependencies**  
   Install all necessary Python packages using the requirements.txt file.
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Application**  
   Start the countdown timer application.
   ```bash
   python metronome.py
   ```

## Usage

- **Input Time**: Enter the desired countdown time in hours, minutes, and seconds.
- **Start**: Click the "Start" button to begin the countdown.
- **Stop**: Click the "Stop" button to pause the countdown.
- **Reset**: Click the "Reset" button to reset the countdown to zero.
- **Enable Sound**: Toggle the "Enable Sound" checkbox to turn sound effects on or off.

## Sound Effects

- **Tick-Tock Sounds**: The application plays alternating tick and tock sounds during the countdown.
- **Alarm Sound**: An alarm sound is played when the countdown reaches zero.

_Note_: Ensure that the sound files (`tick.wav`, `tock.wav`, `alarm.wav`) are present in the `assets/sounds/` directory.

## Design Overview

The application follows a structured flow:

1. **Initialization**:
   - Sets up the Tkinter root window with a dark theme.
   - Initializes variables and loads sound files.
   - Creates and styles widgets for user interaction.

2. **Event Handling**:
   - **Start**: Validates input time, sets the remaining time, and begins the countdown.
   - **Stop**: Cancels scheduled updates and stops the countdown.
   - **Reset**: Stops the timer, resets the remaining time, and clears input fields.

3. **Timer Functionality**:
   - Updates the displayed time every second.
   - Plays tick-tock sounds if enabled.
   - Checks if the countdown has reached zero and plays the alarm sound if enabled.

4. **Error Handling**:
   - Utilizes message boxes to notify users of critical errors, such as failing to load assets or sounds.
   - Logs informational and error messages to the console for debugging purposes.

## Building the Executable

To distribute the application as a standalone .exe file, follow these steps using the provided `build_exe.bat` script.

1. **Ensure Directory Structure**  
   Confirm that your project directory matches the following structure, with all assets correctly placed:

   ```
   Metronome_Desktop_App/
   └── dist/
       └── metronome.exe
   ```

2. **Run the Build Script**  
   Execute the `build_exe.bat` script to build the application into a standalone .exe file.
   ```bash
   build_exe.bat
   ```

3. **Locate the Executable**  
   Upon successful completion, the standalone executable `metronome.exe` will be available in the `dist/` directory within your project folder.

4. **Run the Executable**  
   Navigate to the `dist/` folder and double-click `metronome.exe` to launch the application.
![image](https://github.com/user-attachments/assets/3f70efa5-40b4-479e-b1b3-9a4b8311f2f2)

---

Feel free to reach out if you encounter any further issues or need additional assistance. Happy coding!
