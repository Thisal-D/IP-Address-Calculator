from tkinter import  CENTER, W,E, Tk,Label, PhotoImage,Frame,Button,Entry,Radiobutton,IntVar
from tkinter.font import BOLD, Font
import os
import sys




def create_files_loading() :
    main_window.after(100,main_root_new)

def vercion_set():
     #version
    global version
    version = Label(main_window ,text="V 10.3" ,fg="#ffffff" ,bg="#100e17")
    version.place(rely=0.01 ,relx=0.96)
###################################################
###################################################
###################################################
################################################### 
###################################################
###################################################
def superscripted(val,start,end):
    sup= {"0":"⁰","1":"¹","2":"²","3":"³","4":"⁴","5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹"}
    try:
        try:
            val = int(val)
        except :
            val = val.replace(",","")
            val = int(val)
        power = 0
        while  True:
            if 2**power >= val:
                break
            power += 1
        power = str(power)
        super_script = ""
        for i in power:
            super_script += sup[i]
        value = str(start +"2"+super_script+end)
    except:
        value = ""
    return value

#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
def geometry_reader():
    global window_relx_geomatry_read
    global window_rely_geomatry_read
    root_geomatry = main_window.geometry()
    window_relx = ""
    window_rely = ""

    window_relx_can_start = False
    window_relx_can_end = False
    window_rely_can_start = False
    for i in root_geomatry:
        for x in window_relx:
            for y in range(0,10) :
                if str(x) == str(y) :
                    window_relx_can_end = True
        
        if window_relx_can_end == True and i == "+" :
            window_rely_can_start = True
            window_relx_can_start = False

        if i == "+" and window_relx_can_end == False :
            window_relx_can_start = True

        if window_relx_can_start == True :
            window_relx += i
        
        if window_rely_can_start == True :
            window_rely += i
        
    window_relx_geomatry_read = window_relx.replace("+","")
    window_rely_geomatry_read = window_rely.replace("+","")
    main_window.after(20,geometry_reader)
    

#############################################################
#############################################################
#############################################################

def loading001():
    global loading_display001
    loading_display001 = 0
    global loading_resolution_change_frame001
    global loading_resolution_change_label001
    loading_resolution_change_frame001 = Frame(main_window ,bg="#101010")
    loading_resolution_change_label001= Label(loading_resolution_change_frame001,text="Loading...",bg="#101010" ,fg="#00ff0f")
    
    def loading_001():
        global loading_display001
        loading_display001 += 1 
        loading_resolution_change_label001.config(font=Font(size=font_most ,weight=BOLD))
        loading_resolution_change_frame001.place(relwidth=1 ,relheight=1)
        loading_resolution_change_label001.place(relx=0.47 ,rely=0.45)

        if loading_display001 <= 10 :
            main_window.after(50,loading_001)
        else:
            loading_resolution_change_label001.destroy()
            loading_resolution_change_frame001.destroy()
    loading_001()
    

def change_fslm_vlsm():
    # VLSM or FSLM Frame
    global vlsm_or_flsm_label
    global vlsm_or_flsm_frame
    vlsm_or_flsm_frame = Frame(main_window ,bg="#100e17")
    vlsm_or_flsm_label = Label(vlsm_or_flsm_frame ,bg="#100e17")
    vlsm_or_flsm_label.pack()

    # VLSM or FSLM RadioButton
    global W100
    global W101
    var1 = IntVar()
    W100 = Radiobutton(vlsm_or_flsm_frame, variable=var1 ,value=1 
                    ,bg="#000000" ,fg="#000000" ,activebackground="#000000" ,command=FLSM_mode ,cursor="hand2")
    W101 = Radiobutton(vlsm_or_flsm_frame, variable=var1 ,value=2 
                    ,bg="#000000" ,fg="#000000" ,activebackground="#000000" ,command=VLSM_mode ,cursor="hand2")  
    global variable_length_label
    global fixed_length_label
    fixed_length_label = Button(vlsm_or_flsm_frame, text="FLSM" ,bg="#000000" ,fg="#00ff00" ,cursor="hand2" ,command=FLSM_mode,border=False ,activebackground="#000000" ,activeforeground="#00FF00") 
    variable_length_label = Button(vlsm_or_flsm_frame, text="VLSM" ,bg="#000000" ,fg="#00ff00" ,cursor="hand2",command=VLSM_mode,border=False ,activebackground="#000000" ,activeforeground="#00FF00")

   
    #didplayinformation about ..
    info1 = Label(main_window,text="Fixed Length Subnet-Mask",font=Font(weight=BOLD,size=8) ,bg="#100e17",fg="#00FFFF")
    info2 = Label(main_window,text="Variable Length Subnet-Mask",font=Font(weight=BOLD,size=8),bg="#100e17",fg="#00FFFF")
    ######################################################
    def info1_display(e):
        global fixed_length_button_live 
        global info_diplay_time_wait

        info_diplay_time_wait  = 10
        fixed_length_button_live = True
        def loop():
            global info_diplay_time_wait
            info_diplay_time_wait += 7
            if info_diplay_time_wait > 100 :
                if fixed_length_button_live == True:
                    if real_resolution == 720:
                        f_size ,rel_x ,rel_y = 8 ,0.06 ,0.04
                    elif real_resolution == 900:
                        f_size ,rel_x ,rel_y = 10 ,0.06 ,0.04
                    else:
                        f_size ,rel_x ,rel_y = 13 ,0.06 ,0.04
                    info1.config(font=Font(size=f_size,weight=BOLD))
                    info1.place(relx=rel_x,rely=rel_y)
            else:
                main_window.after(100,loop)
        loop()
    ######################################################
    def info1_display_re(e):
        global fixed_length_button_live 
        fixed_length_button_live = False
        info1.place_forget()
    ######################################################    
    
    fixed_length_label.bind('<Enter>',info1_display)
    fixed_length_label.bind('<Leave>',info1_display_re)

    ###################################################### 
    ######################################################
    ######################################################
    def info2_display(e):
        global variable_length_button_live
        global info2_diplay_time_wait

        info2_diplay_time_wait  = 10
        variable_length_button_live = True
        def loop():
            global info2_diplay_time_wait
            info2_diplay_time_wait +=7
            if info2_diplay_time_wait > 100 :
                if variable_length_button_live == True:
                    if real_resolution == 720:
                        f_size ,rel_x ,rel_y = 8 ,0.12 ,0.04
                    elif real_resolution == 900:
                        f_size ,rel_x ,rel_y = 10 ,0.12 ,0.04
                    else:
                        f_size ,rel_x ,rel_y = 13 ,0.12 ,0.04
                    info2.config(font=Font(size=f_size,weight=BOLD))
                    info2.place(relx=rel_x,rely=rel_y)
            else:
                main_window.after(100,loop)
        loop()
    ######################################################
    def info2_display_re(e):
        global variable_length_button_live 
        variable_length_button_live = False
        info2.place_forget()

    variable_length_label.bind('<Enter>',info2_display)
    variable_length_label.bind('<Leave>',info2_display_re)

    ######################################################
    ######################################################
    ######################################################

    #############################################################
    #place vlms_flsm mode change radio buttons
    def vlsm_flsm_radio_button_select():
            if running_mode == "VLSM":
                W100.deselect()
                W101.select()
            else:
                W100.select()
                W101.deselect()
            main_window.after(100,vlsm_flsm_radio_button_select)  
    vlsm_flsm_radio_button_select()

#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
def loading002():
    global loading_display
    loading_display  = 0
    global loading_resolution_change_frame
    global loading_resolution_change_label
    loading_resolution_change_frame = Frame(main_window ,bg="#101010")
    loading_resolution_change_label = Label(loading_resolution_change_frame,text="Loading...",bg="#101010" ,fg="#00ff0f")
    
    def loading_show_when_resolution_change():
        global loading_display
        loading_display += 1 

        loading_resolution_change_label.config(font=Font(size=font_most ,weight=BOLD))
        loading_resolution_change_frame.place(relwidth=1 ,relheight=1)
        loading_resolution_change_label.place(relx=0.47 ,rely=0.45)

        if loading_display <= 10 :
            main_window.after(125,loading_show_when_resolution_change)
        else:
            loading_resolution_change_label.destroy()
            loading_resolution_change_frame.destroy()
    loading_show_when_resolution_change()

#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
def auto_close_side_panel(e):
        global side_panel_open
        if side_panel_open == True :
            side_panel_open = False
            global close_x
            close_x = 0.76

            setting_button.config(command=display_side_panel ,activebackground="#100e17")

            def closing():
                global close_x
                close_x += 0.02
                side_panel_frame.place(relx=close_x ,rely=0)
                if close_x > 1 :
                    pass
                else:
                    main_window.after(8,closing)
            closing()
        output_frame1.place(relwidth = 0.31 ,relheight=0.25 ,relx= 0.5 ,rely=0.13 )
        output_frame2.place(relwidth = 0.487 ,relheight=0.2 ,relx= 0.42,rely=0.4 )
        output_frame3.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.1 ,rely=0.62 )
        output_frame4.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.45 ,rely=0.62 )

#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
def side_panel():
    global side_panel_frame
    global side_panel_label
    side_panel_frame = Frame(main_window ,bg="#100e17" )
    side_panel_frame.pack(side="right")
    side_panel_label = Label(side_panel_frame ,bg="#100e17" )
    side_panel_label.place(rely=0,relx=0)

    #############################################################
    #############################################################
    #############################################################
    def p720_button_change(e):
        p720_button.config(bg="#00FFFF" ,fg="#000000" ,border=False)
    def p720_button_change_re(e):
        if real_resolution != 720:
            p720_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)
        else:
            p720_button.config(fg="#ff0000" ,bg="#101010" ,border=1)
    #############################################################
    def p900_button_change(e):
        p900_button.config(fg="#000000" ,bg="#00FFFF" ,border=False)
    def p900_button_change_re(e):
        if real_resolution != 900:
            p900_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)
        else:
            p900_button.config(fg="#ff0000" ,bg="#101010" ,border=1)
    #############################################################
    def p1080_button_change(e):
        p1080_button.config(fg="#000000" ,bg="#00FFFF" ,border=False)
    def p1080_button_change_re(e):
        if real_resolution != 1080:
            p1080_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)
        else:
            p1080_button.config(fg="#ff0000" ,bg="#101010" ,border=1)

    #############################################################
    #############################################################
    def resolution_setting_save(resolution):
        resolution = str(resolution)
    
        if int(resolution) == 720 :
            width = "1280"
        elif int(resolution) == 900 :
            width = "1600"
        else:
            width = "1920"
        f  = open('Sources\\Settings\\Resolution_width\\resolution_width.rapa',"w")
        f.write(width)
        f.close()
        f  = open('Sources\\Settings\\Resolution_height\\resolution_height.rapa',"w")
        f.write(resolution)
        f.close()

    #############################################################
    def change_resolution_to_720p():
        global real_resolution 
        if real_resolution != 720 :
            loading002()
            fonts_720p()
            real_resolution = 720
            p900_button.config(fg="#00FFFF" ,bg="#101010" )
            p1080_button.config(fg="#00FFFF" ,bg="#101010")
            p720_button.config(fg="#ff0000" ,bg="#101010")
            check_resolution()
            vlsm_check_resolution()
            resolution_setting_save(real_resolution)

    #############################################################
    def change_resolution_to_900p():
        global real_resolution 
        if real_resolution != 900 :
            loading002()
            fonts_900p()
            real_resolution = 900 
            p720_button.config(fg="#00FFFF" ,bg="#101010")
            p1080_button.config(fg="#00FFFF" ,bg="#101010")
            p900_button.config(fg="#ff0000" ,bg="#101010" )
            check_resolution()
            vlsm_check_resolution()
            resolution_setting_save(real_resolution)


    #############################################################
    def change_resolution_to_1080p():
        global real_resolution 
        if real_resolution != 1080 :
            loading002()
            fonts_1080p()
            real_resolution = 1080
            p720_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)
            p900_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)
            p1080_button.config(fg="#ff0000" ,bg="#101010")
            check_resolution()
            vlsm_check_resolution()
            resolution_setting_save(real_resolution)

    global resolution_label
    global p720_button
    global p900_button
    global p1080_button

    resolution_label = Label(side_panel_frame ,text="Resolution   :" ,fg="#FFFFFF" ,bg="#000000")
    resolution_label.place(rely=0.15 ,relx=0.1)
        
    p720_button = Button(side_panel_frame ,text="720p (1280 X 720)" ,fg="#00FFFF" ,bg="#101010" ,border=1 ,
                            cursor="hand2",command=change_resolution_to_720p)
    p720_button.place(rely=0.19 , relwidth=0.9 ,relx=0.05)

    p900_button = Button(side_panel_frame ,text="900p (1600 X 900)"  ,fg="#00FFFF" ,bg="#101010" ,border=1 ,
                        cursor="hand2" ,command=change_resolution_to_900p )
    p900_button.place(rely=0.24 , relwidth=0.9 ,relx=0.05)

    p1080_button = Button(side_panel_frame ,text="1080p (1920 X 1080)" ,fg="#00FFFF" ,bg="#101010" ,border=1 ,
                            cursor="hand2" ,command=change_resolution_to_1080p)
    p1080_button.place(rely=0.29 , relwidth=0.9 ,relx=0.05)

    if real_resolution == 720 :
        p720_button.config(fg="#ff0000" ,bg="#101010")
    if real_resolution == 900 :
        p900_button.config(fg="#ff0000" ,bg="#101010")
    if real_resolution == 1080 :
        p1080_button.config(fg="#ff0000" ,bg="#101010")
    
    p720_button.bind('<Enter>' ,p720_button_change)
    p720_button.bind('<Leave>' ,p720_button_change_re)
    p900_button.bind('<Enter>' ,p900_button_change)
    p900_button.bind('<Leave>' ,p900_button_change_re)
    p1080_button.bind('<Enter>' ,p1080_button_change)
    p1080_button.bind('<Leave>' ,p1080_button_change_re)
    
    #############################################################
    #############################################################
    def transparency_on_now ():
        global theme_transparent_value

        transparent_on_button.config(text="Enabled")
        transparent_off_button.config(text="Disable Transparency")
        transparent_off_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)  
        transparent_on_button.config(fg="#ff0000" ,bg="#101010" ,border=1)  

        try:
            file = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"r")
            theme_transparent_value = float(file.readline())
            file.close()
        except :
            theme_transparent_value = 0.9
        
        main_window.attributes('-alpha',theme_transparent_value)
        
        f = open("Sources\\Settings\\Theme\\transparency.rapa","w")
        f.write(str(theme_transparent_value))
        f.close()

        def set_radio_button():
            radio_button_list = [W1,W2,W3,W4,W5]

            if real_resolution == 720 :
                transparent_radio_button_rely =  trancparency_radio_button_rely_720p
            if real_resolution == 900 :
                transparent_radio_button_rely = trancparency_radio_button_rely_900p
            if real_resolution == 1080 :
                transparent_radio_button_rely =  trancparency_radio_button_rely_1080p

            relx_radio = 0.55
            for radio_button in radio_button_list :
                radio_button.place(relx=relx_radio ,rely=transparent_radio_button_rely)
                relx_radio = relx_radio + 0.05


        set_radio_button()

    def transparency_off_now ():
        global theme_transparent_value
        transparent_on_button.config(text="Enable Transparency")
        transparent_off_button.config(text="Disabled")
        transparent_on_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)  
        transparent_off_button.config(fg="#ff0000" ,bg="#101010" ,border=1)  

        if theme_transparent_value != 1 :
            theme_transparent_value = 1
            main_window.attributes('-alpha',1)
            
            f = open("Sources\\Settings\\Theme\\transparency.rapa","w")
            f.write("1")
            f.close()

            W1.place_forget()
            W2.place_forget()
            W3.place_forget()
            W4.place_forget()
            W5.place_forget()

        
    def transparent_on_button_change(e):
        transparent_on_button.config(bg="#00FFFF" ,fg="#000000" ,border=False)  
        try:  
            f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"r")
            temp_val = float(f.readline())
            f.close()
        except:
            temp_val = 0.9
        main_window.attributes('-alpha',temp_val)
    def transparent_on_button_change_re(e):
        if theme_transparent_value ==1 :
            transparent_on_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)   
        else:
            transparent_on_button.config(fg="#ff0000" ,bg="#101010" ,border=1)  
        main_window.attributes('-alpha',theme_transparent_value)

    def transparent_off_button_change(e):
        transparent_off_button.config(fg="#000000" ,bg="#00FFFF" ,border=False)
        main_window.attributes('-alpha',1)
    def transparent_off_button_change_re(e):
        if theme_transparent_value != 1  :
            transparent_off_button.config(fg="#00FFFF" ,bg="#101010" ,border=1)   
        else:
            transparent_off_button.config(fg="#ff0000" ,bg="#101010" ,border=1)  
        main_window.attributes('-alpha',theme_transparent_value)

    
    def transparancy_radio_button1():
        global theme_transparent_value
        theme_transparent_value = 0.9
        f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"w")
        f.write(str(theme_transparent_value))
        f.close()
        transparency_on_now ()
    def transparancy_radio_button2():
        global theme_transparent_value
        theme_transparent_value = 0.85
        f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"w")
        f.write(str(theme_transparent_value))
        f.close()
        transparency_on_now ()
    def transparancy_radio_button3():
        global theme_transparent_value
        theme_transparent_value = 0.8
        f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"w")
        f.write(str(theme_transparent_value))
        f.close()
        transparency_on_now ()
    def transparancy_radio_button4():
        global theme_transparent_value
        theme_transparent_value = 0.75
        f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"w")
        f.write(str(theme_transparent_value))
        f.close()
        transparency_on_now ()
    def transparancy_radio_button5():
        global theme_transparent_value
        theme_transparent_value = 0.7
        f = open("Sources\\Settings\\Theme\\transparency_value_temp.rapa" ,"w")
        f.write(str(theme_transparent_value))
        f.close()
        transparency_on_now ()


    global W1
    global W2
    global W3
    global W4
    global W5

    var = IntVar()
    W1 = Radiobutton(side_panel_frame, variable=var ,value=1 ,cursor="hand2" 
                    ,bg="#000000" ,fg="#0000ff" ,activebackground="#000000" ,command=transparancy_radio_button1 )
    W2 = Radiobutton(side_panel_frame, variable=var ,value=2 ,cursor="hand2"  
                    ,bg="#000000" ,fg="#0000ff" ,activebackground="#000000" ,command=transparancy_radio_button2 )
    W3 = Radiobutton(side_panel_frame, variable=var ,value=3 ,cursor="hand2"  
                    ,bg="#000000" ,fg="#0000ff" ,activebackground="#000000" ,command=transparancy_radio_button3 )
    W4 = Radiobutton(side_panel_frame, variable=var ,value=4 ,cursor="hand2" 
                    ,bg="#000000" ,fg="#0000ff" ,activebackground="#000000" ,command=transparancy_radio_button4 )
    W5 = Radiobutton(side_panel_frame, variable=var ,value=5 ,cursor="hand2" 
                    ,bg="#000000" ,fg="#0000ff" ,activebackground="#000000" ,command=transparancy_radio_button5 )
    
    global transparent_mode_label
    global transparent_on_button
    global transparent_off_button
    transparent_mode_label = Label(side_panel_frame ,text="Transparency  :" 
                                ,fg="#FFFFFF" ,bg="#000000")
    transparent_mode_label.place(rely=0.4 ,relx=0.1)

    transparent_on_button = Button(side_panel_frame ,text="Enable Transparency" ,fg="#00FFFF" ,bg="#101010"
                                    ,border=1 ,cursor="hand2" ,command=transparency_on_now)
    transparent_on_button.place(rely=0.44 , relwidth=0.9 ,relx=0.05)

    transparent_off_button = Button(side_panel_frame ,text="Disable Transparency" ,fg="#00FFFF" ,bg="#101010"
                                    ,border=1 ,cursor="hand2" ,command=transparency_off_now )
    transparent_off_button.place(rely=0.49 , relwidth=0.9 ,relx=0.05)

    transparent_on_button.bind('<Enter>' ,transparent_on_button_change )
    transparent_on_button.bind('<Leave>' , transparent_on_button_change_re)
    transparent_off_button.bind('<Enter>' ,transparent_off_button_change )
    transparent_off_button.bind('<Leave>' , transparent_off_button_change_re)
    if theme_transparent_value == 1:
        transparency_off_now ()
    else:
        transparency_on_now ()


    #############################################################
    #############################################################
    def transparency_radio_button_select():
        if theme_transparent_value == 1:
            pass
        else:
            if theme_transparent_value == 0.9 :
                W1.select()
                W2.deselect()
                W3.deselect()
                W4.deselect()
                W5.deselect()
            elif theme_transparent_value == 0.85 :
                W2.select()
                W1.deselect()
                W3.deselect()
                W4.deselect()
                W5.deselect()
            elif theme_transparent_value == 0.8 :
                W3.select()
                W1.deselect()
                W2.deselect()
                W4.deselect()
                W5.deselect()
            elif theme_transparent_value == 0.75 :
                W4.select()
                W1.deselect()
                W2.deselect()
                W3.deselect()
                W5.deselect()
            else:
                W5.select()
                W1.deselect()
                W2.deselect()
                W3.deselect()
                W4.deselect()
        main_window.after(100,transparency_radio_button_select)

    transparency_radio_button_select()

    #############################################################
    #############################################################
    global close_side_panel
    def close_side_panel():
        global side_panel_open
        side_panel_open = False
        global close_x
        close_x = 0.76

        setting_button.config(command=display_side_panel ,activebackground="#100e17")

        def closing():
            global close_x
            close_x += 0.02
            side_panel_frame.place(relx=close_x ,rely=0)
            if close_x > 1 :
                pass
            else:
                main_window.after(8,closing)
        closing()

        output_frame1.place(relwidth = 0.31 ,relheight=0.25 ,relx= 0.5 ,rely=0.13 )
        output_frame2.place(relwidth = 0.487 ,relheight=0.2 ,relx= 0.42,rely=0.4 )
        output_frame3.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.1 ,rely=0.62 )
        output_frame4.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.45 ,rely=0.62 )

    #############################################################
    #############################################################
    global display_side_panel
    def display_side_panel():
        global side_panel_open
        side_panel_open = True
        global open_x
        open_x = 1

        setting_button.config(command=close_side_panel ,activebackground="#000000")

        def opening():
            global open_x
            open_x -= 0.02
            side_panel_frame.place(relx=open_x ,rely=0)
            if open_x < 0.76 :
                pass
            else:
                main_window.after(8,opening)
        opening()

        output_frame1.place(relwidth = 0.31 ,relheight=0.25 ,relx= 0.416 ,rely=0.13 )
        output_frame2.place(relwidth = 0.487 ,relheight=0.2 ,relx= 0.24,rely=0.425 )
        output_frame3.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.1 ,rely=0.65 )
        output_frame4.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.434 ,rely=0.65 )

    ############################################################
    #############################################################
    global setting_button_set
    def setting_button_set():
            global setting_button
            setting_button = Button(main_window ,bg="#100e17" ,cursor="hand2" ,image=setting_button_image
                                    ,activebackground="#100e17" ,border=False ,command=display_side_panel )
            setting_button.place(rely=0.94 ,relx=0.97)
            def change_setting_button(e):
                setting_button.config(image=setting_button_re_image)
            def change_setting_button_re(e):
                setting_button.config(image=setting_button_image)
            setting_button.bind('<Enter>',change_setting_button)
            setting_button.bind('<Leave>',change_setting_button_re)
    
    side_panel_frame.pack_forget()

