import math
from tkinter import *
import ezdxf
from PIL import Image, ImageTk
import tkinter.font as font
import os


cwd = os.getcwd()
path_output = cwd + "/designs/"
try:
    os.mkdir(path_output)
except:
    pass


def Cycloid_rise(theta_zero,theta,theta2,h_zero,h):
    result = math.radians(h_zero) + math.radians(h - h_zero) * ((theta - theta_zero) / (theta2 - theta_zero) -
                    1 / (2 * math.pi) * math.sin(2*math.pi * (theta - theta_zero) / (theta2 - theta_zero)))
    return result

def DCycloid_rise(theta_zero,theta,theta2,h_zero,h):
    result = (h-h_zero) / (theta2 - theta_zero) * (1 - math.cos(2 * math.pi * (theta - theta_zero) / (theta2 - theta_zero)))
    return result

def S(theta,courses_list,n):
    for i in range(0,n):
        if courses_list[i][1] <= theta <= courses_list[i][2]:
            if courses_list[i][0] == 1 or courses_list[i][0] == 3:
                result = Cycloid_rise(courses_list[i][1],theta,courses_list[i][2],courses_list[i][3],courses_list[i][4])
                return result
            if courses_list[i][0] == 2:
                result = math.radians(courses_list[i][3])
                return result

def dS(theta,courses_list,n):
    for i in range(0, n):
        if courses_list[i][1] <= theta <= courses_list[i][2]:
            if courses_list[i][0] == 1 or courses_list[i][0] == 3:
                result = DCycloid_rise(courses_list[i][1],theta,courses_list[i][2],courses_list[i][3],courses_list[i][4])
                return result
            if courses_list[i][0] == 2:
                result = 0
                return result

def Zetta(theta,l,f,b,courses_list,n):
    result = math.acos((l ** 2 + f ** 2 - b ** 2)/(2*l*f)) + S(theta,courses_list,n)
    return result

def q(theta,f,courses_list,n):
    result = f * dS(theta,courses_list,n) / (1-dS(theta,courses_list,n))
    return result


