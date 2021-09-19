from fpdf import FPDF  # fpdf class
import random
import string
def random_string(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
def generar_pdf(carrera, titulo, curso, semestre, alumnos):
    pdf = FPDF()  # pdf object
    pdf.add_page()
    
    # Dimensiones de un pdf A4
    pdf_w = 210
    pdf_h = 297
    pdf.set_y(20.0)
    pdf.image('./generador/assets/logo.png', x=pdf_w/3)
    pdf.set_font(family='Arial', size=18)
    pdf.cell(w=0, h=40.0, txt=carrera.upper(), border=0, align='C')
    pdf.set_y(80.0)
    pdf.cell(w=0, h=40.0, txt=titulo.upper(), border=0, align='C')
    pdf.set_y(95.0)
    pdf.cell(w=0, h=40.0, txt=curso.upper(), border=0, align='C')
    pdf.set_xy(pdf_w/2, 125.5)
    tempheigth = 125.5
    pdf.set_font(family='Arial', size=16)
    for alumno in alumnos:
        pdf.cell(w=pdf_w/2, h=20.0, txt=alumno, border=0, align='L')
        pdf.set_xy(pdf_w/2,tempheigth+15.0)
        tempheigth = tempheigth+15.0
    pdf.set_xy(pdf_w/2, tempheigth)
    pdf.cell(w=pdf_w/2, h=40.0, txt=semestre, border=0, align='L')
    pdf.set_y(195.5)
    if len(alumnos) != 1:
        pdf.cell(w=0, h=40.0, txt='"Los alumnos declaran haber realizado el presente trabajo de',
                 border=0, align='C')
        pdf.set_y(205.5)
        pdf.cell(w=0, h=40.0, txt='acuerdo a las normas de la Universidad Católica San Pablo."',
                 border=0, align='C')
    else:
        pdf.cell(w=0, h=40.0, txt='"El alumno declara haber realizado el presente trabajo de',
                 border=0, align='C')
        pdf.set_y(205.5)
        pdf.cell(
            w=0, h=40.0, txt='acuerdo a las normas de la Universidad Católica San Pablo."', border=0, align='C')
    count = len(alumnos)
    grosor = 40
    if(count > 4):
        grosor = 30
    elif(count==6):
        grosor=25
    space = (pdf_w-(count*grosor))/(count+1)
    pdf.set_font(family='Arial', size=18)
    for i in range(0, count):
        pdf.line(space*(i+1)+(grosor*i), 250.5,
                 space*(i+1)+(grosor*(i+1)), 250.5)
        pdf.set_xy(space*(i+1)+(grosor*i), 260.5)
        pdf.cell(w=grosor, h=0, txt="FIRMA", border=0, align='C')
    nombre_archivo=random_string(8)
    pdf.output('./generador/pdfs/'+nombre_archivo+".pdf", 'F')
    return nombre_archivo
#generar_pdf("Ciencia de la Computación", "Trabajo final",
#            "Ingenieria de Software III", "7mo semestre", ["Rafael Isaac Cano Guitton", "Jean Carlo Cornejo Cornejo", "Iñigo Manuel Diez Canseco Fuentes"])