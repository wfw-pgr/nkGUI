import os, sys, inspect
import cv2
import numpy       as np
import tkinter     as tk
import tkinter.ttk as ttk
import matplotlib.pyplot                 as plt
import matplotlib.backends.backend_tkagg as btk
import nkGUI.gui__base as gui


# ========================================================= #
# ===  define_gui                                       === #
# ========================================================= #

class define__gui:

    # ========================================================= #
    # ===  constructor                                      === #
    # ========================================================= #
    def __init__( title="gui", width=None, height=None ):

        # ------------------------------------------------- #
        # --- [1] arguments                             --- #
        # ------------------------------------------------- #
        if ( width  is None ):
            width  = 400
            print( "[define__gui.py] default {0:12} : {1}  is used.".format( "width" , width  ) )
        if ( height is None ):
            height = 800
            print( "[define__gui.py] default {0:12} : {1}  is used.".format( "height", height ) )
        
        # ------------------------------------------------- #
        # --- [2] define gui application                --- #
        # ------------------------------------------------- #
        frame = tk.Tk()
        frame.title   ( title )
        frame.geometry( "{0}x{1}".format( width, height ) )
        base  = gui__edit( frame, width=width, height=height )
        frame.mainloop()


# ========================================================= #
# ===  gui__edit                                        === #
# ========================================================= #

