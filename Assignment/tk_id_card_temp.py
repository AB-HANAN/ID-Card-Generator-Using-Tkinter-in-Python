from reportlab.lib.units import inch
def my_temp(c):
    c.translate(inch,inch)
    c.setFont("Helvetica" , 14)

    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1)
    c.drawImage('D:\\Assignment\\images\\student(2).jpg',-75,250)

    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 24)
    c.drawRightString(0.8*inch,3*inch,'First Name:')
    c.drawRightString(0.8*inch,2.5*inch,'Last Name:')
    c.drawRightString(0.3*inch,2.0*inch,'Roll No:')
    c.drawRightString(0.3*inch,1.5*inch,'Majors:')
    c.drawRightString(0.3*inch,1.0*inch,'Gender:')


    c.line(-1.1,-0.7*inch,5*inch,-0.7*inch)
    c.setFont("Helvetica",8)
    c.setFillColorRGB(1,0,0)
    c.drawString(0, -0.9*inch, u"\u00A9"+"ABDUL HANAN ASIF")
    
    
    
    
    return c
