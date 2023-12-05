# A function that shows the process of printing 3D designs.

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


# dsgn = ['iphone case', 'NLE pendant', '4PF pendant', 'dodecahedron']
# printed_dsgn = []

# design_printer(dsgn[:], printed_dsgn) # Allows the function to work on the liust without affecting the original list
# design_printer(dsgn, printed_dsgn)
# print(dsgn)
            