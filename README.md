# niceplot
A simple matplotlib wrapper which enables single-call plot generation, without needing to include all the matplotlib setup calls every time. Several "rules" for generating visually-appealing scientific plots are also included (e.g. requiring axis labels).

The basic syntax accepts arguments 

X_data - a 2D list of X values... e.g.[X_data0,X_data1] 

Y_data - a 2D list of corresponding Y values... e.g.[Y_data0,Y_data1] 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# For the simple case:

X_data = np.linspace(0,10,20) (creating the x range )

Y_data = X_data**2 (the x range squared)

#! plot([X_data], [Y_data])

![Screenshot 2024-01-31 at 4 51 08 PM](https://github.com/ExSiTE-Lab/niceplot/assets/112980447/957eaef1-9b78-49ef-877d-d296c01caa8d)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can see we have left out some major component of a "good plot" this being "Title, xlabel, lable and the dataname"
lets add these in with some simple keyword arguments

xlabel - a string of the title of the x axis

ylabel - a string of the title of the y axis

title - a string of the title

labels - a list of strings that correspond to title of each dataset

Lets try it out... dont forget your Units!😤😤

plot([X_data], [Y_data], title="Test Plot",  xlabel="x values (arb. u.)", xlabel="x^2 values (arb. u.)", labels=["Best Data"])

![Screenshot 2024-01-31 at 6 07 39 PM](https://github.com/ExSiTE-Lab/niceplot/assets/112980447/facc64cc-1b1f-4829-a127-fd0cb7f72ab3)

🤯 Much Better!

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



markers can be single-character color and form codes ("k-" = "black line", "b." = "blue dots" and so on), or comma-separated ("blue,:" = "blue dotted", "#9a1ee0" = "purple, default markers")
