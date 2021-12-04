help = ("Welcome to the full help panel, which is only shown upon direct request of it."
        "\n Pressing 'r' at any time will restart where you left. Useful if you want to change a number."
        "\n Pressing 'x' will terminate the program."
        "\n Pressing 'h' will open the \x1B[3mhelp\x1B[0m panel you are seeing."
        "\nFor Choice 1, the allowed operators to use are sum (+), substraction (-), multiplication (*), division (/) and floor division (//)."
        "\nFor Choice 2, you can calculate powers, square roots and logarithms."
        "\nFor Choice 3, you can calculate percentages and values fluctuations over time."
        "\n To calculate what is the 27 percent of 386 use the operator '%'. Example: 27 % 386 (~104)." 
        "\n To calculate what percentage does a number represent in another, use the operator 'in'. Example: 27 in 386 (~7%)."
        "\n To calculate the increase a value has had, use the operator 'inc' (increase). Example: 32 inc 56 (increase of ~57%).")

# Slices
CORE_SLC = help[80:277]
C1_SLC = help[278:410]
C2_SLC = help[410:478]
C3_SLC = help[478:881]

# Italics: \x1B[3mhelp\x1B[0m