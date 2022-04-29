import os, sys
import tkinter            as tk
import tkinter.filedialog as dialog


# ========================================================= #
# ===  open__fileDialogBox                              === #
# ========================================================= #
def open__fileDialogBox( event=None, filetypes=[("","*")], getDirectoryPath=False, \
                         tkString=False, returnType="path", initDir=None ):

    # ------------------------------------------------- #
    # --- [1] arguments                             --- #
    # ------------------------------------------------- #
    if   ( type( filetypes ) is str ):
        filetypes = [ filetypes ]
    elif ( type( filetypes ) is list ):
        pass
    else:
        filetypes = ["","*"]
    if ( initDir is None ):
        initDir  = os.path.abspath( os.path.dirname( __file__ ) )

    # ------------------------------------------------- #
    # --- [2] call file dialog box                  --- #
    # ------------------------------------------------- #
    if ( getDirectoryPath ):
        path = dialog.askdirectory   ( initialdir=initDir )
    else:
        path = dialog.askopenfilename( initialdir=initDir, filetypes=filetypes )

    # ------------------------------------------------- #
    # --- [3] store in tkString                     --- #
    # ------------------------------------------------- #
    if   ( tkString is None ):
        tkString = None
    elif ( ( type( tkString ) is bool ) and ( tkString is True ) ):
        tkString = tk.StringVar()
    elif (   type( tkString ) is type( tk.StringVar() ) ):
        pass
    else:
        tkString = None
    if ( tkString is not None ):
        if ( len( path ) == 0 ):
            tkString.set( "No file selection :: cancelled...." )
        else:
            tkString.set( path )

    # ------------------------------------------------- #
    # --- [3] return type                           --- #
    # ------------------------------------------------- #
    if   ( returnType.lower() == "path" ):
        return( path )
    elif ( returnType.lower() == "tk"   ):
        return( tkString )
    elif ( returnType.lower() == "both" ):
        return( path, tkString )
    else:
        return( path )


# ========================================================= #
# ===   Execution of Pragram                            === #
# ========================================================= #

if ( __name__=="__main__" ):
    ret = open__fileDialogBox()
    print( ret )
