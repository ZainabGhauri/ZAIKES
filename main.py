# DIP SEMESTER PROJECT 

# CYBER SECURITY APPLICATION
# TITLE : ZAIKES
# IT WILL PROVIDE US WITH THE FUNCTIONS RELATED TO CYBERCRIME LIKE STEGANOGRAPHY , WATERMARKS , THERMAL IMAGE CONVERSION 
# RESTORING AND REPAIRING IMAGES AND LETTERS



#importing library here

from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
import  os
import sys
import numpy as np
import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm
from PIL import ImageFilter
from tkinter import messagebox  

# class Zaiks - that contains all the method.
# 1. Steganography
        # a. Text 
        # b. Image
# 2. Movement Detection
# 3. Water Marking
        # a. Text
        # b. Image
# 4. Thermal Imaging
# 5. Text Restoration
        # a. Letter Restoring
        # b. Letter Repairing
        
class Zaiks:

    # size of the output image
    output_image_size = 0

    # main starts from here
    def main(self,root):
        
        # Setting the config of the root elements
        root.title('Our Cyber Security App')
        root.geometry('500x600')
        root.resizable(width =False, height=False)
        root.configure(bg='#D8E7EA')
        # Creating a frame here
        f = Frame(root)
        image = "C:\\Users\\Pakistan\\images\\first image.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((250, 250))
        img = ImageTk.PhotoImage(myimage)
        panel2 = Label(f, image=img)
        panel2.image = img
        panel2.grid(pady=14)
        
        
        title = Label(f,text='* ZAIKES Security * '   , bg = "#0A0E2C" , fg='#E5FFCC')
        title.config(font=('sans serif',29))
        title.grid(pady=10)

        l = Label(f,text='Zaikes~A Cyber security app \n created by A&Z that helps \n to resolve cases of \n Cyber and criminal \nattacks by processing \n of digital images. '  , font ="ar 19 bold" ,  bg = "#031F25" , fg='#E5FFCC')
        l.config(font=('courier',18))
        l.grid(pady=10)

        
        welcome_code = Button(f,text="Continue",command= lambda :self.welcome_screen1(f), padx=14 , font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
        welcome_code.config(font=('courier',14))
        welcome_code.grid(pady=12)
        
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

        f.grid()
        title.grid(row=1)
        l.grid(row=2)
        welcome_code.grid(row=3)
       
    
    def home(self,frame):
    # destroying the previous created frame
            frame.destroy()
            self.main(root)

    def welcome_screen1(self , f):
        
    # destroying the previous created frame
        f.destroy()
        
    # creating a new frame
        ff = Frame(root)
        
        title = Label(ff,text='* Zaikes Security * '   , bg = "black" , fg='#E5FFCC')
        title.config(font=('sans serif',25))
        title.grid(pady=10)
    # set of all the functions button that will point to their respective screens
        st_code = Button(ff,text="SteganoGraphy",command= lambda :self.steganography_screen1(ff), padx=14 , font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
        st_code.config(font=('courier',14))
        st_code.grid(pady=12)
        sub_code = Button(ff, text="Movement Detection",padx=14,command=lambda :self.frame1_move(ff) , font ="ar 15 bold" ,  bg = "#0A0E2C" , fg='#E5FFCC')
        sub_code.config(font=('courier',14))
        sub_code.grid(pady = 12)
        water_code = Button(ff, text="Water Marking",padx=14,command=lambda :self.frame1_watermark(ff) , font ="ar 15 bold" ,  bg = "#0A0E2C" , fg='#E5FFCC')
        water_code.config(font=('courier',14))
        water_code.grid(pady = 12)
        thermal_code = Button(ff, text="Thermal Imaging",padx=14,command=lambda :self.frame1_thermalImage(ff),font ="ar 15 bold" ,  bg = "#0A0E2C" , fg='#E5FFCC')
        thermal_code.config(font=('courier',14))
        thermal_code.grid(pady = 12)
        contrast_code = Button(ff, text=" Text Restoration ",padx=14,command=lambda :self.welcome_letterRestore(ff) , font ="ar 15 bold" ,  bg = "#0A0E2C" , fg='#E5FFCC')
        contrast_code.config(font=('courier',14))
        contrast_code.grid(pady = 12)
        
        # placing the frame , panels , labels 
        ff.grid()
        title.grid(row=1)
        st_code.grid(row=2)
        sub_code.grid(row=3)
        water_code.grid(row = 4)
        thermal_code.grid( row = 5)
        contrast_code.grid( row=6)
      
    
        image = "C:\\Users\\Pakistan\\images\\second image.jpeg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        panel2 = Label(ff, image=img)
        panel2.image = img
        panel2.grid(pady=14)
      
      
    # steganograohy welcome screen # 1
    # this screen will provide two functions
            # 1. Text SteganoGraphy
            # 2. Image steganoGraphy
            
    def steganography_screen1(self,f):
        f.destroy()
        ff = Frame(root)
        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(ff,text='Steganography - Hiding :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(ff, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(ff,text='Choose the type of steganography \n from the following options:' ,  font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',15))
        l1.grid(pady=14)

        bws_button = Button(ff,text='Text Stegano',command=lambda : self.steg_frame1(ff) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC' )
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=10)
        back_button = Button(ff, text='Image Stegano', command=lambda : self.Image_steg_frame1(ff) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        

        ff.grid()
        
       
    # Movement Detection Screen # 1
    # This screen will Asks you to selects two images
    # And A function that will lead to screen that shows the detected movement between two images
    
    def frame1_move(self , f):
        f.destroy()
        ep= Frame(root)

        messagebox.showinfo("Select"," Select the First Image")  

        # Selects First Image
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='First Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l3.config(font=('courier',18))
            l3.grid(pady=10)
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            
            
        messagebox.showinfo("Select"," Select the Second Image ")
        
        # Selects Second Image here
        myfile2 = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg2 = Image.open(myfile2)
            myimage2 = myimg2.resize((300,200))
            img = ImageTk.PhotoImage(myimage2)
            l4= Label(ep,text=' Second Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid(pady=10)
            panel2 = Label(ep, image=img)
            panel2.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel2.grid()
            back_button = Button(ep, text='Movement Detect', command=lambda : self.detectMove(ep) ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            back_button.config(font=('courier',14))
            back_button.grid(pady=15)
        
            ep.grid(row=1)
              
            # this part will be uncommented if we want to detect movement between any two images
            # calls function - method_movement_det (  myimage1 , myimage2  )
            
            '''
            final_image = self.method_movement_det( myimage1 , myimage2)    
            myimg2 = Image.open(myfile2)
            myimage2 = myimg2.resize((300,200))
            img = ImageTk.PhotoImage(myimage2)
            l4= Label(ep,text=' Final Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid(pady=10)
            panel2 = Label(ep, image=img)
            panel2.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel2.grid()
            ep.grid(row=1)
            '''
            
            
    # Welcome Screen of the Watermarking Module   
    # This will allow you to do :
            # 1. Text WaterMark
            # 2. Image WaterMark
            
            
    def frame1_watermark(self , f):
        f.destroy()
        ff = Frame(root)
        image = "C:\\Users\\Pakistan\\images\\water.jpg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(ff,text='WaterMarking - Confidential :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(ff, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(ff,text='Choose the type of watermarking \n fromthe following options :' ,  font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',15))
        l1.grid(pady=14)

        bws_button = Button(ff,text='Text Watermark',command=lambda : self.textMark_frame1(ff) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC' )
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=10)
        back_button = Button(ff, text='Image Watermark', command=lambda : self.Image_watermark_frame1(ff) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        

        ff.grid()
        
    # Welcome screen of the Thermal Image Conversion Module
    # It will ask you to proceed and select an image for conversion
    # Or asks you to cancel and move to Home Page
         
    def frame1_thermalImage(self,f):
        f.destroy()
        d_f2 = Frame(root)
        
        image = "C:\\Users\\Pakistan\\images\\secs.jpeg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        panel2 = Label(d_f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)
        
        l1 = Label(d_f2, text='Select Image For the\n  Thermal Camera Conversion:'  , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
        l1.config(font=('Arial',18))
        l1.grid(pady = 12)
        bws_button = Button(d_f2, text='Select', command=lambda :self.frame2_thermalImage(d_f2) , font ="ar 15 bold" , bg = "#AF4129" , fg='#DACE16')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=19)
        back_button = Button(d_f2, text='Cancel', command=lambda : Zaiks.home(self,d_f2) ,  font ="ar 15 bold" , bg = "#AF4129" , fg='#DACE16')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()
       
       
    
    # Welcome Screen of the Restoring Module
    # Functions :
            # 1. Restore old Hand Written Letters
            # 2. Repair Broken Letters / Phone Number , Number Plates
            
    def welcome_letterRestore(self , f):
        f.destroy()
        f2 = Frame(root)

        image = "C:\\Users\\Pakistan\\images\\letter.jpg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Text Steganography - Hiding :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Do you want to : \n 1. Restore old Letters \n 2. Repair Letter/Digit ' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Restore Letter',command=lambda : self.welcome_letter_restore(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Repair Letter', command=lambda : self.welcome_letter_repair(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()
        
        
    # --------------- PROPER IMPLEMENTATION OF ALL THE FUNCTIONS IS HERE -------------------------------
    # 1.  thermal
    # 2.  method_movement_det
    # 3.  repair_img
    # 4.  getImageWaterMark  
    # 5.  textmarking  
    # 6.  ClosingLetter  
    # 7.  Image_stegnaography_decryption
    # 8.  Image_stegnaography_encryption


    # This function will give us the thermal image of the given input image
    
    def thermal(self):
        
        
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        
        # get the name of the input image
        image_name = input('Enter the Path of the File you want to Repair  =')
        print(image_name)
        image = cv2.imread(image_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
 
        #initialize the colormap (jet)
        colormap = mpl.cm.jet
        #add a normalization
        cNorm = mpl.colors.Normalize(vmin=0, vmax=255)
        #init the mapping
        scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)
        #in the main display loop:
        colors = scalarMap.to_rgba(gray)
        #Get the Name of the output Image
        output=input('Enter output file name +  path  =')   
        cv2.imwrite(output , colors )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    # This function will give the movement detected between two images
    
    def method_movement_det( myimage1 , myimage2):
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
     
        # get the name of the input image
        image_name = input('Enter the Path of the First Image  =')
        print(image_name)
        image1 = cv2.imread(image_name)
        # get the name of the 2nd - input image
        image_name2 = input('Enter the Path of the Second Image  =')
        print(image_name2)
        image2 = cv2.imread(image_name2)
     
        # Subtracting two Images
        subtracted = cv2.subtract(image2, image1)
        # Converting them to Gray scale
        gray = cv2.cvtColor(subtracted, cv2.COLOR_BGR2GRAY)
        # Thresholding the resultant image
        ret, thresh1 = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
        
        
        # get the name of output image with the Path
        filename =input("Enter path of output image = ")
        cv2.imwrite(filename,thresh1)
        
          
        # To close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
       
    # this function will repair the broken letters / phone numbers etc
    
    def repair_img(self):
        
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        
        # get the name of the input image
        image_name = input('Enter the Path of the File you want to Repair  =')
        print(image_name)
        image = cv2.imread(image_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
        #cv2.imshow('Original image',image)
        #cv2.imshow('Gray image', gray)
        kernel = np.ones((5,5), np.uint8)

        ret, thresh1 = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #cv2.imshow('thresh1', thresh1)

        img_dilation = cv2.dilate(thresh1, kernel, iterations=1)
        img_closing = cv2.erode(img_dilation, kernel, iterations=5)
        img_dilation = cv2.dilate(img_closing, kernel, iterations=1)

        #cv2.imshow('IF', img_dilation)
        #cv2.imshow('Closing', img_closing)
               
        # get the name of the Output image
  
        output=input('Enter output file name +  path  =')   
        cv2.imwrite(output , img_dilation )
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    # This function will put the watermark on the image ( Image watermark )
        
    def getImageWaterMark(self , f):
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        # get the name of the input image       
        image_name = input('Enter the Path of the File  =   ')
        print(image_name)
        # get the name of the input image you want as a watermark
        img = cv2.imread('C:\\Users\\Pakistan\\images\\v.png')
        watermark_image_name = input('Enter the Path of the watermark Image  =   ')
        print(watermark_image_name)
        watermark = cv2.imread(watermark_image_name)
        

        percent_of_scaling = 20
        
        new_width = int(img.shape[1] * percent_of_scaling/100)
        
        new_height = int(img.shape[0] * percent_of_scaling/100)
        
        new_dim = (new_width, new_height)
        
        resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)
        
        
        
        
        wm_scale = 40
        
        wm_width = int(watermark.shape[1] * wm_scale/100)
        
        wm_height = int(watermark.shape[0] * wm_scale/100)
        
        wm_dim = (wm_width, wm_height)
        
        
        
        
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
        
        
        
        
        h_img, w_img, _ = resized_img.shape
        
        center_y = int(h_img/2)
        
        center_x = int(w_img/2)
        
        h_wm, w_wm, _ = resized_wm.shape
        
        top_y = center_y - int(h_wm/2)
        
        left_x = center_x - int(w_wm/2)
        
        bottom_y = top_y + h_wm
        
        right_x = left_x + w_wm
        
        
        
        
        roi = resized_img[top_y:bottom_y, left_x:right_x]
        
        result = cv2.addWeighted(roi, 1, resized_wm, 0.3, 0)
        
        resized_img[top_y:bottom_y, left_x:right_x] = result
        
        output=input('Enter output file name +  path  =')   
      
        cv2.imwrite(output, resized_img)
        
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()
                
        return output
        
        
        
     # This functions allows you to create a text watermark on an image
     
    def textmarking(self ,txt):
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        # get the name of the input image
        image_name = input('Enter the Path of the File you want to Repair  =   ')
        print(image_name)
        
        img = Image.open(image_name)
        #Creating draw object
        draw = ImageDraw.Draw(img) 
        
        #Creating text and font object
        text = txt
        font = ImageFont.truetype('arial.ttf', 134)
        
        #Positioning Text
        textwidth, textheight = draw.textsize(text, font)
        width, height = img.size 
        x=width/2-textwidth/2
        y=height-textheight-300
        
        #Applying text on image via draw object
        draw.text((x, y), text, font=font) 
        
        #Saving the new image
        img.save(r'C:\\Users\\Pakistan\\images\\i8.png')


    # This function allows you to Restore the old letters , whose writting are not clear
    
    def ClosingLetter(self):
        
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        
        image_name = input('Enter the Path of the File you want to Repair  =')
        print(image_name)
        
        image = cv2.imread(image_name)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        dimensions = image.shape
        # height, width, number of channels in image
        height = image.shape[0]
        width = image.shape[1]
        #cv2.imshow('Original image',image)
        #cv2.imshow('Gray image', gray)
        kernel = np.ones((3,3),np.float32)/9
        img = 255 - gray
        img_dilation = cv2.dilate(img, kernel, iterations=3)
        #img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
        #mg_dilation = cv2.dilate(img, kernel, iterations=5)
        img_erosion = cv2.erode(img_dilation, kernel, iterations=1)
        #resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        img_dilation= 255 - img_dilation
        img_erosion= 255 - img_erosion

        output=input('Enter output file name +  path  =')   
        cv2.imwrite(output , img_erosion )
           #dilated image
            #cv2.imshow('d', img_dilation)
            #output image
            #cv2.imshow('e', img_erosion)
            #cv2.imwrite("filename.png", img_erosion)


        return img_erosion
        
    # This function allows you do the decryption of the Image.
    # You will Input an image and get the hidden image inside it   
    
    def Image_stegnaography_decryption( self , f):
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        
        image_name_1 = input('Enter the Path of the Image You want to decrypt =')
        print(image_name_1)
        img = cv2.imread(image_name_1)
    
        width = img.shape[0]
        height = img.shape[1]
        img1 = np.zeros((width, height, 3), np.uint8)
        img2 = np.zeros((width, height, 3), np.uint8)
          
        for i in range(width):
            for j in range(height):
                for l in range(3):
                    v1 = format(img[i][j][l], '08b')
                    v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                    v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                      
                    # Appending data to img1 and img2
                    img1[i][j][l]= int(v2, 2)
                    img2[i][j][l]= int(v3, 2)
          
        # These are two images produced from
        # the encrypted image
        output1=input('Enter output file name # 1 +  path  =  ')   
        cv2.imwrite(output1, img1)
        output2=input('Enter output file name # 2 +  path  =  ')   
        cv2.imwrite(output2, img2)
        return output
    
    # This function allows you do the Encryption of the Image.
    # You will Input  base image and  hidden image
    # the hidden image will be encrypted in the base image
   
    def Image_stegnaography_encryption(self , f):
        print(" Current path = C:\\Users\\Pakistan\\images \n ")
        
        image_name_1 = input('Enter the Path of the Upper Image  =')
        print(image_name_1)
        image_num1 = cv2.imread(image_name_1)
       
    
        image_name_2 = input('Enter the Path of the Upper Image  =')
        print(image_name_2)
        image_num2 = cv2.imread(image_name_2)
        
        print(image_num2.shape[0])
        for i in range(image_num2.shape[0]):
            for j in range(image_num2.shape[1]):
                for l in range(3):
                  
                # v1 and v2 are 8-bit pixel values
                # of img1 and img2 respectively
                    v1 = format(image_num1[i][j][l], '08b')
                    v2 = format(image_num1[i][j][l], '08b')
                  
                # Taking 4 MSBs of each image
                    v3 = v1[:4] + v2[:4] 
                  
                    image_num1[i][j][l]= int(v3, 2)
               
        output=input('Enter output file name +  path  =  ')   
        cv2.imwrite(output, image_num1)
        return output
    
    # ------------------------ CORE FUNCTIONS IMPLEMENTATION ENDED HERE -------------------------------
    
    #this function is an interface that will show the image with movement detected
    # it is an binary image
    def detectMove(self , f):
        f.destroy()
        ep= Frame(root)

        l = Label(ep,text=' Zaikes - Security \n  a Cyber Security App \n  '  , font ="ar 19 bold" ,  bg = "#031F25" , fg='#E5FFCC')
        l.config(font=('courier',18))
        l.grid(pady=10)

        myfile ="C:\\Users\\Pakistan\\images\\output.png"
        myimg = Image.open(myfile)
        myimage = myimg.resize((300,300))
        img = ImageTk.PhotoImage(myimage)
        l3= Label(ep,text='The Movement Detected Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
        l3.config(font=('courier',18))
        l3.grid(pady=10)
        panel = Label(ep, image=img)
        panel.image = img
        self.output_image_size = os.stat(myfile)
        self.o_image_w, self.o_image_h = myimg.size
        panel.grid()
        back_button = Button(ep, text='Home', command=lambda : Zaiks.home(self,ep) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
        back_button.config(font=('courier',15))
        back_button.grid(pady=5)
        back_button.grid()
        
        ep.grid(row=1) 
       
       
    # This function will allows you to display the Water Mark image.
    # Image WaterMark
    
    def imagewatermarking( self , f , image1 , image2):
        f.destroy()
        ep= Frame(root)

        l = Label(ep,text='Welcome to Zaiks - Security \n  a Cyber Security App \n  '  , font ="ar 19 bold" ,  bg = "#031F25" , fg='#E5FFCC')
        l.config(font=('courier',18))
        l.grid(pady=10)
        # you will uncomment this if you want to do image watermark with other images
        #image = self.getImageWaterMark()
        #myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        myfile = "C:\\Users\\Pakistan\\images\\Watermakred_Image.jpg"
        myimg = Image.open(myfile)
        myimage = myimg.resize((350,350))
        img = ImageTk.PhotoImage(myimage)
        l3= Label(ep,text='The WaterMarked Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
        l3.config(font=('courier',18))
        l3.grid()
        panel = Label(ep, image=img)
        panel.image = img
        self.output_image_size = os.stat(myfile)
        self.o_image_w, self.o_image_h = myimg.size
        panel.grid()
        back_button = Button(ep, text='Home', command=lambda : Zaiks.home(self,ep) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
        back_button.config(font=('courier',15))
        back_button.grid(pady=5)
        back_button.grid()
        
        ep.grid(row=1)
           
        
    
    # this function will take the two input images needed for the image watermark
            #1.   Base Image
            #2.   Hidden Image
        # and a function button that will allows you to do the image watermarking
        
    def Image_watermark_frame1(self , f):
        f.destroy()
        ep= Frame(root)

        messagebox.showinfo("Select"," Select the Base Image")  
        # Selecting the base image
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='The Original Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l3.config(font=('courier',18))
            l3.grid(pady=10)
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            
            
        messagebox.showinfo("Select"," Select the Image You want as WaterMark")
        # Selects the Hidden Image
        myfile2 = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg2 = Image.open(myfile2)
            myimage2 = myimg2.resize((300,200))
            img = ImageTk.PhotoImage(myimage2)
            l4= Label(ep,text=' Image you Want As WaterMark' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid(pady=10)
            panel2 = Label(ep, image=img)
            panel2.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel2.grid()
            ep.grid(row=1)
              
            myimage = myimg.resize((100,100))
            myimage2 = myimg2.resize((100,100))
          
            # button that will call the function - imagewatermarking
            back_button = Button(ep, text='WaterMark', command=lambda : self.imagewatermarking(ep , myimage , myimage2) ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            back_button.config(font=('courier',14))
            back_button.grid(pady=15)
            
            
    # this function will allows you to give the text watermark image as output
    #   1. Selects the Image
    #   2. Enter the text you want as watermark on console
    # Enter and get the watermarked image with text provided
    
    def textMark_frame1(self , f):
        
        f.destroy()
        d_f3 = Frame(root)
        messagebox.showinfo("information","Select Image you want Text Watermark On")  
        #selects the image here
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            d_f3.grid(row=1)
            l5= Label(d_f3,text='Watermark Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l5.config(font=('courier',18))
            l5.grid()
            
            text = input("What text you Want as a WaterMark on the Selected Image")
            
            #you will uncomment this when you want a text watermark on any other images
            #img_rep = self.textmarking(text)            
            #myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            
            myfile = "C:\\Users\\Pakistan\\images\\i8.png"
            myimg2 = Image.open(myfile, 'r')
            myimage = myimg2.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            panel2 = Label(d_f3, image=img)
            panel2.image = img
            panel2.grid(pady=2)
            
            back_button = Button(d_f3, text='Home', command=lambda : Zaiks.home(self,d_f3) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            back_button.config(font=('courier',12))
            back_button.grid(pady=5)
            back_button.grid()
        

            cv2.waitKey(0)
            cv2.destroyAllWindows()


    # This function allows you to repair the broken letters , number etc
    # This will ask for input image and direct to new window that will further proceed
    def welcome_letter_repair(self , f):
        f.destroy()
        d_f2 = Frame(root)
       
        #"C:\Users\Pakistan\images\broken.jpeg"
        image = "C:\\Users\\Pakistan\\images\\broken.jpeg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(d_f2,text='Letter Repairing - Closing :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(d_f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1 = Label(d_f2, text='Select the image of a document \n or a letter you want \n to repair',font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid(pady=10)
        bws_button = Button(d_f2, text='Select', command=lambda :self.letter_repair(d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(d_f2, text='Cancel', command=lambda : Zaiks.home(self,d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()
        
    
        
    # This function will take the input image and displays the output image that is repaired
    
    def letter_repair( self , f ):
        f.destroy()
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            d_f3.grid(row=1)
            l5= Label(d_f3,text='Repaired Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l5.config(font=('courier',18))
            l5.grid()
            
            # You will uncomment this line when you want to repair an image other than the current one
            #img_rep = self.repair_img()
            #myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            
            myfile = "C:\\Users\\Pakistan\\images\\numr.png"
            myimg2 = Image.open(myfile, 'r')
            myimage = myimg2.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            panel2 = Label(d_f3, image=img)
            panel2.image = img
            panel2.grid(pady=2)
            
            back_button = Button(d_f3, text='Home', command=lambda : Zaiks.home(self,d_f3) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            back_button.config(font=('courier',12))
            back_button.grid(pady=5)
            back_button.grid()
        

            cv2.waitKey(0)
            cv2.destroyAllWindows()


     # This function will Restore the old hand written letters or document that can be barely readable
     # Two Functions 
            # 1. select - new screen to select images
            # 2. cancel - move to home
            
    def welcome_letter_restore(self , f):
        f.destroy()
        d_f2 = Frame(root)
       
        image = "C:\\Users\\Pakistan\\images\\letter.jpg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(d_f2,text='Letter Restoring - Decode :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(d_f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1 = Label(d_f2, text='Select the image of a document \n or a letter you want \n to restore',font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid(pady=10)
        bws_button = Button(d_f2, text='Select', command=lambda :self.letter_restore(d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(d_f2, text='Cancel', command=lambda : Zaiks.home(self,d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()


    # this function will allow you to select the input image and return the output image by applying functions on them
    # 1. Input image of old letter in our case
    # 2. Restored Image
    def letter_restore(self , f):
        f.destroy()
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            d_f3.grid(row=1)
            l5= Label(d_f3,text='Restored Image :' , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
            l5.config(font=('courier',18))
            l5.grid()
            
            # You will uncomment this if you want any image to be restored other than this
            #image = self.ClosingLetter()
            #myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            myfile = "C:\\Users\\Pakistan\\images\\letter out - Copy.png"
            myimg2 = Image.open(myfile, 'r')
            myimage = myimg2.resize((300, 240))
            img = ImageTk.PhotoImage(myimage)
            panel2 = Label(d_f3, image=img)
            panel2.image = img
            panel2.grid(pady=2)
            
            back_button = Button(d_f3, text='Home', command=lambda : Zaiks.home(self,d_f3) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            back_button.config(font=('courier',12))
            back_button.grid(pady=5)
            back_button.grid()
        

            cv2.waitKey(0)
            cv2.destroyAllWindows()

    #This function will allow you take the choice of you wanting a :
    # 1. Encryption of image in image
    # 2. Decryption of image from an image
    def Image_steg_frame1(self , f):
        f.destroy()
        f2 = Frame(root)

        image ="C:\\Users\\Pakistan\\images\\crimescene.jpeg"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Image Steganography - Hiding :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Do you Want to \n Encrypt or Decrypt Images :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Encrypt',command=lambda : self.Image_steg_image1(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Decrypt', command=lambda : self.Image_steg_decrypt1(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()
        
    #This function will allow you take the choice of you wanting a :
    # 1. encoding a text in an image 
    # 2. decoding a text from an image
    
    def steg_frame1(self , f):
        f.destroy()
        f2 = Frame(root)

        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Text Steganography - Hiding :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Do you Want to Encode or Decode :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Encode',command=lambda : self.frame1_encode(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Decode', command=lambda : self.frame1_decode(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()
        
        
    # Screen 1 of DECODING TEXT STEGANOGRAPHY
    # selects image with hidden text
    # or go to home screen
    def frame1_decode(self,f):
        f.destroy()
        d_f2 = Frame(root)
       
        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(d_f2,text='Text Steganography - Decode :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(d_f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1 = Label(d_f2, text='Select Image with Hidden text:',font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid(pady=10)
        bws_button = Button(d_f2, text='Select', command=lambda :self.frame2_decode(d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(d_f2, text='Cancel', command=lambda : Stegno.home(self,d_f2) , font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        d_f2.grid()
  
           
              
    # Screen 2 of DECODING TEXT STEGANOGRAPHY
    # This will output the selectedimage and displays the text encrypted
    
    def frame2_decode(self,d_f2):
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Selected Image :')
            l4.config(font=('courier',18))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid()
            hidden_data = self.decode(myimg)
            l2 = Label(d_f3, text='Hidden data is :')
            l2.config(font=('courier',18))
            l2.grid(pady=10)
            text_area = Text(d_f3, width=50, height=10)
            text_area.insert(INSERT, hidden_data)
            text_area.configure(state='disabled')
            text_area.grid()
            back_button = Button(d_f3, text='Cancel', command= lambda :self.page3(d_f3))
            back_button.config(font=('courier',11))
            back_button.grid(pady=15)
            back_button.grid()
            show_info = Button(d_f3,text='More Info',command=self.info)
            show_info.config(font=('courier',11))
            show_info.grid()
            d_f3.grid(row=1)
            d_f2.destroy()

    # Screen 1 of DECODING IMAGE STEGANOGRAPHY
    # selects image 
    # or go to home screen
            
            
    def Image_steg_decrypt1(self , f):
        f.destroy()
        f2 = Frame(root)

        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Image Steganography - Decrypting :' , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Select the Image \n you want to decrypt  :' ,font ="ar 25 bold" , bg = "black" , fg='#ffffff')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.Image_steg_decrypt2(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Cancel', command=lambda : Zaiks.home(self,f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()
        
        
    
    def Image_steg_image1(self , f):
        f.destroy()
        f2 = Frame(root)

        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Image Steganography - Hiding :' , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Select the Image  :' ,font ="ar 25 bold" , bg = "black" , fg='#ffffff')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.Image_steg_image1_select(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Cancel', command=lambda : Zaiks.home(self,f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()
        
    # Screen 1 of ENCODING TEXT STEGANOGRAPHY
    # selects image with hidden text
    # or go to home screen
    
    def frame1_encode(self,f):
        f.destroy()
        f2 = Frame(root)

        image = "C:\\Users\\Pakistan\\images\\secs3.png"
        myimg2 = Image.open(image, 'r')
        myimage = myimg2.resize((300, 200))
        img = ImageTk.PhotoImage(myimage)
        l5= Label(f2,text='Text Steganography - Hiding :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l5.config(font=('courier',18))
        l5.grid(pady=14)
        panel2 = Label(f2, image=img)
        panel2.image = img
        panel2.grid(pady=14)

        l1= Label(f2,text='Select the Image in which \nyou want to hide text :' , font ="ar 15 bold" ,   bg = "#0A0E2C" , fg='#E5FFCC')
        l1.config(font=('courier',18))
        l1.grid()

        bws_button = Button(f2,text='Select',command=lambda : self.frame2_encode(f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        bws_button.config(font=('courier',18))
        bws_button.grid(pady=14)
        back_button = Button(f2, text='Cancel', command=lambda : Zaiks.home(self,f2),font ="ar 15 bold" ,   bg = "#0D444E" , fg='#E5FFCC')
        back_button.config(font=('courier',18))
        back_button.grid(pady=15)
        back_button.grid()
        f2.grid()

    # Screen 2 of ENCODING IMAGE STEGANOGRAPHY
    # selects the output image you get as a result of function -  Image_stegnaography_encryption
    # displays the base and hidden image too
   
    def imagehide_final(self , f ,  image1 , image2):
         f.destroy()
         ep= Frame(root)
         #you'll uncomment this if you want to do image steganography with images other than these
         #x = self.Image_stegnaography_encryption(ep)
         #print(x)
         
         myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
         myimg = Image.open(myfile)
         myimage = myimg.resize((300,200))
         img = ImageTk.PhotoImage(myimage)
         l2= Label(ep,text='The Encrypted Image' , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
         l2.config(font=('courier',18))
         l2.grid(pady=7)
         panel4 = Label(ep, image=img)
         panel4.image = img
         self.output_image_size = os.stat(myfile)
         self.o_image_w, self.o_image_h = myimg.size
         panel4.grid()
        
    
    
         img = ImageTk.PhotoImage(image1)
         l3= Label(ep,text='The Base Image' )
         l3.config(font=('courier',10))
         l3.grid()
         panel = Label(ep, image=img)
         panel.image = img
         panel.grid()
         
         img2 = ImageTk.PhotoImage(image2)
         l4= Label(ep,text='The Hidden Image' )
         l4.config(font=('courier',10))
         l4.grid()
         panel2 = Label(ep, image=img2)
         panel2.image = img2
         panel2.grid()
         
         back_button = Button(ep, text='Home', command=lambda : Zaiks.home(self,ep) ,  font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
         back_button.config(font=('courier',14))
         back_button.grid(pady=15)
         back_button.grid()
        
         ep.grid(row=1)
            
    # Screen 2 of DECODING IMAGE STEGANOGRAPHY
    # selects the output image you get as a result of function -  Image_stegnaography_decryption
             
    def Image_steg_decrypt1(self ,f):
         f.destroy()
         ep= Frame(root)
         #you'll uncomment this if you want to do image steganography with images other than these
         #x = self.Image_stegnaography_decryption(ep)
         #print(x)
         messagebox.showinfo("information"," Select the Image you want to decrypt")  

         myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
         myimg = Image.open(myfile)
         myimage = myimg.resize((180,180))
         img = ImageTk.PhotoImage(myimage)
         l2= Label(ep,text='Encrypted Image' , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
         l2.config(font=('courier',12))
         l2.grid(pady=7)
         panel4 = Label(ep, image=img)
         panel4.image = img
         self.output_image_size = os.stat(myfile)
         self.o_image_w, self.o_image_h = myimg.size
         panel4.grid()
        
    
         i2 = "C:\\Users\\Pakistan\\images\\d2.png" 
         myimg = Image.open(i2)
         myimage2 = myimg.resize((340,300))
         img2 = ImageTk.PhotoImage(myimage2)
         l4= Label(ep,text='The Hidden Image' )
         l4.config(font=('courier',12))
         l4.grid()
         panel2 = Label(ep, image=img2)
         panel2.image = img2
         panel2.grid()
         
         back_button = Button(ep, text='Home', command=lambda : Zaiks.home(self,ep) ,  font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
         back_button.config(font=('courier',14))
         back_button.grid(pady=15)
         back_button.grid()
        
         ep.grid(row=1)
        

    # Screen 1 of ENCODING IMAGE STEGANOGRAPHY
    # selects base image
    # selects image you want to hide
   
    def Image_steg_image1_select(self,f):
        f.destroy()
        ep= Frame(root)

        messagebox.showinfo("Select"," Select the Base Image")  
        # selects the base image
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='The Base Image' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l3.config(font=('courier',18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            
         
        messagebox.showinfo("Select"," Select the Image You want to hide")
        # selects the image you want to hide
        myfile2 = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg2 = Image.open(myfile2)
            myimage2 = myimg2.resize((300,200))
            img = ImageTk.PhotoImage(myimage2)
            l4= Label(ep,text=' Image you Want to Hide' ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            l4.config(font=('courier',18))
            l4.grid()
            panel2 = Label(ep, image=img)
            panel2.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel2.grid()
            ep.grid(row=1)
              
            myimage = myimg.resize((100,100))
            myimage2 = myimg2.resize((100,100))
          
            back_button = Button(ep, text='Encrypt', command=lambda : self.imagehide_final(ep , myimage , myimage2) ,  font ="ar 15 bold" , bg = "#0A0E2C" , fg='#E5FFCC')
            back_button.config(font=('courier',14))
            back_button.grid(pady=15)
            
    # Screen 1 of ENCODING TEXT STEGANOGRAPHY
    # selects base image
    # Enter text you want to write
        
    def frame2_encode(self,f2):
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='Selected Image')
            l3.config(font=('courier',18))
            l3.grid()
            panel = Label(ep, image=img)
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid()
            l2 = Label(ep, text='Enter the message')
            l2.config(font=('courier',18))
            l2.grid(pady=15)
            text_area = Text(ep, width=50, height=10)
            text_area.grid()
            encode_button = Button(ep, text='Cancel', command=lambda : Zaiks.home(self,ep))
            encode_button.config(font=('courier',11))
            data = text_area.get("1.0", "end-1c")
            back_button = Button(ep, text='Encode', command=lambda : [self.enc_fun(text_area,myimg),Zaiks.home(self,ep)])
            back_button.config(font=('courier',11))
            back_button.grid(pady=15)
            encode_button.grid()
            ep.grid(row=1)
            f2.destroy()
       
    # This function will allow you to display the thermal image we get from the above thermal function
    def frame2_thermalImage(self,d_f2):
        d_f3 = Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","You have selected nothing !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            ltitle= Label(d_f3,text='Thermal Imaging Conversion '  , font ="ar 25 bold" , bg = "black" , fg='#ffffff')
            ltitle.config(font=('courier',18))
            ltitle.grid(pady=14)
            
            l4= Label(d_f3,text='Selected Image :' , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            l4.config(font=('courier',12))
            l4.grid()
            panel = Label(d_f3, image=img)
            panel.image = img
            panel.grid(pady=4)
            # You'll uncomment this if you want to do thermal image conversion other than this image
            #thermal_Img = self.thermal()
            #myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
            myfile = "C:\\Users\\Pakistan\\images\\pop2.png"
            myimg2 = Image.open(myfile, 'r')
            myimage = myimg2.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l5= Label(d_f3,text='Thermal Image :' , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            l5.config(font=('courier',12))
            l5.grid()
            panel2 = Label(d_f3, image=img)
            panel2.image = img
            panel2.grid(pady=6)
            
            back_button = Button(d_f3, text='Home', command=lambda : Zaiks.home(self,d_f3) , font ="ar 15 bold" , bg = "#7F2111" , fg='#DACE16')
            back_button.config(font=('courier',12))
            back_button.grid(pady=15)
            back_button.grid()
        
            d_f3.grid(row=1)
            d_f2.destroy()
        
    # PART OF TEXT STEGANOGRAPHY
    # USED TO DECODE THE IMAGE INTO BINARY DATA FIRST THEN
    # STARTS READING THE THREE BITS AT A TIME
    # IF THE LAST BIT IS ODD - MEANS END OF MSG
    # ELSE MESSAGE IS STILL NOT ENDED
    
    def decode(self, image):
      data = ''
      imgdata = iter(image.getdata())

      while (True):
          pixels = [value for value in imgdata.__next__()[:3] +
                    imgdata.__next__()[:3] +
                    imgdata.__next__()[:3]]
          binstr = ''
          for i in pixels[:8]:
              if i % 2 == 0:
                  binstr += '0'
              else:
                  binstr += '1'

          data += chr(int(binstr, 2))
          if pixels[-1] % 2 != 0:
              return data

    # PART OF TEXT STEGANOGRAPHY
    # THIS FUNCTION SHOWS THE EXTRA INFO OF AN IMAGE
    # LIKE SIZE OF ORIGINAL AND NEW IMAGE ETC
    def info(self):
        try:
            str = 'original image:-\nsize of original image:{}mb\nwidth: {}\nheight: {}\n\n' \
                  'decoded image:-\nsize of decoded image: {}mb\nwidth: {}' \
                '\nheight: {}'.format(self.output_image_size.st_size/1000000,
                                    self.o_image_w,self.o_image_h,
                                    self.d_image_size/1000000,
                                    self.d_image_w,self.d_image_h)
            messagebox.showinfo('info',str)
        except:
            messagebox.showinfo('Info','Unable to get the information')
    
    
    # PART OF TEXT STEGANOGRAPHY
    # THIS FUNCTION CONVERT THE HUMAN READBLE TEXT INTO THE BINARY DATA
         
    def genData(self,data):
        newd = []

        for i in data:
            newd.append(format(ord(i), '08b'))
        return newd

    # Pixels are modified according to the
    # 8-bit binary data and finally returned
    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):

                    if (pix[j] % 2 != 0):
                        pix[j] -= 1

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                    pix[j] -= 1
            # Eighth pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]


    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def enc_fun(self,text_area,myimg):
        data = text_area.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Success","Encoding Successful\nFile is saved as Image_with_hiddentext.png in the same directory")

    def page3(self,frame):
        frame.destroy()
        self.main(root)


# Creates a tkinter root Window
root = Tk()
# Object of our Class Zaiks
o = Zaiks()
# calling main function of Zaiks Class
o.main(root)
# Running the main loop
root.mainloop()
