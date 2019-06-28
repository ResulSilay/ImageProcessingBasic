from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5 import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget,QTableWidget,QTableWidgetItem,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from Design import Ui_MainWindow
from xlrd import open_workbook
from openpyxl.reader.excel import load_workbook
from skimage import data, img_as_float,io
from skimage.measure import compare_ssim as SSIM2
from skimage.measure import structural_similarity as _SSIM
from sklearn.metrics import mean_squared_error as MSE
from PIL import Image
from scipy import ndimage
from PIL.ImageQt import ImageQt
from skimage import data
from skimage import color
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.morphology import skeletonize
from skimage.util import invert
import matplotlib.pyplot as plt
import random
import scipy
import os
import io as _io
import cv2
import math
import numpy as np

class override_graphicsScene (Qt.QGraphicsScene):
    def __init__(self,parent = None):
        super(override_graphicsScene,self).__init__(parent)

    def mousePressEvent(self, event):
        super(override_graphicsScene, self).mousePressEvent(event)
        print(event.pos())

class MainWindow(QWidget,Ui_MainWindow):
    
    temp_path = "image.png"
    temp_path_2 = "image_2.png"
    temp_path_3 = "image_3.png"
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.groupBox_3.setVisible(False)
        
        self.btn_temel_yukle.clicked.connect(self.button_temel_yukle)
        self.btn_temel_gri_cevir.clicked.connect(self.button_temel_gri_cevir)
        self.btn_temel_binary_cevir.clicked.connect(self.button_temel_binary_cevir)
        self.btn_temel_boyutlandir.clicked.connect(self.button_temel_boyutlandir)
        self.btn_temel_sobel.clicked.connect(self.button_temel_sobel)
        self.btn_temel_treshold.clicked.connect(self.button_temel_treshold)
        self.btn_temel_canny.clicked.connect(self.button_diger_canny)
        self.btn_temel_skeletonize.clicked.connect(self.button_temel_skeletonize)
        self.btn_temel_hist_esitle.clicked.connect(self.button_temel_hist_esitle)
        
        self.btn_gurultu_yukle.clicked.connect(self.button_gurultu_yukle)
        self.btn_gurultu_olustur.clicked.connect(self.button_gurultu_olustur)
        
        self.btn_mantiksal_a_yukle.clicked.connect(self.button_mantiksal_a_yukle)
        self.btn_mantiksal_b_yukle.clicked.connect(self.button_mantiksal_b_yukle)
        self.btn_mantiksal_uygula.clicked.connect(self.button_mantiksal_uygula)
        
        self.btn_labeling_yukle.clicked.connect(self.button_labeling_yukle)
        self.btn_labeling_uygula.clicked.connect(self.button_labeling_uygula)
        self.btn_labeling_vurgula.clicked.connect(self.button_labeling_vurgula)
        self.cmb_label_sekiller.activated[str].connect(self.onActivated_label_sekiller)
        
        self.btn_classes_apply_14.clicked.connect(self.button_template_labeling_yukle)
        self.btn_split_next_6.clicked.connect(self.button_template_match_uygula)
        self.btn_split_next_5.clicked.connect(self.button_template_labeling_uygula)
        self.cmb_classes_5.activated[str].connect(self.onActivated_template_label_sekiller)
        
        self.btn_diger_daire.clicked.connect(self.button_diger_daire)
        self.btn_diger_rotate_yukle.clicked.connect(self.button_diger_rotate_yukle)
        self.btn_diger_rotate_sol.clicked.connect(self.button_diger_rotate_sol)
        self.btn_diger_rotate_sag.clicked.connect(self.button_diger_rotate_sag)
        self.btn_diger_rotate_ters.clicked.connect(self.button_diger_rotate_ters)
        self.btn_diger_rotate_yansima.clicked.connect(self.button_diger_rotate_yansima)
        self.btn_diger_sekiller_yukle.clicked.connect(self.button_diger_sekiller_yukle)
        
        
        self.btn_diger_sekil_yukle.clicked.connect(self.button_diger_sekil_yukle)
        self.btn_diger_sekil_bul.clicked.connect(self.button_diger_sekil_bul)
        self.btn_diger_resim_olustur.clicked.connect(self.button_diger_resim_olustur)
        self.btn_diger_tom_yukle.clicked.connect(self.button_diger_tom_yukle)
        self.btn_diger_jery_yukle.clicked.connect(self.button_diger_jery_yukle)
        self.btn_diger_tom_jery_uygula.clicked.connect(self.button_diger_tom_jery_uygula)
        self.btn_diger_tom_jery_arkaplan_yukle_1.clicked.connect(self.button_diger_tom_jery_arkaplan_yukle_1) 
        self.btn_diger_tom_jery_arkaplan_yukle_2.clicked.connect(self.button_diger_tom_jery_arkaplan_yukle_2) 
        self.btn_diger_arkaplan_tom_jery_uygula.clicked.connect(self.button_diger_arkaplan_tom_jery_uygula)
        
    
    def button_diger_daire(self):
        kordinatlar = []
        #image = cv2.imread('image.png',0)
        img = np.zeros((350, 350, 3), np.uint8)
        img[:, :] = [0, 0, 0]
        row = random.randint(100,300)
        col = random.randint(100,300)
        cv2.circle(img,(row, col), 30, (255,255,255), -1)
        
        row = random.randint(100,300)
        col = random.randint(100,300)
        cv2.circle(img,(row, col), 40, (255,255,255), -1)
        
        cv2.imwrite(self.temp_path_2,img)
        image = cv2.imread(self.temp_path_2)
        #image = cv2.medianBlur(image,5)
        copy_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(self.temp_path_2,copy_img)
        
        scene = self.show_image_path(self.temp_path_2,self.img_diger_daire.size())
        self.img_diger_daire.setScene(scene)

        circles = cv2.HoughCircles(copy_img,cv2.HOUGH_GRADIENT,1,20, param1=30,param2=15,minRadius=0,maxRadius=0)
        print(circles)
        circles = np.uint16(np.around(circles))
        for count,i in enumerate(circles[0,:]):
            kordinatlar.append("Daire "+str(count+1)+" kordinat (x,y,r (cap)) = "+str(i[0])+","+str(i[1])+","+str(i[2]))
            cv2.circle(copy_img,(i[0],i[1]),i[2],(0,255,0),2)
            cv2.circle(copy_img,(i[0],i[1]),2,(0,0,255),3)

        print(kordinatlar)
        cv2.imwrite(self.temp_path_2,copy_img)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_daire.size())
        self.img_diger_daire.setScene(scene)
        self.lbl_circle_coordinate.setStyleSheet("background-color:black; color:green;")
        self.lbl_circle_coordinate.setText(str(kordinatlar))

    def button_temel_skeletonize(self):
        img = cv2.imread(self.temp_path,0)
        img = invert(img)
        img = skeletonize(img)
        img.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
        
    def button_diger_canny(self):
        img = cv2.imread(self.temp_path)
        w,h,z = img.shape
        print(w,h)
        edges = cv2.Canny(img,w,h)
        #edges.save(self.temp_path_2)
        cv2.imwrite(self.temp_path_2,edges)
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
        
    def button_diger_rotate_sol(self):
        img = Image.open(self.temp_path)
        img=img.rotate(-90, expand=True)
        img.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_rotate.size())
        self.img_diger_rotate.setScene(scene)
        
    def button_diger_rotate_sag(self):
        img = Image.open(self.temp_path)
        img=img.rotate(90, expand=True)
        img.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_rotate.size())
        self.img_diger_rotate.setScene(scene)
        
    def button_diger_rotate_ters(self):
        img = Image.open(self.temp_path)
        img=img.rotate(180, expand=True)
        img.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_rotate.size())
        self.img_diger_rotate.setScene(scene)
        print("")
    
    def button_diger_rotate_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_diger_rotate.size())
        self.img_diger_rotate.setScene(scene)
        
    def button_diger_rotate_yansima(self):
        org=Image.open(self.temp_path)
        new=Image.new("RGB",org.size)   
        for x in range(org.size[0]):
            flipped_x = org.size[0] - x - 1
            for y in range(org.size[1]):
                pixel=org.getpixel((x,y))
                new.putpixel((flipped_x,y),pixel)
        
        new.save(self.temp_path_2)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_diger_rotate.size())
        self.img_diger_rotate.setScene(scene)

    def button_diger_sekiller_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_diger_sekiller.size())
        self.img_diger_sekiller.setScene(scene)

    def button_diger_sekil_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_sekil_2.size())
        self.img_diger_sekil_2.setScene(scene)
        
    def button_diger_sekil_bul(self):
        img = Image.open(self.temp_path) 
        pix = img.load()
        size = width, height = img.size
        pixel_values = list(img.getdata())
                
        cordinates_x = []
        cordinates_y = []
        
        counter = 0
        for i in range(1,width):
            for j in range(1,height):
                cordinate = i,j
                counter+=1
                if(img.getpixel(cordinate)[0] == 000): #siyah renkleri bul ve listeye ekle.
                    cordinates_x.append([cordinate])
                    cordinates_y.append([cordinate])
                    
        counter = 0
        etiket=""
        for n in range(1,width):
            if(cordinates_x[0][0][0]==cordinates_x[n][0][0]):
                counter+=1
        
        if(counter<5):
            etiket=("#Üçkendir")
        else:
            if(counter>5):
                etiket=("#Karedir")
            if(counter>25):
                etiket=("#Dikdörtgendir.")
        
        self.label.setText(etiket)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_sekil_2.size())
        self.img_diger_sekil_2.setScene(scene)

        
    def button_diger_resim_olustur(self):
        img = Image.new('RGB', (360, 240), color = 'white')
        pixel_img = img.load()
        w,h= img.size
        radius = 355
        
        for i in range(w):
            for j in range(h):
                x = random.randint(-radius, radius)
                y = random.randint(-radius, radius)
    
                if math.sqrt(x ** 2 + y ** 2) < radius:
                    pixel_img[i,j] = 0,0,0
        #img.show()
        img.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_resim_olustur.size())
        self.img_diger_resim_olustur.setScene(scene)  
        
    def button_diger_tom_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_diger_tom.size())
        self.img_diger_tom.setScene(scene)    
        
    def button_diger_jery_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_jery.size())
        self.img_diger_jery.setScene(scene)    
    
    def button_diger_tom_jery_uygula(self):
        img = Image.open(self.temp_path) 
        width, height = img.size
        pixels = img.load()
        
        img_2 = Image.open(self.temp_path_2) 
        width_2, height_2 = img_2.size
        pixels_2 = img_2.load()
        
        x = random.randrange(width)
        y = random.randrange(height)
        
        for i in range(width):
            for j in range(height):
                if(pixels[i,j][0] == 0 and pixels[i,j][1] == 0 and pixels[i,j][2] == 0):
                    pixels[i, j] = pixels_2[i,j]
                
        img.save(self.temp_path_3)
        scene = self.show_image_path(self.temp_path_3,self.img_diger_tom_jery_1.size())
        self.img_diger_tom_jery_1.setScene(scene)  

        
    def button_diger_tom_jery_arkaplan_yukle_1(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_diger_tom_jery_arkaplan.size())
        self.img_diger_tom_jery_arkaplan.setScene(scene)    
    
    def button_diger_tom_jery_arkaplan_yukle_2(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path_2)
        scene = self.show_image_path(self.temp_path_2,self.img_diger_tom_jery_3.size())
        self.img_diger_tom_jery_3.setScene(scene)    
    
    def button_diger_arkaplan_tom_jery_uygula(self):
        img = Image.open(self.temp_path) 
        width, height = img.size
        pixels = img.load()
        
        img_2 = Image.open(self.temp_path_2) 
        width_2, height_2 = img_2.size
        pixels_2 = img_2.load()
        
        x = random.randrange(width)
        y = random.randrange(height)
        
        for i in range(width):
            for j in range(height):
                if(pixels[i,j][0] == 0 and pixels[i,j][1] == 0 and pixels[i,j][2] == 0):
                    pixels[i, j] = pixels_2[i,j]
                
        img.save(self.temp_path_3)
        scene = self.show_image_path(self.temp_path_3,self.img_diger_tom_jery_arkaplan_sonuc.size())
        self.img_diger_tom_jery_arkaplan_sonuc.setScene(scene)    
    
    def button_temel_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_temel_orjinal.size())
        self.img_temel_orjinal.setScene(scene)
        
    
    def button_temel_gri_cevir(self):
        image = io.imread(self.temp_path)      
        height, width, channel = image.shape

        for i in range(0, height):
            for j in range(0, width):
                blueComponent = image[i][j][0]
                greenComponent = image[i][j][1]
                redComponent = image[i][j][2]
                grayValue = 0.07 * blueComponent + 0.72 * greenComponent + 0.21 * redComponent
                image[i][j] = grayValue
       
        #img= np.dot(image[...,:3], [0.299, 0.587, 0.114])
        cv2.imwrite(self.temp_path_2,image)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
        
    
    def button_temel_binary_cevir(self):
        image = io.imread(self.temp_path) 
        height, width,c = image.shape
        for i in range(0, height):
            for j in range(0, width):
                r,g,b = image[i,j][:3]
                grayValue = 0.07 * b + 0.72 * g + 0.21 * r
                if(grayValue<128):
                    image[i][j] = (0,0,0)
                else:
                    image[i][j]=(255,255,255)
        
        cv2.imwrite(self.temp_path_2,image)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
        
        
    def button_temel_boyutlandir(self):
        image = Image.open(self.temp_path)
        image = cv2.imread(self.temp_path)
        w,h=int(self.img_temel_genislik.text()),int(self.img_temel_yukseklik.text())
        image = cv2.resize(image,(w,h))
        #image.thumbnail(size,Image.ANTIALIAS)
        cv2.imwrite(self.temp_path_2,image)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
        
    
    def button_temel_sobel(self):
        image = io.imread(self.temp_path)
        height, width, channel = image.shape
        for i in range(0, height):
            for j in range(0, width):
                blueComponent = image[i][j][0]
                greenComponent = image[i][j][1]
                redComponent = image[i][j][2]
                grayValue = 0.07 * blueComponent + 0.72 * greenComponent + 0.21 * redComponent
                if(grayValue<128):
                    image[i][j] = (0,0,0)
                else:
                    image[i][j]=(255,255,255)
        
        im = image
        im = im.astype('int32')
        dx = ndimage.sobel(im, 0)
        dy = ndimage.sobel(im, 1) 
        mag = np.hypot(dx, dy) 
        mag *= 255.0 / np.max(mag)
        scipy.misc.imsave('sobel.jpg', mag)
        
        scene = QGraphicsScene()
        scene = self.show_image_path("sobel.jpg",self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
    
    #kenar algılama
    def button_temel_treshold(self):
        image = io.imread(self.temp_path)
        height, width, channel = image.shape
        for i in range(0, height):
            for j in range(0, width):
                r,g,b = image[i,j]
                grayValue = 0.2989 * r + 0.5870 * g + 0.1140 * b
                if(grayValue<128):
                    image[i][j] = (0,0,0)
                else:
                    image[i][j]=(255,255,255)
                    
        cv2.imwrite(self.temp_path_2,image)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_temel_sonuc.size())
        self.img_temel_sonuc.setScene(scene)
    
    def button_temel_hist_esitle(self):
        img = cv2.imread(self.temp_path,0)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        equ = cv2.equalizeHist(img)
        #res = np.hstack((img,equ))
        #w,h,c= res.shape
        cv2.imwrite('image_histogram.jpg',equ)
        
        #önce
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path,self.img_temel_hist_once.size())
        self.img_temel_hist_once.setScene(scene)
        #self.img_temel_sonuc.setScene(scene)
        
        #sonra
        scene = QGraphicsScene()
        scene = self.show_image_path("image_histogram.jpg",self.img_temel_hist_sonra.size())
        self.img_temel_hist_sonra.setScene(scene)
        self.groupBox_3.setVisible(True)
    
    
    def button_mantiksal_a_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path,self.img_mantiksal_a.size())
        self.img_mantiksal_a.setScene(scene)
        
    def button_mantiksal_b_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path_2)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_mantiksal_b.size())
        self.img_mantiksal_b.setScene(scene)
        
    def button_mantiksal_uygula(self):
        print(self.cmb_mantiksal_islemler.currentIndex())
        if(self.cmb_mantiksal_islemler.currentIndex()==0):
            self.mantiksal_not()
        if(self.cmb_mantiksal_islemler.currentIndex()==1):
            self.mantiksal_or()
        if(self.cmb_mantiksal_islemler.currentIndex()==2):
            self.mantiksal_and()
        if(self.cmb_mantiksal_islemler.currentIndex()==3):
            self.mantiksal_xor()
            
    
    def mantiksal_not(self):
        img_I = Image.open(self.temp_path)
        img_I_Pixel = img_I.load()
        
        img_New = Image.new(img_I.mode,img_I.size)
        img_New_Pixel = img_New.load()
        
        w,h = img_I.size
        
        for i in range(0,w):
            for j in range(0,h):
                r,g,b = img_I_Pixel[i,j]
                img_New_Pixel[i,j] = 255-r,255-g,255-b
        
        io.imsave(self.temp_path_2,img_New)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_mantiksal_sonuc.size())
        self.img_mantiksal_sonuc.setScene(scene)
        
    def mantiksal_or(self):
        img_a = Image.open(self.temp_path)       
        img_b = Image.open(self.temp_path_2)  

        img_a_pixel = img_a.load()
        img_b_pixel = img_b.load()
        
        img_new = Image.new(img_a.mode,img_a.size)
        pixel_new = img_new.load()
        
        for i in range(0,img_a.size[0]):
            for j in range(0,img_a.size[1]):
                a,b,c= img_a_pixel[i,j]
                d,e,f= img_b_pixel[i,j]
                pixel_new[i,j] = a or d,b or e, c or f
        
        io.imsave(self.temp_path_2,img_new)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_mantiksal_sonuc.size())
        self.img_mantiksal_sonuc.setScene(scene)     
        
    def mantiksal_and(self):
        img_a = Image.open(self.temp_path)       
        img_b = Image.open(self.temp_path_2)  

        img_a_pixel = img_a.load()
        img_b_pixel = img_b.load()
        
        img_new = Image.new(img_a.mode,img_a.size)
        pixel_new = img_new.load()
        
        for i in range(0,img_a.size[0]):
            for j in range(0,img_a.size[1]):
                a,b,c= img_a_pixel[i,j]
                d,e,f= img_b_pixel[i,j]
                pixel_new[i,j] = a and d,b and e, c and f
        
        io.imsave(self.temp_path_2,img_new)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_mantiksal_sonuc.size())
        self.img_mantiksal_sonuc.setScene(scene) 
        
    def mantiksal_and_or(self):
        print("")
        
    def mantiksal_xor(self):
        from operator import xor
        img_a = Image.open(self.temp_path)       
        img_b = Image.open(self.temp_path_2)  

        img_a_pixel = img_a.load()
        img_b_pixel = img_b.load()
        
        img_new = Image.new(img_a.mode,img_a.size)
        pixel_new = img_new.load()
        
        for i in range(0,img_a.size[0]):
            for j in range(0,img_a.size[1]):
                a,b,c= img_a_pixel[i,j]
                d,e,f= img_b_pixel[i,j]
                pixel_new[i,j] = xor(a,d), xor(b,e), xor(c,f)
        
        io.imsave(self.temp_path_2,img_new)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_mantiksal_sonuc.size())
        self.img_mantiksal_sonuc.setScene(scene) 
       
    def button_gurultu_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path,self.img_gurultu_orjinal.size())
        self.img_gurultu_orjinal.setScene(scene)
    
    def button_gurultu_olustur(self):
        image = io.imread(self.temp_path)
        row,col,ch = image.shape
        value = self.trackBar_gurultu.value()
        self.lbl_gurultu_oran.setText(str(value))
        out = np.copy(image)
        
        for i,row in enumerate(out):
                for j, column in enumerate(row):
                    if(i<=value):
                        x = np.random.randint(0, len(out))
                        y = np.random.randint(0, len(out))
                        out[x][y] = 0
  
        
        io.imsave(self.temp_path_2,out)
      
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_gurultu_sonuc.size())
        self.img_gurultu_sonuc.setScene(scene)
        
        
    def button_labeling_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        scene = self.show_image_path(self.temp_path,self.img_label_orjinal.size())
        self.img_label_orjinal.setScene(scene)
    
    label_path=""
    def onActivated_label_sekiller(self, text):
        print("./res/sekil_"+str(self.cmb_label_sekiller.currentIndex())+".png")
        self.label_path="./res/sekil_"+str(self.cmb_label_sekiller.currentIndex())+".png"
        scene = self.show_image_path("./res/sekil_"+str(self.cmb_label_sekiller.currentIndex())+".png",self.img_label_sonuc.size())
        self.img_label_sonuc.setScene(scene)
    
    def button_labeling_uygula(self):
        self.cmb_label_sekiller.clear()
        img = color.rgb2gray(io.imread(self.temp_path))
        clr = clear_border(img)
        lbl_img= label(clr)
        
        for index, region in enumerate(regionprops(lbl_img)):
            min_r,min_c,max_r,max_c = region.bbox        
            area = img[min_r:max_r,min_c:max_c]
            io.imsave("./res/sekil_"+str(index)+".png",area)
            
            self.cmb_label_sekiller.addItem("sekil "+str(index+1))
        
        scene = QGraphicsScene()
        scene = self.show_image_path("./res/sekil_0.png",self.img_label_sonuc.size())
        self.img_label_sonuc.setScene(scene)
    
    def button_labeling_vurgula(self):
        img = cv2.imread(self.temp_path, 0)
        img2 = img.copy()
        template = cv2.imread(self.label_path,0)
        w, h = template.shape[::-1]
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        for meth in methods:
            img = img2.copy()   
            method = eval(meth)
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
        

        scipy.misc.toimage(img, cmin=0.0, cmax=...).save(self.temp_path_2)
        scene = QGraphicsScene()
        scene = self.show_image_path(self.temp_path_2,self.img_label_sonuc.size())
        self.img_label_orjinal.setScene(scene)
        
    
    def button_template_labeling_yukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"Image files (*.png *.gif)")
        #file_image = io.imread(file)
        file_image = Image.open(file)
        file_image.save(self.temp_path)
        
        scene = self.show_image_path(self.temp_path,self.graphicsView_13.size())
        self.graphicsView_13.setScene(scene)
        
    temp_path_match = ""
    def onActivated_template_label_sekiller(self, text):
        self.temp_path_match = "./res/sekil_"+str(self.cmb_classes_5.currentIndex())+".png"
        scene = self.show_image_path("./res/sekil_"+str(self.cmb_classes_5.currentIndex())+".png",self.graphicsView_12.size())
        self.graphicsView_12.setScene(scene)
    
    def button_template_labeling_uygula(self):
        self.cmb_classes_5.clear()
        img = color.rgb2gray(io.imread(self.temp_path))
        clr = clear_border(img)
        lbl_img= label(clr)
        
        for index, region in enumerate(regionprops(lbl_img)):
            min_r,min_c,max_r,max_c = region.bbox        
            area = img[min_r:max_r,min_c:max_c]
            io.imsave("./res/sekil_"+str(index)+".png",area)
            
            self.cmb_classes_5.addItem("sekil "+str(index+1))
        
        scene = QGraphicsScene()
        scene = self.show_image_path("./res/sekil_0.png",self.graphicsView_12.size())
        self.graphicsView_12.setScene(scene)

    def button_template_match_uygula(self):
        
        aranan = self.temp_path_match
        bolge_img = io.imread(self.temp_path)
        
        img = cv2.imread(self.temp_path,0)
        img2 = img.copy()
        
        template = cv2.imread(self.temp_path_match,0)
        w, h = template.shape[::-1]

        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                    'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        
        for i,meth in enumerate(methods):
            img = img2.copy()
            method = eval(meth)
            print(meth,method)
            
            res = cv2.matchTemplate(img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)
        
            cv2.rectangle(img,top_left, bottom_right, 255, 2)
            b_img = bolge_img[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]

            
            io.imsave("./res/match/b_"+str(i)+".png",b_img)
            cv2.imwrite("./res/match/mr_"+str(i)+".png",res)
            io.imsave("./res/match/cv_"+str(i)+".png",img)
            
            #scene = QGraphicsScene()
            if(i==0):
                self.graphicsView_15.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_14.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_16.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_17.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_21.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))   
                self.label_3.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))
            if(i==1):
                self.graphicsView_19.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_21.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_20.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_18.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_26.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))   
                self.label_9.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))
            if(i==2):
                self.graphicsView_23.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_25.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_24.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_22.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_34.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))   
                self.label_38.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))        
            if(i==3):
                self.graphicsView_26.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_28.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_29.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_27.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_53.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))   
                self.label_56.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))
            if(i==4):
                self.graphicsView_30.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_32.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_33.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_31.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_62.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))      
                self.label_65.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))           
            if(i==5):
                self.graphicsView_34.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_36.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_37.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_35.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_71.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))   
                self.label_74.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))          
            """if(i==6):
                self.graphicsView_40.setScene(self.show_image_path("./res/match/cv_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_38.setScene(self.show_image_path("./res/match/mr_"+str(i)+".png",self.graphicsView_17.size()))
                self.graphicsView_39.setScene(self.show_image_path(self.temp_path_match,self.graphicsView_17.size()))
                self.graphicsView_41.setScene(self.show_image_path("./res/match/b_"+str(i)+".png",self.graphicsView_17.size()))
                self.label_82.setText(str(self.ssim(aranan,"./res/match/b_"+str(i)+".png")))                   
                self.label_83.setText(str(self.mse(aranan,"./res/match/b_"+str(i)+".png")))    """      

    #metodlar
    def show_image_path(self,img_path,size):
        self.pixmap = Qt.QPixmap()
        self.pixmap.load(img_path)
        self.pixmap = self.pixmap.scaled(size, Qt.Qt.KeepAspectRatioByExpanding,transformMode=QtCore.Qt.SmoothTransformation)

        self.graphicsPixmapItem = Qt.QGraphicsPixmapItem(self.pixmap)

        self.graphicsScene = override_graphicsScene(self)
        self.graphicsScene.addItem(self.graphicsPixmapItem)
        
        self.img_temel_orjinal.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_orjinal.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_sonuc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_sonuc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_once.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_once.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_sonra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_temel_hist_sonra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_rotate.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.img_diger_rotate.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        return self.graphicsScene
    
    def show_image(self,img,width,height):
        show_image=ImageQt(img)
        pixMap=QtGui.QPixmap.fromImage(show_image)
        pixMap=pixMap.scaled(width-5,height-5)
        pixItem=QtGui.QGraphicsPixmapItem(pixMap)
        scene=QGraphicsScene()
        scene.addItem(pixItem)
        return scene
    
    def ssim(self,img1,img2):
        img_1 = cv2.imread(img1)
        img_2 = cv2.imread(img2)
        
        img_1 = cv2.cvtColor(img_1,cv2.COLOR_BGR2GRAY)
        img_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)
        
        return round(_SSIM(img_1,img_2),2)
    
    def mse(self,img1,img2):
        img_1 = cv2.imread(img1)
        img_2 = cv2.imread(img2)
        
        e = np.sum((img_1.astype("float") - img_2.astype("float"))**2)
        e /= float(img_1.shape[0] * img_2.shape[1])
        r = round(e,2)
        return r