class Conjugate_cam():
    def __init__(self, master):
        self.master = master
        master.title("Bustabit")
        master.geometry('{}x{}'.format(900, 500))
        main_frame = Frame(master, width=550, )
        main_frame.pack(side='top', fill="both")


        myFont16 = font.Font(size=16)
        myFont14 = font.Font(size=12)
        # btm_right
        right_panel = Frame(main_frame, width=480, height=450, highlightbackground="black", highlightthickness=2)
        left_panel = Frame(main_frame, width=420, height=450)
        left_panel.pack(side="left", fill="both", )
        right_panel.pack(side="right", fill="both", expand=True, )

        right_top_frame = Frame(right_panel, width=380, height=450)
        right_top_frame.pack(side="top", fill="both")
        right_bot_fram = Frame(right_panel, width=380, height=450)
        right_bot_fram.pack(side="top", fill="both")

        self.l_label = Label(right_top_frame, text='L', anchor="w", font=myFont14,width=4)
        self.l_entry = Entry(right_top_frame, width=5, font=myFont14, )
        self.l_description_label = Label(right_top_frame, text='arm length of follower', anchor="w", font=myFont14)

        self.f_label = Label(right_top_frame, text='f', anchor="w", font=myFont14)
        self.f_entry = Entry(right_top_frame, width=5, font=myFont14, )
        self.f_description_label = Label(right_top_frame, text='distance from cam center to follower pivot point',
                                         anchor="w", font=myFont14)

        self.rb_label = Label(right_top_frame, text='rb', anchor="w", font=myFont14)
        self.rb_entry = Entry(right_top_frame, width=5, font=myFont14, )
        self.rb_description_label = Label(right_top_frame, text='base circle radius of cam', anchor="w", font=myFont14)

        self.rf_label = Label(right_top_frame, text='rf', anchor="w", font=myFont14)
        self.rf_entry = Entry(right_top_frame, width=5, font=myFont14, )
        self.rf_description_label = Label(right_top_frame, text='radius of the roller follower', anchor="w",
                                          font=myFont14)

        self.motion_label = Label(right_bot_fram, text='Cam Motion Courses', anchor="w", font=myFont16, )

        self.n_label = Label(right_bot_fram, text='n', anchor="w", font=myFont14)
        self.n_entry = Entry(right_bot_fram, width=2, font=myFont14)
        self.n_description_label = Label(right_bot_fram, text='number of cam motion courses', anchor="w", font=myFont14)

        self.course_label1 = Label(right_bot_fram, text='course', anchor="w", font=myFont14)
        self.course_label2 = Label(right_bot_fram, text='Theta Cam', anchor="w", font=myFont14)
        self.course_label3 = Label(right_bot_fram, text='Theta Follower', anchor="w", font=myFont14)
        self.course_label4 = Label(right_bot_fram, text='Motion Type', anchor="w", font=myFont14)

        self.c1_label = Label(right_bot_fram, text='1', anchor="w", font=myFont14)
        self.c1_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c1_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c1_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14)

        self.c2_label = Label(right_bot_fram, text='2', anchor="w", font=myFont14)
        self.c2_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c2_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c2_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14)

        self.c3_label = Label(right_bot_fram, text='3', anchor="w", font=myFont14)
        self.c3_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c3_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c3_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14)

        self.c4_label = Label(right_bot_fram, text='4', anchor="w", font=myFont14)
        self.c4_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c4_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c4_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14)

        self.c5_label = Label(right_bot_fram, text='5', anchor="w", font=myFont14)
        self.c5_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c5_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c5_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14)

        self.c6_label = Label(right_bot_fram, text='6', anchor="w", font=myFont14)
        self.c6_thetac_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c6_thetaf_entry = Entry(right_bot_fram, width=6, font=myFont14)
        self.c6_motiont_entry = Entry(right_bot_fram, width=3, font=myFont14,)


        # right top frame
        # ro0
        self.l_label.grid(row=0, column=0, padx=3, pady=3, sticky="we",)
        self.l_entry.grid(row=0, column=1, sticky="WE")
        self.l_description_label.grid(row=0, column=2, padx=3, pady=3, sticky="wesn")


        # ro1
        self.f_label.grid(row=1, column=0, padx=3, pady=3, sticky="we")
        self.f_entry.grid(row=1, column=1, padx=3, pady=3, sticky="WE")
        self.f_description_label.grid(row=1, column=2, padx=3, pady=3, sticky="we")
        # ro2
        self.rb_label.grid(row=2, column=0, padx=3, pady=3, sticky="we")
        self.rb_entry.grid(row=2, column=1, padx=3, pady=3, sticky="WE")
        self.rb_description_label.grid(row=2, column=2, padx=3, pady=3, sticky="we")
        # ro3
        self.rf_label.grid(row=3, column=0, padx=3, pady=3, sticky="we")
        self.rf_entry.grid(row=3, column=1, padx=3, pady=3, sticky="WE")
        self.rf_description_label.grid(row=3, column=2, padx=3, pady=3, sticky="we")

        # right_bot_frame
        # ro0
        self.motion_label.grid(row=0, column=0, padx=3, pady=3, sticky="we", columnspan=3)

        # ro1
        self.n_label.grid(row=1, column=0, padx=3, pady=3, sticky="we")
        self.n_entry.grid(row=1, column=1, padx=3, pady=3, sticky="w")
        self.n_description_label.grid(row=1, column=2, padx=3, pady=3, sticky="we", columnspan=2)

        # ro2
        self.course_label1.grid(row=2, column=0, padx=3, pady=3, sticky="we")
        self.course_label2.grid(row=2, column=1, padx=3, pady=3, sticky="we")
        self.course_label3.grid(row=2, column=2, padx=3, pady=3, sticky="we")
        self.course_label4.grid(row=2, column=3, padx=3, pady=3, sticky="we")

        # ro3
        self.c1_label.grid(row=3, column=0, padx=3, pady=3, sticky="we")
        self.c1_thetac_entry.grid(row=3, column=1, padx=3, pady=3, )
        self.c1_thetaf_entry.grid(row=3, column=2, padx=3, pady=3, )
        self.c1_motiont_entry.grid(row=3, column=3, padx=3, pady=3,)

        self.c2_label.grid(row=4, column=0, padx=3, pady=3, sticky="we")
        self.c2_thetac_entry.grid(row=4, column=1, padx=3, pady=3, )
        self.c2_thetaf_entry.grid(row=4, column=2, padx=3, pady=3, )
        self.c2_motiont_entry.grid(row=4, column=3, padx=3, pady=3, )

        self.c3_label.grid(row=5, column=0, padx=3, pady=3, sticky="we")
        self.c3_thetac_entry.grid(row=5, column=1, padx=3, pady=3, )
        self.c3_thetaf_entry.grid(row=5, column=2, padx=3, pady=3, )
        self.c3_motiont_entry.grid(row=5, column=3, padx=3, pady=3, )

        self.c4_label.grid(row=6, column=0, padx=3, pady=3, sticky="we")
        self.c4_thetac_entry.grid(row=6, column=1, padx=3, pady=3,)
        self.c4_thetaf_entry.grid(row=6, column=2, padx=3, pady=3, )
        self.c4_motiont_entry.grid(row=6, column=3, padx=3, pady=3, )

        self.c5_label.grid(row=7, column=0, padx=3, pady=3, sticky="we")
        self.c5_thetac_entry.grid(row=7, column=1, padx=3, pady=3,)
        self.c5_thetaf_entry.grid(row=7, column=2, padx=3, pady=3, )
        self.c5_motiont_entry.grid(row=7, column=3, padx=3, pady=3, )

        self.c6_label.grid(row=8, column=0, padx=3, pady=3, sticky="we")
        self.c6_thetac_entry.grid(row=8, column=1, padx=3, pady=3, )
        self.c6_thetaf_entry.grid(row=8, column=2, padx=3, pady=3, )
        self.c6_motiont_entry.grid(row=8, column=3, padx=3, pady=3, )

        img = ImageTk.PhotoImage(Image.open('Conjugate.png').resize((425, 319)))
        photo_label = Label(left_panel, image=img)
        photo_label.image = img  # this feels redundant but the image didn't show up without it in my app
        photo_label.grid(row=0, column=0)

        self.desc0_label = Label(left_panel, text='Guide: ', anchor="w",
                                 font=myFont16)
        self.desc1_label = Label(left_panel, text='Theta Cam: angle of cam at end of course (degrees)', anchor="w",
                                 font=myFont14)
        self.desc2_label = Label(left_panel, text='Theta Follower: angle of Follower at end of course (degrees)',
                                 anchor="w", font=myFont14)
        self.desc3_label = Label(left_panel, text='Motion Type: Cycloid Rise = 1, Dwell = 2, Cycloid Fall = 3,',
                                 anchor="w", font=myFont14)

        self.create_button = Button(left_panel,font=myFont16,text ="Create", padx=5,pady=5,command= self.Create)

        self.desc0_label.grid(row=1, column=0,sticky='w')
        self.desc1_label.grid(row=2, column=0,sticky='w')
        self.desc2_label.grid(row=3, column=0,sticky='w')
        self.desc3_label.grid(row=4, column=0,sticky='w')
        self.create_button.grid(row=5, column=0,sticky='w',padx = 10,pady=10)


    def Create(self):
        l = float(self.l_entry.get())
        f = float(self.f_entry.get())
        rb = float(self.rb_entry.get())
        rf = float(self.rf_entry.get())
        b = rf + rb
        n =  int(self.n_entry.get())
        n = int(n)
        theta_follower_zero = math.degrees(math.acos((l ** 2 + f ** 2 - b ** 2)/(2*l*f)))
        courses_list = []
        c1_thetac_entry = self.c1_thetac_entry.get()
        c1_thetaf_entry = self.c1_thetaf_entry.get()
        c1_motiont_entry = self.c1_motiont_entry.get()

        c2_thetac_entry = self.c2_thetac_entry.get()
        c2_thetaf_entry = self.c2_thetaf_entry.get()
        c2_motiont_entry = self.c2_motiont_entry.get()

        c3_thetac_entry = self.c3_thetac_entry.get()
        c3_thetaf_entry = self.c3_thetaf_entry.get()
        c3_motiont_entry = self.c3_motiont_entry.get()

        c4_thetac_entry = self.c4_thetac_entry.get()
        c4_thetaf_entry = self.c4_thetaf_entry.get()
        c4_motiont_entry = self.c4_motiont_entry.get()

        c5_thetac_entry = self.c5_thetac_entry.get()
        c5_thetaf_entry = self.c5_thetaf_entry.get()
        c5_motiont_entry = self.c5_motiont_entry.get()

        c6_thetac_entry = self.c6_thetac_entry.get()
        c6_thetaf_entry = self.c6_thetaf_entry.get()
        c6_motiont_entry = self.c6_motiont_entry.get()

        try:
            c1_thetaf_entry = float(self.c1_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c1_motiont_entry),0,float(c1_thetac_entry),0,float(c1_thetaf_entry),))
        except:
            pass

        try:
            c2_thetaf_entry = float(self.c2_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c2_motiont_entry), float(c1_thetac_entry), float(c2_thetac_entry), float(c1_thetaf_entry), float(c2_thetaf_entry), ))
        except:
            pass

        try:
            c3_thetaf_entry = float(self.c3_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c3_motiont_entry), float(c2_thetac_entry), float(c3_thetac_entry), float(c2_thetaf_entry), float(c3_thetaf_entry),))
        except:
            pass

        try:
            c4_thetaf_entry = float(self.c4_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c4_motiont_entry), float(c3_thetac_entry), float(c4_thetac_entry), float(c3_thetaf_entry), float(c4_thetaf_entry),))
        except:
            pass

        try:
            c5_thetaf_entry = float(self.c5_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c5_motiont_entry), float(c4_thetac_entry), float(c5_thetac_entry), float(c4_thetaf_entry), float(c5_thetaf_entry),))
        except:
            pass

        try:
            c6_thetaf_entry = float(self.c6_thetaf_entry.get()) - theta_follower_zero
            courses_list.append((int(c6_motiont_entry), float(c5_thetac_entry), float(c6_thetac_entry), float(c5_thetaf_entry), float(c6_thetaf_entry),))
        except:
            pass


        create_cams(l=l,f=f,rf=rf,b=b,courses_list = courses_list[:n],n=n )


