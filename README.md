# Beeline Report to Centerstone Upload
Transforms Beeline Contractor reports for importing into Centerstone CAFM software 

If you use both Beeline and Centerstone for HR and facilities management then this script will come in handy when you have to constantly upload new contractors into Centerstone. This script uses a basic GUI to request an input Excel file (the auto-generated Beeline report) and then requests a save location. Super simple, but effective. 

To use this script input the following commands into your Terminal: 

    $ cd ~ 
    
    $ git clone https://github.com/trevorpburke/beeline_to_centerstone.git

    $ cd beeline_to_centerstone

    $ python script.py path/to/excel/file 


And there you go! 
