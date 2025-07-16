# main.py
import sqlite3, os
from datetime import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from plyer import notification

# Datenbankfunktion
DB = os.path.join(os.getcwd(), "flohmarkt.db")
def init_db():
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS buys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        artikel TEXT, preis REAL, zeit TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit(); conn.close()

def save_buy(artikel, preis):
    conn = sqlite3.connect(DB); c = conn.cursor()
    c.execute("INSERT INTO buys (artikel, preis) VALUES (?,?)", (artikel, preis))
    conn.commit(); conn.close()

def load_history():
    conn = sqlite3.connect(DB); c = conn.cursor()
    rows = c.execute("SELECT artikel, preis, zeit FROM buys ORDER BY zeit DESC").fetchall()
    conn.close()
    return rows

# Screens
class MainScreen(Screen):
    def scan(self):
        # Platzhalter für Scan + Preisabfrage
        artikel = "Beispielartikel"
        preis = round(5 + (datetime.now().second % 5), 2)
        save_buy(artikel, preis)
        notification.notify(title="Erfolgreich gespeichert", message=f"{artikel}: {preis} €")

class HistoryScreen(Screen):
    def on_pre_enter(self):
        self.ids.rv.data = [
            {"text": f"{a}: {p} € – {t}"} for a, p, t in load_history()
        ]

class FlohApp(App):
    def build(self):
        init_db()
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm

if __name__ == "__main__":
    FlohApp().run()