#############################################################
#############################################################
#############################################################
def VLSM_mode():
    global first_time_change_vlsm_flsm_mode
    global running_mode
    if first_time_change_vlsm_flsm_mode == True or running_mode == "FLSM":
        first_time_change_vlsm_flsm_mode = False
        loading001()
        try:
            close_side_panel()
        except:
            pass
        running_mode = "VLSM"
        f = open("Sources\\Settings\\Running_mode\\mode.rapa","w")
        f.write("VLSM")
        f.close()
        vlsm_main_window.place(relwidth=1,relheight=1)
def FLSM_mode():
    global first_time_change_vlsm_flsm_mode
    global running_mode    
    if first_time_change_vlsm_flsm_mode == True or running_mode == "VLSM":
        first_time_change_vlsm_flsm_mode = False
        loading001()
        try:
            close_side_panel()
        except:
            pass
        running_mode = "FLSM"
        f = open("Sources\\Settings\\Running_mode\\mode.rapa","w")
        f.write("FLSM")
        f.close()
        vlsm_main_window.place_forget()


    
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
def fonts_1080p() :
    global loading_title_font_size
    global loading_font_most
    global font_most
    global font_most_1
    global font_table_title
    global vlsm_flsm_font
    global available_host_label_font
    global vlsm_table_font
    
    font_most = 17
    font_most_1 = 17
    font_table_title = 20
    loading_font_most = 13
    loading_title_font_size = 23
    vlsm_flsm_font = 14
    available_host_label_font = 12
    vlsm_table_font = 15

##########################################################
def fonts_900p() :
    global loading_title_font_size
    global loading_font_most
    global font_most
    global font_most_1
    global font_table_title
    global vlsm_flsm_font
    global available_host_label_font
    global vlsm_table_font

    font_most = 14
    font_most_1 = 13
    font_table_title = 17
    loading_font_most = 11
    loading_title_font_size=19
    vlsm_flsm_font = 11
    available_host_label_font = 10
    vlsm_table_font = 13
    
##########################################################
def fonts_720p() :
    global loading_title_font_size
    global loading_font_most
    global font_most
    global font_most_1
    global font_table_title
    global vlsm_flsm_font
    global available_host_label_font
    global vlsm_table_font

    font_most = 11
    font_most_1 = 10
    font_table_title = 15
    loading_font_most = 9
    loading_title_font_size=15
    vlsm_flsm_font = 9
    available_host_label_font = 8
    vlsm_table_font = 10

##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################

def vlsm_set_resolution(flsm_vlsm_mode_image,flsm_vlsm_frame_relwidth,
                        flsm_vlsm_frame_relheight,flsm_vlsm_frame_rely,fixed_variable_length_button_rely,
                        fixed_variable_length_radiobutton_rely,vlsm_input_frame_image,
                        vlsm_input_ipaddress_entry_rely,
                        vlsm_title_inputipaddress_label_rely,vlsm_input_networks_entry_rely,
                        vlsm_title_inputnetworks_label_rely,
                        calculate_button_image_def,calculate_button_image_re_def,
                        calculate_button_error_image_def,reset_button_image,
                        vlsm_table_head_image_def,vlsm_table_row_1_image_def,vlsm_table_head_end_image_def,
                        vlsm_table_th_rely_def,vlsm_table_th_relx_def,vlsm_table_td_relx,vlsm_table_td1_rely,vlsm_table_td_rely_change,
                        table_hiding_frame_relx_def,vlsm_table_range_split_dash1_relx,vlsm_table_range_split_dash2_relx,
                        table_frame_change_special_button_image_def,table_frame_change_special_button_re_image_def,table_frame_change_special_button_error_image_def,
                        vlsm_table_head_full_image_def,vlsm_table_head_end_full_image_def,
                        table_frame_change_special_button_back_image_def,table_frame_change_special_button_back_re_image_def):

    global vlsm_input_frame_rel_y
    global vlsm_input_frame_rel_height
   
    if real_resolution == 1080 :
        vlsm_input_frame_rel_height=0.8
        vlsm_input_frame_rel_y = 0.12
        W100_relx = 0.14
        W101_relx =  0.55
        fixed_length_button_relx = 0.22
        variable_length_button_relx =  0.63
    elif real_resolution == 900 :
        vlsm_input_frame_rel_height=0.8
        vlsm_input_frame_rel_y = 0.12
        W100_relx =  0.16
        W101_relx =  0.54
        fixed_length_button_relx =  0.25
        variable_length_button_relx =  0.63
    else:
        vlsm_input_frame_rel_height=0.84
        vlsm_input_frame_rel_y = 0.114
        W100_relx = 0.14
        W101_relx = 0.51
        fixed_length_button_relx = 0.25
        variable_length_button_relx = 0.62
    
    vlsm_table_th_relx = vlsm_table_th_relx_def
    vlsm_table_th_rely = vlsm_table_th_rely_def

     #fslm vlsm mode change frame 
    if full_table_enable == False:
        vlsm_input_frame.place(relwidth=0.31 ,relheight=vlsm_input_frame_rel_height,relx=0.05 ,rely=vlsm_input_frame_rel_y)
    vlsm_input_label.config(image=vlsm_input_frame_image)
    vlsm_or_flsm_label.config(image=flsm_vlsm_mode_image)
    vlsm_or_flsm_frame.place(relwidth=flsm_vlsm_frame_relwidth ,relheight=flsm_vlsm_frame_relheight ,relx=0.07 ,rely=flsm_vlsm_frame_rely)


    W100.place(relx=W100_relx,rely=fixed_variable_length_radiobutton_rely)
    W101.place(relx=W101_relx,rely=fixed_variable_length_radiobutton_rely)
    
    variable_length_label.config(font=Font(weight=BOLD,size=vlsm_flsm_font))
    fixed_length_label.config(font=Font(weight=BOLD,size=vlsm_flsm_font))

    fixed_length_label.place(relx=fixed_length_button_relx,rely=fixed_variable_length_button_rely)
    variable_length_label.place(relx=variable_length_button_relx,rely=fixed_variable_length_button_rely)

    # input labels ,  entrys 
    vlsm_input_ipaddress.place(rely=vlsm_input_ipaddress_entry_rely ,relx=0.55)
    vlsm_title_inputipaddress.place(rely=vlsm_title_inputipaddress_label_rely ,relx=0.11)
    vlsm_input_networks.place(rely=vlsm_input_networks_entry_rely ,relx=0.55)
    vlsm_title_inputnetworks.place(rely=vlsm_title_inputnetworks_label_rely ,relx=0.11)

    vlsm_input_dash0.place(rely= vlsm_title_inputipaddress_label_rely ,relx=0.45)
    vlsm_input_dash1.place(rely= vlsm_title_inputnetworks_label_rely ,relx=0.45)

    #set fonts font most size
    widgets = [vlsm_input_ipaddress,vlsm_title_inputipaddress,vlsm_input_networks,vlsm_title_inputnetworks,
             vlsm_input_dash0,vlsm_input_dash1]

    for widget in widgets :
        widget.config(font=Font(size=font_most ,weight=BOLD))
    for widget in vlsm_host_input_label_list :
        widget.config(font=Font(size=vlsm_flsm_font+1 ,weight=BOLD))
    for widget in vlsm_host_input_label_dash_list :
        widget.config(font=Font(size=vlsm_flsm_font+1 ,weight=BOLD))
    for widget in vlsm_host_input_entry_list :
        widget.config(font=Font(size=vlsm_flsm_font+1 ,weight=BOLD))


    #button widget loading
    global calculate_button_image , calculate_button_image_re
    calculate_button_image,calculate_button_image_re=calculate_button_image_def,calculate_button_image_re_def 
    global calculate_button_error_image
    calculate_button_error_image = calculate_button_error_image_def 
    #button 
    vlsm_calculate_button.config(image=calculate_button_image)
    vlsm_reset_button.config(image=reset_button_image)

    vlsm_available_host_label.config(font=Font(size=available_host_label_font,weight=BOLD))

    #output label table
    global vlsm_table_row_1_image
    vlsm_table_row_1_image = vlsm_table_row_1_image_def

    for widget in vlsm_table_rows_list :
        widget.config(image=vlsm_table_row_1_image)
    
   
    #table rows labels 
    vlsm_table_th_relx = vlsm_table_th_relx_def
    vlsm_table_th_rely = vlsm_table_th_rely_def
    index = 0
    for title_lable in vlsm_table_head_list:
        title_lable.config(font=Font(size=font_most,weight=BOLD))
        title_lable.config(title_lable.place(relx=vlsm_table_th_relx[index],rely=vlsm_table_th_rely))
        index += 1
        
    #table lables config
    for label in table_td_rows_lables :
        label.config(font=Font(size=vlsm_table_font ,weight=BOLD))
    count_table_row = 0
    for row in table_td_rows_lable_lists :
        index=0
        if count_table_row == 0 :
            vlsm_table_lable_rely = vlsm_table_td1_rely
        else:
            vlsm_table_lable_rely += vlsm_table_td_rely_change
        count_table_row += 1
        for lable in row:
            lable.place(relx=vlsm_table_td_relx[index] ,rely=vlsm_table_lable_rely)
            index+=1

    #place dash in range
    count = 1
    for i in vlsm_table_all_dashes:
        index = 0 
        for i in i :
            if index == 0  :
                vlsm_table_dash_rely = vlsm_table_td1_rely
            else:
                vlsm_table_dash_rely += vlsm_table_td_rely_change
            if count == 1:
                rel_x_dash = vlsm_table_range_split_dash1_relx
            else:
                rel_x_dash = vlsm_table_range_split_dash2_relx
            i.place(relx=rel_x_dash,rely=vlsm_table_dash_rely)
            index += 1 
        count += 1
    for i in vlsm_table_range1_spliter+vlsm_table_range2_spliter:
        i.config(font=Font(weight=BOLD,size=vlsm_flsm_font))
 

    # table hiding frame
    global table_hiding_frame_relx
    table_hiding_frame_relx = table_hiding_frame_relx_def

    table_hiding_frame.place(relx=table_hiding_frame_relx ,rely=0.1,relwidth=0.2 ,relheight=1)

    #change table special button
    global table_frame_change_special_button_image
    table_frame_change_special_button_image = table_frame_change_special_button_image_def
    global table_frame_change_special_button_re_image
    table_frame_change_special_button_re_image = table_frame_change_special_button_re_image_def

    global table_frame_change_special_button_back_image
    global table_frame_change_special_button_back_re_image
    global table_frame_change_special_button_error_image

    table_frame_change_special_button_error_image = table_frame_change_special_button_error_image_def
    table_frame_change_special_button_back_image = table_frame_change_special_button_back_image_def,
    table_frame_change_special_button_back_re_image = table_frame_change_special_button_back_re_image_def
    if vlsm_calculation_done == True:
        if full_table_enable == False :
            table_change_special_button.config(image=table_frame_change_special_button_image)
        else:
            table_change_special_button.config(image=table_frame_change_special_button_back_image)
    else:
        table_change_special_button.config(image=table_frame_change_special_button_error_image)

    #table head 2nd image 
    global vlsm_table_head_end_image
    vlsm_table_head_end_image = vlsm_table_head_end_image_def
    global vlsm_table_head_full_image
    vlsm_table_head_full_image = vlsm_table_head_full_image_def
    global vlsm_table_head_end_full_image
    vlsm_table_head_end_full_image =  vlsm_table_head_end_full_image_def
    global vlsm_table_head_image
    vlsm_table_head_image = vlsm_table_head_image_def
    if full_table_enable == False:
         vlsm_table_head_label.config(image = vlsm_table_head_image_def)
         vlsm_table_last_row.config(image=vlsm_table_head_end_image)
    else:
         vlsm_table_head_label.config(image = vlsm_table_head_full_image)
         vlsm_table_last_row.config(image=vlsm_table_head_end_full_image)


def vlsm_check_resolution():
    if real_resolution == 720 :
        vlsm_set_resolution(flsm_vlsm_mode_image_720p,flsm_vlsm_frame_relwidth_720p,
                        flsm_vlsm_frame_relheight_720p,flsm_vlsm_frame_rely_720p,fixed_variable_length_button_rely_720p,
                        fixed_variable_length_radiobutton_rely_720p,vlsm_input_frame_image_720p,
                        vlsm_input_ipaddress_entry_rely_720p,
                        vlsm_title_inputipaddress_label_rely_720p,vlsm_input_networks_entry_rely_720p,
                        vlsm_title_inputnetworks_label_rely_720p,
                        calculate_button_image_720p ,calculate_button_image_re_720p ,
                        calculate_button_error_image_720p,reset_button_image_720p,
                        vlsm_table_head_image_720p,vlsm_table_row_1_image_720p,vlsm_table_head_end_image_720p,
                        vlsm_table_th_rely_720p,vlsm_table_th_relx_720p,vlsm_table_td_relx_720p,vlsm_table_td1_rely_720p,vlsm_table_td_rely_change_720p,
                        table_hiding_frame_relx_720p,vlsm_table_range_split_dash1_relx_720p,vlsm_table_range_split_dash2_relx_720p,
                        table_frame_change_special_button_image_720p,table_frame_change_special_button_re_image_720p,table_frame_change_special_button_error_image_720p,
                        vlsm_table_head_full_image_720p,vlsm_table_head_end_full_image_720p,
                        table_frame_change_special_button_back_image_720p,table_frame_change_special_button_back_re_image_720p)

    elif real_resolution == 900 :
        vlsm_set_resolution(flsm_vlsm_mode_image_900p,flsm_vlsm_frame_relwidth_900p,
                        flsm_vlsm_frame_relheight_900p,flsm_vlsm_frame_rely_900p,fixed_variable_length_button_rely_900p,
                        fixed_variable_length_radiobutton_rely_900p,vlsm_input_frame_image_900p,
                        vlsm_input_ipaddress_entry_rely_900p,
                        vlsm_title_inputipaddress_label_rely_900p,vlsm_input_networks_entry_rely_900p,
                        vlsm_title_inputnetworks_label_rely_900p,
                        calculate_button_image_900p,calculate_button_image_re_900p,
                        calculate_button_error_image_900p,reset_button_image_900p,
                        vlsm_table_head_image_900p,vlsm_table_row_1_image_900p,vlsm_table_head_end_image_900p,
                        vlsm_table_th_rely_900p,vlsm_table_th_relx_900p,vlsm_table_td_relx_900p,vlsm_table_td1_rely_900p,vlsm_table_td_rely_change_900p,
                        table_hiding_frame_relx_900p,vlsm_table_range_split_dash1_relx_900p,vlsm_table_range_split_dash2_relx_900p,
                        table_frame_change_special_button_image_900p,table_frame_change_special_button_re_image_900p,table_frame_change_special_button_error_image_900p,
                        vlsm_table_head_full_image_900p,vlsm_table_head_end_full_image_900p,
                        table_frame_change_special_button_back_image_900p,table_frame_change_special_button_back_re_image_900p)
    else:
        vlsm_set_resolution(flsm_vlsm_mode_image_1080p,flsm_vlsm_frame_relwidth_1080p,
                        flsm_vlsm_frame_relheight_1080p,flsm_vlsm_frame_rely_1080p,fixed_variable_length_button_rely_1080p,
                        fixed_variable_length_radiobutton_rely_1080p,vlsm_input_frame_image_1080p,
                        vlsm_input_ipaddress_entry_rely_1080p,
                        vlsm_title_inputipaddress_label_rely_1080p,vlsm_input_networks_entry_rely_1080p,
                        vlsm_title_inputnetworks_label_rely_1080p,
                        calculate_button_image_1080p,calculate_button_image_re_1080p,
                        calculate_button_error_image_1080p,reset_button_image_1080p,
                        vlsm_table_head_image_1080p,vlsm_table_row_1_image_1080p,vlsm_table_head_end_image_1080p,
                        vlsm_table_th_rely_1080p,vlsm_table_th_relx_1080p,vlsm_table_td_relx_1080p,vlsm_table_td1_rely_1080p,vlsm_table_td_rely_change_1080p,
                        table_hiding_frame_relx_1080p,vlsm_table_range_split_dash1_relx_1080p,vlsm_table_range_split_dash2_relx_1080p,
                        table_frame_change_special_button_image_1080p,table_frame_change_special_button_re_image_1080p,table_frame_change_special_button_error_image_1080p,
                        vlsm_table_head_full_image_1080p,vlsm_table_head_end_full_image_1080p,
                        table_frame_change_special_button_back_image_1080p,table_frame_change_special_button_back_re_image_1080p)


