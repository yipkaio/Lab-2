def calculate_bmi(height,weight):
    print("Height= "+ str(height))
    print("Weight= ", weight)
    BMI = weight/(height*height)
    print("BMI= ",round(BMI,2))
    if BMI<18.5:
        print("Under Weight")
    elif BMI>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")
        
calculate_bmi(weight=30,height=1.8)
calculate_bmi(weight=70,height=1.8)
calculate_bmi(weight=90,height=1.8)
