from termcolor import colored

def fun_inventory():
  
    print("1.yes\n2.No")
    a = int(input())
    if a == 1:
        inv_list={
        "mushroom":2,
        "knife":1
         }
        print(inv_list)
    else:
      return

def scene_sun():
  
    print("Alas! You got stuck in a desert. You came for a trip in a desert with your friends, but unfortunately there was a sand storm suddenly came because of that sand storm you got missed alone in the desert.You have only the map and the compass, you have also got phone with you but it don't have internet connection...you have also got a lighter with you because you are smoker..")

    print("Then, you are going to find a way out of the desert")
    print("Then, you started walking around the desert....then you find a dates palm tree....then you are giving the signal with the help of the dried leaves in the ground...then, you make a smoke by burning the dried leaves with the lighter...")
    print(" ")
 
    print("1.You'll wait for a long time and expecting your friends to find you \n2.Wait for some times, then you decided to leave that place to find another way")
    print(" ")
    op1=int(input())
    if op1==1:
      print("if you want to wait for a long time you'll just wait for them...they'll not gonna find you because you're far away from them...so you chose the wrong option")
      end()
    else:
        print("yep! it's a right choice..you no need to wait for a long time you just wait for some times then you leave the place and seek for another way to get out of the desert..")
        print("while you are searching for the path to get out of the desert by using map and compass...after a few hours of searching ...you got thirsty, so, you are thinking about the water, then you suddenly see a pond with full of water...then you're running towards it, but it got disapper because it's your bewilderment..")
        print("Now,you need to choose the direction")
    
        print("1.You wants to go in the same direction where you find the imaginary pond \n2.You want to go towards the direction where the compass is pointing")
        op2=int(input())
        if op2==2:
         print("sorry! you chose the wrong decision because in that way you don't get any water so you will die with thirsty")
         end()
        else:
         print("it's really a good choice ")
         print("Because, in this way you will find a real pond after the fake pond")
        print("You have got some water.. you drink it well")
        
        print("Then, you started your searching")
        print("while in your searching process, you see a camel which is searching for the food lonely in the desert... then, you are decided to ride on it to get out of the desert")
        print("you need to chose the way to behave with the camel")
        print(" ")

        print("1.You want to behave strictly with the camel \n2.You want to behave softly with the camel")
        op3=int(input())
        if op3==1:
          print("If you behave strictly or arrogantly with the camel it'll kick the ass out of you.. so you'll end up dead")
          end()
        else:
            print("you chose the right thing..you should handle the animals softly so that only it'll help you with your work")
            print("Then, you are travelling with your camel to find a way out of the desert..")
            print("then your compass showing the directions...But, the compass showing two directions it'll showing north as well as east ..the compass isn't working.. so there is a state of confusion..")
            print("Now, it's your fate..just chose one option to know your luck")
            print("1.Go towards the North direction.\n2.Go towards the East direction.")
            
            op4=int(input())
            if op4 == 1:
               print("OH SHIT!! SORRY HUMAN!! I don't think you have a luck.. it's ok try another game to change your fate..But for now you are dead")
               end()
            else:
              print("SOOO..YOU HAVE A LUCK..try to grab that luck...Now you can travel towards east.. there you can find your friends worrying about you")
              print("You show up yourself with a camel..they're in shock with happy mindset")
              print("Then, you go and complete your trip fully with your friends")
              
              print("Congratulations!!! You successfully escaped from the desert it is the most difficult thing to do with that sad and lonely..you surely a brave human!!!")
              print(colored('The End.','blue'))
  
def scene_winter():
  {}
def scene_center():
  {}
def end():
  print(colored('sorry you are died.', 'red'))
  print(colored('The End...','red'))