##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################
##########################################################


    
def set_resolution(width,height,title_image,input_frame_image,input_frame_lable_rely,input_frame_entry_rely,
                    calculate_button_image_def,calculate_button_image_re_def,reset_button_image_def,reset_button_image_re_def,
                    output_frame1_image,output_frame_label_rely,output_frame1_dash_relx,output_frame2_image,
                    output_frame2_label_rely,output_frame2_dash_relx,output_table_image,table_lable_rely,table1_dash1_relx,
                    table_range_relx,table_range2_relx,setting_button_image_def,setting_button_re_image_def,
                    side_panel_image,side_panel_size_def,transparent_radio_button_rely_temp):

    radio_button_list = [W1,W2,W3,W4,W5]
    global side_panel_size
    side_panel_size = side_panel_size_def
        
    global calculate_button_image_re
    global reset_button_image_re
    calculate_button_image_re = calculate_button_image_re_def
    reset_button_image_re = reset_button_image_re_def

    global calculate_button_image
    global reset_button_image
    calculate_button_image = calculate_button_image_def
    reset_button_image = reset_button_image_def

    global setting_button_re_image
    global setting_button_image
    setting_button_re_image = setting_button_re_image_def
    setting_button_image = setting_button_image_def


    main_window.geometry("{0}x{1}+{2}+{3}".format(width,height,window_relx_geomatry_read,window_rely_geomatry_read))
    main_window.config(main_window.minsize(width,height))
    main_window.config(main_window.maxsize(width ,height))

    main_title.config(image=title_image)

    
    input_frame_label.config(image=input_frame_image)
    title_inputipaddress.place(rely = input_frame_lable_rely[0] ,relx = 0.15 )
    flsm_input_ipaddress.place(rely = input_frame_entry_rely[0] ,relx = 0.55 ,relheight=0.105 ,relwidth=0.35 )         
    title_inputhosts.place(rely = input_frame_lable_rely[1] ,relx = 0.15 )
    flsm_input_usablehosts.place(rely = input_frame_entry_rely[1] ,relx = 0.55 ,relheight=0.105 ,relwidth=0.35 )       
    title_inputnetworks.place(rely = input_frame_lable_rely[2],relx = 0.15 )
    flsm_input_networks.place(rely = input_frame_entry_rely[2] ,relx = 0.55 ,relheight=0.105 ,relwidth=0.35 )       
    title_inputSubnetmask.place(rely = input_frame_lable_rely[3] ,relx = 0.15 )
    flsm_input_subnetmask.place(rely = input_frame_entry_rely[3] ,relx = 0.55 ,relheight=0.105 ,relwidth=0.35 ) 

    #table lable
    # range 1 
    index = 0
    for i in flsm_table_range_1:
        i.place(rely=table_lable_rely[index] ,relx=table_range_relx)
        i.config(font=Font(size=font_most_1 ,weight=BOLD))
        index += 1
    index = 0
    for i in flsm_table_range_2 :
        i.place(rely=table_lable_rely[index] ,relx=table_range2_relx)
        i.config(font=Font(size=font_most_1 ,weight=BOLD))
        index += 1
    # range 2 
    index = 0
    for i in flsm_table_usable_range_1:
        i.place(rely=table_lable_rely[index] ,relx=table_range_relx)
        i.config(font=Font(size=font_most_1 ,weight=BOLD))
        index += 1
    index = 0
    for i in flsm_table_usable_range_2 :
        i.place(rely=table_lable_rely[index] ,relx=table_range2_relx)
        i.config(font=Font(size=font_most_1 ,weight=BOLD))
        index += 1

    index = 0 
    for i in input_dashes :
        i.place(rely = input_frame_lable_rely[index] ,relx=0.45)
        i.config(font=Font(size=font_most ,weight=BOLD))
        index += 1
    
    calculate_button.config(image=calculate_button_image)
    reset_button.config(image=reset_button_image)
    output_frame_label.config(image=output_frame1_image)
    title_ip_address.place(rely = output_frame_label_rely[0] ,relx=0.075)
    display_ip_address.place(rely = output_frame_label_rely[0] ,relx=0.55)
    title_ip_address_class.place(rely = output_frame_label_rely[1] ,relx=0.075)
    display_ip_address_class.place(rely = output_frame_label_rely[1] ,relx=0.55)
    title_subnet_number.place(rely = output_frame_label_rely[2] ,relx=0.075)
    display_subnet_number.place(rely = output_frame_label_rely[2] ,relx=0.55)
    title_numberhost_number.place(rely = output_frame_label_rely[3] ,relx=0.075)
    display_host_number.place(rely = output_frame_label_rely[3] ,relx=0.55)
    title_usable_host_number.place(rely = output_frame_label_rely[4] ,relx=0.075)
    display_usable_host_number.place(rely = output_frame_label_rely[4] ,relx=0.55)
    title_increment_Value_num.place(rely = output_frame_label_rely[5] ,relx=0.075)
    display_Increment_Value_num.place(rely = output_frame_label_rely[5] ,relx=0.55)
    
    output_dash0.place(rely = output_frame_label_rely[0] ,relx=output_frame1_dash_relx)
    output_dash1.place(rely = output_frame_label_rely[1] ,relx=output_frame1_dash_relx)
    output_dash2.place(rely = output_frame_label_rely[2] ,relx=output_frame1_dash_relx)
    output_dash3.place(rely = output_frame_label_rely[3] ,relx=output_frame1_dash_relx)
    output_dash4.place(rely = output_frame_label_rely[4] ,relx=output_frame1_dash_relx)
    output_dash5.place(rely = output_frame_label_rely[5] ,relx=output_frame1_dash_relx)
    
    output_frame2_label.config(image=output_frame2_image)
    title_default_subnet_mask.place(rely = output_frame2_label_rely[0] ,relx = 0.05 )
    display_default_subnet_mask.place(rely = output_frame2_label_rely[0] ,relx = 0.5)
    title_default_subnet_mask_binary.place(rely = output_frame2_label_rely[1] ,relx = 0.05 )
    display_default_subnet_mask_binary.place(rely = output_frame2_label_rely[1] ,relx = 0.5)
    title_subnet_mask.place(rely = output_frame2_label_rely[2] ,relx = 0.05)
    display_subnet_mask.place(rely = output_frame2_label_rely[2] ,relx = 0.5)
    title_subnet_mask_binary.place(rely = output_frame2_label_rely[3] ,relx =0.05)
    display_subnet_mask_binary.place(rely = output_frame2_label_rely[3] ,relx = 0.5)
    
    output2_dash0.place(rely = output_frame2_label_rely[0] ,relx = output_frame2_dash_relx)
    output2_dash1.place(rely = output_frame2_label_rely[1] ,relx =output_frame2_dash_relx)
    output2_dash2.place(rely = output_frame2_label_rely[2] ,relx = output_frame2_dash_relx)
    output2_dash3.place(rely = output_frame2_label_rely[3] ,relx =output_frame2_dash_relx)

    output_table1_label.config(image=output_table_image)
    flsm_range1.place(relx=table_range_relx ,rely=table_lable_rely[0] )
    flsm_range2.place(relx=table_range_relx ,rely=table_lable_rely[1] )
    flsm_range3.place(relx=table_range_relx ,rely=table_lable_rely[2] )
    flsm_range4.place(relx=table_range_relx ,rely=table_lable_rely[3] )
    flsm_range5.place(relx=table_range_relx ,rely=table_lable_rely[4] )
    flsm_range6.place(relx=table_range_relx ,rely=table_lable_rely[5] )

    table1_dash1.place(relx=table1_dash1_relx ,rely=table_lable_rely[0] )
    table1_dash2.place(relx=table1_dash1_relx ,rely=table_lable_rely[1] )
    table1_dash3.place(relx=table1_dash1_relx ,rely=table_lable_rely[2])
    table1_dash4.place(relx=table1_dash1_relx ,rely=table_lable_rely[3])
    table1_dash5.place(relx=table1_dash1_relx ,rely=table_lable_rely[4] )
    table1_dash6.place(relx=table1_dash1_relx ,rely=table_lable_rely[5] )
    
    output_table2_label.config(image=output_table_image)

    flsm_usable_range1.place(relx=table_range_relx ,rely=table_lable_rely[0] )
    flsm_usable_range2.place(relx=table_range_relx ,rely=table_lable_rely[1] )
    flsm_usable_range3.place(relx=table_range_relx ,rely=table_lable_rely[2] )
    flsm_usable_range4.place(relx=table_range_relx ,rely=table_lable_rely[3] )
    flsm_usable_range5.place(relx=table_range_relx ,rely=table_lable_rely[4] )
    flsm_usable_range6.place(relx=table_range_relx ,rely=table_lable_rely[5] )

    table2_dash1.place(relx=table1_dash1_relx ,rely=table_lable_rely[0])
    table2_dash2.place(relx=table1_dash1_relx ,rely=table_lable_rely[1])
    table2_dash3.place(relx=table1_dash1_relx ,rely=table_lable_rely[2])
    table2_dash4.place(relx=table1_dash1_relx ,rely=table_lable_rely[3])
    table2_dash5.place(relx=table1_dash1_relx ,rely=table_lable_rely[4])
    table2_dash6.place(relx=table1_dash1_relx ,rely=table_lable_rely[5])

    
    setting_button.config(image=setting_button_image)
    side_panel_label.config(image=side_panel_image)
    side_panel_frame.config(width=side_panel_size["width"] ,height=side_panel_size["height"] )

    input_labels = [title_inputipaddress ,flsm_input_ipaddress ,title_inputhosts ,flsm_input_usablehosts
                   ,title_inputnetworks,flsm_input_networks ,title_inputSubnetmask ,flsm_input_subnetmask
                    ,resolution_label,p720_button ,p900_button
                   ,p1080_button ,transparent_mode_label ,transparent_on_button ,transparent_off_button]

    for i in input_labels:
        i.config(font=Font(size=font_most ,weight=BOLD))

    output_labels = [title_ip_address ,display_ip_address ,title_ip_address_class ,display_ip_address_class
                    ,title_subnet_number ,display_subnet_number ,title_numberhost_number, display_host_number
                    ,title_usable_host_number ,display_usable_host_number ,title_increment_Value_num
                    ,display_Increment_Value_num ,output_dash0 ,output_dash1, output_dash2 , output_dash3 
                    ,output_dash4 ,output_dash5 ,title_default_subnet_mask ,display_default_subnet_mask
                    ,title_default_subnet_mask_binary ,display_default_subnet_mask_binary ,title_subnet_mask
                    ,display_subnet_mask ,title_subnet_mask_binary ,display_subnet_mask_binary ,output2_dash0
                    ,output2_dash1 ,output2_dash2 ,output2_dash3
                    ,flsm_range1,flsm_range2,flsm_range3,flsm_range4,flsm_range5,flsm_range6
                    ,flsm_usable_range1,flsm_usable_range2,flsm_usable_range3,flsm_usable_range4,flsm_usable_range5,flsm_usable_range6,
                    table2_dash1 ,table2_dash2 ,table2_dash3 ,table2_dash4 ,table2_dash5 ,table2_dash6 ,
                    table1_dash1 ,table1_dash2 ,table1_dash3 ,table1_dash4 ,table1_dash5 ,table1_dash6 ]
    for i in output_labels:
        i.config(font=Font(size=font_most_1 ,weight=BOLD))

    if theme_transparent_value != 1 :
        radio_relx = 0.55 
        for radio_button in radio_button_list:
            radio_button.place(relx=radio_relx ,rely=transparent_radio_button_rely_temp)
            radio_relx += 0.05 

    title_ipranges.config(font=Font(size=font_table_title ,weight=BOLD))
    title_usable_ipranges.config(font=Font(size=font_table_title ,weight=BOLD))
    version.config(font=Font(size=font_most-3 ,weight=BOLD))

def check_resolution():
    if real_resolution == 720 :
        set_resolution(1280,640,title_image_720p,input_frame_image_720p,input_frame_lable_rely_720p,input_frame_entry_rely_720p,
                            calculate_button_image_720p,calculate_button_image_re_720p,reset_button_image_720p,reset_button_image_re_720p,
                            output_frame1_image_720p,output_frame_label_rely_720p,output_frame1_dash_relx_720p,output_frame2_image_720p,
                            output_frame2_label_rely_720p,output_frame2_dash_relx_720p,output_table_image_720p,table_lable_rely_720p,table1_dash1_relx_720p,
                            table_range_relx_720p,table_range2_relx_720p,setting_button_image_720p,setting_button_re_image_720p,
                            side_panel_image_720p,side_panel_size_720p,trancparency_radio_button_rely_720p)

    elif real_resolution == 900 :
        set_resolution(1600,820,title_image_900p,input_frame_image_900p,input_frame_lable_rely_900p,input_frame_entry_rely_900p,
                            calculate_button_image_900p,calculate_button_image_re_900p,reset_button_image_900p,reset_button_image_re_900p,
                            output_frame1_image_900p,output_frame_label_rely_900p,output_frame1_dash_relx_900p,output_frame2_image_900p,
                            output_frame2_label_rely_900p,output_frame2_dash_relx_900p,output_table_image_900p,table_lable_rely_900p,table1_dash1_relx_900p,
                            table_range_relx_900p,table_range2_relx_900p,setting_button_image_900p,setting_button_re_image_900p,
                            side_panel_image_900p,side_panel_size_900p,trancparency_radio_button_rely_900p,)
    else:
        set_resolution(1920,1000,title_image_1080p,input_frame_image_1080p,input_frame_lable_rely_1080p,input_frame_entry_rely_1080p,
                            calculate_button_image_1080p,calculate_button_image_re_1080p,reset_button_image_1080p,reset_button_image_re_1080p,
                            output_frame1_image_1080p,output_frame_label_rely_1080p,output_frame1_dash_relx_1080p,output_frame2_image_1080p,
                            output_frame2_label_rely_1080p,output_frame2_dash_relx_1080p,output_table_image_1080p,table_lable_rely_1080p,table1_dash1_relx_1080p,
                            table_range_relx_1080p,table_range2_relx_1080p,setting_button_image_1080p,setting_button_re_image_1080p,
                            side_panel_image_1080p,side_panel_size_1080p,trancparency_radio_button_rely_1080p)

    
########################################  ##########                          ##################################     ################                                 ################
########################################  ##########                        ######################################   #################                               #################
########################################  ##########                       ########################################  ##################                             ##################
########################################  ##########                       ########################################  ###################                           ###################
##########                                ##########                       ##########                                ####################                         ####################
##########                                ##########                       ##########                                ########## ##########                       ########## ##########
##########                                ##########                       ##########                                ##########  ##########                     ##########  ##########
##########                                ##########                       ##########                                ##########   ##########                   ##########   ##########
########################################  ##########                       ##########                                ##########    ##########                 ##########    ##########
########################################  ##########                       ######################################    ##########     ##########               ##########     ##########
########################################  ##########                       #######################################   ##########      ##########             ##########      ##########      
########################################  ##########                       ########################################  ##########       ##########           ##########       ##########          
##########                                ##########                        #######################################  ##########        ##########         ##########        ########## 
##########                                ##########                                                     ##########  ##########         ##########       ##########         ##########
##########                                ##########                                                     ##########  ##########          ##########     ##########          ########## 
##########                                ##########                                                     ##########  ##########           ##########   ##########           ##########
##########                                ##########                                                     ##########  ##########            ########## ##########            ########## 
##########                                ##########                                                     ##########  ##########             ###################             ##########
##########                                ###############################  ########################################  ##########              #################              ##########
##########                                ###############################  ########################################  ##########               ###############               ##########
##########                                ###############################   ######################################   ##########                #############                ##########
##########                                ###############################     ###################################    ##########                 ###########                 ##########

