"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
from tkinter import Widget, ttk
import ttk_helper
from ttk_helper import ToolTip

class ButtonsFrame(ttk.Frame):
    """
    Load Config Frame contains action buttons to load default simulation configuration for COVID and Influenza viruses
    """

    def __init__(self, master=None, height=100, width=100):
        """
        Constructor to set the master frame, height and width

        Parameters
        ----------
        :param master: parent frame
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
        Creates button widgets for loading config data of COVID and Influenza viruses
        """
        label_frame_label = ttk.Label(text="", style="Bold.TLabel")
        label_frame = ttk.LabelFrame(master=self, labelwidget=label_frame_label, height=self.height*0.95,
                                    width=self.width*0.90)
        label_frame.grid(row=0, column=0, pady=self.height * 0.02, padx=(0, self.width * 0.06))
        label_frame.grid_propagate(0)

        label_frame_label2 = ttk.Label(text="Simulation Mode")
        label_frame2 = ttk.LabelFrame(master=label_frame, labelwidget=label_frame_label2, height=float(label_frame.winfo_reqheight())/6,
                                    width=float(label_frame.winfo_reqwidth()))
        label_frame2.grid(row=0, column=0, columnspan=1, padx=(float(label_frame.winfo_reqwidth()) * 0.05, float(label_frame.winfo_reqwidth()) * 0.1))
        label_frame2.grid_propagate(0)

        self.my_var = tk.IntVar()
        self.my_var.set(2)
        rb1 = ttk.Radiobutton(master=label_frame2, text='Render Mode', variable=self.my_var, value=1)
        rb2 = ttk.Radiobutton(master=label_frame2, text='Live Simulation', variable=self.my_var, value=2)
        rb1.grid(row=0,column=0,columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.10, pady=float(label_frame.winfo_reqheight())*0.005, sticky=tk.W)
        rb2.grid(row=1,column=0,columnspan=1, padx=float(label_frame.winfo_reqwidth()) * 0.10, pady=float(label_frame.winfo_reqheight())*0.005, sticky=tk.W)

        label_frame_label3 = ttk.Label(text="Preventive Options")
        label_frame3 = ttk.LabelFrame(master=label_frame, labelwidget=label_frame_label3, height=float(label_frame.winfo_reqheight())/6,
                                    width=float(label_frame.winfo_reqwidth()))
        label_frame3.grid(row=1, column=0, columnspan=1, padx=(float(label_frame.winfo_reqwidth()) * 0.05, float(label_frame.winfo_reqwidth()) * 0.1))
        label_frame3.grid_propagate(0)

        #social_distance_enable = tk.IntVar()
        social_distance_check = ttk.Checkbutton(master=label_frame3, text='Enable Social Distancing')
        social_distance_check.invoke()

        social_distance_check.grid(row=0,column=0,columnspan=1, padx=float(label_frame.winfo_reqwidth())*0.10, pady=float(label_frame.winfo_reqheight())*0.005, sticky=tk.W)

        #mask_wearing_enable = tk.IntVar()
        mask_wearing_check = ttk.Checkbutton(master=label_frame3, text='Enable Mask Wearing')

        mask_wearing_check.grid(row=1,column=0,columnspan=1, padx=float(label_frame.winfo_reqwidth())*0.10, pady=float(label_frame.winfo_reqheight())*0.005, sticky=tk.W)
        mask_wearing_check.invoke()

        # Load Config Data button
        self.load_button = ttk.Button(master=label_frame, text="Start Covid Simulation", command="#")
        self.load_button.grid(row=4,column=0,columnspan=1, sticky="nesw", pady=float(label_frame.winfo_reqheight()) * 0.02)

        # Load influenza data button
        self.load_inf_button = ttk.Button(master=label_frame, text="Start Influenza Simulation", command="#")       
        self.load_inf_button.grid(row=5,column=0,columnspan=1, sticky="nesw", pady=float(label_frame.winfo_reqheight()) * 0.02)

        #Start custom sim button
        self.start_sim_button = ttk.Button(master=label_frame, text="Start Custom Simulation", command='#')
        self.start_sim_button.grid(row=6,column=0,columnspan=1, sticky="nesw", pady=float(label_frame.winfo_reqheight()) * 0.02)


        


        
        

        
