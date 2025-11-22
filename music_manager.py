
import pygame
import os
import random
from threading import Thread
import time
class MusicManager:
    def __init__(self, songs_folder="songs"):
        self.songs_folder = songs_folder
        self.current_volume = 1.0  # Volumen actual (0.0 a 1.0)
        self.target_volume = 1.0   # Volumen objetivo
        self.is_fading = False     # Indica si hay un fade en progreso
        self.playlist = []         # Lista de canciones en orden aleatorio
        self.current_song_index = 0  # Índice de la canción actual
        try:
            pygame.mixer.init()
        except Exception as e:
            print(f"Error inicializando mixer: {e}")
            return
        self._load_playlist()
        self.fade_thread = None
    def _load_playlist(self):
        if not os.path.exists(self.songs_folder):
            print(f"Carpeta de canciones no encontrada: {self.songs_folder}")
            self.playlist = []
            return
        songs = [f for f in os.listdir(self.songs_folder)
                 if f.endswith(('.wav', '.mp3', '.ogg', '.flac'))]
        if not songs:
            print("No se encontraron canciones en la carpeta")
            self.playlist = []
            return
        self.playlist = [os.path.join(self.songs_folder, song) for song in songs]
        random.shuffle(self.playlist)
        self.current_song_index = 0
        print(f"Playlist cargada: {len(self.playlist)} canciones")
    def play(self):
        if not self.playlist:
            print("No hay canciones en la playlist")
            return
        try:
            if self.current_song_index >= len(self.playlist):
                self.current_song_index = 0
            song_path = self.playlist[self.current_song_index]
            print(f"Reproduciendo: {os.path.basename(song_path)}")
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.set_volume(self.current_volume)
            pygame.mixer.music.play()
            self._start_song_end_detector()
        except Exception as e:
            print(f"Error reproduciendo canción: {e}")
    def _start_song_end_detector(self):
        def detector():
            while pygame.mixer.music.get_busy():
                time.sleep(0.5)
            self.next_song()
        thread = Thread(target=detector, daemon=True)
        thread.start()
    def next_song(self):
        if not self.playlist:
            print("No hay canciones en la playlist")
            return
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        if self.current_song_index == 0:
            random.shuffle(self.playlist)
        self.play()
    def fade_out(self, duration=5.0):
        if self.is_fading:
            return  # Ya hay un fade en progreso
        self.is_fading = True
        self.target_volume = 0.0
        def fade_worker():
            start_time = time.time()
            start_volume = self.current_volume
            while time.time() - start_time < duration and self.current_volume > 0:
                elapsed = time.time() - start_time
                progress = elapsed / duration
                self.current_volume = start_volume * (1.0 - progress)
                self.current_volume = max(0.0, self.current_volume)
                pygame.mixer.music.set_volume(self.current_volume)
                time.sleep(0.05)  # Actualizar cada 50ms
            self.current_volume = 0.0
            pygame.mixer.music.set_volume(0.0)
            self.is_fading = False
        self.fade_thread = Thread(target=fade_worker, daemon=True)
        self.fade_thread.start()
    def fade_in(self, duration=5.0, target_volume=1.0):
        if self.is_fading:
            return  # Ya hay un fade en progreso
        self.is_fading = True
        self.target_volume = target_volume
        def fade_worker():
            start_time = time.time()
            start_volume = self.current_volume
            while time.time() - start_time < duration and self.current_volume < target_volume:
                elapsed = time.time() - start_time
                progress = elapsed / duration
                self.current_volume = start_volume + (target_volume - start_volume) * progress
                self.current_volume = min(target_volume, self.current_volume)
                pygame.mixer.music.set_volume(self.current_volume)
                time.sleep(0.05)  # Actualizar cada 50ms
            self.current_volume = target_volume
            pygame.mixer.music.set_volume(target_volume)
            self.is_fading = False
        self.fade_thread = Thread(target=fade_worker, daemon=True)
        self.fade_thread.start()
    def stop(self):
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"Error deteniendo música: {e}")
    def get_current_volume(self):
        return self.current_volume
    def set_volume(self, volume):
        self.current_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.current_volume)
