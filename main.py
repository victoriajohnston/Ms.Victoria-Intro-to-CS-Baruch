# Ms. Victoria     04/01/2023
# Introduction to Computer Science - Baruch College STEP Academy
# Hands-On Lab Part 2 - QR Code Resume

# Let's import Segno - open-source QR Code generator
import segno
qr_code = segno.make("Ms. Victoria's Resume QR Code")
qr_code.save("Victoria_Resume_QR_Code.png")

# Our QR is now generated and saved in our project directory. 
# Let's add some borders to our QR code for style. 
qr_code.save("Victoria_Resume_QR_Code.png", border = 10)

# Let's make our QR code bigger, since it's a bit small. 
qr_code.save("Victoria_Resume_QR_Code.png", border = 5, scale = 10)

# Time to add some color! 
qr_code.save("Victoria_Resume_QR_Code.png", dark = "purple", light = "lightpink", scale = 10)

# Finally - let's link our resumes to the QR code!
resume = segno.make('https://drive.google.com/file/d/1Mkdk-cbpBtMy7Of3VPIFep1gZXnBBPXc/view?usp=sharing')
resume.save("Victoria_Resume_QR_Code.png", dark = "purple", light = "lightpink", scale = 10)