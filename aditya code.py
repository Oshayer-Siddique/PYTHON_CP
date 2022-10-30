from qiskit.visualization import plot_bloch_vector

%matplotlib inline
print("You Have Only Three Chances!")
n=0
while n<3 :
    x= int(input(" Put the possible x[ -1 to 1 ] coordinate for the qubit = "))
    y= int(input(" Put the possible y[ -1 to 1 ] coordinate for the qubit = "))
    z= int(input(" Put the possible z[ -1 to 1 ] coordinate for the qubit = "))
    
    plot_bloch_vector([x,y,z], title="Your Bloch Sphere")
    if x == 0 and y == 1 and z == 0 :
        print("\x1b[1;32;43m Congratulations , You Got It Right! \x1b[0;0m")
        break
    
    else :
        print("\033[1;31;43m Opps! Try Again.\033[0;0m]")
    
        n=n+1
    if n==3 :
        print("\033[1;33;43m Sorry , Better Luck Next Time \033[0;0m] ")