def main_root_new():
    global side_panel_open
    side_panel_open = False      

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    #input frame
    global input_frame_label
    input_frame = Frame(main_window ,bg="#100e17")
    input_frame.place(relwidth=0.31 ,relheight=0.29 ,relx=0.05 ,rely=0.12)
    input_frame_label = Label(input_frame,bg="#100e17")
    input_frame_label.pack()

    #input 
    ##########################################################
    #########################################################
    ##########################################################
    ##########################################################
    # -------- input ip address
    global flsm_input_ipaddress
    global title_inputipaddress
    title_inputipaddress = Label(input_frame ,text="IP Address" ,fg ="#FFFFFF" ,bg="#303030")
    flsm_input_ipaddress = Entry(input_frame, fg ="#151515" ,bg="#252525", justify='center' ,borderwidth=0)


    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    global flsm_ip_before_auto_fill
    global flsm_auto_fill_ipd1_before
    global flsm_auto_fill_ipd2_before
    global flsm_auto_fill_ipd3_before
    flsm_ip_before_auto_fill  = ""
    flsm_auto_fill_ipd1_before=""
    flsm_auto_fill_ipd2_before =""
    flsm_auto_fill_ipd3_before = ""

    def auto_fill_ipaddress_flsm():
        global flsm_ip_before_auto_fill
        global flsm_auto_fill_ipd1_before
        global flsm_auto_fill_ipd2_before
        global flsm_auto_fill_ipd3_before

        if flsm_input_ipaddress.get() != flsm_ip_before_auto_fill:
            print("def : {0} --> running".format("auto_fill_ipaddress_flsm"),end="\r")
            print(" "*50,end="\r")
            flsm_ip_before_auto_fill = flsm_input_ipaddress.get()
            
            ip1 = ""
            ip2 = ""
            ip3 = ""
            index = 0
            for i in flsm_input_ipaddress.get() :
                if i == "." :
                    break
                ip1 += i
                index += 1

            index += 1   
            for i in flsm_input_ipaddress.get()[index:] :
                if i == ".":
                    break
                ip2 += i
                index += 1

            index += 1
            for i in flsm_input_ipaddress.get()[index:] :
                if i == ".":
                    break
                ip3 += i
                index += 1
            
            ##########################################################
            ##########################################################
            #class a
            try:
                if int(ip1) > 0 and int(ip1)  < 127 :
                    try:
                        p1,p2,p3,p4 = flsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+".0.0.0"
                        flsm_input_ipaddress.delete(0,"end")
                        flsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if flsm_auto_fill_ipd1_before != ip1 :
                            flsm_auto_fill_ipd1_before = ip1
                            try:
                                ip1 = int(ip1) 
                                ip_ad = str(ip1)+".0.0.0"
                                flsm_input_ipaddress.delete(0,"end")
                                flsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
            ##########################################################
            ##########################################################
            #class b
                elif int(ip1) > 127 and int(ip1) <192 :
                    try:
                        p1,p2,p3,p4 = flsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+"."+str(p2) + ".0.0"
                        flsm_input_ipaddress.delete(0,"end")
                        flsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if flsm_auto_fill_ipd1_before != ip1 or  flsm_auto_fill_ipd2_before != ip2:
                            flsm_auto_fill_ipd1_before = ip1
                            flsm_auto_fill_ipd2_before = ip2
                            try:
                                ip1 = int(ip1) 
                                ip2 = int(ip2)
                                ip_ad = str(ip1)+ "."  + str(ip2)+ ".0.0"
                                flsm_input_ipaddress.delete(0,"end")
                                flsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
                ##########################################################
                ##########################################################
                #class c
                elif int(ip1) > 191 and int(ip1) <224:
                    try:
                        p1,p2,p3,p4 = flsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+"."+str(p2) + "." + str(p3) + ".0"
                        flsm_input_ipaddress.delete(0,"end")
                        flsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if flsm_auto_fill_ipd1_before != ip1 or  flsm_auto_fill_ipd2_before != ip2 or flsm_auto_fill_ipd3_before != ip3:
                            flsm_auto_fill_ipd1_before = ip1
                            flsm_auto_fill_ipd2_before = ip2
                            flsm_auto_fill_ipd3_before = ip3
                            try:
                                ip1 = int(ip1) 
                                ip2 = int(ip2)
                                ip3 = int(ip3)
                                ip_ad = str(ip1)+ "."  + str(ip2)+ "." +str(ip3) +".0"
                                flsm_input_ipaddress.delete(0,"end")
                                flsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
            except:
                pass
        main_window.after(50,auto_fill_ipaddress_flsm)
    auto_fill_ipaddress_flsm()
    ##########################################################
    ##########################################################

    global flsm_ip_before
    global ipd_class
    global flsm_input_ipaddress_value
    global input_ipaddress_entry_live

    flsm_input_ipaddress_value = False
    flsm_ip_before  = ""
    ipd_class = "classless"
    input_ipaddress_entry_live = False

    def check_flsm_input_ip():
        global flsm_input_ipaddress_value
        global flsm_ip_before
        global ipd_class
        flsm_ip_now = flsm_input_ipaddress.get()
        if flsm_ip_now != flsm_ip_before:
            print("def : {0} --> running".format("check_flsm_input_ip"),end="\r")
            print(" "*50,end="\r")
            flsm_ip_before = flsm_ip_now
            try:
                ipd1,ipd2,ipd3,ipd4 = flsm_ip_now.split('.')
                ipd1,ipd2,ipd3,ipd4 = int(ipd1),int(ipd2),int(ipd3),int(ipd4)
                if ipd1<256 and ipd2<256 and ipd3<256 and ipd4<256 and ipd1>0 and ipd2>=0 and ipd3>=0 and ipd4>=0 and ipd1!= 127 and ipd1< 224 :
                    if ipd1 > 191 :
                        ipd_class = "class c"
                    elif ipd1 >127 :
                        ipd_class = "class b"
                    else :
                        ipd_class = "class a"
                    flsm_input_ipaddress_value = True
                    if input_ipaddress_entry_live == True:
                        flsm_input_ipaddress.config(fg="#252525")
                    else:
                        flsm_input_ipaddress.config(fg="#ffffff")
                else:
                    flsm_input_ipaddress_value = False
                    flsm_input_ipaddress.config(fg="#ff0000")
                    ipd_class = "classless"
            except:
                flsm_input_ipaddress_value = False
                flsm_input_ipaddress.config(fg="#ff0000")
                ipd_class = "classless"

           
        main_window.after(100,check_flsm_input_ip)
    check_flsm_input_ip()

    def change_input_ipaddress(e):
        global input_ipaddress_entry_live
        input_ipaddress_entry_live = True
        if flsm_input_ipaddress_value == True:
            flsm_input_ipaddress.config(fg="#252525")
        else:
            flsm_input_ipaddress.config(fg="#ff0000")
        flsm_input_ipaddress.config(bg="#ffffff")
        flsm_input_ipaddress.configure(insertbackground='#000000')

    def change_input_ipaddress_re(e):
        global input_ipaddress_entry_live
        input_ipaddress_entry_live = False
        if flsm_input_ipaddress_value == True:
             flsm_input_ipaddress.config(fg="#ffffff")
        else:
            flsm_input_ipaddress.config(fg="#ff0000")
        flsm_input_ipaddress.config(bg="#252525")
        flsm_input_ipaddress.configure(insertbackground='#FFFFFF')
 
    flsm_input_ipaddress.bind("<Enter>",change_input_ipaddress)
    flsm_input_ipaddress.bind("<Leave>",change_input_ipaddress_re)

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    # -------- input usable hosts
    global title_inputhosts
    global flsm_input_usablehosts
    title_inputhosts = Label(input_frame ,text="Hosts" ,fg ="#FFFFFF" ,bg="#303030")
    flsm_input_usablehosts = Entry(input_frame, fg ="#151515" ,bg="#252525", justify='center' ,borderwidth=0 ,
                              disabledbackground="#454545" ) 
  
    ##########################################################
    ##########################################################

    global flsm_host_before
    global flsm_input_hosts_value
    global ip_class_host_before
    global input_host_entry_live
    global ipd_class_before_host

    flsm_input_hosts_value = False
    flsm_host_before = ""
    ip_class_host_before = "classless"
    input_host_entry_live = False
    ipd_class_before_host = ""

    def check_flsm_input_host():
        global flsm_input_hosts_value
        global flsm_host_before
        global ipd_class_before_host
        flsm_host_now = flsm_input_usablehosts.get()
     
        if flsm_host_now != flsm_host_before or ipd_class != ipd_class_before_host :
            print("def : {0} --> running".format("check_flsm_input_host"),end="\r")
            print(" "*50,end="\r")
            ipd_class_before_host  = ipd_class
            flsm_host_before = flsm_host_now
            try:
                flsm_host_now = int(flsm_host_now)
                flsm_input_hosts_value = True
                if ipd_class == "class c" :
                    if  flsm_host_now <= 254 and flsm_host_now >= 0  :
                        flsm_input_hosts_value = True
                    else:
                        flsm_input_hosts_value = False
                elif ipd_class == "class b" :
                    if flsm_host_now <= 65534 and flsm_host_now >= 0  :
                        flsm_input_hosts_value = True
                    else:
                        flsm_input_hosts_value = False
                elif ipd_class == "class a" :
                    if flsm_host_now <= 16777214 and flsm_host_now >= 0  :
                        flsm_input_hosts_value = True
                    else:
                        flsm_input_hosts_value = False
                else:
                    flsm_input_hosts_value = True
            except :
                flsm_input_hosts_value = False

            if flsm_input_hosts_value == False :
                flsm_input_usablehosts.config(fg="#ff0000")
            else:
                if input_host_entry_live == True :
                    flsm_input_usablehosts.config(fg="#252525")
                else:
                    flsm_input_usablehosts.config(fg="#ffffff")
        
        main_window.after(100,check_flsm_input_host)

    check_flsm_input_host()
    #entrys  style
   
    def change_input_hosts(e):
        global input_host_entry_live
        input_host_entry_live = True
        if flsm_input_hosts_value  == True:
            flsm_input_usablehosts.config(fg="#252525")
        else:
            flsm_input_usablehosts.config(fg="#ff0000")
        flsm_input_usablehosts.config(bg="#ffffff")

        flsm_input_usablehosts.configure(insertbackground='#000000')

    def change_input_hosts_re(e):
        global input_host_entry_live
        input_host_entry_live = False
        if flsm_input_hosts_value  == True:
            flsm_input_usablehosts.config(fg="#ffffff")
        else:
            flsm_input_usablehosts.config(fg="#ff0000")
        flsm_input_usablehosts.config(bg="#252525")

        flsm_input_usablehosts.configure(insertbackground='#FFFFFF')

    flsm_input_usablehosts.bind("<Enter>",change_input_hosts)
    flsm_input_usablehosts.bind("<Leave>",change_input_hosts_re)

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################

    # -------- input networks
    global title_inputnetworks
    global flsm_input_networks
    title_inputnetworks = Label(input_frame ,text="Sub-networks" ,fg ="#FFFFFF" ,bg="#303030")
    flsm_input_networks = Entry(input_frame, fg ="#151515" ,bg="#252525", justify='center' ,borderwidth=0 ,
                           disabledbackground="#454545")

    ################################ ##########################
    ##########################################################
    global flsm_network_before
    global flsm_input_networks_value
    global ip_class_network_before
    global input_network_entry_live
    global ipd_class_before_network

    flsm_input_networks_value = False
    flsm_network_before = ""
    ip_class_network_before = "classless"
    input_network_entry_live = False
    ipd_class_before_network = ""

    def check_flsm_input_network():
        global flsm_input_networks_value
        global flsm_network_before
        global ipd_class_before_network
        flsm_network_now = flsm_input_networks.get()
     
        if flsm_network_now != flsm_network_before or ipd_class != ipd_class_before_network :
            print("def : {0} --> running".format("check_flsm_input_network"),end="\r")
            print(" "*50,end="\r")
            ipd_class_before_network  = ipd_class
            flsm_network_before = flsm_network_now
            try:
                flsm_network_now = int(flsm_network_now)
                flsm_input_networks_value = True
                if ipd_class == "class c" :
                    if  flsm_network_now <= 256 and flsm_network_now >= 0  :
                        flsm_input_networks_value = True
                    else:
                        flsm_input_networks_value = False
                elif ipd_class == "class b" :
                    if flsm_network_now <= 65536 and flsm_network_now >= 0  :
                        flsm_input_networks_value = True
                    else:
                        flsm_input_networks_value = False
                elif ipd_class == "class a" :
                    if flsm_network_now <= 16777216 and flsm_network_now >= 0  :
                        flsm_input_networks_value = True
                    else:
                        flsm_input_networks_value = False
                else:
                    flsm_input_networks_value = True
            except :
                flsm_input_networks_value = False

            if flsm_input_networks_value == False :
                flsm_input_networks.config(fg="#ff0000")
            else:
                if input_network_entry_live == True :
                    flsm_input_networks.config(fg="#252525")
                else:
                    flsm_input_networks.config(fg="#ffffff")
            
        main_window.after(100,check_flsm_input_network)

    check_flsm_input_network()
    #entrys  style

    def change_input_networks(e):
        global input_network_entry_live
        input_network_entry_live = True
        if flsm_input_networks_value== True:
            flsm_input_networks.config(fg="#252525")
        else:
            flsm_input_networks.config(fg="#ff0000")
        flsm_input_networks.config(bg="#ffffff")

        flsm_input_networks.configure(insertbackground='#000000')

    def change_input_networks_re(e):
        global input_network_entry_live
        input_network_entry_live = False
        if flsm_input_networks_value== True:
            flsm_input_networks.config(fg="#ffffff")
        else:
            flsm_input_networks.config(fg="#ff0000")
        flsm_input_networks.config(bg="#252525")
        flsm_input_networks.configure(insertbackground='#FFFFFF')
        
    flsm_input_networks.bind("<Enter>",change_input_networks)
    flsm_input_networks.bind("<Leave>",change_input_networks_re)


    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    # -------- input SubnetMask
    global title_inputSubnetmask
    global flsm_input_subnetmask
    title_inputSubnetmask = Label(input_frame ,text="Subnet Mask" ,fg ="#FFFFFF" ,bg="#303030")
    flsm_input_subnetmask = Entry(input_frame, fg ="#151515" ,bg="#252525", justify='center' ,borderwidth=0,
                            disabledbackground="#454545")
    
    global flsm_subnet_mask_before
    global ipd_class_before_subnet_mask

    flsm_subnet_mask_before =  ""
    ipd_class_before_subnet_mask =""

    def check_subnet_mask_for_class(subs,ipd_class) :
        if ipd_class == "class c" :
            if subs[0]==255 and subs[1]==255 and subs[2]==255 :
                value = True
            else:
                value = False
        ##########################################################
        elif ipd_class == "class b" :
            
            if subs[0]== 255 and subs[1]== 255 :
                if subs[2] == 255 :
                    value = True
                else:
                   
                    if subs[3] == 0 :
                        value = True
                    else:
                        value =  False
            else:
                value = False
        ##########################################################
        else :

            
            if subs[0] == 255:
                if subs[1] == 255:
                    if subs[2] == 255 :
                        value = True
                    else:
                        if subs[3] == 0 :
                            value = True
                        else:
                            value= False 
                else:
                    if subs[2] == 0 and subs[3] == 0 :
                        value = True
                    else:
                        value = False
            else:
                value = False
        return value
        
    def check_flsm_input_subnetmask() :
        global flsm_subnet_mask_before
        global ipd_class_before_subnet_mask
        global flsm_input_subnet_mask_value

        flsm_subnet_mask_now = flsm_input_subnetmask.get()
        if flsm_subnet_mask_now != flsm_subnet_mask_before or ipd_class != ipd_class_before_subnet_mask :
            print("def : {0} --> running".format("check_flsm_input_subnetmask"),end="\r")
            print(" "*50,end="\r")
            ipd_class_before_subnet_mask = ipd_class
            flsm_subnet_mask_before = flsm_subnet_mask_now
          
            try:
                sub1,sub2,sub3,sub4 = flsm_subnet_mask_now.split(".")
                try:
                    sub1,sub2,sub3,sub4 = int(sub1),int(sub2),int(sub3),int(sub4) 
                    subs = [sub1,sub2,sub3,sub4]
                    sub_vals = [255,254,248,240,224,192,128,0]
                    temp_flsm_input_subnet_mask_value  = True
                    for sub in subs :
                        sub_value = False
                        for sub_val in sub_vals :
                            if sub == sub_val:
                                sub_value = True
                        if sub_value == False:
                            temp_flsm_input_subnet_mask_value = False
                            flsm_input_subnet_mask_value = False
                    if temp_flsm_input_subnet_mask_value != False :
                        flsm_input_subnet_mask_value = check_subnet_mask_for_class(subs,ipd_class)
                except :
                    flsm_input_subnet_mask_value = False
            except:
                flsm_input_subnet_mask_value = False
            
            if flsm_input_subnet_mask_value == False:
                flsm_input_subnetmask.config(fg="#ff0000")
            else:
                if input_subnet_mask_entry_live == True:
                    flsm_input_subnetmask.config(fg="#252525")
                else:
                    flsm_input_subnetmask.config(fg="#ffffff")
        main_window.after(100,check_flsm_input_subnetmask)
    check_flsm_input_subnetmask()

    def change_input_subnetmask(e):
        global input_subnet_mask_entry_live
        input_subnet_mask_entry_live = True
        if flsm_input_subnet_mask_value == True:
            flsm_input_subnetmask.config(fg="#252525")
        else:
            flsm_input_subnetmask.config(fg="#ff0000")
        flsm_input_subnetmask.config(bg="#ffffff")
        flsm_input_subnetmask.configure(insertbackground='#000000')
        
    def change_input_subnetmask_re(e):
        global input_subnet_mask_entry_live
        input_subnet_mask_entry_live = False
        if flsm_input_subnet_mask_value == True:
            flsm_input_subnetmask.config(fg="#ffffff")
        else:
            flsm_input_subnetmask.config(fg="#ff0000")
        flsm_input_subnetmask.config(bg="#252525")
        flsm_input_subnetmask.configure(insertbackground='#FFFFFF')

    flsm_input_subnetmask.bind("<Enter>",change_input_subnetmask)
    flsm_input_subnetmask.bind("<Leave>",change_input_subnetmask_re)
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    #check all entry 
    def set_state_input_entry():
        print("def : {0} --> running".format("set_state_input_entry"),end="\r")
        print(" "*50,end="\r")
        hosts = flsm_input_usablehosts.get().replace(" ","")
        subnetworks = flsm_input_networks.get().replace(" ","")
        submask = flsm_input_subnetmask.get().replace(" ","")

        if hosts != "" :
            flsm_input_networks.config(state="disabled")
            flsm_input_subnetmask.config(state="disabled")
        elif subnetworks != "":
            flsm_input_usablehosts.config(state="disabled")
            flsm_input_subnetmask.config(state="disabled")
        elif submask != "" :
            flsm_input_networks.config(state="disabled")
            flsm_input_usablehosts.config(state="disabled")
        else:
            flsm_input_subnetmask.config(state="normal")
            flsm_input_networks.config(state="normal")
            flsm_input_usablehosts.config(state="normal")
        
        main_window.after(100,set_state_input_entry)
    set_state_input_entry()

    flsm_input_ipaddress.bind("<FocusIn>",auto_close_side_panel)
    flsm_input_usablehosts.bind("<FocusIn>",auto_close_side_panel)
    flsm_input_networks.bind("<FocusIn>",auto_close_side_panel)
    flsm_input_subnetmask.bind("<FocusIn>",auto_close_side_panel)
      

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    
    # -------- print(:)

    global input_dashes
    
    input_dash0 = Label(input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    input_dash1 = Label(input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    input_dash2 = Label(input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    input_dash3 = Label(input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    input_dashes = [input_dash0,input_dash1,input_dash2,input_dash3]

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################

    def set_flsm_calculate_buttons_style():
        print("def : {0} --> running".format("set_flsm_calculate_buttons_style"),end="\r")
        print(" "*50,end="\r")
        if flsm_input_ipaddress_value == True  and ( flsm_input_hosts_value == True or  flsm_input_networks_value== True or flsm_input_subnet_mask_value == True) :
            if calculate_button_widget_live == True:
                calculate_button.config(image=calculate_button_image_re,command = start_flsm_calculate )
            else:
                calculate_button.config(image=calculate_button_image,command = start_flsm_calculate )
        else:
            calculate_button.config(image=calculate_button_error_image ,command="")
        main_window.after(100,set_flsm_calculate_buttons_style)
    # -------- Button
    global calculate_button
    global reset_button
    calculate_button = Button(input_frame , border=False ,activebackground="#151515" ,
                                bg="#151515",cursor="hand2")
    calculate_button.place(rely = 0.77 ,relx = 0.45) 


    global calculate_button_widget_live
    calculate_button_widget_live = False
    def change_calculate_button(e):
        global calculate_button_widget_live
        calculate_button_widget_live = True
        if flsm_input_ipaddress_value == True  and ( flsm_input_hosts_value == True or  flsm_input_networks_value== True or flsm_input_subnet_mask_value == True) :
            calculate_button.config(image=calculate_button_image_re)
    def change_calculate_button_re(e):
        global calculate_button_widget_live
        calculate_button_widget_live = False
        if flsm_input_ipaddress_value == True  and ( flsm_input_hosts_value == True or  flsm_input_networks_value== True or flsm_input_subnet_mask_value == True) :
            calculate_button.config(image=calculate_button_image)
    calculate_button.bind("<Leave>",change_calculate_button_re)
    calculate_button.bind("<Enter>",change_calculate_button)

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    def reset_flsm_inputs():
        flsm_input_ipaddress.delete(0,"end")
        flsm_input_usablehosts.delete(0,"end")
        flsm_input_networks.delete(0,"end")
        flsm_input_subnetmask.delete(0,"end")
        for widget in flsm_out_put_widget:
            widget.config(text="")
        for widget in flsm_table_range_1 + flsm_table_range_2:
            widget.config(text="")
        for widget in flsm_table_usable_range_1 + flsm_table_usable_range_2:
            widget.config(text="")
    def reset_flsm_lable():
        for widget in flsm_out_put_widget:
            widget.config(text="")
        for widget in flsm_table_range_1 + flsm_table_range_2:
            widget.config(text="")
        for widget in flsm_table_usable_range_1 + flsm_table_usable_range_2:
            widget.config(text="")
            
    reset_button = Button(input_frame , border=False ,activebackground="#151515" ,command=reset_flsm_inputs,
                           bg="#151515" ,fg="#ffffff" ,cursor="hand2")
    reset_button.place(rely = 0.77,relx = 0.68)

    def change_reset_button(e):
        reset_button.config(image=reset_button_image_re)
    def change_reset_button_re(e):
        reset_button.config(image=reset_button_image)
    reset_button.bind("<Enter>",change_reset_button)
    reset_button.bind("<Leave>",change_reset_button_re)

    ##########################################################
    global flsm_before_ip
    global flsm_before_networks
    global flsm_before_subnet_mask
    global flsm_before_hosts
    flsm_before_ip = ""
    flsm_before_networks =""
    flsm_before_subnet_mask = ""
    flsm_before_hosts = ""
    def auto_reset_flsm_values():
        global flsm_before_ip
        global flsm_before_networks
        global flsm_before_subnet_mask
        global flsm_before_hosts
        if flsm_before_ip != flsm_input_ipaddress.get() or flsm_before_networks!=flsm_input_networks.get()\
            or flsm_before_subnet_mask != flsm_input_subnetmask.get() or flsm_before_hosts != flsm_input_usablehosts.get():
            print("def : {0} --> running".format("set_flsm_calculate_buttons_style"),end="\r")
            print(" "*50,end="\r")
            flsm_before_ip = flsm_input_ipaddress.get()
            flsm_before_networks = flsm_input_networks.get()
            flsm_before_subnet_mask = flsm_input_subnetmask.get()
            flsm_before_hosts = flsm_input_usablehosts.get()
            reset_flsm_lable()
        main_window.after(100,auto_reset_flsm_values)

    auto_reset_flsm_values()
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################

    #outputs 
    global output_frame1
    global output_frame_label

    output_frame1 = Frame(main_window ,bg="#100e17")
    output_frame1.place(relwidth = 0.31 ,relheight=0.25 ,relx= 0.5 ,rely=0.13 )
    output_frame_label = Label(output_frame1,bg="#100e17")
    output_frame_label.place(rely=0)

    # -------- Dsiplay IP Address
    global title_ip_address
    global display_ip_address
    global title_ip_address_class
    global display_ip_address_class
    global title_subnet_number
    global display_subnet_number
    global display_host_number
    global title_numberhost_number
    global title_usable_host_number
    global display_usable_host_number
    global title_increment_Value_num
    global display_Increment_Value_num
   
    # -------- Dsiplay ip Address
    title_ip_address = Label(output_frame1 ,text="IP Address" ,fg ="#FFFFFF" ,bg="#303030")
    display_ip_address = Label(output_frame1 ,fg ="#FFFFFF" ,bg="#303030")          
    # -------- Dsiplay ip class
    title_ip_address_class = Label(output_frame1 ,text="IP Address Class" ,fg ="#FFFFFF" ,bg="#050505")
    display_ip_address_class = Label(output_frame1 ,fg ="#FFFFFF"  ,bg="#050505")
    # -------- display number of subnetworks
    title_subnet_number = Label(output_frame1 ,text="No. of Sub-Networks" ,fg ="#FFFFFF"  ,bg="#303030")
    display_subnet_number = Label(output_frame1 ,fg ="#FFFFFF" ,bg="#303030")
    # -------- display number of hosts
    title_numberhost_number = Label(output_frame1 ,text="No. of IP Addresses" ,fg ="#FFFFFF" ,bg="#050505")
    display_host_number = Label(output_frame1 ,fg ="#FFFFFF"  ,bg="#050505")
    # -------- display number of usable hosts
    title_usable_host_number = Label(output_frame1 ,text="Hosts per Subnet" ,fg ="#FFFFFF"  ,bg="#303030")
    display_usable_host_number = Label(output_frame1 ,fg ="#FFFFFF" ,bg="#303030")
    # -------- display increment value
    title_increment_Value_num = Label(output_frame1 ,text="Increment Value" ,fg ="#FFFFFF" ,bg="#050505")
    display_Increment_Value_num = Label(output_frame1 ,fg ="#FFFFFF"  ,bg="#050505")

    # -------- print(:)
    global output_dash0
    global output_dash1
    global output_dash2
    global output_dash3
    global output_dash4
    global output_dash5

    output_dash0 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    output_dash1 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#050505")
    output_dash2 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    output_dash3 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#050505")
    output_dash4 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    output_dash5 = Label(output_frame1 ,text=":" ,fg ="#FFFFFF" ,bg="#050505")
                            
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    #ouput2
    global output_frame2_label
    global output_frame2

    output_frame2 = Frame(main_window ,bg="#100e17")
    output_frame2.place(relwidth = 0.487 ,relheight=0.2 ,relx= 0.42,rely=0.4 )
    output_frame2_label = Label(output_frame2,bg="#100e17")
    output_frame2_label.place(rely=0)

    # -------- display default subnet mask
    global title_default_subnet_mask
    global display_default_subnet_mask
    global title_default_subnet_mask_binary
    global display_default_subnet_mask_binary

    title_default_subnet_mask = Label(output_frame2 ,text="Default Subnet Mask" ,fg ="#FFFFFF" ,bg="#303030")
    display_default_subnet_mask = Label(output_frame2  ,fg ="#FFFFFF" ,bg="#303030")
    title_default_subnet_mask_binary = Label(output_frame2 ,text="Default Subnet Mask(Binary)" ,fg ="#FFFFFF" ,bg="#050505")
    display_default_subnet_mask_binary = Label(output_frame2 ,fg ="#FFFFFF" ,bg="#050505")
                    
    #---------------------------display subnet mask
    global title_subnet_mask
    global display_subnet_mask
    global title_subnet_mask_binary
    global display_subnet_mask_binary

    title_subnet_mask = Label(output_frame2 ,text="Subnet Mask" ,fg ="#FFFFFF" ,bg="#303030")
    display_subnet_mask = Label(output_frame2 ,fg ="#FFFFFF" ,bg="#303030")
    title_subnet_mask_binary = Label(output_frame2 ,text="Subnet Mask(Binary)" ,fg ="#FFFFFF" ,bg="#050505")
    display_subnet_mask_binary = Label(output_frame2 ,fg="#FFFFFF" ,bg="#050505")
                                
    # -------- print(:)
    global output2_dash0
    global output2_dash1
    global output2_dash2
    global output2_dash3

    output2_dash0 = Label(output_frame2 ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    output2_dash1 = Label(output_frame2 ,text=":" ,fg ="#FFFFFF" ,bg="#050505") 
    output2_dash2 = Label(output_frame2 ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    output2_dash3 = Label(output_frame2 ,text=":" ,fg ="#FFFFFF" ,bg="#050505")
     

    global flsm_out_put_widget
    flsm_out_put_widget = [display_ip_address , display_ip_address_class , display_subnet_number ,
                          display_host_number ,display_usable_host_number ,display_Increment_Value_num ,
                          display_default_subnet_mask ,display_default_subnet_mask_binary,
                          display_subnet_mask,display_subnet_mask_binary]                     
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #ip ranges
    global output_table1_label
    global output_frame3

    output_frame3 = Frame(main_window ,bg="#100e17")
    output_frame3.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.1 ,rely=0.62 )
    output_table1_label = Label(output_frame3 ,bg="#100e17")
    output_table1_label.pack()

    # -------- table title label 
    global title_ipranges
    title_ipranges = Label(output_frame3 ,text="IP Ranges" ,fg ="#FFFFFF" ,bg="#000000")
    title_ipranges.place(relx=0.37 ,rely=0.07 )

    # --------Range 
    global flsm_range1
    global flsm_range2
    global flsm_range3
    global flsm_range4
    global flsm_range5
    global flsm_range6
    flsm_range1 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="e")
    flsm_range2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="e")
    flsm_range3 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="e")
    flsm_range4 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="e")                         
    flsm_range5 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="e")
    flsm_range6 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="e")

    flsm_range1_2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_range2_2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="w")
    flsm_range3_2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_range4_2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="w")                         
    flsm_range5_2 = Label(output_frame3  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_range6_2 = Label(output_frame3 ,fg ="#FFFFFF"  ,bg="#000000",width=15 ,anchor="w")

    global flsm_table_range
    flsm_table_range = [[flsm_range1,flsm_range2,flsm_range3,
                       flsm_range4,flsm_range5,flsm_range6],
                       [flsm_range1_2,flsm_range2_2,flsm_range3_2,
                       flsm_range4_2,flsm_range5_2,flsm_range6_2]]        

    global flsm_table_range_1
    global flsm_table_range_2
    flsm_table_range_1  = [flsm_range1,flsm_range2,flsm_range3,
                       flsm_range4,flsm_range5,flsm_range6]
    flsm_table_range_2 = [flsm_range1_2,flsm_range2_2,flsm_range3_2,
                       flsm_range4_2,flsm_range5_2,flsm_range6_2]

      # -------- print("-")
    global table1_dash1
    global table1_dash2
    global table1_dash3
    global table1_dash4
    global table1_dash5
    global table1_dash6

    table1_dash1 = Label(output_frame3 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030") 
    table1_dash2 = Label(output_frame3 ,text="-" ,fg ="#FFFFFF"  ,bg="#000000")
    table1_dash3 = Label(output_frame3 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030")                        
    table1_dash4 = Label(output_frame3 ,text="-" ,fg ="#FFFFFF"  ,bg="#000000")
    table1_dash5 = Label(output_frame3 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030")
    table1_dash6 = Label(output_frame3 ,text="-" ,fg ="#ffffff" ,bg="#000000")
    
    
    #############################################################
    #############################################################
    #############################################################
    # --------Usable Range 
    global output_table2_label
    global output_frame4

    output_frame4 = Frame(main_window ,bg="#100e17")
    output_frame4.place(relwidth = 0.288 ,relheight=0.31 ,relx= 0.45 ,rely=0.62 )
    output_table2_label = Label(output_frame4 ,bg="#100e17")
    output_table2_label.pack()

    # -------- table title label
    global title_usable_ipranges
    title_usable_ipranges = Label(output_frame4 ,text="Usable IP Ranges" ,fg ="#FFFFFF" ,bg="#000000")
    title_usable_ipranges.place(relx=0.27 ,rely=0.07 )

    # -------- label for range 1
    global flsm_usable_range1
    global flsm_usable_range2
    global flsm_usable_range3
    global flsm_usable_range4
    global flsm_usable_range5
    global flsm_usable_range6

    flsm_usable_range1 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#303030" ,width=15 ,anchor="e" )
    flsm_usable_range2 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#000000" ,width=15 ,anchor="e" )
    flsm_usable_range3 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#303030" ,width=15 ,anchor="e" )
    flsm_usable_range4 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#000000" ,width=15 ,anchor="e" )
    flsm_usable_range5 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#303030" ,width=15 ,anchor="e" )
    flsm_usable_range6 = Label(output_frame4 ,fg ="#FFFFFF" ,bg="#000000" ,width=15 ,anchor="e" )
    
    flsm_usable_range1_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_usable_range2_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="w")
    flsm_usable_range3_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_usable_range4_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="w")                         
    flsm_usable_range5_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#303030",width=15 ,anchor="w")
    flsm_usable_range6_2 = Label(output_frame4  ,fg ="#FFFFFF" ,bg="#000000",width=15 ,anchor="w")

    
    global flsm_table_usable_range
    flsm_table_usable_range = [[flsm_usable_range1,flsm_usable_range2,flsm_usable_range3,
                                flsm_usable_range4,flsm_usable_range5,flsm_usable_range6,],
                               [flsm_usable_range1_2,flsm_usable_range2_2,flsm_usable_range3_2,
                                flsm_usable_range4_2,flsm_usable_range5_2,flsm_usable_range6_2]]   

    global flsm_table_usable_range_1
    global flsm_table_usable_range_2
    flsm_table_usable_range_1 = [flsm_usable_range1,flsm_usable_range2,flsm_usable_range3,
                          flsm_usable_range4,flsm_usable_range5,flsm_usable_range6,]
    flsm_table_usable_range_2 = [flsm_usable_range1_2,flsm_usable_range2_2,flsm_usable_range3_2,
                          flsm_usable_range4_2,flsm_usable_range5_2,flsm_usable_range6_2]


    # -------- print("-")
    global table2_dash1
    global table2_dash2
    global table2_dash3
    global table2_dash4
    global table2_dash5
    global table2_dash6

    table2_dash1 = Label(output_frame4 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030" )
    table2_dash2 = Label(output_frame4 ,text="-" ,fg ="#FFFFFF"  ,bg="#000000" )
    table2_dash3 = Label(output_frame4 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030" )                    
    table2_dash4 = Label(output_frame4 ,text="-" ,fg ="#FFFFFF"  ,bg="#000000" )
    table2_dash5 = Label(output_frame4 ,text="-" ,fg ="#FFFFFF"  ,bg="#303030" )
    table2_dash6 = Label(output_frame4 ,text="-" ,fg ="#ffffff"  ,bg="#000000" )
                             
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################

    def flsm_read_flsm_output_val():
        files = ["ip_address.rapa" ,"ip_address_class.rapa", "sub_nets.rapa",
                "ip_addresses.rapa" ,"hosts.rapa" ,"increment_value.rapa",
                "default_subnet_mask.rapa","binary_default_subnet_mask.rapa",
                "subnet_mask.rapa","binary_subnet_mask.rapa"]

        flsm_output_values = []

        for file in files :
            f = open("FLSM\\"+file,"r")
            flsm_output_values.append((f.readline()))
            f.close()

        display_ip_address.config(text=flsm_output_values[0])
        display_ip_address_class.config(text=flsm_output_values[1])
        display_subnet_number.config(text=flsm_output_values[2]       + superscripted(flsm_output_values[2],"   (",")") )
        display_host_number.config(text=flsm_output_values[3]         + superscripted(flsm_output_values[3],"   (",")" ) )

        try:
            if int(flsm_output_values[4]) <  0 :
                flsm_output_values[4] = "-"
            elif int(flsm_output_values[4]) ==  0 :
                flsm_output_values[4] = 0
            else:
                flsm_output_values[4]  = flsm_output_values[4]  + superscripted(flsm_output_values[4],"   (","-2)" )
        except:
            flsm_output_values[4]  = flsm_output_values[4]  + superscripted(flsm_output_values[4],"   (","-2)" )

        display_usable_host_number.config(text=flsm_output_values[4])

        display_Increment_Value_num.config(text=flsm_output_values[5] + superscripted(flsm_output_values[5],"   (",")" ) )
        display_default_subnet_mask.config(text=flsm_output_values[6])
        display_default_subnet_mask_binary.config(text=flsm_output_values[7])
        display_subnet_mask.config(text=flsm_output_values[8])
        display_subnet_mask_binary.config(text=flsm_output_values[9])

        ##########################################################
        ##########################################################
        ##########################################################
        ##########################################################
        ##########################################################
        ##########################################################

        #read ip range
        ipranges_output_tem = []
        ipranges_output_tem2 = []
        file_start_ip = open("FLSM\\ip_ranges.rapa","r")
        for i in range(6) :
            ip = file_start_ip.readline()
            replace_x = ""
            if ip == "":
                ip = "Not  Available-Not  Available"
                replace_x = " "
            ip1,ip2 = (ip.replace("\n","").replace(' ',replace_x)).split("-")
            ipranges_output_tem.append(ip1)
            ipranges_output_tem2.append(ip2)
        
        #read usable ip range
        ipranges_us_output_tem = []
        ipranges_us_output_tem2 = []
        file_start_ip_us = open("FLSM\\ip_usable_ranges.rapa","r")
        for i in range(6) :
            ip_us = file_start_ip_us.readline()
            replace_x  = ""
            if ip_us == "":
                ip_us = "Not  Available-Not  Available"
                replace_x= " "
            ip_us1,ip_us2 = (ip_us.replace("\n","").replace(' ',replace_x)).split("-")
            
            ipranges_us_output_tem.append(ip_us1)
            ipranges_us_output_tem2.append(ip_us2)

        ##########################################################
        ##########################################################
        ##########################################################
        #########################################################
        # display table 
        index= 0
        for widget in flsm_table_range_1:
            if ipranges_output_tem[index] == "Not  Available":
                widget.config(fg="#808080")
            else:
                widget.config(fg="#ffffff")
            widget.config(text=ipranges_output_tem[index])
            index += 1
        index= 0
        for widget in flsm_table_range_2:
            if ipranges_output_tem2[index] == "Not  Available":
                widget.config(fg="#808080")
            else:
                widget.config(fg="#ffffff")
            widget.config(text=ipranges_output_tem2[index])
            index += 1
        index= 0
        for widget in flsm_table_usable_range_1:
            if ipranges_us_output_tem[index] == "Not  Available":
                widget.config(fg="#808080")
            else:
                widget.config(fg="#ffffff")
            widget.config(text=ipranges_us_output_tem[index])
            index += 1
        index= 0
        for widget in flsm_table_usable_range_2:
            if ipranges_us_output_tem2[index] == "Not  Available":
                widget.config(fg="#808080")
            else:
                widget.config(fg="#ffffff")
            widget.config(text=ipranges_us_output_tem2[index])
            index += 1

    ##########################################################
    def start_flsm_calculate() :
        try:
            os.mkdir("FLSM")
        except:
            pass

        #get old files and delete
        del_files_flsm = os.listdir("FLSM")
        for i in  del_files_flsm:
            os.remove("FLSM\\"+i)

        files =  ["flsm_input_ipaddress.rapa","flsm_input_hosts.rapa","flsm_input_subnets.rapa","flsm_input_subnetmask.rapa"]
        flsm_input_entrys = [flsm_input_ipaddress,flsm_input_usablehosts,flsm_input_networks,flsm_input_subnetmask]

        for i in range(len(flsm_input_entrys)):
            f = open("FLSM\\" + files[i] ,"w" )
            f.write(flsm_input_entrys[i].get())
            f.close()
        
        try:
            os.remove("FLSM\\process_status.rapa")
        except:
            pass

        try:
            os.startfile("flsm cal.exe")
        except:
            os.startfile("flsm cal.py")
    
        while True:
            try:
                file  = open("FLSM\\process_status.rapa","r")
                file.close()
                break
            except:
                pass

        flsm_read_flsm_output_val()


    
    #add vlsm mode wiget to window
    main_root_vlsm_mode()
    loading002()
    #set widget to window same as resolution
    vercion_set()
    check_resolution()
    #set widget to window same as resolution
    vlsm_check_resolution()
    set_flsm_calculate_buttons_style()
    set_vlsm_calculate_buttons_style()
    change_vlsm_special_button_auto()

    #use for get window loaction and save to use next time 
    geometry_reader()

    
##########                             ##########  ##########                          ##################################     ################                                 ################
 ##########                           ##########   ##########                        ######################################   #################                               #################
  ##########                         ##########    ##########                       ########################################  ##################                             ##################
   ##########                       ##########     ##########                       ########################################  ###################                           ###################
    ##########                     ##########      ##########                       ##########                                ####################                         ####################
     ##########                   ##########       ##########                       ##########                                ########## ##########                       ########## ##########
      ##########                 ##########        ##########                       ##########                                ##########  ##########                     ##########  ##########
       ##########               ##########         ##########                       ##########                                ##########   ##########                   ##########   ##########
        ##########             ##########          ##########                       ##########                                ##########    ##########                 ##########    ##########
         ##########           ##########           ##########                       ######################################    ##########     ##########               ##########     ##########
          ##########         ##########            ##########                       #######################################   ##########      ##########             ##########      ##########      
           ##########       ##########             ##########                       ########################################  ##########       ##########           ##########       ##########          
            ##########     ##########              ##########                        #######################################  ##########        ##########         ##########        ########## 
             ##########   ##########               ##########                                                     ##########  ##########         ##########       ##########         ##########
              ########## ##########                ##########                                                     ##########  ##########          ##########     ##########          ########## 
               ###################                 ##########                                                     ##########  ##########           ##########   ##########           ##########
                #################                  ##########                                                     ##########  ##########            ########## ##########            ########## 
                 ###############                   ##########                                                     ##########  ##########             ###################             ##########
                  #############                    ###############################  ########################################  ##########              #################              ##########
                   ###########                     ###############################  ########################################  ##########               ###############               ##########
                    #########                      ###############################   ######################################   ##########                #############                ##########
                     #######                       ###############################     ###################################    ##########                 ###########                 ##########

def main_root_vlsm_mode():
    ##########################################################
    #########################################################
    global vlsm_main_window
    vlsm_main_window = Frame(main_window ,bg="#100e17")
    vlsm_main_window.place(relwidth=1 ,relheight=1)

    #ip address calculator title placing
    global main_title
    main_title_frame = Frame(main_window ,bg="#100e17")
    main_title_frame.place(rely=0.001 ,relx=0.37)
    main_title = Label(main_title_frame,bg="#100e17")
    main_title.pack()

    #########################################################
    #########################################################
    #########################################################

    global vlsm_input_label
    global vlsm_input_frame
    #inputs frame
    vlsm_input_frame = Frame(vlsm_main_window ,bg="#100e17")
    vlsm_input_label = Label(vlsm_input_frame,bg="#100e17")
    vlsm_input_label.pack()

    #input 
    # -------- input ip address
    global vlsm_input_ipaddress
    global vlsm_title_inputipaddress
    vlsm_title_inputipaddress = Label(vlsm_input_frame ,text="IP Address" ,fg ="#FFFFFF" ,bg="#303030" )
    vlsm_input_ipaddress = Entry(vlsm_input_frame, fg ="#151515" ,bg="#252525", justify='center' , borderwidth=0 ,width=15)

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    global vlsm_ip_before_auto_fill
    global vlsm_auto_fill_ipd1_before
    global vlsm_auto_fill_ipd2_before
    global vlsm_auto_fill_ipd3_before
    vlsm_ip_before_auto_fill  = ""
    vlsm_auto_fill_ipd1_before=""
    vlsm_auto_fill_ipd2_before =""
    vlsm_auto_fill_ipd3_before = ""

    def auto_fill_ipaddress_vlsm():
        global vlsm_ip_before_auto_fill
        global vlsm_auto_fill_ipd1_before
        global vlsm_auto_fill_ipd2_before
        global vlsm_auto_fill_ipd3_before

        if vlsm_input_ipaddress.get() != vlsm_ip_before_auto_fill:
            vlsm_ip_before_auto_fill = vlsm_input_ipaddress.get()
            
            ip1 = ""
            ip2 = ""
            ip3 = ""
            index = 0
            for i in vlsm_input_ipaddress.get() :
                if i == "." :
                    break
                ip1 += i
                index += 1

            index += 1   
            for i in vlsm_input_ipaddress.get()[index:] :
                if i == ".":
                    break
                ip2 += i
                index += 1

            index += 1
            for i in vlsm_input_ipaddress.get()[index:] :
                if i == ".":
                    break
                ip3 += i
                index += 1
            
            ##########################################################
            ##########################################################
            #class a
            try:
                if int(ip1) > 0 and int(ip1)  < 127 :
                    try:
                        p1,p2,p3,p4 = vlsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+".0.0.0"
                        vlsm_input_ipaddress.delete(0,"end")
                        vlsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if vlsm_auto_fill_ipd1_before != ip1:
                            vlsm_auto_fill_ipd1_before = ip1
                            try:
                                ip1 = int(ip1) 
                                ip_ad = str(ip1)+".0.0.0"
                                vlsm_input_ipaddress.delete(0,"end")
                                vlsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
            ##########################################################
            ##########################################################
            #class b
                elif int(ip1) > 127 and int(ip1) <192 :
                    try:
                        p1,p2,p3,p4 = vlsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+"."+str(p2) + ".0.0"
                        vlsm_input_ipaddress.delete(0,"end")
                        vlsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if vlsm_auto_fill_ipd1_before != ip1 or  vlsm_auto_fill_ipd2_before != ip2:
                            vlsm_auto_fill_ipd1_before = ip1
                            vlsm_auto_fill_ipd2_before = ip2
                            try:
                                ip1 = int(ip1) 
                                ip2 = int(ip2)
                                ip_ad = str(ip1)+ "."  + str(ip2)+ ".0.0"
                                vlsm_input_ipaddress.delete(0,"end")
                                vlsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
                ##########################################################
                ##########################################################
                #class c
                elif int(ip1) > 191 and int(ip1) <224:
                    try:
                        p1,p2,p3,p4 = vlsm_input_ipaddress.get().split(".")
                        int(p1),int(p2),int(p3),int(p4)
                        ip = str(p1)+"."+str(p2) + "." + str(p3) + ".0"
                        vlsm_input_ipaddress.delete(0,"end")
                        vlsm_input_ipaddress.insert(0,ip)
                    except:
                        pass
                    if i == ".":
                        if vlsm_auto_fill_ipd1_before != ip1 or  vlsm_auto_fill_ipd2_before != ip2 or vlsm_auto_fill_ipd3_before != ip3:
                            vlsm_auto_fill_ipd1_before = ip1
                            vlsm_auto_fill_ipd2_before = ip2
                            vlsm_auto_fill_ipd3_before = ip3
                            try:
                                ip1 = int(ip1) 
                                ip2 = int(ip2)
                                ip3 = int(ip3)
                                ip_ad = str(ip1)+ "."  + str(ip2)+ "." +str(ip3) +".0"
                                vlsm_input_ipaddress.delete(0,"end")
                                vlsm_input_ipaddress.insert(0,ip_ad)
                            except:
                                pass
            except:
                pass
        main_window.after(50,auto_fill_ipaddress_vlsm)
    auto_fill_ipaddress_vlsm()
    #check ip address 
    ################################################
    ################################################
    ################################################
    global vlsm_input_ipaddress_value
    vlsm_input_ipaddress_value = False

    global vlsm_ip_address_before
    vlsm_ip_address_before = ""

    global vlsm_ip_class
    vlsm_ip_class = False
    global vlsm_ip_class_before
    vlsm_ip_class_before = False
    ################################################
    ################################################
    ################################################
    def check_vlsm_ip_address():
        global vlsm_input_ipaddress_value 
        global vlsm_ip_address_before
        global vlsm_ip_class
        ip = vlsm_input_ipaddress.get()

        if vlsm_ip_address_before !=  ip :
            vlsm_ip_address_before = ip
            try:
                ip1,ip2,ip3,ip4 = ip.split(".")
                try:
                    ip1,ip2,ip3,ip4  = int(ip1),int(ip2),int(ip3),int(ip4)
                    if ip1>255 or ip2>255 or ip3>255 or ip4>255 or ip1<1 or ip2<0 or ip3<0 or ip4<0 or ip1 == 127 or ip1 >223:
                        vlsm_input_ipaddress.config(fg="#ff0000")
                        vlsm_ip_class = False
                    else:
                        vlsm_input_ipaddress_value = True
                        if vlsm_input_ipaddress_entry_enter == True:
                            vlsm_input_ipaddress.config(fg="#000000")
                        else:
                            vlsm_input_ipaddress.config(fg="#ffffff")
                        if ip1 > 191 :
                            vlsm_ip_class = "class c"
                        elif ip1 > 127 :
                            vlsm_ip_class = "class b"
                        else:
                            vlsm_ip_class = "class a"
                    
                except :
                    vlsm_ip_class = False
                    vlsm_input_ipaddress_value = False
                    vlsm_input_ipaddress.config(fg="#ff0000")
            except:
                vlsm_ip_class = False
                vlsm_input_ipaddress_value = False
                vlsm_input_ipaddress.config(fg="#ff0000")
            
        main_window.after(100,check_vlsm_ip_address)
    check_vlsm_ip_address()


    global vlsm_input_dash0
    vlsm_input_dash0 = Label(vlsm_input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")
    global vlsm_input_ipaddress_entry_enter
    vlsm_input_ipaddress_entry_enter = False

    def vlsm_change_input_ipaddress(e):
        global vlsm_input_ipaddress_entry_enter
        vlsm_input_ipaddress_entry_enter = True
        vlsm_input_ipaddress.config(bg="#ffffff")
        if vlsm_input_ipaddress_value == True:
            vlsm_input_ipaddress.config(fg="#000000")
        else:
            vlsm_input_ipaddress.config(fg="#ff0000")
        vlsm_input_ipaddress.configure(insertbackground='#000000')

    def vlsm_change_input_ipaddress_re(e):
        global vlsm_input_ipaddress_entry_enter
        vlsm_input_ipaddress_entry_enter = False
        vlsm_input_ipaddress.config(bg="#252525")
        if vlsm_input_ipaddress_value == True:
            vlsm_input_ipaddress.config(fg="#ffffff")
        else:
            vlsm_input_ipaddress.config(fg="#ff0000")
        vlsm_input_ipaddress.configure(insertbackground='#FFFFFF')
    
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################

    # -------- input networks
    global vlsm_title_inputnetworks
    global vlsm_input_networks
    vlsm_title_inputnetworks = Label(vlsm_input_frame ,text="Sub-networks" ,fg ="#FFFFFF" ,bg="#303030")
    vlsm_input_networks = Entry(vlsm_input_frame, fg ="#151515" ,bg="#252525", justify='center' ,borderwidth=0 ,width=15)

    global vlsm_network_input_invalid
    vlsm_network_input_invalid = False
    global input_networks_entry_live
    input_networks_entry_live = False 

    global vlsm_input_network_entry_enter
    vlsm_input_network_entry_enter = False
    global vlsm_input_subnet_value
    vlsm_input_subnet_value = False

    #########################################################
    #########################################################
    #########################################################
    # networks input
    def vlsm_change_input_networks(e):
        global vlsm_input_network_entry_enter
        vlsm_input_network_entry_enter = True
        if vlsm_input_subnet_value == True:
            vlsm_input_networks.config(fg="#252525")
        else:
            vlsm_input_networks.config(fg="#ff0000")
        vlsm_input_networks.config(bg="#ffffff")

        vlsm_input_networks.configure(insertbackground='#000000')

    def vlsm_change_input_networks_re(e):
        global vlsm_input_network_entry_enter
        vlsm_input_network_entry_enter = False 
        if vlsm_input_subnet_value == True:
            vlsm_input_networks.config(fg="#ffffff")
        else:
            vlsm_input_networks.config(fg="#ff0000")
        vlsm_input_networks.config(bg="#252525")

        vlsm_input_networks.configure(insertbackground='#FFFFFF')

    #########################################################
    #########################################################
    #########################################################
        
    vlsm_input_networks.bind("<Enter>",vlsm_change_input_networks)
    vlsm_input_networks.bind("<Leave>",vlsm_change_input_networks_re)
    vlsm_input_ipaddress.bind("<Enter>",vlsm_change_input_ipaddress)
    vlsm_input_ipaddress.bind("<Leave>",vlsm_change_input_ipaddress_re)

    vlsm_input_networks.bind('<FocusIn>',auto_close_side_panel)
    vlsm_input_ipaddress.bind("<FocusIn>",auto_close_side_panel)

    #########################################################
    #########################################################
    #########################################################

        # use to set usable host reader

    global vlsms_subnetworks
    vlsms_subnetworks = 0

    def vlsm_set_host_per_subnet_reader():
        global vlsms_subnetworks
        global vlsm_input_subnet_value 
        vlsms_subnetworks_now  =  vlsm_input_networks.get()
        vlsms_subnetworks_now = vlsms_subnetworks_now.replace(" ","")
        if vlsms_subnetworks_now != vlsms_subnetworks:
            vlsms_subnetworks = vlsms_subnetworks_now
            if vlsms_subnetworks_now == "" :
                vlsm_input_subnet_value = False
                set_vlsm_host_input(0)
            else:
                try:
                    int(vlsms_subnetworks_now)
                    if int(vlsms_subnetworks_now) > 15 or int(vlsms_subnetworks_now) < 1 :
                        set_vlsm_host_input(0)
                        vlsm_input_subnet_value = False
                        vlsm_input_networks.config(fg="#ff0000")
                    else:
                        set_vlsm_host_input(int(vlsms_subnetworks_now))
                        vlsm_input_subnet_value = True
                        if vlsm_input_network_entry_enter == True :
                            vlsm_input_networks.config(fg="#000000")
                        else:
                            vlsm_input_networks.config(fg="#ffffff")
                except :
                    set_vlsm_host_input(0)
                    vlsm_input_subnet_value = False
                    vlsm_input_networks.config(fg="#ff0000")
        main_window.after(100,vlsm_set_host_per_subnet_reader)

    
    global vlsm_input_dash1
    vlsm_input_dash1 = Label(vlsm_input_frame ,text=":" ,fg ="#FFFFFF" ,bg="#303030")

    #########################################################
    #########################################################
    #########################################################
    vlsm_host_1_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center')
    vlsm_host_2_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_3_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_4_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_5_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_6_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_7_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_8_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center' )
    vlsm_host_9_input_entry  = Entry(vlsm_input_frame ,width=10  ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_10_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_11_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_12_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_13_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_14_input_entry  = Entry(vlsm_input_frame ,width=10 ,fg="#ffffff" ,bg="#101010" ,justify='center'  )
    vlsm_host_15_input_entry  = Entry(vlsm_input_frame ,width=10,fg="#ffffff" ,bg="#101010" ,justify='center'  )

    vlsm_host_1_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 01)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_2_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 02)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_3_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 03)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_4_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 04)"  ,fg="#ffffff" ,bg="#101010"  )
    vlsm_host_5_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 05)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_6_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 06)"  ,fg="#ffffff" ,bg="#101010"  )
    vlsm_host_7_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 07)"  ,fg="#ffffff" ,bg="#101010"  )
    vlsm_host_8_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 08)"  ,fg="#ffffff" ,bg="#101010"  )
    vlsm_host_9_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 09)"  ,fg="#ffffff"  ,bg="#101010"   )
    vlsm_host_10_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 10)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_11_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 11)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_12_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 12)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_13_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 13)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_14_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 14)"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_15_input_label  = Label(vlsm_input_frame ,text = "Hosts  (Sub-net 15)"  ,fg="#ffffff" ,bg="#101010"   )

    vlsm_host_1_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_2_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_3_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_4_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_5_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_6_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_7_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_8_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_9_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"   )
    vlsm_host_10_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_11_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_12_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_13_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_14_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )
    vlsm_host_15_input_label_dash = Label(vlsm_input_frame ,text = ":"  ,fg="#ffffff" ,bg="#101010"    )

    global vlsm_host_input_entry_list
    vlsm_host_input_entry_list = [vlsm_host_1_input_entry,vlsm_host_2_input_entry,vlsm_host_3_input_entry,
                                    vlsm_host_4_input_entry,vlsm_host_5_input_entry,vlsm_host_6_input_entry,
                                    vlsm_host_7_input_entry,vlsm_host_8_input_entry,vlsm_host_9_input_entry,
                                vlsm_host_10_input_entry,vlsm_host_11_input_entry,vlsm_host_12_input_entry,
                                vlsm_host_13_input_entry,vlsm_host_14_input_entry,vlsm_host_15_input_entry]
    
    for i in vlsm_host_input_entry_list :
        i.bind('<FocusIn>',auto_close_side_panel)
        i.configure(insertbackground='white')

    global vlsm_host_input_label_list
    vlsm_host_input_label_list = [vlsm_host_1_input_label,vlsm_host_2_input_label,vlsm_host_3_input_label,
                                    vlsm_host_4_input_label,vlsm_host_5_input_label,vlsm_host_6_input_label,
                                    vlsm_host_7_input_label,vlsm_host_8_input_label,vlsm_host_9_input_label,
                                    vlsm_host_10_input_label,vlsm_host_11_input_label,vlsm_host_12_input_label,
                                    vlsm_host_13_input_label,vlsm_host_14_input_label,vlsm_host_15_input_label]
    global vlsm_host_input_label_dash_list
    vlsm_host_input_label_dash_list = [vlsm_host_1_input_label_dash,vlsm_host_2_input_label_dash,vlsm_host_3_input_label_dash,
                                    vlsm_host_4_input_label_dash,vlsm_host_5_input_label_dash,vlsm_host_6_input_label_dash,
                                    vlsm_host_7_input_label_dash,vlsm_host_8_input_label_dash,vlsm_host_9_input_label_dash,
                                vlsm_host_10_input_label_dash,vlsm_host_11_input_label_dash,vlsm_host_12_input_label_dash,
                                vlsm_host_13_input_label_dash,vlsm_host_14_input_label_dash,vlsm_host_15_input_label_dash]
    #########################################################
    #########################################################
    #########################################################

    def set_vlsm_host_input(index_limit):            
        for widget in  vlsm_host_input_label_list :
            widget.place_forget()
        for widget in vlsm_host_input_label_dash_list :   
            widget.place_forget()
        for widget in vlsm_host_input_entry_list :
            widget.place_forget()

        if real_resolution ==1080 :
            relx_label = 0.035
            relx_dash = 0.35
            relx_entry = 0.4
        elif real_resolution == 900 :
            relx_label = 0.035
            relx_dash = 0.35
            relx_entry = 0.4
        else:
            relx_label = 0.035
            relx_dash = 0.355
            relx_entry = 0.4
        
        vlsm_host_label_rely = 0.18
        vlsm_host_dash_rely = 0.18
        vlsm_host_entry_rely = 0.18
        for index in range(0,index_limit) :
            vlsm_host_input_label_list[index].place(rely=vlsm_host_label_rely ,relx=relx_label)
            vlsm_host_input_label_dash_list[index].place(rely=vlsm_host_dash_rely ,relx=relx_dash)
            vlsm_host_input_entry_list[index].place(rely=vlsm_host_entry_rely ,relx=relx_entry)
            vlsm_host_label_rely += 0.045
            vlsm_host_dash_rely += 0.045
            vlsm_host_entry_rely += 0.0452

    #check netwotrks input value
    vlsm_set_host_per_subnet_reader()

    ##########################################################
    ##########################################################
    ##########################################################
    ########################################################## 
    ##########################################################
    global vlsm_input_host_value
    vlsm_input_host_value = False

    #available host
    vlsm_available_host_frame = Frame(vlsm_input_frame ,bg="#101010")
    vlsm_available_host_frame.place(relx=0.6,rely=0.17 ,relwidth=0.35 ,relheight=0.04)

    global vlsm_available_host_label 
    vlsm_available_host_label = Label(vlsm_available_host_frame,bg="#101010" ,font=Font(size=11,weight=BOLD),
                                        text="Available IPs : " ,fg="#00ff00")

    def round_number_twos_power(num):
        #plus 2 because always 2 ips cant use for hosts 
        num +=2
        n = 0
        while True :
            if 2**n >= num :
                break
            n += 1 
        round_num = 2**n
        return round_num

    ########################################################## 
    ##########################################################

    global vlsm_host_needs_now
    global vlsm_host_needs_before
    global ip_address_before_0101
    vlsm_host_needs_before = ["","","","","","","","","",""]
    vlsm_host_needs_now = []
    ip_address_before_0101 = ""


    #########################################################
    #########################################################
    global vlsm_calculation_done
    vlsm_calculation_done = False

    def set_available_host_label():
        global vlsm_host_needs_now
        global vlsm_host_needs_before
        global vlsm_input_host_value
        global vlsm_ip_class_before
        global ip_address_before_0101
        global vlsm_calculation_done

        try:
            limit = int(vlsms_subnetworks)
            if limit > 15 :
                limit = 0
        except:
            limit = 0
        for i in range(0,limit):
            vlsm_host_needs_now.append((vlsm_host_input_entry_list[i].get()))
        if vlsm_host_needs_now != vlsm_host_needs_before or vlsm_ip_class != vlsm_ip_class_before or vlsm_input_ipaddress.get() != ip_address_before_0101   :
            vlsm_calculation_done = False
            ip_address_before_0101 = vlsm_input_ipaddress.get()
            vlsm_host_needs_before = vlsm_host_needs_now
            vlsm_ip_class_before = vlsm_ip_class

            #reset table
            for table_data in table_td_rows_lables :
                table_data.config(text="")
            
            #add range spliter to table
            # reset
            for i in range(15):
                vlsm_table_range1_spliter[i].config(text="",bg="#100e17" ,fg="#ffffff" )
                vlsm_table_range2_spliter[i].config(text="",bg="#100e17" ,fg="#ffffff" )
            
            for i in range(limit):
                vlsm_table_range1_spliter[i].config(text="",bg="#151515" ,fg="#ffffff" )
                vlsm_table_range2_spliter[i].config(text="",bg="#151515" ,fg="#ffffff" )

            # table data reset 
            for i in range(limit):
                for x in range(8):
                    table_td_rows_lable_lists[i][x].config(bg="#151515" ,fg="#ffffff")
            for i in range(limit,15):
                for x in range(8):
                    table_td_rows_lable_lists[i][x].config(bg="#100e17" ,fg="#ffffff")

            
            if vlsm_ip_class == "class a" :
                max_ip_address =  16777216
            elif vlsm_ip_class == "class b" :
                max_ip_address =  65536
            elif vlsm_ip_class == "class c":
                max_ip_address =  256
            else:
                max_ip_address = 0
            
            if max_ip_address == 0 :
                vlsm_available_host_label.pack_forget()
            else:
                vlsm_available_host_label.pack()
            total_host = 0
            input_count = 0
            for index in range(limit) :
                try:
                    host_temp = int(vlsm_host_input_entry_list[index].get())
                    total_host += round_number_twos_power(host_temp)
                    input_count += 1
                    vlsm_host_input_entry_list[index].config(highlightthickness = 0 ,highlightbackground= "#151515")
                except:
                    vlsm_input_host_value = False
                    vlsm_host_input_entry_list[index].config(highlightthickness=0.5,highlightbackground = "red" ,highlightcolor="red")
            free_host = max_ip_address-total_host
            if free_host >= 0   :
                vlsm_available_host_label.config(fg="#00ff00")
                out_text= "Available IPs  :  {}".format(free_host)
                if input_count == limit:
                    vlsm_input_host_value = True
            else:
                vlsm_available_host_label.config(fg="#ff0000")
                out_text= "Available IPs  :  {}".format(0)
                vlsm_input_host_value = False

            vlsm_available_host_label.config(text=out_text)
        vlsm_host_needs_now = []
        main_window.after(10,set_available_host_label)

    # set_available_host_label call agter make table data
    
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    vlsm_table_frame = Frame(vlsm_main_window ,bg="#100e17")
    vlsm_table_frame.place(relx=0.39 ,rely=0.18,relwidth=0.77 ,relheight=0.8)

    global table_change_subnets_before
    table_change_subnets_before = ""
    global vlsm_table_rely_auto
    vlsm_table_rely_auto = 0.18

    def change_vlsm_table_rely():
        global vlsm_table_rely_auto
        global table_change_subnets_before
        table_change_subnets_now = vlsm_input_networks.get()
        if table_change_subnets_now != table_change_subnets_before :
            table_change_subnets_before = table_change_subnets_now
            try:
                int(table_change_subnets_now)
                if int(table_change_subnets_now) > -1 and int(table_change_subnets_now) < 16 :
                    vlsm_table_rely_auto = 0.43
                    for i in range(0,int(table_change_subnets_now)) :
                        vlsm_table_frame.place(relx=0.39 ,rely=vlsm_table_rely_auto)
                        vlsm_table_rely_auto -= 0.02
                else:
                    vlsm_table_frame.place(relx=0.39 ,rely=0.18)
            except:
                vlsm_table_frame.place(relx=0.39 ,rely=0.18)
        main_window.after(100,change_vlsm_table_rely)
    change_vlsm_table_rely()

    #table head
    global vlsm_table_head_label
    vlsm_table_head_label = Label(vlsm_table_frame ,bg="#100e17")
    # table head
    vlsm_table_title_01 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="Sub-net" ,bg="#000000" ,fg="#ffffff")
    vlsm_table_title_02 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="IP Addresses" ,bg="#000000" ,fg="#ffffff")
    vlsm_table_title_03 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="Hosts" ,bg="#000000" ,fg="#ffffff")
    vlsm_table_title_04 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="Subnet Mask" ,bg="#000000" ,fg="#ffffff")
    vlsm_table_title_05 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="IP Ranges" ,bg="#000000" ,fg="#ffffff")
    vlsm_table_title_06 = Label(vlsm_table_frame,font=Font(size=font_most,weight=BOLD) ,text="Usable IP Ranges" ,bg="#000000" ,fg="#ffffff")

    global vlsm_table_head_list
    vlsm_table_head_list = [vlsm_table_title_01,vlsm_table_title_02,vlsm_table_title_03,vlsm_table_title_04,vlsm_table_title_05,vlsm_table_title_06]
   

    # rows in table
    vlsm_table_row_1  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_2  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_3  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_4  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_5  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_6  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_7  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_8  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_9  =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_10 =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_11 =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_12 =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_13 =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_14 =  Label(vlsm_table_frame ,bg="#100e17")
    vlsm_table_row_15 =  Label(vlsm_table_frame ,bg="#100e17")

    global vlsm_table_rows_list
    vlsm_table_rows_list = [vlsm_table_row_1,vlsm_table_row_2,vlsm_table_row_3,
                            vlsm_table_row_4,vlsm_table_row_5,vlsm_table_row_6,
                            vlsm_table_row_7,vlsm_table_row_8,vlsm_table_row_9,
                            vlsm_table_row_10,vlsm_table_row_11,vlsm_table_row_12,
                            vlsm_table_row_13,vlsm_table_row_14,vlsm_table_row_15]

    global vlsm_table_last_row
    vlsm_table_last_row = vlsm_table_rows_list[14]

    #########################################################
    #########################################################
    
    global vlsm_table_rows_before
    vlsm_table_rows_before = 0
    
    global set_table_rows
    def set_table_rows():
        global vlsm_table_last_row
        global vlsm_table_rows_before
        table_row_rely =  0.0738
        
        try:
            vlsm_table_rows_now = int(vlsm_input_networks.get())
            if vlsm_table_rows_now > 15 or vlsm_table_rows_now < 0 :
                vlsm_table_rows_now = 0
                vlsm_table_head_label.place_forget()
                for table_th_label in  vlsm_table_head_list:
                    table_th_label.config(fg="#100e17",bg="#100e17")
        except:
            vlsm_table_rows_now = 0
            for table_th_label in  vlsm_table_head_list:
                table_th_label.config(fg="#100e17",bg="#100e17")
            vlsm_table_head_label.place_forget()
           
        if vlsm_table_rows_before != vlsm_table_rows_now :
            vlsm_table_rows_before = vlsm_table_rows_now
            #table haead
            for table_th_label in  vlsm_table_head_list:
                table_th_label.config(fg="#ffffff",bg="#000000")
            for widget in vlsm_table_rows_list:
                widget.place_forget()
            
            if vlsm_table_rows_now != 0 :
                vlsm_table_head_label.place(rely=0,relx=0)
            for index in range(0,vlsm_table_rows_now):
                #place end
                if index ==  vlsm_table_rows_now-1 :
                    vlsm_table_rows_list[index].config(image=vlsm_table_head_end_image)
                    vlsm_table_last_row = vlsm_table_rows_list[index]
                else:
                    #place row
                    vlsm_table_rows_list[index].config(image=vlsm_table_row_1_image)
                vlsm_table_rows_list[index].place(relx=0,rely=table_row_rely)
                table_row_rely += 0.055
        main_window.after(20,set_table_rows)

    set_table_rows()

    #########################################################
    #########################################################
    #########################################################
    #########################################################
    
    #row 1 
    vlsm_tr1_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr1_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr1_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr1_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr1_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr1_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr1_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr1_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr1_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr1_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row 2 
    vlsm_tr2_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr2_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr2_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr2_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr2_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr2_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr2_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr2_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr2_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr2_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row3
    vlsm_tr3_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr3_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr3_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr3_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr3_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr3_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr3_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr3_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr3_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr3_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row4
    vlsm_tr4_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr4_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr4_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr4_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr4_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr4_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr4_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr4_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr4_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr4_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row5
    vlsm_tr5_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr5_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr5_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr5_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr5_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr5_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr5_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr5_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr5_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr5_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row6
    vlsm_tr6_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr6_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr6_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr6_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr6_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr6_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr6_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr6_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr6_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr6_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)

    #row7
    vlsm_tr7_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr7_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr7_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr7_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr7_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr7_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr7_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr7_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr7_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr7_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row8
    vlsm_tr8_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr8_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr8_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr8_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr8_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr8_td5_2 = Label(vlsm_table_frame  ,width=13 ,anchor=W)
    vlsm_tr8_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr8_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr8_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr8_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)

    #row9
    vlsm_tr9_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr9_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr9_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr9_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr9_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr9_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr9_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr9_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr9_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr9_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)

    #row10
    vlsm_tr10_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr10_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr10_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr10_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr10_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr10_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr10_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr10_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr10_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr10_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row11
    vlsm_tr11_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr11_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr11_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr11_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr11_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr11_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr11_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr11_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr11_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr11_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row12
    vlsm_tr12_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr12_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr12_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr12_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr12_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr12_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr12_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr12_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr12_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr12_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row13
    vlsm_tr13_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr13_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr13_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr13_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr13_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr13_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr13_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr13_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr13_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr13_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row14
    vlsm_tr14_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr14_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr14_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr14_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr14_td5 = Label(vlsm_table_frame  ,width=13 ,anchor=E)
    vlsm_tr14_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr14_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr14_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr14_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr14_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    #row15
    vlsm_tr15_td1 = Label(vlsm_table_frame ,width=5 ,anchor=E)
    vlsm_tr15_td2 = Label(vlsm_table_frame ,width=12 ,anchor=E)
    vlsm_tr15_td3 = Label(vlsm_table_frame ,width=8 ,anchor=E)
    vlsm_tr15_td4 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr15_td5 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr15_td5_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr15_td6 = Label(vlsm_table_frame ,width=13 ,anchor=E)
    vlsm_tr15_td6_2 = Label(vlsm_table_frame ,width=13 ,anchor=W)
    vlsm_tr15_dash1 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)
    vlsm_tr15_dash2 = Label(vlsm_table_frame ,width=1 ,anchor=CENTER)


    global table_td_rows_lable_lists
    global table_td_rows_lables
    table_td_rows_lable_lists = [
                                [ vlsm_tr1_td1  ,vlsm_tr1_td2  ,vlsm_tr1_td3  ,vlsm_tr1_td4  ,vlsm_tr1_td5  ,vlsm_tr1_td5_2  ,vlsm_tr1_td6  ,vlsm_tr1_td6_2],
                                [ vlsm_tr2_td1  ,vlsm_tr2_td2  ,vlsm_tr2_td3  ,vlsm_tr2_td4  ,vlsm_tr2_td5  ,vlsm_tr2_td5_2  ,vlsm_tr2_td6  ,vlsm_tr2_td6_2],
                                [ vlsm_tr3_td1  ,vlsm_tr3_td2  ,vlsm_tr3_td3  ,vlsm_tr3_td4  ,vlsm_tr3_td5  ,vlsm_tr3_td5_2  ,vlsm_tr3_td6  ,vlsm_tr3_td6_2],
                                [ vlsm_tr4_td1  ,vlsm_tr4_td2  ,vlsm_tr4_td3  ,vlsm_tr4_td4  ,vlsm_tr4_td5  ,vlsm_tr4_td5_2  ,vlsm_tr4_td6  ,vlsm_tr4_td6_2],
                                [ vlsm_tr5_td1  ,vlsm_tr5_td2  ,vlsm_tr5_td3  ,vlsm_tr5_td4  ,vlsm_tr5_td5  ,vlsm_tr5_td5_2  ,vlsm_tr5_td6  ,vlsm_tr5_td6_2],
                                [ vlsm_tr6_td1  ,vlsm_tr6_td2  ,vlsm_tr6_td3  ,vlsm_tr6_td4  ,vlsm_tr6_td5  ,vlsm_tr6_td5_2  ,vlsm_tr6_td6  ,vlsm_tr6_td6_2],
                                [ vlsm_tr7_td1  ,vlsm_tr7_td2  ,vlsm_tr7_td3  ,vlsm_tr7_td4  ,vlsm_tr7_td5  ,vlsm_tr7_td5_2  ,vlsm_tr7_td6  ,vlsm_tr7_td6_2],
                                [ vlsm_tr8_td1  ,vlsm_tr8_td2  ,vlsm_tr8_td3  ,vlsm_tr8_td4  ,vlsm_tr8_td5  ,vlsm_tr8_td5_2  ,vlsm_tr8_td6  ,vlsm_tr8_td6_2],
                                [ vlsm_tr9_td1  ,vlsm_tr9_td2  ,vlsm_tr9_td3  ,vlsm_tr9_td4  ,vlsm_tr9_td5  ,vlsm_tr9_td5_2  ,vlsm_tr9_td6  ,vlsm_tr9_td6_2],
                                [ vlsm_tr10_td1 ,vlsm_tr10_td2 ,vlsm_tr10_td3 ,vlsm_tr10_td4 ,vlsm_tr10_td5 ,vlsm_tr10_td5_2 ,vlsm_tr10_td6 ,vlsm_tr10_td6_2],
                                [ vlsm_tr11_td1 ,vlsm_tr11_td2 ,vlsm_tr11_td3 ,vlsm_tr11_td4 ,vlsm_tr11_td5 ,vlsm_tr11_td5_2 ,vlsm_tr11_td6 ,vlsm_tr11_td6_2],
                                [ vlsm_tr12_td1 ,vlsm_tr12_td2 ,vlsm_tr12_td3 ,vlsm_tr12_td4 ,vlsm_tr12_td5 ,vlsm_tr12_td5_2 ,vlsm_tr12_td6 ,vlsm_tr12_td6_2],
                                [ vlsm_tr13_td1 ,vlsm_tr13_td2 ,vlsm_tr13_td3 ,vlsm_tr13_td4 ,vlsm_tr13_td5 ,vlsm_tr13_td5_2 ,vlsm_tr13_td6 ,vlsm_tr13_td6_2],
                                [ vlsm_tr14_td1 ,vlsm_tr14_td2 ,vlsm_tr14_td3 ,vlsm_tr14_td4 ,vlsm_tr14_td5 ,vlsm_tr14_td5_2 ,vlsm_tr14_td6 ,vlsm_tr14_td6_2],
                                [ vlsm_tr15_td1 ,vlsm_tr15_td2 ,vlsm_tr15_td3 ,vlsm_tr15_td4 ,vlsm_tr15_td5 ,vlsm_tr15_td5_2 ,vlsm_tr15_td6 ,vlsm_tr15_td6_2]
                                ]
    table_td_rows_lables = [ vlsm_tr1_td1 ,vlsm_tr1_td2  ,vlsm_tr1_td3  ,vlsm_tr1_td4  ,vlsm_tr1_td5  ,vlsm_tr1_td6  ,vlsm_tr1_td5_2, vlsm_tr1_td6_2,
                            vlsm_tr2_td1  ,vlsm_tr2_td2  ,vlsm_tr2_td3  ,vlsm_tr2_td4  ,vlsm_tr2_td5  ,vlsm_tr2_td6  ,vlsm_tr2_td5_2, vlsm_tr2_td6_2,
                            vlsm_tr3_td1  ,vlsm_tr3_td2  ,vlsm_tr3_td3  ,vlsm_tr3_td4  ,vlsm_tr3_td5  ,vlsm_tr3_td6  ,vlsm_tr3_td5_2, vlsm_tr3_td6_2,
                            vlsm_tr4_td1  ,vlsm_tr4_td2  ,vlsm_tr4_td3  ,vlsm_tr4_td4  ,vlsm_tr4_td5  ,vlsm_tr4_td6  ,vlsm_tr4_td5_2, vlsm_tr4_td6_2,
                            vlsm_tr5_td1  ,vlsm_tr5_td2  ,vlsm_tr5_td3  ,vlsm_tr5_td4  ,vlsm_tr5_td5  ,vlsm_tr5_td6  ,vlsm_tr5_td5_2, vlsm_tr5_td6_2,
                            vlsm_tr6_td1  ,vlsm_tr6_td2  ,vlsm_tr6_td3  ,vlsm_tr6_td4  ,vlsm_tr6_td5  ,vlsm_tr6_td6  ,vlsm_tr6_td5_2, vlsm_tr6_td6_2,
                            vlsm_tr7_td1  ,vlsm_tr7_td2  ,vlsm_tr7_td3  ,vlsm_tr7_td4  ,vlsm_tr7_td5  ,vlsm_tr7_td6  ,vlsm_tr7_td5_2, vlsm_tr7_td6_2,
                            vlsm_tr8_td1  ,vlsm_tr8_td2  ,vlsm_tr8_td3  ,vlsm_tr8_td4  ,vlsm_tr8_td5  ,vlsm_tr8_td6  ,vlsm_tr8_td5_2, vlsm_tr8_td6_2,
                            vlsm_tr9_td1  ,vlsm_tr9_td2  ,vlsm_tr9_td3  ,vlsm_tr9_td4  ,vlsm_tr9_td5  ,vlsm_tr9_td6  ,vlsm_tr9_td5_2, vlsm_tr9_td6_2,
                            vlsm_tr10_td1 ,vlsm_tr10_td2 ,vlsm_tr10_td3 ,vlsm_tr10_td4 ,vlsm_tr10_td5 ,vlsm_tr10_td6 ,vlsm_tr10_td5_2, vlsm_tr10_td6_2,
                            vlsm_tr11_td1 ,vlsm_tr11_td2 ,vlsm_tr11_td3 ,vlsm_tr11_td4 ,vlsm_tr11_td5 ,vlsm_tr11_td6 ,vlsm_tr11_td5_2, vlsm_tr11_td6_2,
                            vlsm_tr12_td1 ,vlsm_tr12_td2 ,vlsm_tr12_td3 ,vlsm_tr12_td4 ,vlsm_tr12_td5 ,vlsm_tr12_td6 ,vlsm_tr12_td5_2, vlsm_tr12_td6_2,
                            vlsm_tr13_td1 ,vlsm_tr13_td2 ,vlsm_tr13_td3 ,vlsm_tr13_td4 ,vlsm_tr13_td5 ,vlsm_tr13_td6 ,vlsm_tr13_td5_2, vlsm_tr13_td6_2,
                            vlsm_tr14_td1 ,vlsm_tr14_td2 ,vlsm_tr14_td3 ,vlsm_tr14_td4 ,vlsm_tr14_td5 ,vlsm_tr14_td6 ,vlsm_tr14_td5_2, vlsm_tr14_td6_2,
                            vlsm_tr15_td1 ,vlsm_tr15_td2 ,vlsm_tr15_td3 ,vlsm_tr15_td4 ,vlsm_tr15_td5 ,vlsm_tr15_td6 ,vlsm_tr15_td5_2, vlsm_tr15_td6_2,]

    global vlsm_table_range1_spliter
    global vlsm_table_range2_spliter
    global vlsm_table_all_dashes
    vlsm_table_range1_spliter  =  [vlsm_tr1_dash1,vlsm_tr2_dash1,vlsm_tr3_dash1,vlsm_tr4_dash1,vlsm_tr5_dash1,
                                 vlsm_tr6_dash1,vlsm_tr7_dash1,vlsm_tr8_dash1,vlsm_tr9_dash1,vlsm_tr10_dash1,
                                 vlsm_tr11_dash1,vlsm_tr12_dash1, vlsm_tr13_dash1,vlsm_tr14_dash1,vlsm_tr15_dash1]
    vlsm_table_range2_spliter  =  [vlsm_tr1_dash2,vlsm_tr2_dash2,vlsm_tr3_dash2,vlsm_tr4_dash2,vlsm_tr5_dash2,
                                 vlsm_tr6_dash2,vlsm_tr7_dash2,vlsm_tr8_dash2,vlsm_tr9_dash2,vlsm_tr10_dash2,
                                 vlsm_tr11_dash2,vlsm_tr12_dash2, vlsm_tr13_dash2,vlsm_tr14_dash2,vlsm_tr15_dash2]

    vlsm_table_all_dashes = [vlsm_table_range1_spliter,vlsm_table_range2_spliter]

    for table_data in table_td_rows_lables :
        table_data.config(fg="#ffffff" ,bg="#151515")

    for table_dash in vlsm_table_range1_spliter + vlsm_table_range2_spliter:
        table_dash.config(text="-")
       
    set_available_host_label()


    #table hide frame 
    global table_hiding_frame
    table_hiding_frame = Frame(vlsm_main_window ,bg="#100e17")

    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    global before_button_frame_place_rely
    before_button_frame_place_rely = 0
    def replace_buttons():
        global before_button_frame_place_rely
        button_frame_rely=0.25
        if vlsm_input_networks.get() != before_button_frame_place_rely :
            before_button_frame_place_rely = vlsm_input_networks.get()
            try:
                index_max_button_place = int(vlsm_input_networks.get())
                if index_max_button_place < 1 or index_max_button_place > 15 :
                    index_max_button_place=1
            except:
                index_max_button_place = 1
        
            for index in range(0,index_max_button_place) :
                vlsm_button_frame.place(rely=button_frame_rely ,relx=0.65)
                button_frame_rely+=0.03
        main_window.after(100,replace_buttons)

    global vlsm_input_calculate_button_enter
    vlsm_input_calculate_button_enter = False

    global vlsm_button_frame
    global vlsm_calculate_button
    #BUTTONS PLACE
    vlsm_button_frame = Frame(vlsm_input_frame,bg="#101010")
    vlsm_button_frame.place(relx=0.73,rely=0.25 ,relheight=0.12 ,relwidth=0.23)
    vlsm_calculate_button = Button(vlsm_button_frame ,bg="#101010" ,border=False ,activebackground="#101010",
                                    cursor="hand2")
    vlsm_calculate_button.place(relx=0,rely=0)

    replace_buttons()

    def change_vlsm_calculate_button(e):
        global vlsm_input_calculate_button_enter
        vlsm_input_calculate_button_enter = True
        if vlsm_input_subnet_value == True and vlsm_input_ipaddress_value==True and vlsm_input_host_value==True:
            vlsm_calculate_button.config(image=calculate_button_image_re)
    def change_vlsm_calculate_button_re(e):
        global vlsm_input_calculate_button_enter
        vlsm_input_calculate_button_enter = False
        if vlsm_input_subnet_value == True and vlsm_input_ipaddress_value ==True and vlsm_input_host_value==True:
            vlsm_calculate_button.config(image=calculate_button_image)
    vlsm_calculate_button.bind('<Enter>',change_vlsm_calculate_button)
    vlsm_calculate_button.bind('<Leave>',change_vlsm_calculate_button_re)

    #########################################################
    #########################################################
    
    global set_vlsm_calculate_buttons_style
    def set_vlsm_calculate_buttons_style():
        if vlsm_input_subnet_value == False or vlsm_input_ipaddress_value==False or vlsm_input_host_value==False :
            vlsm_calculate_button.config(image=calculate_button_error_image)
            vlsm_calculate_button.config(command="nothing")
        else:
            vlsm_calculate_button.config(command=start_vlsm_calculate)
            if  vlsm_input_calculate_button_enter == False:
                vlsm_calculate_button.config(image=calculate_button_image)
            else:
                vlsm_calculate_button.config(image=calculate_button_image_re)

        main_window.after(100,set_vlsm_calculate_buttons_style)


    #########################################################
    #########################################################
    def reset_vlsm_inputs():
        for widget in vlsm_host_input_entry_list:
            widget.delete(0,"end")
        vlsm_input_ipaddress.delete(0,"end")
        vlsm_input_networks.delete(0,"end")
   

    global vlsm_reset_button
    vlsm_reset_button = Button(vlsm_button_frame ,bg="#101010" ,border=False ,activebackground="#101010",
                                    cursor="hand2" ,command=reset_vlsm_inputs)
    vlsm_reset_button.place(relx=0,rely=0.5)

    def change_vlsm_reset_button(e):
        vlsm_reset_button.config(image=reset_button_image_re)
    def change_vlsm_reset_button_re(e):
        vlsm_reset_button.config(image=reset_button_image)
    vlsm_reset_button.bind('<Enter>',change_vlsm_reset_button)
    vlsm_reset_button.bind('<Leave>',change_vlsm_reset_button_re)

    vlsm_main_window.place(relheight=1 ,relwidth=1)

    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    global full_table_enable
    full_table_enable = False
    def change_table_rel_x():

        #disable vlsm all inputs 
        for input_widget in vlsm_host_input_entry_list:
            input_widget.config(state="disabled")
        vlsm_input_ipaddress.config(state="disabled")
        vlsm_input_networks.config(state="disabled")

        if side_panel_open == True:
            close_side_panel()
        global full_table_enable
        full_table_enable = True

        #table head and last row change
        vlsm_table_head_label.config(image=vlsm_table_head_full_image)
        vlsm_table_last_row.config(image=vlsm_table_head_end_full_image)
        #input frame displaced
        vlsm_input_frame.place_forget()

        #change special button 
        table_change_special_button.config(image=table_frame_change_special_button_back_image)
        #table change special button place back
        table_change_special_button.place(relx=0.072,rely=0.45)

        global vlsm_table_frame_start_placeing_relx
        vlsm_table_frame_start_placeing_relx = 0.39

        def placing_table():
            global vlsm_table_frame_start_placeing_relx
            vlsm_table_frame.place(relx=vlsm_table_frame_start_placeing_relx,rely=vlsm_table_rely_auto+0.02)
            vlsm_table_frame_start_placeing_relx -= 0.05
            if vlsm_table_frame_start_placeing_relx > 0.1 :
                main_window.after(5,placing_table)
            else:
                #change button command to full table hide mod 
                table_change_special_button.config(command=change_table_rel_x_re)
        placing_table()

    def change_table_rel_x_re():

        #enable vlsm all inputs 
        for input_widget in vlsm_host_input_entry_list:
            input_widget.config(state="normal")
        vlsm_input_ipaddress.config(state="normal")
        vlsm_input_networks.config(state="normal")
        
        if side_panel_open == True:
            close_side_panel()
        global full_table_enable
        full_table_enable = False

        global vlsm_table_frame_start_placeing_relx_re
        vlsm_table_frame_start_placeing_relx_re = 0.089

        def placing_table_re():
            global vlsm_table_frame_start_placeing_relx_re
            vlsm_table_frame.place(relx=vlsm_table_frame_start_placeing_relx_re,rely=vlsm_table_rely_auto+0.02)
            vlsm_table_frame_start_placeing_relx_re += 0.05
            if vlsm_table_frame_start_placeing_relx_re <= 0.39 :
                main_window.after(5,placing_table_re)
            else:
                #change back to normal table head and last row
                vlsm_table_head_label.config(image=vlsm_table_head_image)
                vlsm_table_last_row.config(image=vlsm_table_head_end_image)
                #change button command to full table mod 
                table_change_special_button.config(command=change_table_rel_x)
                #input frame placed
                vlsm_input_frame.place(rely=vlsm_input_frame_rel_y,relx=0.05,relwidth=0.31,relheight=vlsm_input_frame_rel_height)
                #table change special button place back
                table_change_special_button.place(relx=0.37 ,rely=0.45)
                #change special button back
                #change special button 
                table_change_special_button.config(image=table_frame_change_special_button_image)
        placing_table_re()

    #table change button
    global table_change_special_button
    table_change_special_button = Button(vlsm_main_window ,activebackground="#100e17" ,bg="#100e17" ,border=0,
                                            cursor="hand2" ,command=change_table_rel_x)
    table_change_special_button.place(relx=0.37 ,rely=0.45)

    #########################################################
    #########################################################
    #########################################################
    global vlsm_calculation_status_before
    vlsm_calculation_status_before = ""
    global change_vlsm_special_button_auto
    def change_vlsm_special_button_auto():
        global vlsm_calculation_status_before

        if  vlsm_calculation_done != vlsm_calculation_status_before:
            vlsm_calculation_status_before = vlsm_calculation_done
            if vlsm_calculation_done == False:
                table_change_special_button.config(image = table_frame_change_special_button_error_image)
                table_change_special_button.config(command="")
            else:
                table_change_special_button.config(command=change_table_rel_x)
                if vlsm_special_button_live == True:
                    table_change_special_button.config(image=table_frame_change_special_button_re_image)
                else:
                    table_change_special_button.config(image=table_frame_change_special_button_image)
        main_window.after(100,change_vlsm_special_button_auto)

    global vlsm_special_button_live
    vlsm_special_button_live = False
    def change_table_change_special_button(e):
        global vlsm_special_button_live
        vlsm_special_button_live = True
        if vlsm_calculation_done == True :
            if full_table_enable == False :
                table_change_special_button.config(image=table_frame_change_special_button_re_image)
            else:
                table_change_special_button.config(image=table_frame_change_special_button_back_re_image)
        
    def change_table_change_special_button_re(e):
        global vlsm_special_button_live
        vlsm_special_button_live =  False
        if vlsm_calculation_done == True :
            if full_table_enable == False :
                table_change_special_button.config(image=table_frame_change_special_button_image)
            else:
                table_change_special_button.config(image=table_frame_change_special_button_back_image)

    table_change_special_button.bind('<Enter>',change_table_change_special_button)
    table_change_special_button.bind('<Leave>',change_table_change_special_button_re)

    #########################################################
    #########################################################
    #########################################################
    #########################################################
    #########################################################
    change_fslm_vlsm()
    vlsm_main_window.place_forget()

    global first_time_change_vlsm_flsm_mode
    first_time_change_vlsm_flsm_mode = True
    if running_mode == "VLSM":
        VLSM_mode()
   

    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    def vlsm_read_vlsm_output_val(limit):
        #read hosts
        hosts_output_tem  = []
        file_host = open("VLSM\\ip_hosts.rapa","r")
        for i in range(limit):
            tem_h = file_host.readline()
            tem_h = tem_h.replace("\n","")
            hosts_output_tem.append(tem_h)

        #read ips
        ips_output_tem = []
        file_ip = open("VLSM\\ip_addresses.rapa","r")
        for i in range(limit):
            tem_ip = file_ip.readline()
            tem_ip = tem_ip.replace("\n","")
            ips_output_tem.append(tem_ip+superscripted(tem_ip," (",")"))

        #read subnet masks 
        submasks_output_tem = []
        file_submask = open("VLSM\\subnet_mask.rapa","r")
        for i in range(limit):
            tem_submask = file_submask.readline()
            tem_submask = tem_submask.replace("\n","")
            submasks_output_tem.append(tem_submask) 

        #read ip range
        ipranges_output_tem = []
        ipranges_output_tem2 = []
        file_start_ip = open("VLSM\\ip_start_range.rapa","r")
        file_end_ip   = open("VLSM\\ip_end_range.rapa","r")
        for i in range(limit) :
            st_ip = file_start_ip.readline()
            st_ip = st_ip.replace("\n","")
            en_ip = file_end_ip.readline()
            en_ip = en_ip.replace("\n","")
            ipranges_output_tem.append(st_ip)
            ipranges_output_tem2.append(en_ip)
        
        #read usable ip range
        ipranges_us_output_tem = []
        ipranges_us_output_tem2 = []
        file_start_ip_us = open("VLSM\\ip_start_usable_range.rapa","r")
        file_end_ip_us  = open("VLSM\\ip_end_usable_range.rapa","r")
        for i in range(limit) :
            st_ip_us = file_start_ip_us.readline()
            st_ip_us = st_ip_us.replace("\n","")
            en_ip_us = file_end_ip_us.readline()
            en_ip_us = en_ip_us.replace("\n","")
            ipranges_us_output_tem.append(st_ip_us)
            ipranges_us_output_tem2.append(en_ip_us)

        #sub name 
        subname_output_tem = []
        name = "Sub"
        for i in range(1,limit+1):
            sub_num =  "0"*(2-len(str(i))) + str(i)
            name_tem = name+sub_num
            subname_output_tem.append(name_tem)



        total_output = [subname_output_tem,ips_output_tem,hosts_output_tem,submasks_output_tem,
                        ipranges_output_tem,ipranges_output_tem2,ipranges_us_output_tem,ipranges_us_output_tem2]

        ##########################################################
        ##########################################################
        ##########################################################
        #display output
        for i in range(limit):
            for widget_num in range(8) :
                table_td_rows_lable_lists[i][widget_num].config(text=total_output[widget_num][i])

        #add - to ranges
        for i in range(limit) :
            vlsm_table_range1_spliter[i].config(text="-",bg="#151515",fg="#ffffff")
            vlsm_table_range2_spliter[i].config(text="-",bg="#151515",fg="#ffffff")

        global vlsm_calculation_done
        vlsm_calculation_done = True

        
        
    def start_vlsm_calculate():
        try:
            os.mkdir("VLSM")
        except:
            pass
        #get old files and delete
        del_files_vlsm = os.listdir("VLSM")
        for i in del_files_vlsm:
            os.remove("VLSM\\"+i)

        #write inputs
        vlsm_ip_address = vlsm_input_ipaddress.get()
        vlsm_subnets = vlsm_input_networks.get()
        vlsm_hosts = []
        for index in range(0,int(vlsm_subnets)) :
            vlsm_hosts.append(int(vlsm_host_input_entry_list[index].get()))
        f = open("VLSM\\vlsm_input_subnets.rapa","w")
        f.write(vlsm_subnets)
        f.close()

        f = open( "VLSM\\vlsm_input_ipaddress.rapa","w" )
        f.write(vlsm_ip_address)
        f.close()

        f = open("VLSM\\vlsm_input_hosts.rapa","w" )
        for i in vlsm_hosts :
            f.write(str(i)+"\n")
        f.close()

        #restore process status
        try:
            os.remove("VLSM\\process_status.rapa")
        except:
            pass
        try :
            os.startfile("vlsm cal.exe")
        except:
            os.startfile("vlsm cal.py")
        #check process - completed
        while True:
            try:
                f = open("VLSM\\process_status.rapa","r")
                f.close()
                break
            except:
                pass

        vlsm_read_vlsm_output_val(int(vlsm_subnets))

    side_panel()
    setting_button_set()
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
    ##########################################################
