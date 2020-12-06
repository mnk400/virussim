"""
Load Config Window application window for Virussim application, built using Tkinter

Created on 2nd Dec, 2020
@author Yatish Pitta
"""

import tkinter as tk
import tkinter.ttk as ttk
import gui.ttk_helper
from gui.ttk_helper import ToolTip
from gui.data_store import DataStore


class SetConfigFrame(ttk.Frame):
    """
    Frame widget for configuring and customizing simulation
    """

    def __init__(self, master=None, height=100, width=70):
        """
        Constructor to set the master frame, height and width

        Parameters
        ----------
        :param master: parent frame
        :param height: height of frame
        :param width: width of frame
        """
        super().__init__(master, height=height, width=width,)
        self.master = master
        self.height = height
        self.width = width
        self.data = DataStore.get_instance()
        self.create_widgets()

    def create_widgets(self):
        """
        Creates slider and button widgets for configuring simulation
        """
        
        # Main label frame to hold widgets
        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(text="Modify Configuration", style="Bold.TLabel")
        label_frame = ttk.LabelFrame(master=self, labelwidget=label_frame_label, height=self.height * 0.95,
                                    width=self.width * 0.95)
        #, font="helvetica 24 bold", background="#ECECEC" text="Modify Configuration"
        label_frame.grid(row=0, column=0, pady=self.height * 0.02, padx=(self.width * 0.03, 0))
        label_frame.grid_propagate(0)
        
        # Population value slider
        population_label = ttk.Label(master=label_frame, anchor=tk.E, text='Population:')
        population_label.grid(row=0, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)
        popToolTip = ToolTip(widget = population_label, text = "The size of the population for the simulation")

        population_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = popToolTip))
        population_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = popToolTip))

        population_scale_val = tk.StringVar()
        population_scale_val.set('1000')

        population_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=200, to=3000, 
                                    length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:self.data.population_val.set('%d' % int(float(s))))
        population_scale.set(1000)
        population_scale.grid(row=0, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                              pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)

        population_scale_val_label = ttk.Label(label_frame, textvariable=self.data.population_val)
        # population_scale_val_label.place(in_=population_scale, bordermode='outside', x=0, y=0, anchor='s')
        population_scale_val_label.grid(row=0, column=1, columnspan=1, sticky = tk.W)


        # Social distancing value slider
        social_distancing_label = ttk.Label(master=label_frame, text='Social Distancing:')
        # social_distancing_label.grid(row=1, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
        #             pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        social_distancing_label.grid(row=1, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)
        socToolTip = ToolTip(widget = social_distancing_label, text = "The percentage of the total population who will be social distancing")

        social_distancing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = socToolTip))
        social_distancing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = socToolTip))

        social_distancing_val = tk.StringVar()
        social_distancing_val.set('50%')

        social_distance_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100, 
                                         length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:social_distancing_val.set('%d%%' % int(float(s))))
        social_distance_scale.set(50)
        social_distance_scale.grid(row=1, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                   pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)

        distancing_val_label = ttk.Label(label_frame, textvariable=social_distancing_val)
        # distancing_val_label.place(in_=social_distance_scale, bordermode='outside', x=0, y=0, anchor='s')
        distancing_val_label.grid(row=1, column=1, columnspan=1, sticky = tk.W)

        # Hospital capacity value slider
        hostpital_capacity_label = ttk.Label(master=label_frame, text='Hospital Capacity:')
        hostpital_capacity_label.grid(row=2, column=0, columnspan=1, sticky = tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        hosToolTip = ToolTip(widget = hostpital_capacity_label, 
                    text = "The hospital capacity as a percentage of the population. \nWe found in our research that the hospital capacity is generally a function of the population.")

        hostpital_capacity_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = hosToolTip))
        hostpital_capacity_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = hosToolTip))

        hostpital_capacity_val = tk.StringVar()
        hostpital_capacity_val.set('20%')

        hospital_capacity_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:hostpital_capacity_val.set('%d%%' % int(float(s))))
        hospital_capacity_scale.set(20)
        hospital_capacity_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        hospital_capacity_val_label = ttk.Label(label_frame, textvariable=hostpital_capacity_val)
        # hostpital_capacity_val_label.place(in_=hospital_capacity_scale, bordermode='outside', x=0, y=0, anchor='s')
        hospital_capacity_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        # Recovery time value slider
        recovery_time_label = ttk.Label(master=label_frame, text='Recovery Time:')
        recovery_time_label.grid(row=3, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        recoveryToolTip = ToolTip(widget = recovery_time_label, 
                    text = "The time a person needs to recover from the virus in unit of frames. \nThis takes into account both if the person is recovering without medical attention or if they needed hospitalization. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        recovery_time_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = recoveryToolTip))
        recovery_time_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = recoveryToolTip))

        recovery_time_val = tk.StringVar()
        recovery_time_val.set('150')

        recovery_time_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=100, to=500,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:recovery_time_val.set('%d' % int(float(s))))
        recovery_time_scale.set(150)
        recovery_time_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        recovery_time_val_label = ttk.Label(label_frame, textvariable=recovery_time_val)
        # recovery_time_val_label.place(in_=recovery_time_scale, bordermode='outside', x=0, y=0, anchor='s')
        recovery_time_val_label.grid(row = 3, column=1, columnspan=1, sticky=tk.W)
        # # Death rate value slider
        # self.death_rate_var = tk.DoubleVar()
        # label5 = tk.Label(master=label_frame, anchor='center', text='Death rate')
        # label5.grid(row=4, column=0, padx=float(label_frame.winfo_reqwidth()) * 0.025,
        #             pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=1)
        # label5.grid_propagate(0)
        # death_rate_scale = tk.Scale(master=label_frame, variable=self.death_rate_var, orient='horizontal', from_=0, to=100,
        #                             width=25, sliderlength=100, length=float(label_frame.winfo_reqwidth()) * 0.65)
        # death_rate_scale.grid(row=4, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
        #                       pady=float(label_frame.winfo_reqheight()) * 0.025, columnspan=3)
        # death_rate_scale.grid_propagate(0)

        # R value setter button
        r_value_label = ttk.Label(master=label_frame, text='R value:')
        r_value_label.grid(row=4, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        rValueToolTip = ToolTip(widget = r_value_label, 
                    text = "The reproduction rate or the R value of the virus. \nThis is defined as the average number of people an infected person goes on to infect.")

        r_value_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = rValueToolTip))
        r_value_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = rValueToolTip))

        r_value_val = tk.StringVar()
        r_value_val.set('3.00')

        r_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:r_value_val.set('%0.2f' % float(s)))
        r_value_scale.set(3.00)
        r_value_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        r_value_val_label = ttk.Label(label_frame, textvariable=r_value_val)
        # r_value_val_label.place(in_=r_value_scale, bordermode='outside', x=0, y=0, anchor='s')
        r_value_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)
        # K value setter button
        k_value_label = ttk.Label(master=label_frame,  text='K value:')
        k_value_label.grid(row=5, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        kValueToolTip = ToolTip(widget = r_value_label, 
                    text = "The K value of the virus. \nThis is defined as the dispersion rate of the R value of the virus.")

        k_value_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = kValueToolTip))
        k_value_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = kValueToolTip))

        k_value_val = tk.StringVar()
        k_value_val.set('0.10')

        k_value_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=3,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:k_value_val.set('%0.2f' % float(s)))
        k_value_scale.set(0.1)
        k_value_scale.grid(row=5, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        k_value_val_label = ttk.Label(label_frame, textvariable=k_value_val)
        # k_value_val_label.place(in_=k_value_scale, bordermode='outside', x=0, y=0, anchor='s')
        k_value_val_label.grid(row=5, column=1, columnspan=1, sticky=tk.W)
        

        #Enforce Social Distancing At
        enforce_social_distancing_label = ttk.Label(master=label_frame,  text='Social Distancing Starts:')
        enforce_social_distancing_label.grid(row=6, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        enforceSocToolTip = ToolTip(widget = r_value_label, 
                    text = "The time at which the city officials decided to announce the social distancing advisory. \n-1 refers to the city officials never providing a social distancing advisory. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        enforce_social_distancing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = enforceSocToolTip))
        enforce_social_distancing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = enforceSocToolTip))

        enforce_social_distancing_val = tk.StringVar()
        enforce_social_distancing_val.set('200')

        enforce_social_distancing_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=-1, to=1000,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:enforce_social_distancing_val.set('%d' % int(float(s))))
        enforce_social_distancing_scale.set(200)
        enforce_social_distancing_scale.grid(row=6, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        enforce_social_distancing_val_label = ttk.Label(label_frame, textvariable=enforce_social_distancing_val)
        enforce_social_distancing_val_label.grid(row=6, column=1, columnspan=1, sticky=tk.W)

        #Mask Wearing Starts At
        enforce_mask_wearing_label = ttk.Label(master=label_frame,  text='Mask Mandate Starts:')
        enforce_mask_wearing_label.grid(row=7, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        enforceMaskToolTip = ToolTip(widget = r_value_label, 
                    text = "The time at which the city officials decided to announce the mask mandate. \n-1 refers to the city officials never mandating masks in their area. \nIn our simulation, 1 day roughly amounts to 5 frames.")

        enforce_mask_wearing_label.bind("<Enter>", lambda event: self.enter(event = event, tooltip = enforceMaskToolTip))
        enforce_mask_wearing_label.bind("<Leave>", lambda event: self.leave(event = event, tooltip = enforceMaskToolTip))

        enforce_mask_wearing_val = tk.StringVar()
        enforce_mask_wearing_val.set('200')

        enforce_mask_wearing_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=-1, to=1000,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:enforce_mask_wearing_val.set('%d' % int(float(s))))
        enforce_mask_wearing_scale.set(200)
        enforce_mask_wearing_scale.grid(row=7, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        enforce_mask_wearing_val_label = ttk.Label(label_frame, textvariable=enforce_mask_wearing_val)
        enforce_mask_wearing_val_label.grid(row=7, column=1, columnspan=1, sticky=tk.W)

        #Set mask effectiveness
        mask_effectiveness_label = ttk.Label(master=label_frame,  text='Mask Effectiveness:')
        mask_effectiveness_label.grid(row=8, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        mask_effectiveness_set_button = ttk.Button(label_frame, text="Set Mask Effectiveness", command=self.openMaskWindow)
        mask_effectiveness_set_button.grid(row=8, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3, sticky='ew')

        #Set mortality rate
        mortality_rate_label = ttk.Label(master=label_frame,  text='Mortality Rate:')
        mortality_rate_label.grid(row=9, column=0, columnspan=1, sticky=tk.W, padx=float(label_frame.winfo_reqwidth()) * 0.03)

        mortality_rate_set_button = ttk.Button(label_frame, text="Set Mortality Rate", command=self.openMortalityWindow)
        mortality_rate_set_button.grid(row=9, column=1, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3, sticky='ew')
        
    def openMaskWindow(self): 

        newWindow = tk.Toplevel(self.master, height = 700, width = 700) 

        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(master = newWindow, text="Set Mask Effectiveness", style = "Bold.TLabel")
        label_frame = ttk.LabelFrame(master=newWindow, labelwidget=label_frame_label, height = 700, width = 700)
        label_frame.grid(row = 0, column = 0, columnspan=1)
        mask_type_header_label = ttk.Label(master=label_frame,  text='Mask Type')
        mask_effectivenss_header_label = ttk.Label(master=label_frame,  text='Mask Effectiveness')
        empty_label_1  = ttk.Label(master=label_frame,  text='        ')
        mask_type_header_label.grid(row = 1, column = 0, columnspan=1, sticky = tk.W)
        empty_label_1.grid(row = 1, column = 1, columnspan=1)
        mask_effectivenss_header_label.grid(row = 1, column = 2, columnspan=1)

        #Cloth Mask
        cloth_mask_effectiveness = ttk.Label(master=label_frame,  text='Cloth Mask:')
        cloth_mask_effectiveness.grid(row = 2, column = 0, columnspan=1, sticky = tk.W)
        cloth_mask_effectiveness_val = tk.StringVar()
        cloth_mask_effectiveness_val.set('50%')
        cloth_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:cloth_mask_effectiveness_val.set('%d%%' % int(float(s))))
        cloth_mask_effectiveness_scale.set(50)
        cloth_mask_effectiveness_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        cloth_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=cloth_mask_effectiveness_val)
        cloth_mask_effectiveness_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        #Surgical Mask
        surgical_mask_effectiveness = ttk.Label(master=label_frame,  text='Surgical Mask:')
        surgical_mask_effectiveness.grid(row = 3, column = 0, columnspan=1, sticky = tk.W)
        surgical_mask_effectiveness_val = tk.StringVar()
        surgical_mask_effectiveness_val.set('70%')
        surgical_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:surgical_mask_effectiveness_val.set('%d%%' % int(float(s))))
        surgical_mask_effectiveness_scale.set(70)
        surgical_mask_effectiveness_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        surgical_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=surgical_mask_effectiveness_val)
        surgical_mask_effectiveness_val_label.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        #N95 Mask
        n95_mask_effectiveness = ttk.Label(master=label_frame,  text='N95 Mask:')
        n95_mask_effectiveness.grid(row = 4, column = 0, columnspan=1, sticky = tk.W)
        n95_mask_effectiveness_val = tk.StringVar()
        n95_mask_effectiveness_val.set('90%')
        n95_mask_effectiveness_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0, to=100,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:n95_mask_effectiveness_val.set('%d%%' % int(float(s))))
        n95_mask_effectiveness_scale.set(90)
        n95_mask_effectiveness_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        n95_mask_effectiveness_val_label = ttk.Label(label_frame, textvariable=n95_mask_effectiveness_val)
        n95_mask_effectiveness_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)

    def openMortalityWindow(self): 

        newWindow = tk.Toplevel(self.master, height = 700, width = 700) 

        style = ttk.Style(self)
        style.configure("Bold.TLabel", font=("Helvetica", 19, "bold"))
        label_frame_label = ttk.Label(master = newWindow, text="Set Mortality Rate", style = "Bold.TLabel")
        label_frame = ttk.LabelFrame(master=newWindow, labelwidget=label_frame_label, height = 700, width = 700)
        label_frame.grid(row = 0, column = 0, columnspan=1)
        mask_type_header_label = ttk.Label(master=label_frame,  text='Age Group')
        mask_effectivenss_header_label = ttk.Label(master=label_frame,  text='Mortality Rate')
        empty_label_1  = ttk.Label(master=label_frame,  text='        ')
        mask_type_header_label.grid(row = 1, column = 0, columnspan=1, sticky = tk.W)
        empty_label_1.grid(row = 1, column = 1, columnspan=1)
        mask_effectivenss_header_label.grid(row = 1, column = 2, columnspan=1)

        #0-19 Age Group
        zeronineteen_mortality_rate = ttk.Label(master=label_frame,  text='0-19:')
        zeronineteen_mortality_rate.grid(row = 2, column = 0, columnspan=1, sticky = tk.W)
        zeronineteen_mortality_rate_val = tk.StringVar()
        zeronineteen_mortality_rate_val.set('0.003%')
        zeronineteen_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:zeronineteen_mortality_rate_val.set('%0.03f%%' % float(s)))
        zeronineteen_mortality_rate_scale.set(0.003)
        zeronineteen_mortality_rate_scale.grid(row=2, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        zeronineteen_mortality_rate_val_label = ttk.Label(label_frame, textvariable=zeronineteen_mortality_rate_val)
        zeronineteen_mortality_rate_val_label.grid(row=2, column=1, columnspan=1, sticky=tk.W)

        #20-49 Age Group
        twentyfortynine_mortality_rate = ttk.Label(master=label_frame,  text='20-49:')
        twentyfortynine_mortality_rate.grid(row = 3, column = 0, columnspan=1, sticky = tk.W)
        twentyfortynine_mortality_rate_val = tk.StringVar()
        twentyfortynine_mortality_rate_val.set('0.02%')
        twentyfortynine_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:twentyfortynine_mortality_rate_val.set('%0.03f%%' % float(s)))
        twentyfortynine_mortality_rate_scale.set(0.02)
        twentyfortynine_mortality_rate_scale.grid(row=3, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        twentyfortynine_mortality_rate_val_label = ttk.Label(label_frame, textvariable=twentyfortynine_mortality_rate_val)
        twentyfortynine_mortality_rate_val_label.grid(row=3, column=1, columnspan=1, sticky=tk.W)

        #50-69 Age Group
        fiftysixtynine_mortality_rate = ttk.Label(master=label_frame,  text='50-69:')
        fiftysixtynine_mortality_rate.grid(row = 4, column = 0, columnspan=1, sticky = tk.W)
        fiftysixtynine_mortality_rate_val = tk.StringVar()
        fiftysixtynine_mortality_rate_val.set('0.05%')
        fiftysixtynine_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:fiftysixtynine_mortality_rate_val.set('%0.03f%%' % float(s)))
        fiftysixtynine_mortality_rate_scale.set(0.05)
        fiftysixtynine_mortality_rate_scale.grid(row=4, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        fiftysixtynine_mortality_rate_val_label = ttk.Label(label_frame, textvariable=fiftysixtynine_mortality_rate_val)
        fiftysixtynine_mortality_rate_val_label.grid(row=4, column=1, columnspan=1, sticky=tk.W)

        #70 > Age Group
        seventyplus_mortality_rate = ttk.Label(master=label_frame,  text='70-100:')
        seventyplus_mortality_rate.grid(row = 5, column = 0, columnspan=1, sticky = tk.W)
        seventyplus_mortality_rate_val = tk.StringVar()
        seventyplus_mortality_rate_val.set('0.054%')
        seventyplus_mortality_rate_scale = ttk.Scale(master=label_frame, orient='horizontal', from_=0.001, to=10,
                                           length=float(label_frame.winfo_reqwidth()) * 0.35, command=lambda s:seventyplus_mortality_rate_val.set('%0.03f%%' % float(s)))
        seventyplus_mortality_rate_scale.set(0.054)
        seventyplus_mortality_rate_scale.grid(row=5, column=2, padx=float(label_frame.winfo_reqwidth()) * 0.05,
                                     pady=float(label_frame.winfo_reqheight()) * 0.01, columnspan=3)
        
        seventyplus_mortality_rate_val_label = ttk.Label(label_frame, textvariable=seventyplus_mortality_rate_val)
        seventyplus_mortality_rate_val_label.grid(row=5, column=1, columnspan=1, sticky=tk.W)

    
    def get_population_value(self) -> int:
        """
        Get current value of the population slider
        :return: Population value
        """
        return self.population_var

    def set_popluation_value(self, val: int):
        """
        Sets and updates the population value of the slider
        :param val:
        """
        self.population_var = val

    def get_social_distance_value(self) -> float:
        """
        Get current value of the social distance proportion
        :return: Social distance proportion
        """
        return self.social_distance_var

    def set_social_distance_value(self, val: float):
        """
        Sets and updates the social distance proportion value of the slider
        :param val:
        """
        self.social_distance_var = val

    def get_hospital_capacity_value(self) -> int:
        """
        Get current value of the hospital capacity
        :return: Social distance proportion
        """
        return self.hospital_capacity_var

    def set_hospital_capacity_value(self, val: int):
        """
        Sets and updates the hospital capacity value of the slider
        :param val:
        """
        self.hospital_capacity_var = val

    def get_recovery_time_value(self) -> int:
        """
        Get current value of the recovery time
        :return: Social distance proportion
        """
        return self.recovery_time_var

    def set_recovery_time_value(self, val: int):
        """
        Sets and updates the recovery time value of the slider
        :param val:
        """
        self.recovery_time_var = val

    def get_death_rate_value(self) -> float:
        """
        Get current value of the death rate
        :return: Social distance proportion
        """
        return self.death_rate_var

    def set_death_rate_value(self, val: float):
        """
        Sets and updates the death rate value of the slider
        :param val:
        """
        self.death_rate_var = val

    def get_r_value(self) -> int:
        """
        Get current r value
        :return: Social distance proportion
        """
        return self.r_val

    def set_r_value(self, val: int):
        """
        Sets and updates the r value of the slider
        :param val:
        """
        self.r_val = val

    def get_k_value(self) -> float:
        """
        Get current k value
        :return: Social distance proportion
        """
        return self.k_val

    def set_k_value(self, val: float):
        """
        Sets and updates the k value of the slider
        :param val:
        """
        self.k_val = val

    def enter(self, event, tooltip):
            tooltip.showtip()

    def leave(self, event, tooltip):
            tooltip.hidetip()