class gui__edit( gui.gui__base ):

    # ========================================================= #
    # ===  initialize of the class                          === #
    # ========================================================= #
    def __init__( self, root=None, width=400, height=800 ):
        super().__init__( root, width=width, height=height )

    # ========================================================= #
    # ===  Parameter Setting part                           === #
    # ========================================================= #
        
    # ========================================================= #
    # ===  set function name                                === #
    # ========================================================= #
    def set__functions( self ):

        # ------------------------------------------------- #
        # ---   store associated function name          --- #
        # ------------------------------------------------- #
        self.functions["Adjust01"]          = lambda: self.update__opencvWindow( key="opencv" )
        self.functions["Adjust02"]          = lambda: self.update__opencvWindow( key="opencv" )
        self.functions["Adjust03"]          = lambda: self.update__opencvWindow( key="opencv" )
        self.functions["FileOpen01.button"] = self.load__fileButton
        self.functions["FileOpen01.dialog"] = self.load__fileDialog
        self.functions["FileOpen01"]        = lambda: self.draw__opencvWindow  ( key="opencv" )
        self.functions["opencv"]            = lambda: self.draw__opencvWindow  ( key="opencv" )

        return()


    # ========================================================= #
    # ===  set Parameters                                   === #
    # ========================================================= #
    def set__params( self ):

        # ------------------------------------------------- #
        # ---   store parameters to be used             --- #
        # ------------------------------------------------- #
        #   < params > [ min, max, init, increment ]   #
        self.params["Spinbox01"]   = [ 0, 255,  90,   1 ]  
        self.params["Spinbox02"]   = [ 0, 255, 110,   1 ] 
        self.params["Spinbox03"]   = [ 0,   5, 1.5, 0.1 ]
        self.params["Adjust01"]    = [ 0, 200, 110,   1 ]
        self.params["Adjust02"]    = [ 0, 200,  20,   1 ]
        self.params["Adjust03"]    = [ 0, 200, 120,   1 ]
        #   < params > None :: initialize
        self.params["opencv"]      = None

        #   < params > target params key to store file name & Data #
        self.params["FileOpen01"]  = "opencv"
        
        return()


    # ========================================================= #
    # ===  set label name                                   === #
    # ========================================================= #
    def set__labels( self ):

        # ------------------------------------------------- #
        # ---   store lable for each widget             --- #
        # ------------------------------------------------- #
        self.labels["Spinbox01"]          = "threshold1"
        self.labels["Spinbox02"]          = "threshold2"
        self.labels["Spinbox03"]          = "dp"
        self.labels["Adjust01"]           = "min_Distance"
        self.labels["Adjust02"]           = "min_Radius"
        self.labels["Adjust03"]           = "max_Radius"
        self.labels["FileOpen01.button"]  = "Load"
        self.labels["FileOpen01.dialog"]  = "Open File"

        return()


    # ========================================================= #
    # ===  set position of the widgets                      === #
    # ========================================================= #
    def set__positions( self ):

        # posits (list) :: [ relx, rely, relwidth, relheight, anchor ]
        
        # ------------------------------------------------- #
        # ---     specify position directory            --- #
        # ------------------------------------------------- #
        self.posits ["FileOpen01.entry"]  = [  0.05, 0.03, 0.70, None ]
        self.posits ["FileOpen01.button"] = [  0.77, 0.03, 0.18, None ]
        self.posits ["FileOpen01.dialog"] = [  0.05, 0.07, 0.90, None ]
        self.posits ["Spinbox01"]         = [  0.05, 0.13, 0.20, None ]
        self.posits ["Spinbox01.label"]   = [  0.05, 0.11, 0.20, None ]
        self.posits ["Spinbox02"]         = [  0.40, 0.13, 0.20, None ]
        self.posits ["Spinbox02.label"]   = [  0.40, 0.11, 0.20, None ]
        self.posits ["Spinbox03"]         = [  0.75, 0.13, 0.20, None ]
        self.posits ["Spinbox03.label"]   = [  0.75, 0.11, 0.20, None ]
        self.posits ["Adjust01.label"]    = [  0.50, 0.22, 0.90, 0.08, "center" ]
        self.posits ["Adjust01.scale"]    = [  0.08, 0.22, 0.68, None ]
        self.posits ["Adjust01.spinb"]    = [  0.78, 0.22, 0.16, None ]
        self.posits ["Adjust02.label"]    = [  0.50, 0.32, 0.90, 0.08, "center" ]
        self.posits ["Adjust02.scale"]    = [  0.08, 0.32, 0.68, None ]
        self.posits ["Adjust02.spinb"]    = [  0.78, 0.32, 0.16, None ]
        self.posits ["Adjust03.label"]    = [  0.50, 0.42, 0.90, 0.08, "center" ]
        self.posits ["Adjust03.scale"]    = [  0.08, 0.42, 0.68, None ]
        self.posits ["Adjust03.spinb"]    = [  0.78, 0.42, 0.16, None ]
        self.posits ["opencv"]            = [  0.1,  0.50, 0.80, 0.45 ]
        return()


    # ========================================================= #
    # ===  create widgets                                   === #
    # ========================================================= #
    def create__widgets( self ):

        self.widgets__FileOpen    ( key="FileOpen01" )
        self.widgets__Spinbox     ( key="Spinbox01"  )
        self.widgets__Spinbox     ( key="Spinbox02"  )
        self.widgets__Spinbox     ( key="Spinbox03"  )
        self.widgets__adjustParams( key="Adjust01"   )
        self.widgets__adjustParams( key="Adjust02"   )
        self.widgets__adjustParams( key="Adjust03"   )
        self.create__matplotlibWindow( key="opencv" )

    # ========================================================= #
    # ===  user definition functions                        === #
    # ========================================================= #

    # ========================================================= #
    # ===  update__opencv                                   === #
    # ========================================================= #
    def update__opencvWindow( self, event=None, key=None ):

        name_, img_    = 0, 1
        if ( key is None ): sys.exit( "[update__opencvWindow] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] modify opencv images                  --- #
        # ------------------------------------------------- #
        _,ax,pE,canvas = self.values[key]
        th1            =   int(        self.values["Spinbox01"].get()   )
        th2            =   int(        self.values["Spinbox02"].get()   )
        dp             =        float( self.values["Spinbox03"].get() )
        minDist        =   int( float( self.values["Adjust01" ].get() ) )
        minRadius      =   int( float( self.values["Adjust02" ].get() ) )
        maxRadius      =   int( float( self.values["Adjust03" ].get() ) )

        # ------------------------------------------------- #
        # --- [2] canny                                 --- #
        # ------------------------------------------------- #
        img_rgb        = cv2.cvtColor( self.params[key][img_], cv2.COLOR_BGR2RGB  )
        img_gray       = cv2.cvtColor( self.params[key][img_], cv2.COLOR_BGR2GRAY )
        img_gauss      = cv2.GaussianBlur( img_gray, (5,5), 0 )
        img_canny      = cv2.Canny( img_gauss, threshold1=th1, threshold2=th2 )
        circles        = cv2.HoughCircles( img_canny, cv2.HOUGH_GRADIENT, minDist=minDist, \
                                           dp=dp, minRadius=minRadius, maxRadius=maxRadius )
        if ( circles is not None ):
            circles        = circles[0]
            nCircles       = circles.shape[0]
            for circle in circles:
                x, y, r    = int( circle[0] ), int( circle[1] ), int( circle[2] )
                img_show   = cv2.circle( img_rgb, (x, y), r, (255, 255, 0), 4 )
        else:
            img_show = np.copy( img_rgb )
        pE.set_data( img_show )
        canvas.draw()

        
    # ========================================================= #
    # ===  draw__matplotlib                                 === #
    # ========================================================= #
    def draw__matplotlibWindow( self, event=None, key=None ):

        if ( key is None ): sys.exit( "[draw__matplotlibWindow] key == ???" )
        
        params_key    = "Adjust01.scale"
        # ------------------------------------------------- #
        # --- [2] plot area                             --- #
        # ------------------------------------------------- #
        ax,pE,canvas  = ( self.values[key] )[1:]
        ax.set_position   ( [ 0.12, 0.12, 0.90, 0.90 ] )
        ax.set_xticks     ( np.round( np.linspace(  0.0, 1.0, 6 ), 2 ) )
        ax.set_yticks     ( np.round( np.linspace(  0.0, 1.0, 6 ), 2 ) )
        ax.set_xticklabels( np.round( np.linspace(  0.0, 1.0, 6 ), 2 ), fontsize=6 )
        ax.set_yticklabels( np.round( np.linspace(  0.0, 1.0, 6 ), 2 ), fontsize=6 )
        ax.set_xlim( 0.0, 1.0 )
        ax.set_ylim( 0.0, 1.0 )
        # ------------------------------------------------- #
        # --- [3] coefficient & function                --- #
        # ------------------------------------------------- #
        a             = self.widgets[params_key].get()
        x             = np.linspace( 0.0, 1.0, 101 )
        y             = x**a
        # ------------------------------------------------- #
        # --- [4] plot                                  --- #
        # ------------------------------------------------- #
        pE.set_data( x, y )
        canvas.draw()
        
    
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    ret = define__gui()