try:
    file = open("Sources\\Settings\Theme\\transparency.rapa","r")
    transparent = file.readline()
    file.close()
except Exception :
    transparent = "1"

if transparent == "1" :
    theme_transparent_value = 1
   
else:
    theme_transparent_value = float(transparent)
   

#############################################################
#############################################################
try :
    f2  = open('Sources\\Settings\\Resolution_width\\resolution_width.rapa',"r")
    winreso_width = int(f2.readline())
    f2.close()
    f3  = open('Sources\\Settings\\Resolution_height\\resolution_height.rapa',"r")
    winreso_height = int(f3.readline())
    f3.close()
except Exception:
    winreso_width = 1280
    winreso_height = 720

if winreso_width == 1920 and winreso_height == 1080 :
    fonts_1080p()
    winresolution_width = 1920
    winresolution_height = 1080
    real_resolution = 1080
elif winreso_width == 1600 and winreso_height == 900 :
    fonts_900p()
    winresolution_width = 1600
    winresolution_height = 900
    real_resolution = 900
else:
    fonts_720p()
    winresolution_width = 1280
    winresolution_height = 720
    real_resolution =  720

#############################################################
#############################################################
#############################################################
try:
    f=open("Sources\\Settings\\resolution_set\\location.rapa","r")
    x,y = f.readline().split(",")
    try:
        x = int(x)
        y = int(y)
        window_relx_geomatry_read , window_rely_geomatry_read = x,y
    except Exception:
        window_relx_geomatry_read , window_rely_geomatry_read = -8,0
