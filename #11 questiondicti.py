# Create a dictionary and take input from the users
# and return the meaning of word from dictionary....

oxford = {"HTML":"hypertext markup language","JS":"java script","CSS":"cascading style sheets","NODE":"fetch Api's"}

while(True):
    print(oxford.keys())
    word = input("choose any word from above:")
    print(f"{word.upper()} = {oxford[word.upper()]}")   #important

