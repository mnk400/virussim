"""
Simulator Command Window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk


class SimCommandFrame(tk.Frame):
    """
    Sim Command Frame contains action buttons to start render mode and start virus simulation
    """

    def __init__(self, master=None, height=100, width=100):
        """
        Constructor to initialize height, width and set master frame

        Parameters
        ----------
        :param master: master frame
        :param height: height of frame
        :param width: width of frame
        """
        super().__init__(master, height=height, width=width)
        self.master = master
        self.height = height
        self.width = width
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the Render Mode and View Simulation buttons
        """
        self.render_button = tk.Button(self)
        self.render_button["text"] = "Render Mode"
        self.render_button["command"] = "hi there, everyone!"
        self.render_button.pack(expand=True, fill='both', side="top")

        self.start_sim_button = tk.Button(self, text="View Simulation", fg="red",
                              command='#')
        self.start_sim_button.pack(expand=True, fill='both', side="bottom")