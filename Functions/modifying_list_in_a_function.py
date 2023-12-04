# A function that shows shows printing 3D designs.

# This will contain two functions.
# The first will show that the 3D designs are being printed.

def printin_design(uncompleted_design, completed_design):
    """A function that shows that 3D designs are being printed."""
    
    while uncompleted_design:
        current_design = uncompleted_design.pop()
        
        print(current_design.title() + ' is printing')
        completed_design.append(current_design)
        

            