import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            n_alb = int(self._view.txtNumAlbumMin)
        except ValueError:
            self._view.show_alert("Inserisci un valore intero")
            return
        if n_alb < 0:
            self._view.show_alert("Inserisci un valore maggiore di 0")
            return

        self._model.build_graph(n_alb)
        self._view.btnArtistsConnected.disabled = True
        self._view.btnSearchArtists.disabled = True
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {self._model._graph.number_of_nodes()} nodi(artisti) e {self._model._graph.number_of_edges()} archi"))
        self._view.update_page()

    def handle_connected_artists(self, e):
        self._view.btnArtistsConnected.disabled = False
        self._view.btnSearchArtists.disabled = False
        self._view.ddArtist.options.clear()
        for a in self._model._lista_archi():
            self._view.ddArtist.options.append(ft.dropdown.Option(str(a[0])))
        self._view.update_page()

        if self._view.ddArtist is None:
            self._view.show_alert("Inserisci uno degli archi nel dropdown")
            return

        i = self._view.ddArtist.options[0]
        dimesione = self._model.analisiComponente(i)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Aristi direttamenrte collegati: {dimesione} a {i} "))
        self._view.update_page()

    def handle_riocerca(self,e):
        n_art = int(self._view.txtNumAlbumMin)
        try:
            d_min = float(self._view.txtMinDuration.value)
        except ValueError:
            self._view.show_alert("Inserisci un numero frazionario")
            return

        if d_min < 0 and n_art > 1:
            self._view.show_alert("Inserisci una d_min maggiore di 0 o un n_art compreso")
            return






