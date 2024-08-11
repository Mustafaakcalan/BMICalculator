import tkinter

screen = tkinter.Tk()
screen.title("BMI Calculator")
screen.config(padx=30,pady=30)
screen.minsize(width=189,
               height=185)
def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()
    if weight == "" or height == "":
        result_label.config(text="Boş alan bırakmayınız")
    else:
        try:
            bmi = float(weight) / ((float(height) /100) **2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Düzgün bir sayı giriniz")

def write_result(bmi):
    result_string = f"Vücut kitle indeksiniz {round(bmi,2)}. Sonuç : "
    if bmi <=16:
        result_string += "Çok zayıf"
    elif 16 < bmi <= 18.5:
        result_string += "Zayıf"
    elif 18.5 < bmi <=25:
        result_string += "Sağlıklı"
    elif 25 < bmi <= 30:
        result_string += "Şişman"
    elif 30 < bmi :
        result_string += "Çok şişman (obez)"
    return result_string



weight_input_label = tkinter.Label(text="Kilonuzu girin")
weight_input_label.pack()
weight_input = tkinter.Entry(width="10")
weight_input.pack()

height_input_label = tkinter.Label(text="Boyunuzu girin")
height_input_label.pack()
height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text='Calculate', command=calculate_bmi)
calculate_button.pack()
result_label = tkinter.Label()
result_label.pack()


screen.mainloop()