def create_cams(l,f,rf,b,courses_list,n):
    doc = ezdxf.new('R2010')
    msp = doc.modelspace()
    doc2 = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
    msp2 = doc2.modelspace()
    primary_list = []
    conjugate_list = []
    for i in range(0, 3600):
        theta = i / 10
        c = f
        QC = (l ** 2 + (c + q(theta,f,courses_list,n)) ** 2 - 2 * l * (c + q(theta,f,courses_list,n)) * math.cos(Zetta(theta,l,f,b,courses_list,n))) ** 0.5
        QD = (l ** 2 + (c + q(theta,f,courses_list,n)) ** 2 - 2 * l * (c + q(theta,f,courses_list,n)) * math.cos(math.radians(90) - Zetta(theta,l,f,b,courses_list,n))) ** 0.5

        Alpha_a = math.asin((l * math.sin(Zetta(theta,l,f,b,courses_list,n)) / QC))
        Alpha_b = math.asin(l * math.sin(math.radians(90) - Zetta(theta,l,f,b,courses_list,n)) / QD)

        O2Q_i = q(theta,f,courses_list,n) * math.cos(math.radians(180 + theta))
        O2Q_j = q(theta,f,courses_list,n) * math.sin(math.radians(180 + theta))

        QA_i = (QC - rf) * math.cos(math.radians(theta) + Alpha_a)
        QA_j = (QC - rf) * math.sin(math.radians(theta) + Alpha_a)

        O2A_i = O2Q_i + QA_i
        O2A_j = O2Q_j + QA_j

        QB_i = (QD - rf) * math.cos(math.radians(theta) - Alpha_b)
        QB_j = (QD - rf) * math.sin(math.radians(theta) - Alpha_b)

        O2B_i = O2Q_i + QB_i
        O2B_j = O2Q_j + QB_j

        primary_list.append((O2A_i, O2A_j, 0))

        conjugate_list.append((O2B_i, O2B_j, 0))

    list_out = os.listdir(path_output)
    list_out_number = []
    for item in list_out:
        list_out_number.append(int(item))
    list_out_number = sorted(list_out_number)
    if list_out_number == []:
        folder_name = 1
    else:
        folder_name = list_out_number[-1] + 1
    os.mkdir(path_output + str(folder_name))
    path_save = path_output + str(folder_name) + "/"
    msp.add_closed_spline(primary_list)
    doc.saveas(path_save + 'primary.dxf')

    msp2.add_closed_spline(conjugate_list)
    doc2.saveas(path_save + 'conjugate.dxf')


root = Tk()
my_gui = Conjugate_cam(root)
root.mainloop()
