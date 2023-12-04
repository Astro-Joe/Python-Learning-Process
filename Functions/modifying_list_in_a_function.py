# A function that shows shows printing 3D designs.

# This will contain two functions.
# The first will show that the 3D designs are being printed.

def design_printer(uncompleted_design, completed_design):
    """Shows the process of printing a 3D design."""
    
    while uncompleted_design:
        current_design = uncompleted_design.pop()
        
        print('-' + current_design.upper() + ' is printing')
        completed_design.append(current_design)
    
    print('\n')
    for design in completed_design:
        msg = '-'  + design.upper() + ' has been printed'
        print(msg)


dsgn = ['iphone case', 'NLE pendant', '4PF pendant', 'dodecahedron']
printed_dsgn = []
design_printer(dsgn, printed_dsgn)
            