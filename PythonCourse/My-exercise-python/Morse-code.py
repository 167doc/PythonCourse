choice=input("Do you wish to encode or decode? (e/d)\n")
if choice=="d":
        coded_message=input("Enter Morse-code to decode")             #Morse-code into -> text
        coded_message_list=coded_message.split(" ")
        morse_letters = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
            "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
            "-.--", "--.."]

        alphabetic_letters = "abcdefghijklmnopqrstuvwxyz"
        decoded_message=""

        for morse_letter in coded_message_list: # The loop repeats for each element in the list.
            alphabetic_letter="?"
            if morse_letter in morse_letters:
                letter_num=morse_letters.index(morse_letter)
                alphabetic_letter=alphabetic_letters[letter_num]
                decoded_message+=alphabetic_letter
            else:
                decoded_message+="?"
        print(decoded_message)

else:                                                               #Text -> Morse-code
    encoded_message=""    
    decoded_message=input("Enter your message for encoding\n").lower()
    morse_letters = [
                ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                "-.--", "--.."]
    
    alphabetic_letters = "abcdefghijklmnopqrstuvwxyz"
    for alphabethic_letter in decoded_message:
        if alphabethic_letter in alphabetic_letters:
              letter_num=alphabetic_letters.index(alphabethic_letter)
              morse_letter=morse_letters[letter_num]
              encoded_message= encoded_message + morse_letter + " "
        
    print(f"Zakódovaná zpráva: {encoded_message}")

