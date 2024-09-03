
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
my_path='D:\\Assignment\\idcard_pdf.pdf'

from tk_id_card_temp import my_temp
from tk_id_input import firstName,lastName,rollNo,Majors,gender,s_filename
c = canvas.Canvas(my_path,pagesize = (500,400))
c = my_temp(c)
c.drawImage(s_filename,3*inch,1*inch)

c.setFillColorRGB(0,0,1)
c.setFont("Helvetica", 20)

c.drawString(0.8*inch,3*inch,firstName.get()) 
c.drawString(0.8*inch,2.5*inch,lastName.get())    
c.drawString(0.3*inch,2.0*inch,str(rollNo.get()))    
c.drawString(0.3*inch,1.5*inch,Majors.get())
c.drawString(0.3*inch,1.0*inch,gender.get()) 


c.showPage()
c.save()