except Exception:
    window_relx_geomatry_read , window_rely_geomatry_read = -8,0

#############################################################
#############################################################
#############################################################
try:
    file = open("Sources\\Settings\\Running_mode\\mode.rapa","r")
    running_mode = file.readline()
except:
    running_mode = "FLSM"

if running_mode == "FLSM":
    pass
elif running_mode == "VLSM" :
    pass
else:
    running_mode == "FLSM"

#############################################################
#############################################################
#############################################################  
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################  
#############################################################
#############################################################
#############################################################

main_window = Tk()
main_window.title("IPv4 Calculator")
main_window.iconbitmap('Sources\\Icon\\ip-address.ico')
main_window.attributes('-alpha',theme_transparent_value)
main_window.config(bg="#100e17")


# loading images , use to make ui
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#############################################################
#input frame
try:
    title_image_720p = PhotoImage(file=r"ui sources\\720p\\title.ui")
    input_frame_image_720p = PhotoImage(file=r"ui sources\\720p\\input frame.ui")
    input_frame_lable_rely_720p = [0.105 ,0.27 ,0.441 ,0.61] 
    input_frame_entry_rely_720p = [0.115 ,0.282 ,0.455 ,0.624] 

    #buttons
    calculate_button_image_720p= PhotoImage(file=r"ui sources\\720p\\calculate button.ui")
    calculate_button_image_re_720p= PhotoImage(file=r"ui sources\\720p\\calculate button re.ui")
    reset_button_image_720p= PhotoImage(file=r"ui sources\\720p\\reset button.ui")
    reset_button_image_re_720p= PhotoImage(file=r"ui sources\\720p\\reset button re.ui")

    #error buttons
    calculate_button_error_image_720p= PhotoImage(file=r"ui sources\\720p\\calculate button error.ui")

    #output frame
    output_frame1_image_720p = PhotoImage(file=r"ui sources\\720p\\output frame1.ui")
    output_frame_label_rely_720p = [0.066 ,0.22 ,0.36 ,0.51 ,0.655 ,0.8] 
    output_frame1_dash_relx_720p = 0.47

    output_frame2_image_720p = PhotoImage(file=r"ui sources\\720p\\output frame2.ui")
    output_frame2_label_rely_720p = [0.13,0.31 ,0.52 ,0.69]
    output_frame2_dash_relx_720p= 0.42

    #table for ip ranges
    output_table_image_720p = PhotoImage(file=r"ui sources\\720p\\table.ui")
    table_lable_rely_720p = [0.242 ,0.37 ,0.49,0.615 ,0.735 ,0.86]
    table_range_relx_720p = 0.095
    table_range2_relx_720p = 0.565
    table1_dash1_relx_720p = 0.485
 

    #setting button
    setting_button_image_720p = PhotoImage(file=r"ui sources\\720p\\setting button.ui")
    setting_button_re_image_720p = PhotoImage(file=r"ui sources\\720p\\setting button re.ui")

    #side panel
    side_panel_image_720p = PhotoImage(file=r"ui sources\\720p\\side panel.ui")
    side_panel_size_720p = {"width":313 ,"height":720}

    #radio buttons place rely
    trancparency_radio_button_rely_720p = 0.402

    #VLSM OR FLSM
    flsm_vlsm_mode_image_720p = PhotoImage(file=r"ui sources\\720p\\vlsm flsm frame.ui")
    flsm_vlsm_frame_relwidth_720p = 0.15
    flsm_vlsm_frame_relheight_720p = 0.045
    flsm_vlsm_frame_rely_720p = 0.075

    fixed_variable_length_button_rely_720p = 0.15
    fixed_variable_length_radiobutton_rely_720p = 0.081

    #############################################################
    #############################################################
    #############################################################
    #############################################################
    vlsm_input_frame_image_720p = PhotoImage(file=r"ui sources\\720p\\input frame vlsm.ui")
    
    vlsm_title_inputipaddress_label_rely_720p= 0.067
    vlsm_input_ipaddress_entry_rely_720p = 0.07

    vlsm_title_inputnetworks_label_rely_720p = 0.121
    vlsm_input_networks_entry_rely_720p = 0.124

    #############################################################
    #############################################################
    vlsm_table_head_image_720p = PhotoImage(file=r"ui sources\\720p\\table head vlsm.ui")
    vlsm_table_row_1_image_720p = PhotoImage(file=r"ui sources\\720p\\table row vlsm.ui")
    vlsm_table_head_end_image_720p =  PhotoImage(file=r"ui sources\\720p\\table head end vlsm.ui")
    

    #############################################################
    #############################################################
    
    vlsm_table_th_rely_720p  = 0.025
    vlsm_table_th_relx_720p  = [0.01,0.085,0.21,0.305,0.53,0.782]

    vlsm_table_td_relx_720p  = [0.018,0.084,0.2,0.302  ,0.452,0.58,0.732,0.862]
    vlsm_table_td1_rely_720p  = 0.085
    vlsm_table_td_rely_change_720p = 0.055
    vlsm_table_td1_start_rely_720p = 0.0738

    vlsm_table_range_split_dash1_relx_720p = 0.5662
    vlsm_table_range_split_dash2_relx_720p  = 0.847


    #############################################################
    #############################################################
    table_hiding_frame_relx_720p= 0.9371
    table_frame_change_special_button_image_720p = PhotoImage(file=r"ui sources\\720p\\special button vlsm.ui")
    table_frame_change_special_button_re_image_720p = PhotoImage(file=r"ui sources\\720p\\special button re vlsm.ui")
    table_frame_change_special_button_error_image_720p = PhotoImage(file=r"ui sources\\720p\\special button error vlsm.ui")

    table_frame_change_special_button_back_image_720p = PhotoImage(file=r"ui sources\\720p\\special button back vlsm.ui")
    table_frame_change_special_button_back_re_image_720p = PhotoImage(file=r"ui sources\\720p\\special button back re vlsm.ui")
    vlsm_table_head_full_image_720p = PhotoImage(file=r"ui sources\\720p\\table head full vlsm.ui")
    vlsm_table_head_end_full_image_720p =  PhotoImage(file=r"ui sources\\720p\\table head end full vlsm.ui")
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #input frame
    title_image_900p=PhotoImage(file=r"ui sources\\900p\\title.ui")
    input_frame_image_900p = PhotoImage(file=r"ui sources\\900p\\input frame.ui") 
    input_frame_lable_rely_900p = [0.10 ,0.26 ,0.43 ,0.59] 
    input_frame_entry_rely_900p = [0.11 ,0.27 ,0.432 ,0.591] 

    #buttons
    calculate_button_image_900p = PhotoImage(file=r"ui sources\\900p\\calculate button.ui")
    calculate_button_image_re_900p = PhotoImage(file=r"ui sources\\900p\\calculate button re.ui")
    reset_button_image_900p = PhotoImage(file=r"ui sources\\900p\\reset button.ui")
    reset_button_image_re_900p = PhotoImage(file=r"ui sources\\900p\\reset button re.ui")

    #error buttons
    calculate_button_error_image_900p= PhotoImage(file=r"ui sources\\900p\\calculate button error.ui")

    #output frame
    output_frame1_image_900p = PhotoImage(file=r"ui sources\\900p\\output frame1.ui")
    output_frame_label_rely_900p = [0.08 ,0.22 ,0.36 ,0.5 ,0.64 ,0.78] 
    output_frame1_dash_relx_900p = 0.47

    output_frame2_image_900p = PhotoImage(file=r"ui sources\\900p\\output frame2.ui")
    output_frame2_label_rely_900p = [0.127,0.3 ,0.505 ,0.68] 
    output_frame2_dash_relx_900p = 0.42

    #table for ip ranges
    output_table_image_900p = PhotoImage(file=r"ui sources\\900p\\table.ui")
    table_lable_rely_900p = [0.217 ,0.329 ,0.446 ,0.562 ,0.68 ,0.802]
    table_range_relx_900p = 0.095
    table_range2_relx_900p = 0.565
    table1_dash1_relx_900p = 0.485
  
    #setting button
    setting_button_image_900p = PhotoImage(file=r"ui sources\\900p\\setting button.ui")
    setting_button_re_image_900p = PhotoImage(file=r"ui sources\\900p\\setting button re.ui")

    #side panel
    side_panel_image_900p = PhotoImage(file=r"ui sources\\900p\\side panel.ui")
    side_panel_size_900p = {"width":392 ,"height":900}

    #radio buttons place rely
    trancparency_radio_button_rely_900p = 0.404

    #VLSM OR FLSM
    flsm_vlsm_mode_image_900p = PhotoImage(file=r"ui sources\\900p\\vlsm flsm frame.ui")
    flsm_vlsm_frame_relwidth_900p = 0.15
    flsm_vlsm_frame_relheight_900p = 0.045
    flsm_vlsm_frame_rely_900p = 0.075

    fixed_variable_length_button_rely_900p=0.152
    fixed_variable_length_radiobutton_rely_900p = 0.181

    #############################################################
    #############################################################
    #############################################################
    #############################################################
    vlsm_input_frame_image_900p = PhotoImage(file=r"ui sources\\900p\\input frame vlsm.ui")
    vlsm_title_inputipaddress_label_rely_900p = 0.067
    vlsm_input_ipaddress_entry_rely_900p = 0.069

    vlsm_title_inputnetworks_label_rely_900p = 0.12
    vlsm_input_networks_entry_rely_900p = 0.124

    #############################################################
    #############################################################
    vlsm_table_head_image_900p = PhotoImage(file=r"ui sources\\900p\\table head vlsm.ui")
    vlsm_table_row_1_image_900p = PhotoImage(file=r"ui sources\\900p\\table row vlsm.ui")
    vlsm_table_head_end_image_900p =  PhotoImage(file=r"ui sources\\900p\\table head end vlsm.ui")

    #############################################################
    #############################################################
    vlsm_table_th_rely_900p  = 0.025
    vlsm_table_th_relx_900p  =  [0.01,0.084,0.21,0.305,0.53,0.782]

    vlsm_table_td_relx_900p  =  [0.019,0.084,0.2005,0.303  ,0.454,0.582,0.735,0.864]
    vlsm_table_td1_rely_900p  = 0.083
    vlsm_table_td_rely_change_900p = 0.055
    vlsm_table_td1_start_rely_900p = 0.0738

    vlsm_table_range_split_dash1_relx_900p = 0.567
    vlsm_table_range_split_dash2_relx_900p  = 0.849

    #############################################################
    #############################################################
    table_hiding_frame_relx_900p= 0.938
    table_frame_change_special_button_image_900p = PhotoImage(file=r"ui sources\\900p\\special button vlsm.ui")
    table_frame_change_special_button_re_image_900p = PhotoImage(file=r"ui sources\\900p\\special button re vlsm.ui")
    table_frame_change_special_button_error_image_900p = PhotoImage(file=r"ui sources\\900p\\special button error vlsm.ui")

    table_frame_change_special_button_back_image_900p = PhotoImage(file=r"ui sources\\900p\\special button back vlsm.ui")
    table_frame_change_special_button_back_re_image_900p = PhotoImage(file=r"ui sources\\900p\\special button back re vlsm.ui")
    vlsm_table_head_full_image_900p = PhotoImage(file=r"ui sources\\900p\\table head full vlsm.ui")
    vlsm_table_head_end_full_image_900p =  PhotoImage(file=r"ui sources\\900p\\table head end full vlsm.ui")

    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #input frame
    title_image_1080p =PhotoImage(file=r"ui sources\\1080p\\title.ui")
    input_frame_image_1080p = PhotoImage(file=r"ui sources\\1080p\\input frame.ui") 
    input_frame_lable_rely_1080p = [0.1 ,0.27 ,0.43 ,0.6] 
    input_frame_entry_rely_1080p = [0.107 ,0.271 ,0.435 ,0.602] 

    #buttons
    calculate_button_image_1080p = PhotoImage(file=r"ui sources\\1080p\\calculate button.ui")
    calculate_button_image_re_1080p = PhotoImage(file=r"ui sources\\1080p\\calculate button re.ui")
    reset_button_image_1080p = PhotoImage(file=r"ui sources\\1080p\\reset button.ui")
    reset_button_image_re_1080p  = PhotoImage(file=r"ui sources\\1080p\\reset button re.ui")

    #error button
    calculate_button_error_image_1080p= PhotoImage(file=r"ui sources\\1080p\\calculate button error.ui")

    #output frame
    output_frame1_image_1080p = PhotoImage(file=r"ui sources\\1080p\\output frame1.ui")
    output_frame_label_rely_1080p = [0.08 ,0.22 ,0.366 ,0.51 ,0.655 ,0.8] 
    output_frame1_dash_relx_1080p = 0.5

    output_frame2_image_1080p = PhotoImage(file=r"ui sources\\1080p\\output frame2.ui")
    output_frame2_label_rely_1080p = [0.127,0.3 ,0.505 ,0.68] 
    output_frame2_dash_relx_1080p = 0.445

    #table for ip ranges
    output_table_image_1080p = PhotoImage(file=r"ui sources\\1080p\\table.ui")
    table_lable_rely_1080p = [0.241 ,0.351 ,0.465 ,0.576 ,0.69 ,0.8]
    table_range_relx_1080p = 0.05
    table_range2_relx_1080p = 0.56
    table1_dash1_relx_1080p = 0.485
  
    #setting button
    setting_button_image_1080p = PhotoImage(file=r"ui sources\\1080p\\setting button.ui")
    setting_button_re_image_1080p = PhotoImage(file=r"ui sources\\1080p\\setting button re.ui")

    #side panel
    side_panel_image_1080p = PhotoImage(file=r"ui sources\\1080p\\side panel.ui")
    side_panel_size_1080p = {"width":462 ,"height":1080}

    #radio vuttons place rely
    trancparency_radio_button_rely_1080p = 0.407

    #VLSM OR FLSM
    flsm_vlsm_mode_image_1080p = PhotoImage(file=r"ui sources\\1080p\\vlsm flsm frame.ui")
    flsm_vlsm_frame_relwidth_1080p = 0.1527
    flsm_vlsm_frame_relheight_1080p = 0.0455
    flsm_vlsm_frame_rely_1080p = 0.07

    fixed_variable_length_button_rely_1080p=0.15
    fixed_variable_length_radiobutton_rely_1080p = 0.25

    #############################################################
    #############################################################
    #############################################################
    #############################################################
    vlsm_input_frame_image_1080p = PhotoImage(file=r"ui sources\\1080p\\input frame vlsm.ui")
    vlsm_title_inputipaddress_label_rely_1080p= 0.067
    vlsm_input_ipaddress_entry_rely_1080p = 0.068

    vlsm_title_inputnetworks_label_rely_1080p = 0.12
    vlsm_input_networks_entry_rely_1080p = 0.124

    #############################################################
    #############################################################
    vlsm_table_head_image_1080p = PhotoImage(file=r"ui sources\\1080p\\table head vlsm.ui")
    vlsm_table_row_1_image_1080p = PhotoImage(file=r"ui sources\\1080p\\table row vlsm.ui")
    vlsm_table_head_end_image_1080p =  PhotoImage(file=r"ui sources\\1080p\\table head end vlsm.ui")


    #############################################################
    #############################################################
    vlsm_table_th_rely_1080p  = 0.025
    vlsm_table_th_relx_1080p  =  [0.01,0.084,0.205,0.304,0.53,0.78]

    vlsm_table_td_relx_1080p  =  [0.018,0.082,0.199,0.3  ,0.45,0.578,0.729,0.859]
    vlsm_table_td1_rely_1080p  = 0.083
    vlsm_table_td_rely_change_1080p = 0.055
    vlsm_table_td1_start_rely_1080p = 0.0738

    vlsm_table_range_split_dash1_relx_1080p = 0.563
    vlsm_table_range_split_dash2_relx_1080p  = 0.843

    #############################################################
    #############################################################
    table_hiding_frame_relx_1080p= 0.9339
    table_frame_change_special_button_image_1080p = PhotoImage(file=r"ui sources\\1080p\\special button vlsm.ui")
    table_frame_change_special_button_re_image_1080p = PhotoImage(file=r"ui sources\\1080p\\special button re vlsm.ui")
    table_frame_change_special_button_error_image_1080p = PhotoImage(file=r"ui sources\\1080p\\special button error vlsm.ui")

    table_frame_change_special_button_back_image_1080p = PhotoImage(file=r"ui sources\\1080p\\special button back vlsm.ui")
    table_frame_change_special_button_back_re_image_1080p = PhotoImage(file=r"ui sources\\1080p\\special button back re vlsm.ui")
    vlsm_table_head_full_image_1080p = PhotoImage(file=r"ui sources\\1080p\\table head full vlsm.ui")
    vlsm_table_head_end_full_image_1080p =  PhotoImage(file=r"ui sources\\1080p\\table head end full vlsm.ui")

    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################
except :
    os.startfile("error.py")
    sys.exit()

if real_resolution== 720:
    setting_button_image = setting_button_image_720p
if real_resolution== 900:
    setting_button_image = setting_button_image_900p
if real_resolution== 1080:    
    setting_button_image = setting_button_image_1080p

#############################################################
#############################################################
#############################################################
#############################################################
create_files_loading()
#############################################################
#############################################################
main_window.mainloop()

fgeomatry = open("Sources\\Settings\\resolution_set\\location.rapa","w")
fgeomatry.write(str(int(window_relx_geomatry_read))+","+str(int(window_rely_geomatry_read)))
fgeomatry.close()

files = os.listdir("FLSM")
files1 = os.listdir("VLSM")
for file in files:
    os.remove("FLSM\\"+file)
for file in files1:
    os.remove("VLSM\\"+file)