def scene_rain():
  
    print("you are entered into a AMAZON RAIN FOREST.")
    print("The rain was pouring heavily and it was a night time,since you need a shelter to spend the night,hence the forest has many dangerous animals, it might kill you.so quickly you need to find a place to stay.")
    print("")
    print("1.At some distance you find a small den, you can spend the night there.\n2.or else you will move on and search for another place to stay.")
    print("")
    op1=int(input())
    if op1==1:
      print("since the den has a lion inside it,soo...")
      end()
    else:
      print("you are luckily got a small hut to spend the night.finally you spent the night there,the next morning, still it's raining heavily because it was a rainy forest,you are very hungry,you need food to eat.")
      print("")
      print("1.There was some mushrooms that are fully grown beside the hut,you can use that.\n2.or you will enter the forest and hunt the animals for food.")
      op2=int(input())
      if op2==2:
        print("since it was raining heavily,it is a challenging task  to find the animals,if you get over wet,it results in janni vanthu sethuruva da.")
        end()
      else:
        print("good choice all the mushrooms are not harmful")
        print("")
        print("You have inventory now. Would you like to see inventory?")
        fun_inventory()
        print("")
        print("After sometime the rain was decreasing slowly,you want to escape from this forest in that point of view you are searching for a way ,at that time you find two caves,you have to choose any one from that.")   
        print("")
        print("1.In the first cave the rain water was flowing into the cave heavily,it was difficult to move inside that cave.\n2.In the second cave there was some THORNY PLANTS in front of that cave and it is difficult to remove those plants.")
        op3=int(input())
        if op3==2:
          print("This cave doesn't have any way,you caught up inside that cave.")
          end()
        else:
          print("good job!,if the water flows ,there must be a way in the other side,so you reached the another side of that cave.still it was raining,most of the trees were fallen due to heavy rain.there was a river in front of you,water was flowing forcefully,you want to cross that river,you don't have time with in today's night you want to get out from that forest.")
          print("")
          print("1.create a boat using that fallen trees and cross the river\n2.check for the another way to cross it.")
          op3=int(input())
          if op3==1:
            print(" creaing a boat takes some time,hence you wasted the time ,as i already said that the water was flowing forcefully,it is impossible to sail")
            end()
          else:
            print("luckily you find a tree which was fallen across the river,using that tree you crossed the river successesfully.after crossing there was a large tree in front of you,suspiciously there was a door in that tree,since the door was being closed ,you want to open the door.since you are tired and the door was very strong it is difficult to break it")
            print("")
            print("1.There was a key which is placed beside the tree and it is made up of wood,it will be helpful.\n2.In the other hand you are going to  open the door using your strength.")
            op4=int(input())
            if op4 == 1:
               print("it is a key,but not the correct key for that door,hence you caught up there.")
               end()
            else:
              print("The door was closed but not locked ,if you push the door ,it will be opened, finally you entered into the tree, there was two ways inside the tree ,you want to select any one from that.")
              print("")
              print("1.In the first way you can hear the sound of water which is flowing\n2.In the second way ,you can hear the noise of bats.")
              op5=int(input())
              if op5==1:
                print("The first way brings you into the same forest,finally you caught up there.") 
                end()
              else:
                print("congrats!!! successfully you escaped from that forest.")
                print(colored('The End.','blue'))
  
print("WELCOME TO ADVENTURE GAME.")
print("")
print("")
print("Rules:You will be given 4 senarios you can choose any one of them as your wish.you will be given a series of tasks based on that senario you need to complete those tasks and escape from that situation.One wrong decision can kill you.you will be given an option to type in a number so enter your number and click the enter key,only enter the valid number.Be careful and good luck.")
print("")
print("")
name=input("Enter your name here:")
print("")
print("")
print(name+" "+"welcome to the game.Try to escape from that situation and try not to die whilst you're at it.Good luck...")
print("")
print("")
print("select the senario:\n")
print(colored('1.Sunny','red'))
print(colored('2.Rainy','blue'))
print('3.Winter')
print(colored('4.center of Earth','green'))
num=int(input())
if num==1:
  scene_sun()
elif num==3:
  scene_winter()
elif num==4:
  scene_center()
else:
  scene_rain()
  
