    """Jhon affraids of death. Once he met a fortune teller. She told him that he would die when he reached 90 years old. 
    Help Jhon to write a program which will tell him the of his death. 
    He wants to enter the proposal age and recieves the answer.

    - Level: for beginners"""
    
    # adding date library into our program to detect current year
    from datetime import datetime

    #input fields
    name = input ("Enter character\'s name ")
    current_age = int(input ("Enter character\'s age "))
    death_year = int(input("Please enter character\'s age of death "))

    #making calculation
    current_year = datetime.today().year
    print (current_year + (death_year - current_age) "- character\'s age of death")

    # 90 - is the age when Jhon dies according to fortune teller words
    if death_year > 90:
        print(str(name.title()), "seems you want to live forever")
    
    # 65 - is the common age when Jhon dies according to statistik
    elif death_year <= 65:
        print ("Is your caharacter going to commit a suicide? Don\'t think so. So please re-enter", name, "age of death")
        death_year = input("Please enter character\'s age of death ")
    else:
        print(str(name.title()), "don\'t be sad, you don't need to beleve a fortune teller \n this is only a joke :)")
