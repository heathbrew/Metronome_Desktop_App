import tkinter as tk
from tkinter import ttk
import pygame
import logging
import sys
import traceback
import os

# Function to get resource paths, compatible with PyInstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Set up logging configuration without file handler
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Removed RotatingFileHandler to stop logging to a file
# file_handler = RotatingFileHandler("countdown_timer.log", maxBytes=5*1024*1024, backupCount=5)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# Stream handler for console output
console_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  # Moved formatter here
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class CountdownTimerApp:
    def __init__(self, root, enable_sound=True):
        self.root = root
        self.root.title("Cyberpunk Countdown Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")  # Dark background

        # Set custom icon if exists
        icon_path = resource_path(os.path.join("assets", "images", "Icon.png"))
        if os.path.exists(icon_path):
            try:
                self.root.iconphoto(False, tk.PhotoImage(file=icon_path))
                logging.info(f"Custom icon set from {icon_path}.")
            except Exception as e:
                logging.error(f"Error setting custom icon: {e}")
                traceback.print_exc()
        else:
            logging.warning(f"Icon file not found at {icon_path}. Using default icon.")

        # Initialize variables
        self.running = False
        self.remaining_time = 0
        self.tick = True
        self.timer = None
        self.enable_sound = enable_sound

        # Initialize pygame mixer
        if self.enable_sound:
            try:
                pygame.mixer.init()
                logging.info("Pygame mixer initialized successfully.")
            except Exception as e:
                logging.error(f"Error initializing pygame mixer: {e}")
                traceback.print_exc()
                self.enable_sound = False  # Disable sound if mixer fails to initialize

        # Load sounds if enabled
        if self.enable_sound:
            self.load_sounds()

        # Log initialization
        logging.info("Initialized Countdown Timer App with a cyberpunk theme.")

        # Create and style widgets
        self.create_widgets()
        self.style_widgets()

    def load_sounds(self):
        try:
            # Corrected sound paths based on directory structure
            tick_path = resource_path(os.path.join("assets", "sounds", "tick.wav"))
            tock_path = resource_path(os.path.join("assets", "sounds", "tock.wav"))
            alarm_path = resource_path(os.path.join("assets", "sounds", "alarm.wav"))

            self.tick_sound = pygame.mixer.Sound(tick_path)
            self.tock_sound = pygame.mixer.Sound(tock_path)
            self.alarm_sound = pygame.mixer.Sound(alarm_path)  # Load alarm sound
            logging.info("Loaded tick, tock, and alarm sound files successfully with pygame.")
            
            # Assign a dedicated channel for the alarm
            self.alarm_channel = pygame.mixer.Channel(1)  # Ensure channel 1 is available
        except Exception as e:
            logging.error(f"Error loading sound files with pygame: {e}")
            traceback.print_exc()
            self.tick_sound = None
            self.tock_sound = None
            self.alarm_sound = None
            self.alarm_channel = None

    def create_widgets(self):
        try:
            # Time input frame
            input_frame = ttk.Frame(self.root)
            input_frame.pack(pady=20)

            # Validation command to ensure only digits are entered
            vcmd = (self.root.register(self.validate_time_input), '%P')

            # Hours input
            self.hours_var = tk.StringVar(value="00")
            self.hours_entry = ttk.Entry(
                input_frame, textvariable=self.hours_var, width=3, font=("Helvetica", 24),
                validate='key', validatecommand=vcmd
            )
            self.hours_entry.grid(row=0, column=0, padx=5)

            # Minutes input
            self.minutes_var = tk.StringVar(value="00")
            self.minutes_entry = ttk.Entry(
                input_frame, textvariable=self.minutes_var, width=3, font=("Helvetica", 24),
                validate='key', validatecommand=vcmd
            )
            self.minutes_entry.grid(row=0, column=1, padx=5)

            # Seconds input
            self.seconds_var = tk.StringVar(value="00")
            self.seconds_entry = ttk.Entry(
                input_frame, textvariable=self.seconds_var, width=3, font=("Helvetica", 24),
                validate='key', validatecommand=vcmd
            )
            self.seconds_entry.grid(row=0, column=2, padx=5)

            # Time display
            self.time_label = ttk.Label(self.root, text="00:00:00", font=("Digital-7 Mono", 48))
            self.time_label.pack(pady=20)

            # Control buttons frame
            buttons_frame = ttk.Frame(self.root)
            buttons_frame.pack(pady=10)

            # Start button
            self.start_button = ttk.Button(buttons_frame, text="Start", command=self.start)
            self.start_button.grid(row=0, column=0, padx=5)

            # Stop button
            self.stop_button = ttk.Button(buttons_frame, text="Stop", command=self.stop)
            self.stop_button.grid(row=0, column=1, padx=5)

            # Reset button
            self.reset_button = ttk.Button(buttons_frame, text="Reset", command=self.reset)
            self.reset_button.grid(row=0, column=2, padx=5)

            # Sound toggle checkbox
            self.sound_var = tk.BooleanVar(value=self.enable_sound)
            self.sound_checkbox = ttk.Checkbutton(
                self.root, text="Enable Sound", variable=self.sound_var, command=self.toggle_sound
            )
            self.sound_checkbox.pack(pady=10)

            logging.debug("Widgets created successfully.")
        except Exception as e:
            logging.error(f"Error creating widgets: {e}")
            traceback.print_exc()

    def style_widgets(self):
        try:
            style = ttk.Style()
            style.theme_use('clam')

            # Style for the time label
            style.configure('TLabel', foreground='#39ff14', background='#1e1e1e')

            # Style for the entries
            style.configure('TEntry', foreground='#39ff14', background='#1e1e1e', insertcolor='#39ff14',
                            fieldbackground='#1e1e1e', font=('Digital-7 Mono', 24))

            # Style for the buttons
            style.configure('TButton', foreground='#1e1e1e', background='#39ff14',
                            font=('Arial', 12, 'bold'), padding=10)
            style.map('TButton',
                      foreground=[('pressed', '#1e1e1e'), ('active', '#1e1e1e')],
                      background=[('pressed', '#39ff14'), ('active', '#39ff14')])

            # Style for the checkbox
            style.configure('TCheckbutton', foreground='#39ff14', background='#1e1e1e',
                            font=('Arial', 10, 'bold'))

            logging.debug("Widgets styled successfully.")
        except Exception as e:
            logging.error(f"Error styling widgets: {e}")
            traceback.print_exc()

    def validate_time_input(self, P):
        """Validate that the input is either empty or consists of digits only."""
        if P.isdigit() or P == "":
            return True
        else:
            return False

    def start(self):
        logging.info("Start button pressed.")
        if not self.running:
            try:
                hours = int(self.hours_var.get())
                minutes = int(self.minutes_var.get())
                seconds = int(self.seconds_var.get())
                self.remaining_time = hours * 3600 + minutes * 60 + seconds
                if self.remaining_time <= 0:
                    raise ValueError("Time must be greater than 0.")
            except ValueError as ve:
                self.time_label.config(text="Invalid Input")
                logging.error(f"Invalid input in time fields: {ve}")
                return

            self.running = True
            self.update_display()
            logging.info(f"Time set to {self.format_time(self.remaining_time)}.")
            self.schedule_update_time()

    def stop(self):
        if self.running:
            if self.timer:
                self.root.after_cancel(self.timer)
                self.timer = None
                logging.debug("Cancelled scheduled update_time.")
            self.running = False
            logging.info("Countdown stopped.")

    def reset(self):
        logging.info("Reset button pressed.")
        self.stop()
        self.remaining_time = 0
        self.time_label.config(text="00:00:00")
        self.hours_var.set("00")
        self.minutes_var.set("00")
        self.seconds_var.set("00")
        logging.info("Countdown reset to 00:00:00.")

        # Stop the alarm sound if it's playing
        if self.enable_sound and self.alarm_channel and self.alarm_channel.get_busy():
            self.alarm_channel.stop()
            logging.info("Alarm sound stopped.")

    def schedule_update_time(self):
        try:
            self.timer = self.root.after(1000, self.update_time)
            logging.debug("Scheduled next update_time call in 1 second.")
        except Exception as e:
            logging.error(f"Error scheduling update_time: {e}")
            traceback.print_exc()

    def update_time(self):
        logging.debug("update_time called.")
        try:
            if self.running and self.remaining_time > 0:
                # Play tick or tock sound
                self.play_tick_tock()

                # Decrement time
                self.remaining_time -= 1
                self.update_display()
                logging.info(f"Time updated to {self.format_time(self.remaining_time)}. Remaining time: {self.remaining_time} seconds.")

                # Schedule next update
                self.schedule_update_time()
            else:
                self.stop()
                if self.remaining_time == 0:
                    self.time_label.config(text="Time's Up!")
                    logging.info("Countdown finished. Time's Up!")

                    # Play alarm sound on loop
                    if self.enable_sound and self.alarm_sound and self.alarm_channel:
                        self.alarm_channel.play(self.alarm_sound, loops=-1)
                        logging.info("Alarm sound started on loop.")
        except Exception as e:
            logging.error(f"Exception in update_time: {e}")
            traceback.print_exc()
            self.stop()

    def play_tick_tock(self):
        try:
            if self.enable_sound:
                sound_to_play = self.tick_sound if self.tick else self.tock_sound
                sound_desc = "tick" if self.tick else "tock"

                if sound_to_play:
                    sound_to_play.play()  # pygame's play is non-blocking
                    logging.info(f"Played {sound_desc} sound with pygame.")
                else:
                    logging.warning(f"{sound_desc.capitalize()} sound not loaded.")

                # Toggle tick/tock
                self.tick = not self.tick
            else:
                logging.debug("Sound playback is disabled.")
        except Exception as e:
            logging.error(f"Exception in play_tick_tock with pygame: {e}")
            traceback.print_exc()

    def update_display(self):
        try:
            formatted_time = self.format_time(self.remaining_time)
            self.time_label.config(text=formatted_time)
            logging.debug(f"Display updated to {formatted_time}.")
        except Exception as e:
            logging.error(f"Exception in update_display: {e}")
            traceback.print_exc()

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, secs = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(secs):02}"

    def toggle_sound(self):
        """Toggle sound on or off based on the checkbox."""
        self.enable_sound = self.sound_var.get()
        if not self.enable_sound:
            # Stop all sounds
            pygame.mixer.stop()
            logging.info("Sound disabled by user.")
        else:
            logging.info("Sound enabled by user.")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CountdownTimerApp(root, enable_sound=True)  # Ensure sound is enabled
        root.mainloop()
    except Exception as e:
        logging.critical(f"Unhandled exception: {e}")
        traceback.print_exc()
