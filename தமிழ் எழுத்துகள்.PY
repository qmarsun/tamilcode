from tkinter import *
import pygame
from gtts import gTTS
import os
import pyttsx3


pygame.init()
root=Tk()
root.title("தமிழ் எழுத்துகள்")
root.geometry('1352x652+0+0')
root.configure(background='white')

#icon
icon_image=PhotoImage(file="tamilicon.png")
root.iconphoto(False,icon_image)  

str1= StringVar ()
str1.set("தமிழ் எழுத்து")
ABC= Frame(root, bg="white")
ABC.grid()

def Alphabet_1():
    str1.set("ஃ")
    tts = gTTS(text= "ஃ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_1():
    pygame.mixer.music.load("245.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_2():
    str1.set("அ")
    tts = gTTS(text= "அ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_2():
    pygame.mixer.music.load("232.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_3():
    str1.set("ஆ")
    tts = gTTS(text= "ஆ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_3():
    pygame.mixer.music.load("233.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_4():
    str1.set("இ")
    tts = gTTS(text= "இ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_4():
    pygame.mixer.music.load("234.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_5():
    str1.set("ஈ")
    tts = gTTS(text= "ஈ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_5():
    pygame.mixer.music.load("235.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_6():
    str1.set("உ")
    tts = gTTS(text= "உ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_6():
    pygame.mixer.music.load("236.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_7():
    str1.set("ஊ")
    tts = gTTS(text= "ஊ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_7():
    pygame.mixer.music.load("237.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_8():
    str1.set("எ")
    tts = gTTS(text= "எ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_8():
    pygame.mixer.music.load("238.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_9():
    str1.set("ஏ")
    tts = gTTS(text= "ஏ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_9():
    pygame.mixer.music.load("239.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_10():
    str1.set("ஐ")
    tts = gTTS(text= "ஐ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_10():
    pygame.mixer.music.load("240.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_11():
    str1.set("ஒ")
    tts = gTTS(text= "ஒ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_11():
    pygame.mixer.music.load("241.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_12():
    str1.set("ஓ")
    tts = gTTS(text= "ஓ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_12():
    pygame.mixer.music.load("242.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_13():
    str1.set("ஔ")
    tts = gTTS(text= "ஔ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_13():
    pygame.mixer.music.load("243.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_14():
    str1.set("க்")
    tts = gTTS(text= "க்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_14():
    pygame.mixer.music.load("13.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_15():
    str1.set("க ")
    tts = gTTS(text= "க" , lang ='ta')
    pygame.mixer.init()
def Alphabet_15():
    pygame.mixer.music.load("1.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_16():
    str1.set("கா")
    tts = gTTS(text= "கா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_16():
    pygame.mixer.music.load("2.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_17():
    str1.set("கி")
    tts = gTTS(text= "கி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_17():
    pygame.mixer.music.load("3.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_18():
    str1.set("கீ")
    tts = gTTS(text= "கீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_18():
    pygame.mixer.music.load("4.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_19():
    str1.set("கு")
    tts = gTTS(text= "கு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_19():
    pygame.mixer.music.load("5.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_20():
    str1.set("கூ")
    tts = gTTS(text= "கூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_20():
    pygame.mixer.music.load("6.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_21():
    str1.set("கெ")
    tts = gTTS(text= "கெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_21():
    pygame.mixer.music.load("7.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_22():
    str1.set("கே")
    tts = gTTS(text= "கே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_22():
    pygame.mixer.music.load("8.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_23():
    str1.set("கை")
    tts = gTTS(text= "கை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_23():
    pygame.mixer.music.load("9.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_24():
    str1.set("கொ")
    tts = gTTS(text= "கொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_24():
    pygame.mixer.music.load("10.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_25():
    str1.set("கோ")
    tts = gTTS(text= "கோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_25():
    pygame.mixer.music.load("11.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_26():
    str1.set("கௌ")
    tts = gTTS(text= "கௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_26():
    pygame.mixer.music.load("12.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_27():
    str1.set("ங்")
    tts = gTTS(text= "ங்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_27():
    pygame.mixer.music.load("25.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_28():
    str1.set("ங")
    tts = gTTS(text= "ங" , lang ='ta')
    pygame.mixer.init()
def Alphabet_28():
    pygame.mixer.music.load("14.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_29():
    str1.set("ஙா")
    tts = gTTS(text= "ஙா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_29():
    pygame.mixer.music.load("15.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_30():
    str1.set("ஙி")
    tts = gTTS(text= "ஙி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_30():
    pygame.mixer.music.load("16.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_31():
    str1.set("ஙீ")
    tts = gTTS(text= "ஙீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_31():
    pygame.mixer.music.load("17.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_32():
    str1.set("ஙு")
    tts = gTTS(text= "ஙு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_32():
    pygame.mixer.music.load("18.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_33():
    str1.set("ஙூ")
    tts = gTTS(text= "ஙூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_33():
    pygame.mixer.music.load("19.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_34():
    str1.set("ஙெ")
    tts = gTTS(text= "ஙெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_34():
    pygame.mixer.music.load("20.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_35():
    str1.set("ஙே")
    tts = gTTS(text= "ஙே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_35():
    pygame.mixer.music.load("21.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_36():
    str1.set("ஙை")
    tts = gTTS(text= "ஙை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_36():
    pygame.mixer.music.load("22.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_37():
    str1.set("ஙொ")
    tts = gTTS(text= "ஙொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_37():
    pygame.mixer.music.load("23.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_38():
    str1.set("ஙோ")
    tts = gTTS(text= "ஙோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_38():
    pygame.mixer.music.load("23.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_39():
    str1.set("ஙௌ")
    tts = gTTS(text= "ஙௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_39():
    pygame.mixer.music.load("24.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_40():
    str1.set("ச்")
    tts = gTTS(text= "ச்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_40():
    pygame.mixer.music.load("37.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_41():
    str1.set("ச")
    tts = gTTS(text= "ச" , lang ='ta')
    pygame.mixer.init()
def Alphabet_41():
    pygame.mixer.music.load("26.mp3")
    pygame.mixer.music.play(loops=0) 

def Alphabet_42():
    str1.set("சா")
    tts = gTTS(text= "சா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_42():
    pygame.mixer.music.load("saaa.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_43():
    str1.set("சி")
    tts = gTTS(text= "சி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_43():
    pygame.mixer.music.load("27.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_44():
    str1.set("சீ")
    tts = gTTS(text= "சீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_44():
    pygame.mixer.music.load("28.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_45():
    str1.set("சு")
    tts = gTTS(text= "சு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_45():
    pygame.mixer.music.load("29.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_46():
    str1.set("சூ")
    tts = gTTS(text= "சூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_46():
    pygame.mixer.music.load("30.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_47():
    str1.set("செ")
    tts = gTTS(text= "செ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_47():
    pygame.mixer.music.load("31.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_48():
    str1.set("சே")
    tts = gTTS(text= "சே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_48():
    pygame.mixer.music.load("32.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_49():
    str1.set("சை")
    tts = gTTS(text= "சை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_49():
    pygame.mixer.music.load("33.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_50():
    str1.set("சொ")
    tts = gTTS(text= "சொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_50():
    pygame.mixer.music.load("34.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_51():
    str1.set("சோ")
    tts = gTTS(text= "சோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_51():
    pygame.mixer.music.load("35.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_52():
    str1.set("சௌ")
    tts = gTTS(text= "சௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_52():
    pygame.mixer.music.load("36.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_53():
    str1.set("ஞ்")
    tts = gTTS(text= "ஞ்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_53():
    pygame.mixer.music.load("50.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_54():
    str1.set("ஞ")
    tts = gTTS(text= "ஞ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_54():
    pygame.mixer.music.load("38.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_55():
    str1.set("ஞா")
    tts = gTTS(text= "ஞா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_55():
    pygame.mixer.music.load("39.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_56():
    str1.set("ஞி")
    tts = gTTS(text= "ஞி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_56():
    pygame.mixer.music.load("40.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_57():
    str1.set("ஞீ")
    tts = gTTS(text= "ஞீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_57():
    pygame.mixer.music.load("41.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_58():
    str1.set("ஞு")
    tts = gTTS(text= "ஞு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_58():
    pygame.mixer.music.load("42.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_59():
    str1.set("ஞூ")
    tts = gTTS(text= "ஞூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_59():
    pygame.mixer.music.load("43.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_60():
    str1.set("ஞெ")
    tts = gTTS(text= "ஞெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_60():
    pygame.mixer.music.load("44.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_61():
    str1.set("ஞே")
    tts = gTTS(text= "ஞே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_61():
    pygame.mixer.music.load("45.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_62():
    str1.set("ஞை")
    tts = gTTS(text= "ஞை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_62():
    pygame.mixer.music.load("46.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_63():
    str1.set("ஞொ")
    tts = gTTS(text= "ஞொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_63():
    pygame.mixer.music.load("47.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_64():
    str1.set("ஞோ")
    tts = gTTS(text= "ஞோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_64():
    pygame.mixer.music.load("48.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_65():
    str1.set("ஞௌ")
    tts = gTTS(text= "ஞௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_65():
    pygame.mixer.music.load("49.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_66():
    str1.set("ட்")
    tts = gTTS(text= "ட்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_66():
    pygame.mixer.music.load("ட்.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_67():
    str1.set("ட")
    tts = gTTS(text= "ட" , lang ='ta')
    pygame.mixer.init()
def Alphabet_67():
    pygame.mixer.music.load("51.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_68():
    str1.set("டா")
    tts = gTTS(text= "டா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_68():
    pygame.mixer.music.load("52.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_69():
    str1.set("டி")
    tts = gTTS(text= "டி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_69():
    pygame.mixer.music.load("53.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_70():
    str1.set("டீ")
    tts = gTTS(text= "டீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_70():
    pygame.mixer.music.load("54.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_71():
    str1.set("டு")
    tts = gTTS(text= "டு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_71():
    pygame.mixer.music.load("55.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_72():
    str1.set("டூ")
    tts = gTTS(text= "டூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_72():
    pygame.mixer.music.load("56.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_73():
    str1.set("டெ")
    tts = gTTS(text= "டெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_73():
    pygame.mixer.music.load("57.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_74():
    str1.set("டே")
    tts = gTTS(text= "டே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_74():
    pygame.mixer.music.load("58.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_75():
    str1.set("டை")
    tts = gTTS(text= "டை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_75():
    pygame.mixer.music.load("59.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_76():
    str1.set("டொ")
    tts = gTTS(text= "டொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_76():
    pygame.mixer.music.load("60.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_77():
    str1.set("டோ")
    tts = gTTS(text= "டோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_77():
    pygame.mixer.music.load("61.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_78():
    str1.set("டௌ")
    tts = gTTS(text= "டௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_78():
    pygame.mixer.music.load("62.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_79():
    str1.set("ண்")
    tts = gTTS(text= "ண்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_79():
    pygame.mixer.music.load("76.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_80():
    str1.set("ண")
    tts = gTTS(text= "ண" , lang ='ta')
    pygame.mixer.init()
def Alphabet_80():
    pygame.mixer.music.load("64.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_81():
    str1.set("ணா")
    tts = gTTS(text= "ணா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_81():
    pygame.mixer.music.load("65.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_82():
    str1.set("ணி")
    tts = gTTS(text= "ணி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_82():
    pygame.mixer.music.load("66.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_83():
    str1.set("ணீ")
    tts = gTTS(text= "ணீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_83():
    pygame.mixer.music.load("67.mp3")
    pygame.mixer.music.play(loops=0)
    


def Alphabet_84():
    str1.set("ணு")
    tts = gTTS(text= "ணு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_84():
    pygame.mixer.music.load("68.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_85():
    str1.set("ணூ")
    tts = gTTS(text= "ணூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_85():
    pygame.mixer.music.load("69.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_86():
    str1.set("ணெ")
    tts = gTTS(text= "ணெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_86():
    pygame.mixer.music.load("70.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_87():
    str1.set("ணே")
    tts = gTTS(text= "ணே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_87():
    pygame.mixer.music.load("71.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_88():
    str1.set("ணை")
    tts = gTTS(text= "ணை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_88():
    pygame.mixer.music.load("72.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_89():
    str1.set("ணொ")
    tts = gTTS(text= "ணொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_89():
    pygame.mixer.music.load("73.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_90():
    str1.set("ணோ")
    tts = gTTS(text= "ணோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_90():
    pygame.mixer.music.load("74.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_91():
    str1.set("ணௌ")
    tts = gTTS(text= "ணௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_91():
    pygame.mixer.music.load("75.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_92():
    str1.set("த்")
    tts = gTTS(text= "த்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_92():
    pygame.mixer.music.load("89.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_93():
    str1.set("த")
    tts = gTTS(text= "த" , lang ='ta')
    pygame.mixer.init()
def Alphabet_93():
    pygame.mixer.music.load("77.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_94():
    str1.set("தா")
    tts = gTTS(text= "தா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_94():
    pygame.mixer.music.load("78.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_95():
    str1.set("தி")
    tts = gTTS(text= "தி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_95():
    pygame.mixer.music.load("79.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_96():
    str1.set("தீ")
    tts = gTTS(text= "தீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_96():
    pygame.mixer.music.load("80.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_97():
    str1.set("து")
    tts = gTTS(text= "து" , lang ='ta')
    pygame.mixer.init()
def Alphabet_97():
    pygame.mixer.music.load("81.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_98():
    str1.set("தூ")
    tts = gTTS(text= "தூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_98():
    pygame.mixer.music.load("82.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_99():
    str1.set("தெ")
    tts = gTTS(text= "தெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_99():
    pygame.mixer.music.load("83.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_100():
    str1.set("தே")
    tts = gTTS(text= "தே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_100():
    pygame.mixer.music.load("84.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_101():
    str1.set("தை")
    tts = gTTS(text= "தை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_101():
    pygame.mixer.music.load("85.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_102():
    str1.set("தொ")
    tts = gTTS(text= "தொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_102():
    pygame.mixer.music.load("86.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_103():
    str1.set("தோ")
    tts = gTTS(text= "தோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_103():
    pygame.mixer.music.load("87.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_104():
    str1.set("தௌ")
    tts = gTTS(text= "தௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_104():
    pygame.mixer.music.load("88.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_105():
    str1.set("ந்")
    tts = gTTS(text= "ந்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_105():
    pygame.mixer.music.load("100.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_106():
    str1.set("ந")
    tts = gTTS(text= "ந" , lang ='ta')
    pygame.mixer.init()
def Alphabet_106():
    pygame.mixer.music.load("90.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_107():
    str1.set("நா")
    tts = gTTS(text= "நா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_107():
    pygame.mixer.music.load("91.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_108():
    str1.set("நி")
    tts = gTTS(text= "நி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_108():
    pygame.mixer.music.load("92.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_109():
    str1.set("நீ")
    tts = gTTS(text= "நீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_109():
    pygame.mixer.music.load("93.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_110():
    str1.set("நு")
    tts = gTTS(text= "நு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_110():
    pygame.mixer.music.load("94.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_111():
    str1.set("நூ")
    tts = gTTS(text= "நூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_111():
    pygame.mixer.music.load("nu.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_112():
    str1.set("நெ")
    tts = gTTS(text= "நெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_112():
    pygame.mixer.music.load("nhe.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_113():
    str1.set("நே")
    tts = gTTS(text= "நே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_113():
    pygame.mixer.music.load("95.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_114():
    str1.set("நை")
    tts = gTTS(text= "நை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_114():
    pygame.mixer.music.load("96.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_115():
    str1.set("நொ")
    tts = gTTS(text= "நொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_115():
    pygame.mixer.music.load("97.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_116():
    str1.set("நோ")
    tts = gTTS(text= "நோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_116():
    pygame.mixer.music.load("98.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_117():
    str1.set("நௌ")
    tts = gTTS(text= "நௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_117():
    pygame.mixer.music.load("99.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_118():
    str1.set("ப")
    tts = gTTS(text= "ப" , lang ='ta')
    pygame.mixer.init()
def Alphabet_118():
    pygame.mixer.music.load("101.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_119():
    str1.set("பா")
    tts = gTTS(text= "பா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_119():
    pygame.mixer.music.load("102.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_120():
    str1.set("பி")
    tts = gTTS(text= "பி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_120():
    pygame.mixer.music.load("103.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_121():
    str1.set("பீ")
    tts = gTTS(text= "பீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_121():
    pygame.mixer.music.load("104.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_122():
    str1.set("பு")
    tts = gTTS(text= "பு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_122():
    pygame.mixer.music.load("105.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_123():
    str1.set("பூ")
    tts = gTTS(text= "பூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_123():
    pygame.mixer.music.load("106.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_124():
    str1.set("பெ")
    tts = gTTS(text= "பெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_124():
    pygame.mixer.music.load("107.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_125():
    str1.set("பே")
    tts = gTTS(text= "பே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_125():
    pygame.mixer.music.load("108.mp3")
    pygame.mixer.music.play(loops=0)

    

def Alphabet_126():
    str1.set("பை")
    tts = gTTS(text= "பை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_126():
    pygame.mixer.music.load("109.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_127():
    str1.set("பொ")
    tts = gTTS(text= "பொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_127():
    pygame.mixer.music.load("110.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_128():
    str1.set("போ")
    tts = gTTS(text= "போ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_128():
    pygame.mixer.music.load("111.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_129():
    str1.set("பௌ")
    tts = gTTS(text= "பௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_129():
    pygame.mixer.music.load("112.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_130():
    str1.set("ப்")
    tts = gTTS(text= "ப்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_130():
    pygame.mixer.music.load("p.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_131():
    str1.set("ம")
    tts = gTTS(text= "ம" , lang ='ta')
    pygame.mixer.init()
def Alphabet_131():
    pygame.mixer.music.load("114.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_132():
    str1.set("மா")
    tts = gTTS(text= "மா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_132():
    pygame.mixer.music.load("115.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_133():
    str1.set("மி")
    tts = gTTS(text= "மி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_133():
    pygame.mixer.music.load("116.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_134():
    str1.set("மீ")
    tts = gTTS(text= "மீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_134():
    pygame.mixer.music.load("117.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_135():
    str1.set("மு")
    tts = gTTS(text= "மு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_135():
    pygame.mixer.music.load("118.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_136():
    str1.set("மூ")
    tts = gTTS(text= "மூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_136():
    pygame.mixer.music.load("119.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_137():
    str1.set("மெ")
    tts = gTTS(text= "மெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_137():
    pygame.mixer.music.load("120.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_138():
    str1.set("மே")
    tts = gTTS(text= "மே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_138():
    pygame.mixer.music.load("121.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_139():
    str1.set("மை")
    tts = gTTS(text= "மை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_139():
    pygame.mixer.music.load("122.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_140():
    str1.set("மொ")
    tts = gTTS(text= "மொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_140():
    pygame.mixer.music.load("123.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_141():
    str1.set("மோ")
    tts = gTTS(text= "மோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_141():
    pygame.mixer.music.load("124.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_142():
    str1.set("மௌ")
    tts = gTTS(text= "மௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_142():
    pygame.mixer.music.load("125.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_143():
    str1.set("ம்")
    tts = gTTS(text= "ம்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_143():
    pygame.mixer.music.load("126.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_144():
    str1.set("ய")
    tts = gTTS(text= "ய" , lang ='ta')
    pygame.mixer.init()
def Alphabet_144():
    pygame.mixer.music.load("127.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_145():
    str1.set("யா")
    tts = gTTS(text= "யா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_145():
    pygame.mixer.music.load("128.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_146():
    str1.set("யி")
    tts = gTTS(text= "யி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_146():
    pygame.mixer.music.load("129.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_147():
    str1.set("யீ")
    tts = gTTS(text= "யீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_147():
    pygame.mixer.music.load("130.mp3")
    pygame.mixer.music.play(loops=0)
    
def Alphabet_148():
    str1.set("யு")
    tts = gTTS(text= "யு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_148():
    pygame.mixer.music.load("131.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_149():
    str1.set("யூ")
    tts = gTTS(text= "யூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_149():
    pygame.mixer.music.load("132.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_150():
    str1.set("யெ")
    tts = gTTS(text= "யெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_150():
    pygame.mixer.music.load("133.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_151():
    str1.set("யே")
    tts = gTTS(text= "யே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_151():
    pygame.mixer.music.load("134.mp3")
    pygame.mixer.music.play(loops=0)

    
def Alphabet_152():
    str1.set("யை")
    tts = gTTS(text= "யை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_152():
    pygame.mixer.music.load("135.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_153():
    str1.set("யொ")
    tts = gTTS(text= "யொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_153():
    pygame.mixer.music.load("136.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_154():
    str1.set("யோ")
    tts = gTTS(text= "யோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_154():
    pygame.mixer.music.load("137.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_155():
    str1.set("யௌ")
    tts = gTTS(text= "யௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_155():
    pygame.mixer.music.load("138.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_156():
    str1.set("ய்")
    tts = gTTS(text= "ய்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_156():
    pygame.mixer.music.load("139.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_157():
    str1.set("ர")
    tts = gTTS(text= "ர" , lang ='ta')
    pygame.mixer.init()
def Alphabet_157():
    pygame.mixer.music.load("140.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_158():
    str1.set("ரா")
    tts = gTTS(text= "ரா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_158():
    pygame.mixer.music.load("141.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_159():
    str1.set("ரி")
    tts = gTTS(text= "ரி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_159():
    pygame.mixer.music.load("142.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_160():
    str1.set("ரீ")
    tts = gTTS(text= "ரீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_160():
    pygame.mixer.music.load("143.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_161():
    str1.set("ரு")
    tts = gTTS(text= "ரு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_161():
    pygame.mixer.music.load("144.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_162():
    str1.set("ரூ")
    tts = gTTS(text= "ரூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_162():
    pygame.mixer.music.load("145.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_163():
    str1.set("ரெ")
    tts = gTTS(text= "ரெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_163():
    pygame.mixer.music.load("146.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_164():
    str1.set("ரே")
    tts = gTTS(text= "ரே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_164():
    pygame.mixer.music.load("147.mp3")
    pygame.mixer.music.play(loops=0)

    

def Alphabet_165():
    str1.set("ரை")
    tts = gTTS(text= "ரை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_165():
    pygame.mixer.music.load("148.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_166():
    str1.set("ரொ")
    tts = gTTS(text= "ரொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_166():
    pygame.mixer.music.load("149.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_167():
    str1.set("ரோ")
    tts = gTTS(text= "ரோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_167():
    pygame.mixer.music.load("150.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_168():
    str1.set("ரௌ")
    tts = gTTS(text= "ரௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_168():
    pygame.mixer.music.load("151.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_169():
    str1.set("ர்")
    tts = gTTS(text= "ர்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_169():
    pygame.mixer.music.load("ர்.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_170():
    str1.set("ல")
    tts = gTTS(text= "ல" , lang ='ta')
    pygame.mixer.init()
def Alphabet_170():
    pygame.mixer.music.load("153.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_171():
    str1.set("லா")
    tts = gTTS(text= "லா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_171():
    pygame.mixer.music.load("laa.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_172():
    str1.set("லி")
    tts = gTTS(text= "லி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_172():
    pygame.mixer.music.load("154.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_173():
    str1.set("லீ")
    tts = gTTS(text= "லீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_173():
    pygame.mixer.music.load("155.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_174():
    str1.set("லு")
    tts = gTTS(text= "லு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_174():
    pygame.mixer.music.load("156.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_175():
    str1.set("லூ")
    tts = gTTS(text= "லூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_175():
    pygame.mixer.music.load("157.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_176():
    str1.set("லெ")
    tts = gTTS(text= "லெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_176():
    pygame.mixer.music.load("158.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_177():
    str1.set("லே")
    tts = gTTS(text= "லே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_177():
    pygame.mixer.music.load("159.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_178():
    str1.set("லை")
    tts = gTTS(text= "லை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_178():
    pygame.mixer.music.load("160.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_179():
    str1.set("லொ")
    tts = gTTS(text= "லொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_179():
    pygame.mixer.music.load("161.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_180():
    str1.set("லோ")
    tts = gTTS(text= "லோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_180():
    pygame.mixer.music.load("162.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_181():
    str1.set("லௌ")
    tts = gTTS(text= "லௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_181():
    pygame.mixer.music.load("163.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_182():
    str1.set("ல்")
    tts = gTTS(text= "ல்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_182():
    pygame.mixer.music.load("164.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_183():
    str1.set("வ")
    tts = gTTS(text= "வ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_183():
    pygame.mixer.music.load("165.mp3")
    pygame.mixer.music.play(loops=0)
    
def Alphabet_184():
    str1.set("வா")
    tts = gTTS(text= "வா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_184():
    pygame.mixer.music.load("166.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_185():
    str1.set("வி")
    tts = gTTS(text= "வி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_185():
    pygame.mixer.music.load("167.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_186():
    str1.set("வீ")
    tts = gTTS(text= "வீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_186():
    pygame.mixer.music.load("168.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_187():
    str1.set("வு")
    tts = gTTS(text= "வு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_187():
    pygame.mixer.music.load("169.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_188():
    str1.set("வூ")
    tts = gTTS(text= "வூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_188():
    pygame.mixer.music.load("170.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_189():
    str1.set("வெ")
    tts = gTTS(text= "வெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_189():
    pygame.mixer.music.load("171.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_190():
    str1.set("வே")
    tts = gTTS(text= "வே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_190():
    pygame.mixer.music.load("172.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_191():
    str1.set("வை")
    tts = gTTS(text= "வை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_191():
    pygame.mixer.music.load("173.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_192():
    str1.set("வொ")
    tts = gTTS(text= "வொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_192():
    pygame.mixer.music.load("174.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_193():
    str1.set("வோ")
    tts = gTTS(text= "வோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_193():
    pygame.mixer.music.load("175.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_194():
    str1.set("வௌ")
    tts = gTTS(text= "வௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_194():
    pygame.mixer.music.load("176.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_195():
    str1.set("வ்")
    tts = gTTS(text= "வ்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_195():
    pygame.mixer.music.load("177.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_196():
    str1.set("ழ")
    tts = gTTS(text= "ழ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_196():
    pygame.mixer.music.load("180.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_197():
    str1.set("ழா")
    tts = gTTS(text= "ழா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_197():
    pygame.mixer.music.load("181.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_198():
    str1.set("ழி")
    tts = gTTS(text= "ழி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_198():
    pygame.mixer.music.load("182.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_199():
    str1.set("ழீ")
    tts = gTTS(text= "ழீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_199():
    pygame.mixer.music.load("183.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_200():
    str1.set("ழு")
    tts = gTTS(text= "ழு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_200():
    pygame.mixer.music.load("184.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_201():
    str1.set("ழூ")
    tts = gTTS(text= "ழூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_201():
    pygame.mixer.music.load("185.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_202():
    str1.set("ழெ")
    tts = gTTS(text= "ழெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_202():
    pygame.mixer.music.load("186.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_203():
    str1.set("ழே")
    tts = gTTS(text= "ழே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_203():
    pygame.mixer.music.load("187.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_204():
    str1.set("ழை")
    tts = gTTS(text= "ழை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_204():
    pygame.mixer.music.load("188.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_205():
    str1.set("ழொ")
    tts = gTTS(text= "ழொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_205():
    pygame.mixer.music.load("189.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_206():
    str1.set("ழோ")
    tts = gTTS(text= "ழோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_206():
    pygame.mixer.music.load("190.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_207():
    str1.set("ழௌ")
    tts = gTTS(text= "ழௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_207():
    pygame.mixer.music.load("191.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_208():
    str1.set("ழ்")
    tts = gTTS(text= "ழ்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_208():
    pygame.mixer.music.load("192.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_209():
    str1.set("ள")
    tts = gTTS(text= "ள" , lang ='ta')
    pygame.mixer.init()
def Alphabet_209():
    pygame.mixer.music.load("193.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_210():
    str1.set("ளா")
    tts = gTTS(text= "ளா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_210():
    pygame.mixer.music.load("194.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_211():
    str1.set("ளி")
    tts = gTTS(text= "ளி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_211():
    pygame.mixer.music.load("195.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_212():
    str1.set("ளீ")
    tts = gTTS(text= "ளீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_212():
    pygame.mixer.music.load("196.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_213():
    str1.set("ளு")
    tts = gTTS(text= "ளு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_213():
    pygame.mixer.music.load("197.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_214():
    str1.set("ளூ")
    tts = gTTS(text= "ளூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_214():
    pygame.mixer.music.load("198.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_215():
    str1.set("ளெ")
    tts = gTTS(text= "ளெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_215():
    pygame.mixer.music.load("199.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_216():
    str1.set("ளே")
    tts = gTTS(text= "ளே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_216():
    pygame.mixer.music.load("200.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_217():
    str1.set("ளை")
    tts = gTTS(text= "ளை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_217():
    pygame.mixer.music.load("201.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_218():
    str1.set("ளொ")
    tts = gTTS(text= "ளொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_218():
    pygame.mixer.music.load("202.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_219():
    str1.set("ளோ")
    tts = gTTS(text= "ளோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_219():
    pygame.mixer.music.load("203.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_220():
    str1.set("ளௌ")
    tts = gTTS(text= "ளௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_220():
    pygame.mixer.music.load("204.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_221():
    str1.set("ள்")
    tts = gTTS(text= "ள்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_221():
    pygame.mixer.music.load("205.mp3")
    pygame.mixer.music.play(loops=0)
    
def Alphabet_222():
    str1.set("ற")
    tts = gTTS(text= "ற" , lang ='ta')
    pygame.mixer.init()
def Alphabet_222():
    pygame.mixer.music.load("206.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_223():
    str1.set("றா")
    tts = gTTS(text= "றா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_223():
    pygame.mixer.music.load("207.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_224():
    str1.set("றி")
    tts = gTTS(text= "றி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_224():
    pygame.mixer.music.load("208.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_225():
    str1.set("றீ")
    tts = gTTS(text= "றீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_225():
    pygame.mixer.music.load("209.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_226():
    str1.set("று")
    tts = gTTS(text= "று" , lang ='ta')
    pygame.mixer.init()
def Alphabet_226():
    pygame.mixer.music.load("210.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_227():
    str1.set("றூ")
    tts = gTTS(text= "றூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_227():
    pygame.mixer.music.load("211.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_228():
    str1.set("றெ")
    tts = gTTS(text= "றெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_228():
    pygame.mixer.music.load("212.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_229():
    str1.set("றே")
    tts = gTTS(text= "றே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_229():
    pygame.mixer.music.load("213.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_230():
    str1.set("றை")
    tts = gTTS(text= "றை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_230():
    pygame.mixer.music.load("214.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_231():
    str1.set("றொ")
    tts = gTTS(text= "றொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_231():
    pygame.mixer.music.load("215.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_232():
    str1.set("றோ")
    tts = gTTS(text= "றோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_232():
    pygame.mixer.music.load("216.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_233():
    str1.set("றௌ")
    tts = gTTS(text= "றௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_233():
    pygame.mixer.music.load("217.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_234():
    str1.set("ற்")
    tts = gTTS(text= "ற்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_234():
    pygame.mixer.music.load("218.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_235():
    str1.set("ன")
    tts = gTTS(text= "ன" , lang ='ta')
    pygame.mixer.init()
def Alphabet_235():
    pygame.mixer.music.load("219.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_236():
    str1.set("னா")
    tts = gTTS(text= "னா" , lang ='ta')
    pygame.mixer.init()
def Alphabet_236():
    pygame.mixer.music.load("220.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_237():
    str1.set("னி")
    tts = gTTS(text= "னி" , lang ='ta')
    pygame.mixer.init()
def Alphabet_237():
    pygame.mixer.music.load("221.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_238():
    str1.set("னீ")
    tts = gTTS(text= "னீ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_238():
    pygame.mixer.music.load("222.mp3")
    pygame.mixer.music.play(loops=0)
    

def Alphabet_239():
    str1.set("னு")
    tts = gTTS(text= "னு" , lang ='ta')
    pygame.mixer.init()
def Alphabet_239():
    pygame.mixer.music.load("223.mp3")
    pygame.mixer.music.play(loops=0)



def Alphabet_240():
    str1.set("னூ")
    tts = gTTS(text= "னூ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_240():
    pygame.mixer.music.load("224.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_241():
    str1.set("னெ")
    tts = gTTS(text= "னெ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_241():
    pygame.mixer.music.load("225.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_242():
    str1.set("னே")
    tts = gTTS(text= "னே" , lang ='ta')
    pygame.mixer.init()
def Alphabet_242():
    pygame.mixer.music.load("226.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_243():
    str1.set("னை")
    tts = gTTS(text= "னை" , lang ='ta')
    pygame.mixer.init()
def Alphabet_243():
    pygame.mixer.music.load("227.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_244():
    str1.set("னொ")
    tts = gTTS(text= "னொ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_244():
    pygame.mixer.music.load("228.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_245():
    str1.set("னோ")
    tts = gTTS(text= "னோ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_245():
    pygame.mixer.music.load("229.mp3")
    pygame.mixer.music.play(loops=0)


def Alphabet_246():
    str1.set("னௌ")
    tts = gTTS(text= "னௌ" , lang ='ta')
    pygame.mixer.init()
def Alphabet_246():
    pygame.mixer.music.load("230.mp3")
    pygame.mixer.music.play(loops=0)

def Alphabet_247():
    str1.set("ன்")
    tts = gTTS(text= "ன்" , lang ='ta')
    pygame.mixer.init()
def Alphabet_247():
    pygame.mixer.music.load("ன்.mp3")
    pygame.mixer.music.play(loops=0)

    
txtDisplay=Entry(ABC,textvariable=str1, font=('arial', 20, 'bold'), bg="powder blue", bd=30, width=30, justify=CENTER)
txtDisplay.grid(row=0,column=1,columnspan=18,pady=1)
btn1 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஃ", command=Alphabet_1 ).grid(row=1, column=2)
btn2 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="அ", command=Alphabet_2).grid(row=2, column=2)
btn3 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஆ", command=Alphabet_3 ).grid(row=3, column=2)
btn4 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="இ", command=Alphabet_4).grid(row=4, column=2)
btn5 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஈ", command=Alphabet_5 ).grid(row=5, column=2)
btn6 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="உ", command=Alphabet_6 ).grid(row=6, column=2)
btn7 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஊ", command=Alphabet_7).grid(row=7, column=2)
btn8 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="எ", command=Alphabet_8 ).grid(row=8, column=2)
btn9 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஏ", command=Alphabet_9 ).grid(row=9, column=2)
btn10 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஐ", command=Alphabet_10 ).grid(row=10, column=2)
btn11 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஒ", command=Alphabet_11).grid(row=11, column=2)
btn12 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஓ", command=Alphabet_12).grid(row=12, column=2)
btn13 = Button (ABC, pady=1, background="red", font=('arial', 14, 'bold'), width=5, height=1, text="ஔ", command=Alphabet_13).grid(row=13, column=2)
btn14 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="க்", command=Alphabet_14 ).grid(row=1, column=3)
btn15 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="க", command=Alphabet_15).grid(row=2, column=3)
btn16 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கா", command=Alphabet_16 ).grid(row=3, column=3)
btn17 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கி", command=Alphabet_17).grid(row=4, column=3)
btn18 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கீ", command=Alphabet_18).grid(row=5, column=3)
btn19 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கு", command=Alphabet_19 ).grid(row=6, column=3)
btn20 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கூ", command=Alphabet_20).grid(row=7, column=3)
btn21 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கெ", command=Alphabet_21 ).grid(row=8, column=3)
btn22 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கே", command=Alphabet_22 ).grid(row=9, column=3)
btn23 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கை", command=Alphabet_23 ).grid(row=10, column=3)
btn24 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கொ", command=Alphabet_24 ).grid(row=11, column=3)
btn25 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கோ", command=Alphabet_25 ).grid(row=12, column=3)
btn26 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="கௌ", command=Alphabet_26 ).grid(row=13, column=3)
btn27 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ங்", command=Alphabet_27 ).grid(row=1, column=4)
btn28 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ங", command=Alphabet_28).grid(row=2, column=4)
btn29 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙா", command=Alphabet_29 ).grid(row=3, column=4)
btn30 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙி", command=Alphabet_30).grid(row=4, column=4)
btn31 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙீ", command=Alphabet_31 ).grid(row=5, column=4)
btn32 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙு", command=Alphabet_32 ).grid(row=6, column=4)
btn33 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙூ", command=Alphabet_33).grid(row=7, column=4)
btn34 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙெ", command=Alphabet_34 ).grid(row=8, column=4)
btn35 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙே", command=Alphabet_35 ).grid(row=9, column=4)
btn36 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙை", command=Alphabet_36 ).grid(row=10, column=4)
btn37 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙொ", command=Alphabet_37).grid(row=11, column=4)
btn38 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙோ", command=Alphabet_38).grid(row=12, column=4)
btn39 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஙௌ", command=Alphabet_39).grid(row=13, column=4)
btn40 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ச்", command=Alphabet_40 ).grid(row=1, column=5)
btn41 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ச", command=Alphabet_41).grid(row=2, column=5)
btn42 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சா", command=Alphabet_42 ).grid(row=3, column=5)
btn43 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சி", command=Alphabet_43).grid(row=4, column=5)
btn44 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சீ", command=Alphabet_44 ).grid(row=5, column=5)
btn45 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சு", command=Alphabet_45 ).grid(row=6, column=5)
btn46 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சூ", command=Alphabet_46).grid(row=7, column=5)
btn47 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="செ", command=Alphabet_47 ).grid(row=8, column=5)
btn48 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சே", command=Alphabet_48 ).grid(row=9, column=5)
btn49 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சை", command=Alphabet_49 ).grid(row=10, column=5)
btn50 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சொ", command=Alphabet_50).grid(row=11, column=5)
btn51 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சோ", command=Alphabet_51).grid(row=12, column=5)
btn52 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="சௌ", command=Alphabet_52).grid(row=13, column=5)
btn53 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ஞ்", command=Alphabet_53 ).grid(row=1, column=6)
btn54 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞ", command=Alphabet_54).grid(row=2, column=6)
btn55 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞா", command=Alphabet_55 ).grid(row=3, column=6)
btn56 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞி", command=Alphabet_56).grid(row=4, column=6)
btn57 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞீ", command=Alphabet_57 ).grid(row=5, column=6)
btn58 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞு", command=Alphabet_58 ).grid(row=6, column=6)
btn59 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞூ", command=Alphabet_59).grid(row=7, column=6)
btn60 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞெ", command=Alphabet_60 ).grid(row=8, column=6)
btn61 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞே", command=Alphabet_61 ).grid(row=9, column=6)
btn62 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞை", command=Alphabet_62).grid(row=10, column=6)
btn63 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞொ", command=Alphabet_63).grid(row=11, column=6)
btn64 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞோ", command=Alphabet_64).grid(row=12, column=6)
btn65 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ஞௌ", command=Alphabet_65).grid(row=13, column=6)
btn66 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ட்", command=Alphabet_66 ).grid(row=1, column=7)
btn67 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ட", command=Alphabet_67).grid(row=2, column=7)
btn68 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டா", command=Alphabet_68 ).grid(row=3, column=7)
btn69 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டி", command=Alphabet_69).grid(row=4, column=7)
btn70 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டீ", command=Alphabet_70 ).grid(row=5, column=7)
btn71 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டு", command=Alphabet_71 ).grid(row=6, column=7)
btn72 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டூ", command=Alphabet_72).grid(row=7, column=7)
btn73 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டெ", command=Alphabet_73 ).grid(row=8, column=7)
btn74 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டே", command=Alphabet_74 ).grid(row=9, column=7)
btn75 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டை", command=Alphabet_75 ).grid(row=10, column=7)
btn76 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டொ", command=Alphabet_76).grid(row=11, column=7)
btn77 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டோ", command=Alphabet_77).grid(row=12, column=7)
btn78 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="டௌ", command=Alphabet_78).grid(row=13, column=7)
btn79 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ண்", command=Alphabet_79 ).grid(row=1, column=8)
btn80 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ண", command=Alphabet_80).grid(row=2, column=8)
btn81 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணா", command=Alphabet_81 ).grid(row=3, column=8)
btn82 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணி", command=Alphabet_82).grid(row=4, column=8)
btn83 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணீ", command=Alphabet_83 ).grid(row=5, column=8)
btn84 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணு", command=Alphabet_84 ).grid(row=6, column=8)
btn85 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணூ", command=Alphabet_85).grid(row=7, column=8)
btn86 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணெ", command=Alphabet_86 ).grid(row=8, column=8)
btn87 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணே", command=Alphabet_87).grid(row=9, column=8)
btn88 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணை", command=Alphabet_88 ).grid(row=10, column=8)
btn89 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணொ", command=Alphabet_89).grid(row=11, column=8)
btn90 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணோ", command=Alphabet_90).grid(row=12, column=8)
btn91 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ணௌ", command=Alphabet_91).grid(row=13, column=8)
btn92 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="த", command=Alphabet_93).grid(row=2, column=9)
btn93 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="த்", command=Alphabet_92 ).grid(row=1, column=9)
btn94 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தா", command=Alphabet_94 ).grid(row=3, column=9)
btn95 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தி", command=Alphabet_95).grid(row=4, column=9)
btn96 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தீ", command=Alphabet_96 ).grid(row=5, column=9)
btn97 = Button (ABC, pady=1, background="yellow", font=('arial', 14 ,'bold'), width=5, height=1, text="து", command=Alphabet_97 ).grid(row=6, column=9)
btn98 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தூ", command=Alphabet_98).grid(row=7, column=9)
btn99 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தெ", command=Alphabet_99 ).grid(row=8, column=9)
btn100 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தே", command=Alphabet_100).grid(row=9, column=9)
btn101 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தை", command=Alphabet_101 ).grid(row=10, column=9)
btn102 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தொ", command=Alphabet_102).grid(row=11, column=9)
btn103 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தோ", command=Alphabet_103).grid(row=12, column=9)
btn104 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="தௌ", command=Alphabet_104).grid(row=13, column=9)
btn105 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ந்", command=Alphabet_105 ).grid(row=1, column=10)
btn106 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ந", command=Alphabet_106).grid(row=2, column=10)
btn107 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நா", command=Alphabet_107 ).grid(row=3, column=10)
btn108 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நி", command=Alphabet_108).grid(row=4, column=10)
btn109 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நீ", command=Alphabet_109 ).grid(row=5, column=10)
btn110 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நு", command=Alphabet_110 ).grid(row=6, column=10)
btn111 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நூ", command=Alphabet_111).grid(row=7, column=10)
btn112 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நெ", command=Alphabet_112 ).grid(row=8, column=10)
btn113 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நே", command=Alphabet_113 ).grid(row=9, column=10)
btn114 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நை", command=Alphabet_114 ).grid(row=10, column=10)
btn115 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நொ", command=Alphabet_115).grid(row=11, column=10)
btn116 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நோ", command=Alphabet_116).grid(row=12, column=10)
btn117 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="நௌ", command=Alphabet_117).grid(row=13, column=10)
btn118 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ப", command=Alphabet_118).grid(row=2, column=11)
btn119 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பா", command=Alphabet_119 ).grid(row=3, column=11)
btn120 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பி", command=Alphabet_120).grid(row=4, column=11)
btn121 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பீ", command=Alphabet_121 ).grid(row=5, column=11)
btn122 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பு", command=Alphabet_122 ).grid(row=6, column=11)
btn123 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பூ", command=Alphabet_123).grid(row=7, column=11)
btn124 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பெ", command=Alphabet_124 ).grid(row=8, column=11)
btn125 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பே", command=Alphabet_125 ).grid(row=9, column=11)
btn126 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பை", command=Alphabet_126 ).grid(row=10, column=11)
btn127 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பொ", command=Alphabet_127).grid(row=11, column=11)
btn128 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="போ", command=Alphabet_128).grid(row=12, column=11)
btn129 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="பௌ", command=Alphabet_129).grid(row=13, column=11)
btn130 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ப்", command=Alphabet_130 ).grid(row=1, column=11)
btn131 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ம", command=Alphabet_131).grid(row=2, column=12)
btn132 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மா", command=Alphabet_132 ).grid(row=3, column=12)
btn133 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மி", command=Alphabet_133).grid(row=4, column=12)
btn134 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மீ", command=Alphabet_134 ).grid(row=5, column=12)
btn135 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மு", command=Alphabet_135 ).grid(row=6, column=12)
btn136 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மூ", command=Alphabet_136).grid(row=7, column=12)
btn137 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மெ", command=Alphabet_137 ).grid(row=8, column=12)
btn138 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மே", command=Alphabet_138 ).grid(row=9, column=12)
btn139 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மை", command=Alphabet_139 ).grid(row=10, column=12)
btn140 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மொ", command=Alphabet_140).grid(row=11, column=12)
btn141 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="மோ", command=Alphabet_141).grid(row=12, column=12)
btn142= Button (ABC, pady=1, background="yellow", font=('arial', 14 ,'bold'), width=5, height=1, text="மௌ", command=Alphabet_142).grid(row=13, column=12)
btn143 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ம்", command=Alphabet_143 ).grid(row=1, column=12)
btn144 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ய", command=Alphabet_144).grid(row=2, column=13)
btn145 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யா", command=Alphabet_145 ).grid(row=3, column=13)
btn146 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யி", command=Alphabet_146).grid(row=4, column=13)
btn147 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யீ", command=Alphabet_147 ).grid(row=5, column=13)
btn148 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யு", command=Alphabet_148 ).grid(row=6, column=13)
btn149 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யூ", command=Alphabet_149).grid(row=7, column=13)
btn150 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யெ", command=Alphabet_150 ).grid(row=8, column=13)
btn151 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யே", command=Alphabet_151 ).grid(row=9, column=13)
btn152 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யை", command=Alphabet_152 ).grid(row=10, column=13)
btn153 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யொ", command=Alphabet_153).grid(row=11, column=13)
btn154 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யோ", command=Alphabet_154).grid(row=12, column=13)
btn155 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="யௌ", command=Alphabet_155).grid(row=13, column=13)
btn156 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ய்", command=Alphabet_156 ).grid(row=1, column=13)
btn157 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ர", command=Alphabet_157).grid(row=2, column=14)
btn158 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரா", command=Alphabet_158 ).grid(row=3, column=14)
btn159 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரி", command=Alphabet_159).grid(row=4, column=14)
btn160 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரீ", command=Alphabet_160 ).grid(row=5, column=14)
btn161 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரு", command=Alphabet_161 ).grid(row=6, column=14)
btn162 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரூ", command=Alphabet_162).grid(row=7, column=14)
btn163 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரெ", command=Alphabet_163 ).grid(row=8, column=14)
btn164= Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரே", command=Alphabet_164).grid(row=9, column=14)
btn165 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரை", command=Alphabet_165 ).grid(row=10, column=14)
btn166= Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரொ", command=Alphabet_166).grid(row=11, column=14)
btn167 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ரோ", command=Alphabet_167).grid(row=12, column=14)
btn168= Button (ABC, pady=1, background="yellow", font=('arial', 14 ,'bold'), width=5, height=1, text="ரௌ", command=Alphabet_168).grid(row=13, column=14)
btn169 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ர்", command=Alphabet_169 ).grid(row=1, column=14)
btn170 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ல", command=Alphabet_170).grid(row=2, column=15)
btn171 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லா", command=Alphabet_171 ).grid(row=3, column=15)
btn172 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லி", command=Alphabet_172).grid(row=4, column=15)
btn173 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லீ", command=Alphabet_173 ).grid(row=5, column=15)
btn174 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லு", command=Alphabet_174 ).grid(row=6, column=15)
btn175 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லூ", command=Alphabet_175).grid(row=7, column=15)
btn176 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லெ", command=Alphabet_176 ).grid(row=8, column=15)
btn177 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லே", command=Alphabet_177 ).grid(row=9, column=15)
btn178 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லை", command=Alphabet_178 ).grid(row=10, column=15)
btn179 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லொ", command=Alphabet_179).grid(row=11, column=15)
btn180 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லோ", command=Alphabet_180).grid(row=12, column=15)
btn181 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="லௌ", command=Alphabet_181).grid(row=13, column=15)
btn182 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ல்", command=Alphabet_182 ).grid(row=1, column=15)
btn183 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வ", command=Alphabet_183).grid(row=2, column=16)
btn184 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வா", command=Alphabet_184 ).grid(row=3, column=16)
btn185 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வி", command=Alphabet_185).grid(row=4, column=16)
btn186 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வீ", command=Alphabet_186 ).grid(row=5, column=16)
btn187 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வு", command=Alphabet_187 ).grid(row=6, column=16)
btn188 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வூ", command=Alphabet_188).grid(row=7, column=16)
btn189 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வெ", command=Alphabet_189 ).grid(row=8, column=16)
btn190 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வே", command=Alphabet_190 ).grid(row=9, column=16)
btn191 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வை", command=Alphabet_191 ).grid(row=10, column=16)
btn192 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வொ", command=Alphabet_192).grid(row=11, column=16)
btn193 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வோ", command=Alphabet_193).grid(row=12, column=16)
btn194 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="வௌ", command=Alphabet_194).grid(row=13, column=16)
btn195 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="வ்", command=Alphabet_195 ).grid(row=1, column=16)
btn196 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழ", command=Alphabet_196).grid(row=2, column=17)
btn197 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழா", command=Alphabet_197 ).grid(row=3, column=17)
btn198 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழி", command=Alphabet_198).grid(row=4, column=17)
btn199 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழீ", command=Alphabet_199).grid(row=5, column=17)
btn200 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழு", command=Alphabet_200 ).grid(row=6, column=17)
btn201 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழூ", command=Alphabet_201).grid(row=7, column=17)
btn202 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழெ", command=Alphabet_202 ).grid(row=8, column=17)
btn203 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழே", command=Alphabet_203 ).grid(row=9, column=17)
btn204 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழை", command=Alphabet_204 ).grid(row=10, column=17)
btn205 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழொ", command=Alphabet_205).grid(row=11, column=17)
btn206 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழோ", command=Alphabet_206).grid(row=12, column=17)
btn207 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ழௌ", command=Alphabet_207).grid(row=13, column=17)
btn208 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ழ்", command=Alphabet_208).grid(row=1, column=17)
btn209 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ள", command=Alphabet_209).grid(row=2, column=18)
btn210 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளா", command=Alphabet_210 ).grid(row=3, column=18)
btn211 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளி", command=Alphabet_211).grid(row=4, column=18)
btn212 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளீ", command=Alphabet_212 ).grid(row=5, column=18)
btn213 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளு", command=Alphabet_213 ).grid(row=6, column=18)
btn214 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளூ", command=Alphabet_214).grid(row=7, column=18)
btn215 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளெ", command=Alphabet_215 ).grid(row=8, column=18)
btn216 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளே", command=Alphabet_216).grid(row=9, column=18)
btn217 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளை", command=Alphabet_217 ).grid(row=10, column=18)
btn218 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளொ", command=Alphabet_218).grid(row=11, column=18)
btn219 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளோ", command=Alphabet_219).grid(row=12, column=18)
btn220 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ளௌ", command=Alphabet_220).grid(row=13, column=18)
btn221 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ள்", command=Alphabet_221 ).grid(row=1, column=18)
btn222 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ற", command=Alphabet_222).grid(row=2, column=19)
btn223 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றா", command=Alphabet_223 ).grid(row=3, column=19)
btn224 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றி", command=Alphabet_224).grid(row=4, column=19)
btn225 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றீ", command=Alphabet_225).grid(row=5, column=19)
btn226 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="று", command=Alphabet_226 ).grid(row=6, column=19)
btn227 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றூ", command=Alphabet_227).grid(row=7, column=19)
btn228 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றெ", command=Alphabet_228 ).grid(row=8, column=19)
btn229 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றே", command=Alphabet_229).grid(row=9, column=19)
btn230 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றை", command=Alphabet_230 ).grid(row=10, column=19)
btn231 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றொ", command=Alphabet_231).grid(row=11, column=19)
btn232 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றோ", command=Alphabet_232).grid(row=12, column=19)
btn233 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="றௌ", command=Alphabet_233).grid(row=13, column=19)
btn234 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ற்", command=Alphabet_234 ).grid(row=1, column=19)
btn235 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="ன", command=Alphabet_235).grid(row=2, column=50)
btn236 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னா", command=Alphabet_236 ).grid(row=3, column=50)
btn237 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னி", command=Alphabet_237).grid(row=4, column=50)
btn238 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னீ", command=Alphabet_238 ).grid(row=5, column=50)
btn239 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னு", command=Alphabet_239 ).grid(row=6, column=50)
btn240 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னூ", command=Alphabet_240).grid(row=7, column=50)
btn241 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னெ", command=Alphabet_241 ).grid(row=8, column=50)
btn242 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னே", command=Alphabet_242 ).grid(row=9, column=50)
btn243 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னை", command=Alphabet_243 ).grid(row=10, column=50)
btn244 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னொ", command=Alphabet_244).grid(row=11, column=50)
btn245 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னோ", command=Alphabet_245).grid(row=12, column=50)
btn246 = Button (ABC, pady=1, background="yellow", font=('arial', 14, 'bold'), width=5, height=1, text="னௌ", command=Alphabet_246).grid(row=13, column=50)
btn247 = Button (ABC, pady=1, background="blue", font=('arial', 14, 'bold'), width=5, height=1, text="ன்", command=Alphabet_247 ).grid(row=1, column=50)

root.mainloop()
