import os, sys, inspect
import cv2
import numpy       as np
import tkinter     as tk
import tkinter.ttk as ttk
import matplotlib.pyplot                 as plt
import matplotlib.backends.backend_tkagg as btk
import nkGUI.open__fileDialogBox         as fdb


# ========================================================= #
# ===  gui__base.py                                 === #
# ========================================================= #

class gui__base( ttk.Frame ):
    
    # ========================================================= #
    # ===  initialize                                       === #
    # ========================================================= #
    def __init__( self, root=None, width=400, height=800 ):
        super().__init__( root, width=width, height=height, \
                          borderwidth=3, relief="groove" )
        # ------------------------------------------------- #
        # --- [1] variables                             --- #
        # ------------------------------------------------- #
        self.root        = root
        self.widgets     = {}
        self.params      = {}
        self.values      = {}
        self.labels      = {}
        self.posits      = {}
        self.functions   = {}
        self.Menu_Entity = None
        self.Menus       = {}
        # ------------------------------------------------- #
        # --- [2] set values                            --- #
        # ------------------------------------------------- #
        self.set__params()
        self.set__labels()
        self.set__functions()
        self.set__positions()
        # ------------------------------------------------- #
        # --- [3] widgets                               --- #
        # ------------------------------------------------- #
        self.create__widgets()
        
        # ------------------------------------------------- #
        # --- [4] placemant                             --- #
        # ------------------------------------------------- #
        self.place__widgets( verbose=True )
        self.pack_propagate( False ) # to stop shrinking into minimum size.
        self.pack()


    # ========================================================= #
    # ===  set function name                                === #
    # ========================================================= #
    def set__functions( self ):

        # ------------------------------------------------- #
        # ---   store associated function name          --- #
        # ------------------------------------------------- #
        return()


    # ========================================================= #
    # ===  set Parameters                                   === #
    # ========================================================= #
    def set__params( self ):

        # ------------------------------------------------- #
        # ---   store parameters to be used             --- #
        # ------------------------------------------------- #
        return()


    # ========================================================= #
    # ===  set label name                                   === #
    # ========================================================= #
    def set__labels( self ):

        # ------------------------------------------------- #
        # ---   store lable for each widget             --- #
        # ------------------------------------------------- #
        return()


    # ========================================================= #
    # ===  set position of the widgets                      === #
    # ========================================================= #
    def set__positions( self ):

        # posits (list) :: [ relx, rely, relwidth, relheight, anchor ]
        
        # ------------------------------------------------- #
        # ---     specify position directory            --- #
        # ------------------------------------------------- #
        return()


    # ========================================================= #
    # ===  create widgets                                   === #
    # ========================================================= #
    def create__widgets( self ):

        # ------------------------------------------------- #
        # ---   put widgets                             --- #
        # ------------------------------------------------- #
        return()
    

    # ========================================================= #
    # ===  widgets to open file                             === #
    # ========================================================= #
    def widgets__FileOpen( self, key=None ):
        
        if ( key is None ): sys.exit( "[widgets__FileOpen] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] File Open Set                         --- #
        # ------------------------------------------------- #
        ekey, bkey, dkey   = [ key+suffix for suffix in [ ".entry", ".button", ".dialog" ] ]
        self.values [key]  = tk.StringVar()
        self.widgets[ekey] = ttk.Entry ( self, textvariable=self.values[key] )
        self.widgets[bkey] = ttk.Button( self, text=self.labels[bkey], \
                                         command=lambda:self.functions[bkey]( **{"key":key} ) )
        self.widgets[dkey] = ttk.Button( self, text=self.labels[dkey], \
                                         command=lambda:self.functions[dkey]( **{"key":key} ) )

        
    # ========================================================= #
    # ===  widgets of Spinbox                               === #
    # ========================================================= #
    def widgets__Spinbox( self, key=None ):

        min_,max_,ini_,inc_ = 0, 1, 2, 3
        if ( key is None ): sys.exit( "[widgets__Spinbox] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] spinbox for parameters                --- #
        # ------------------------------------------------- #
        lkey                = "{}.label".format( key )
        self.widgets[lkey]  = ttk.Label( self, text=self.labels[key] )
        self.values [key]   = tk.StringVar()
        self.values [key].set( str( self.params[key][ini_] ) )
        self.widgets[key]   = ttk.Spinbox( self, state="readonly", \
                                           textvariable=self.values[key], \
                                           from_       =self.params[key][min_], \
                                           to_         =self.params[key][max_], \
                                           increment   =self.params[key][inc_]  )
        

    # ========================================================= #
    # ===  widgets for adjust in parameters                 === #
    # ========================================================= #
    def widgets__adjustParams( self, key=None ):

        min_,max_,ini_,inc_ = 0, 1, 2, 3
        borderwidth         = 8
        if ( key is None ): sys.exit( "[widgets__adjustParams] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] adjust set widgets                    --- #
        # ------------------------------------------------- #
        lkey,sckey,spkey    = [ key+suffix for suffix in [ ".label", ".scale", ".spinb" ] ]
        self.widgets[lkey]  = ttk.LabelFrame( self, text=self.labels[key], \
                                              borderwidth=borderwidth, labelanchor=tk.N )
        self.values [key]   = tk.StringVar()
        self.values [key].set( str( self.params[key][ini_] ) )
        self.widgets[sckey] = ttk.Scale  ( self, variable=self.values[key], \
                                           orient        =tk.HORIZONTAL, \
                                           from_         =self.params[key][min_], \
                                           to_           =self.params[key][max_], \
                                           command       =lambda event: self.functions[key]() )
        self.widgets[spkey] = ttk.Spinbox( self, state   ="readonly", \
                                           textvariable  =self.values[key], \
                                           from_         =self.params[key][min_], \
                                           to_           =self.params[key][max_], \
                                           increment     =self.params[key][inc_], \
                                           command       =lambda      : self.functions[key]() )
        # --- [Caution] :: ttk.Scale takes 1 positional argument.
        #                  Be carefull when you use lambda.                   --- #

        
    # ========================================================= #
    # ===  window of a matplotlib                           === #
    # ========================================================= #
    def window__matplotlib( self, key=None ):
        
        if ( key is None ): sys.exit( "[window__matplotlib] key == ???" )
            
        # ------------------------------------------------- #
        # --- [1] set figure area                       --- #
        # ------------------------------------------------- #
        fig                = plt.figure()
        ax                 = fig.add_axes( [0,0,1,1] )
        canvas             = btk.FigureCanvasTkAgg( fig, self.root )
        plot_entity,       = ax.plot( [], [], color="RoyalBlue", linewidth=1.2 )
        self.values [key]  = [ fig, ax, plot_entity, canvas ]
        self.widgets[key]  = canvas.get_tk_widget()
        self.functions[key]()


    # ========================================================= #
    # ===  draw__opencvWindow                               === #
    # ========================================================= #
    def draw__opencvWindow( self, event=None, key=None ):

        fig_, ax_, pE_, canvas_ = 0, 1, 2, 3
        name_, img_             = 0, 1
        if ( key is None ): sys.exit( "[draw__opencvWindow] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] plot area                             --- #
        # ------------------------------------------------- #
        fig, ax = ( self.values[key] )[0:2]
        ax.set_position( [ 0.05, 0.05, 0.9, 0.9 ] )
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        fig.patch.set_facecolor( "black" )
        fig.patch.set_alpha( 1.0 )
        # ------------------------------------------------- #
        # --- [2] image opencv                          --- #
        # ------------------------------------------------- #
        if ( self.params[key] is not None ):
            self.params[key][img_] = cv2.imread  ( self.params[key][name_] )
            img_rgb                = cv2.cvtColor( self.params[key][img_] , cv2.COLOR_BGR2RGB )
        else:
            img_rgb                = np.array( [ [0,0,0] ] )
            self.params[key]       = [ None, img_rgb ]
        self.values[key][pE_] = ax.imshow( img_rgb )
        self.values[key][canvas_].draw()


    # ========================================================= #
    # ===  place widgets ( relative position )              === #
    # ========================================================= #
    def place__widgets( self, verbose=True, anchor_default=tk.NW ):

        into_tkAnchor = { "w" :tk.W , "e" :tk.E , "s" :tk.N , "n" :tk.N , "center":tk.CENTER, \
                          "sw":tk.SW, "se":tk.SE, "nw":tk.NW, "ne":tk.NE }
        
        # ------------------------------------------------- #
        # --- [1] for every widgets place               --- #
        # ------------------------------------------------- #
        common_keys   = set( self.widgets.keys() ) & set( self.posits.keys() )
        not_specified = set( self.widgets.keys() ) - set( self.posits.keys() )
        if ( verbose ):
            print( "\n\n" + "[define__gui.place__widgets] common keys   :: " )
            for ik,key in enumerate( common_keys   ):
                print( "     {0:15}".format( key ), end="" )
                if ( (ik+1)%3 == 0 ): print()
                
            print( "\n\n" + "[define__gui.place__widgets] not specified :: " )
            for ik,key in enumerate( not_specified ):
                print( "     {0:15}".format( key ), end="" )
                if ( (ik+1)%3 == 0 ): print()
            print()
    
        # ------------------------------------------------- #
        # --- [2] place widgets                         --- #
        # ------------------------------------------------- #
        for ik,key in enumerate( common_keys ):
            posits = self.posits[key]

            # ------------------------------------------------- #
            # --- [2-1] irregular value check               --- #
            # ------------------------------------------------- #
            if   ( len( posits ) == 5 ):
                pass
            elif ( len( posits ) == 4 ):
                posits += [ anchor_default ]
            elif ( len( posits ) == 3 ):
                posits += [ None, anchor_default ]
            elif ( len( posits ) == 2 ):
                posits += [ None, None, anchor_default ]
            else:
                print( "[define__gui.py::place__widgets] unknown posits..." )
                print( "[define__gui.py::place__widgets] ", posits )
                sys.exit()
            if ( type( posits[4] ) is None ):
                posits[4] = anchor_default
            if ( type( posits[4] ) is str ):
                try:
                    posits[4] = into_tkAnchor[ ( posits[4] ).lower() ]
                except KeyError:
                    print( "[define__gui.py::place__widgets] unknown anchor:(posits[4])..." )
                    print( "[define__gui.py::place__widgets] ", posits )
                    sys.exit()
            if ( not( posits[4] in into_tkAnchor.values() ) ):
                print( "[define__gui.py::place__widgets] unknown posits..." )
                print( "[define__gui.py::place__widgets] ", posits )
                sys.exit()
                
            # ------------------------------------------------- #
            # --- [2-2] actual placement                    --- #
            # ------------------------------------------------- #
            relx, rely, relw, relh, anchor = posits
            self.widgets[key].place( relx=relx, rely=rely, \
                                     relwidth=relw, relheight=relh, anchor=anchor )
        return()


    # ========================================================= #
    # ===  load file Button ( call by widgets__FileOpen )   === #
    # ========================================================= #
    def load__fileButton( self, event=None, key=None ):

        # - [action] - press button
        #                 -> store file path in Entry.
        #              >> into self.params[ ( self.params[key] ) ]
        #              :: self.params[key] == params's key ( where to save )
        #                                        should be window's name ( e.g. plot01 )
        #              :: self.params[ self.params[key] ] = ( path, None )
        # - [action]
        
        if ( key is None ): sys.exit( "[load__fileButton] key == ???" )
        
        # ------------------------------------------------- #
        # --- [1] get File path from Entry              --- #
        # ------------------------------------------------- #
        ekey = key + ".entry"
        path = ( self.widgets[ekey].get() )
        if ( not( os.path.exists( path ) ) ):
            print( "\n" + "[define__gui.py] Cannot find such a file... [ERROR] "   )
            print(        "[define__gui.py]  filename :: {}".format( path ) + "\n" )
            return()
        # ------------------------------------------------- #
        # --- [2] if the path is directory              --- #
        # ------------------------------------------------- #
        if ( os.path.isdir( path ) ):
            path = fdb.open__fileDialogBox( initDir=path )
        # ------------------------------------------------- #
        # --- [3] set path to the variable              --- #
        # ------------------------------------------------- #
        if ( os.path.isfile( path ) ):
            self.values [key].set( path )
            target               = self.params [key]   # where to store the [ path & Data ]
            self.params[target]  = [ path, None ]
            self.functions[key]()
        else:
            print( "\n" + "[define__gui.py] path is NOT file path... [ERROR] "   )
            print(        "[define__gui.py]  filename :: {}".format( path ) + "\n" )
        return()
    
            
    # ========================================================= #
    # ===  load__fileDialog ( call by widgets__FileOpen )   === #
    # ========================================================= #
    def load__fileDialog( self, event=None, key=None  ):

        # - [action] - press button
        #                 -> store file path in Entry.
        #              >> into self.params[ ( self.params[key] ) ]
        #              :: self.params[key] == params's key ( where to save )
        #                                        should be window's name ( e.g. plot01 )
        #              :: self.params[ self.params[key] ] = ( path, None )
        # - [action]

        if ( key is None ): sys.exit( "[load__fileDialog] key == ???" )

        # ------------------------------------------------- #
        # --- [1] open Dialog Box & set it in variable  --- #
        # ------------------------------------------------- #
        path = fdb.open__fileDialogBox()
        if ( len( path ) == 0 ):
            return
        self.values [key].set( path )
        target               = self.params [key]   # where to store the [ path & Data ]
        self.params[target]  = [ path, None ]
        self.functions[key]()
        return()

    
# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    ret = define__gui()







        # # ------------------------------------------------- #
        # # --- [1] Entry widgets                         --- #
        # # ------------------------------------------------- #
        # #  -- for multi line text input,                --  #
        # #  --    use tk.Text, instead                   --  #
        # # ------------------------------------------------- #
        # self.widgets["Entry01"] = ttk.Entry( self )

        # # ------------------------------------------------- #
        # # --- [2] Button widgets                        --- #
        # # ------------------------------------------------- #
        # self.functions["Button01"] = self.function
        # self.widgets  ["Button01"] = ttk.Button( self, text="update", \
        #                                          command=self.functions["Button01"] )
        
        # # ------------------------------------------------- #
        # # --- [3] Label widgets                         --- #
        # # ------------------------------------------------- #
        # #  -- for multi line message,                   --  #
        # #  --    use tk.Message, instead                --  #
        # # ------------------------------------------------- #
        # self.widgets["Label01"] = ttk.Label( self, text="Label", width=200 )

        # # ------------------------------------------------- #
        # # --- [4] Checkbutton widgets                   --- #
        # # ------------------------------------------------- #
        # self.values ["Checkbutton01"] = tk.BooleanVar()
        # self.widgets["Checkbutton01"] = ttk.Checkbutton( self, text="Checkbutton", \
        #                                                  variable=self.values["Checkbutton01"] )
        
        # # ------------------------------------------------- #
        # # --- [5] Radiobutton widgets                   --- #
        # # ------------------------------------------------- #
        # key   = "Radiobutton01"
        # items = { "A":"A", "B":"B", "C":"C" }
        # self.values [key]  = tk.StringVar()
        # self.params [key]  = items
        # for ik,item_key in enumerate( self.params[key].keys() ):
        #     wkey               = "{0}-{1}".format( key, item_key )
        #     text,value         =  item_key, self.params[key][item_key] 
        #     self.widgets[wkey] = ttk.Radiobutton( self, text=text, value=value,\
        #                                           variable=self.values[key] )

        # # ------------------------------------------------- #
        # # --- [6] Combobox widgets                      --- #
        # # ------------------------------------------------- #
        # self.values ["Combobox01"] = tk.StringVar()
        # self.params ["Combobox01"] = [ "type-A", "type-B", "type-C" ]
        # self.widgets["Combobox01"] = ttk.Combobox( self, textvariable=self.values["Combobox01"],\
        #                                            values=self.params["Combobox01"] )

        # # ------------------------------------------------- #
        # # --- [7] Scale widgets                         --- #
        # # ------------------------------------------------- #
        # self.values ["Scale01"] = tk.DoubleVar()
        # self.params ["Scale01"] = [ 0, 10 ]
        # self.widgets["Scale01"] = ttk.Scale( self, variable=self.values["Scale01"], \
        #                                      orient=tk.HORIZONTAL, length=200, \
        #                                      from_=self.params["Scale01"][0], \
        #                                      to_  =self.params["Scale01"][1], \
        #                                      command=self.draw__matplotlibWindow )
        
        # # ------------------------------------------------- #
        # # --- [6] Spinbox widgets                       --- #
        # # ------------------------------------------------- #
        # self.params ["Spinbox01"] = ["Type-A", "Type-B", "Type-C"]
        # self.widgets["Spinbox01"] = ttk.Spinbox( self, values=self.params["Spinbox01"] )
        # self.widgets["Spinbox02"] = ttk.Spinbox( self, values=self.params["Spinbox01"] )


        
        # # ------------------------------------------------- #
        # # --- [8] File Dialog Box Button                --- #
        # # ------------------------------------------------- #
        # self.widgets["FileDialog01"] = ttk.Button( self, text="Open File",\
        #                                            command=fdb.open__fileDialogBox )
        
        # # ------------------------------------------------- #
        # # --- [10] menu widgets                         --- #
        # # ------------------------------------------------- #
        # self.Menu_Entity     = tk.Menu( self.root )
        # self.Menus["menu01"] = tk.Menu( self.Menu_Entity, tearoff=False )
        # self.Menus["menu01"].add_command( label="command01", command=self.function )
        # self.Menus["menu01"].add_command( label="command02", command=self.function )
        # self.Menus["menu02"] = tk.Menu( self.Menu_Entity, tearoff=False )
        # self.Menus["menu02"].add_command( label="command01", command=self.function )
        # self.Menus["menu02"].add_command( label="command02", command=self.function )
        # self.Menu_Entity.add_cascade( label="menu01", menu=self.Menus["menu01"] )
        # self.Menu_Entity.add_cascade( label="menu02", menu=self.Menus["menu02"] )
        # self.root.config( menu=self.Menu_Entity )
        
