# game_app.py
import tkinter as tk
from tkinter import messagebox
from game_data import GAME_STRUCTURE
# Importa todos tus métodos del otro archivo
import methods_engine as me 

class NumericalMethodsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Métodos Numéricos - El Juego") # [cite: 596]
        self.root.geometry("800x600")
        
        # Estado del juego [cite: 701, 702]
        self.username = "Jugador 1"
        self.errors_committed = 0
        self.time_elapsed = "0h 0m"
        self.medals = []
        
        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.current_screen = None
        self.show_main_menu()

    def clear_screen(self):
        """Limpia el frame principal para la nueva pantalla."""
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = tk.Frame(self.main_frame)
        self.current_screen.pack(fill=tk.BOTH, expand=True)

    def show_main_menu(self):
        """Muestra el menú principal [cite: 596-600]"""
        self.clear_screen()
        
        tk.Label(self.current_screen, text="¡Aprende, Juega, Domina!", font=("Arial", 24)).pack(pady=20)
        
        tk.Button(self.current_screen, text="JUGAR", command=self.show_chapter_menu).pack(pady=10)
        tk.Button(self.current_screen, text="VER PERFIL", command=self.show_user_menu).pack(pady=10)
        tk.Button(self.current_screen, text="SALIR", command=self.root.quit).pack(pady=10)

    def show_user_menu(self):
        """Muestra el menú de usuario [cite: 601-606]"""
        self.clear_screen()
        
        tk.Label(self.current_screen, text=f"PERFIL DE: {self.username}", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.current_screen, text=f"TIEMPO TRANSCURRIDO: {self.time_elapsed}").pack(pady=5) # [cite: 604]
        tk.Label(self.current_screen, text=f"ERRORES COMETIDOS: {self.errors_committed}").pack(pady=5) # [cite: 605]
        
        tk.Label(self.current_screen, text="MEDALLAS GANADAS:", font=("Arial", 14)).pack(pady=10)
        for medal in self.medals:
            tk.Label(self.current_screen, text=f"🏅 {medal}").pack()
        if not self.medals:
            tk.Label(self.current_screen, text="(Aún no hay medallas)").pack()
            
        tk.Button(self.current_screen, text="VOLVER", command=self.show_main_menu).pack(pady=20)
        # Aquí iría la lógica de "Cerrar Sesión" [cite: 606, 703]

    def show_chapter_menu(self):
        """Muestra el menú de capítulos [cite: 607, 609, 617]"""
        self.clear_screen()
        
        tk.Label(self.current_screen, text="LECCIONES", font=("Arial", 20)).pack(pady=10)
        
        for chapter_name in GAME_STRUCTURE.keys():
            # Crear un botón para cada capítulo
            # 'lambda c=chapter_name:' es necesario para pasar el nombre correcto
            btn = tk.Button(self.current_screen, text=chapter_name, 
                            command=lambda c=chapter_name: self.show_level_menu(c))
            btn.pack(fill=tk.X, padx=50, pady=5)
            
        tk.Button(self.current_screen, text="VOLVER AL MENÚ", command=self.show_main_menu).pack(pady=20)

    def show_level_menu(self, chapter_name):
        """Muestra el menú de niveles para un capítulo [cite: 608, 618]"""
        self.clear_screen()
        
        tk.Label(self.current_screen, text=chapter_name, font=("Arial", 20)).pack(pady=10)
        
        levels = GAME_STRUCTURE[chapter_name]['levels']
        for level_name in levels.keys():
            btn = tk.Button(self.current_screen, text=level_name,
                            command=lambda l=level_name: self.start_lesson(chapter_name, l, 0))
            btn.pack(fill=tk.X, padx=50, pady=5)
            
        tk.Button(self.current_screen, text="VOLVER A CAPÍTULOS", command=self.show_chapter_menu).pack(pady=20)

    def start_lesson(self, chapter, level, lesson_index):
        """Muestra la lección actual [cite: 714]"""
        self.clear_screen()
        
        lessons = GAME_STRUCTURE[chapter]['levels'][level]
        
        # Chequear si completó el nivel
        if lesson_index >= len(lessons):
            messagebox.showinfo("¡Felicidades!", f"¡Nivel '{level}' completado!")
            if f"{level}" not in self.medals:
                self.medals.append(f"{level}") # [cite: 729]
            self.show_level_menu(chapter)
            return

        current_lesson = lessons[lesson_index]
        lesson_type = current_lesson['type']
        
        tk.Label(self.current_screen, text=f"{level} - Lección {lesson_index + 1}", font=("Arial", 18)).pack(pady=10)
        
        if lesson_type == 'explicativa':
            self.show_explicativa(current_lesson, chapter, level, lesson_index)
        elif lesson_type == 'practica' or lesson_type == 'examen':
            self.show_practica(current_lesson, chapter, level, lesson_index)
            
    def show_explicativa(self, lesson, chapter, level, lesson_index):
        """Muestra una lección explicativa [cite: 715]"""
        tk.Label(self.current_screen, text=lesson['content'], wraplength=600, justify=tk.LEFT).pack(pady=20, padx=20)
        
        # Botón para continuar a la siguiente lección
        tk.Button(self.current_screen, text="CONTINUAR",
                  command=lambda: self.start_lesson(chapter, level, lesson_index + 1)).pack(pady=20)
        
        # Lógica de castigo (ejemplo)
        # tk.Button(self.current_screen, text="¡Me equivoqué!",
        #           command=lambda: self.apply_penalty('alto', chapter, level)).pack(pady=5)

    def show_practica(self, lesson, chapter, level, lesson_index):
        """Muestra una lección de práctica o examen [cite: 716, 718]"""
        tk.Label(self.current_screen, text=f"Pregunta: {lesson['content']}", wraplength=600).pack(pady=10, padx=20)
        
        # Esto es para preguntas de opción múltiple, como en [cite: 626]
        if 'options' in lesson:
            for option in lesson['options']:
                btn = tk.Button(self.current_screen, text=option,
                                command=lambda o=option: self.check_answer(o, lesson, chapter, level, lesson_index))
                btn.pack(pady=5)
                
        # Esto es para problemas que llaman al motor de métodos (ej. [cite: 636])
        elif 'problem_id' in lesson:
            # Aquí se mostraría la tabla del problema [cite: 641] y un campo de entrada
            tk.Label(self.current_screen, text=f"(Mostrando problema: {lesson['problem_id']})").pack(pady=10)
            tk.Label(self.current_screen, text="Ingresa tu respuesta:").pack()
            entry = tk.Entry(self.current_screen)
            entry.pack(pady=5)
            
            # Botón para checar la respuesta (no implementado)
            # Habría que llamar a la función de 'methods_engine.py' y comparar
            tk.Button(self.current_screen, text="REVISAR",
                      command=lambda: messagebox.showinfo("WIP", "Lógica de revisión no implementada")).pack(pady=10)


    def check_answer(self, user_answer, lesson, chapter, level, lesson_index):
        """Revisa la respuesta de una lección de práctica"""
        correct_answer = lesson['answer']
        lesson_type = lesson['type']
        
        if user_answer == correct_answer:
            messagebox.showinfo("¡Correcto!", "¡Muy bien! Pasando a la siguiente lección.")
            self.start_lesson(chapter, level, lesson_index + 1)
        else:
            # Aplicar castigo según el boceto [cite: 723-727]
            self.errors_committed += 1
            if lesson_type == 'practica':
                messagebox.showerror("Incorrecto", f"La respuesta correcta era '{correct_answer}'. [cite: 696]\nRegresando a la lección anterior. [cite: 726]")
                self.start_lesson(chapter, level, lesson_index - 1) # Castigo intermedio
            elif lesson_type == 'examen':
                messagebox.showerror("Incorrecto", f"Respuesta incorrecta. [cite: 718]\nReiniciando la lección. [cite: 727]")
                self.start_lesson(chapter, level, lesson_index) # Castigo bajo