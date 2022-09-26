try:
    import time         #importing time function
    print('''=====================================================
=========== Welcome to VPS Quiz Masters =============
=====================================================''')
    time.sleep(1)
    print()
    print("Please read the rules of quiz carefully before you start to play")
    print()
    print()
    print("It is recommended that you play the quiz in fullscreen mode")
    time.sleep(2)
    print()
    print()
    print('''
The rules of the quiz are:

-> Each user will be given Five/Ten question per quiz.
-> For each RIGHT ANSWER '4' will be awarded. Whereas for every WRONG ANSWER '1' mark will be DEDUCTED from the total score.
-> If the question is left UNATTEMPTED, no mraks will be awarded or deducted.
-> Enter the input(ONLY DIGIT) after the phrase 'Type your input here: '.
-> The game will proceed once the question displayed is answered.
-> The Total Score will be displyed once all the questions are answered.
-> Here is a sample Question and answering format:

    1.Which is the Scotland's national animal?

    1) Lion
      
    2) Dragon
      
    3) Unicorn
      
    4) Panther

    Type your input here: 

      #The correct answer is "Unicorn". Therefore the correct format(ONLY DIGIT) of answering is:
      
      Type your input here: 3                                          <--ONLY CORRECT SYNTAX

      #Invalid inputs' example:

      Type your input here: 3)                                         }
      Type your input here: 3) Unicorn                                 }Wrong syntax
      Type your input here: Unicorn                                    }''')
    print()
    print("Please read the instuctons carefully until we load the quiz for you....")
    time.sleep(6) # It ensures that the player reads the quiz instuctions throughly
    print('The quiz starts here and "ALL THE BEST"')
    while True: # This condition ensures that the player can play the quiz multiple times without quitting
            print('''=====================================================
          1.Play Genral Knowledge quiz
          2.Play Coumputer Science quiz
          3.Attempt JEE Mains mock test
          4.Rules
          5.Exit''')
    
            n=input('''      Type your input here: ''') # Accepting input to proceed to a type of quiz
            if n=='1':
                marks=0
                correct=0
                wrong=0
                unattem=0
                #The questions start here.
                print('''============================->>> GENERAL KNOWLEDGE QUIZ <<<-===================================
            ''')
                a='''What are the grass lands of South America called?

    1) Pampas

    2) Savanna

    3) Stepes

    4) Prairies'''
                b='''Which of the following is the reason(s) behind the different seasons to occur?

    1) Periodic increase and decrease in activity of Sun

    2) Tilt of Earth's axis

    3) More eccentricity of Earth's orbit around Sun

    4) All of the above'''
                c='''What is the approximate mass of earth in kg?

    1) 6*10^24

    2) 9*10^20

    3) 6*10^23

    4) 1*10^20'''
                d='''Which creature has no bones ?

    1) Seal

    2) Shark

    3) Sea Horse

    4) Blue Whale.'''

                e='''Who among the following is known as “The Saint of Gutters”?

    1) Baba Amte

    2) Mother Teresa

    3) Anna Hazare

    4) None of these'''

                f='''Which one of the following glasses is used in bulletproof screens?

    1) Soda glass

    2) Pyrex glass

    3) Jena glass

    4) Reinforced glass'''

                g='''Who among the following got the Bharat Ratna award before becoming the president of India?

    1) R. Venkataraman

    2) Dr. Rajendra Prasad

    3) W. Giri

    4) Dr. Zakir Hussian'''

                h='''India’s first-ever national police museum will be established in which city?

    1) Chennai

    2) Delhi

    3) Nagpur

    4) Kolkata'''

                i=''' The Maratha and The Kesri were the two main newspapers started by which of the following people?

    1) Lala Lajpat Rai

    2) Gopal Krishna Gokhale

    3) Bal Gangadhar Tilak

    4) Madan Mohan Malviya'''

                j='''National emergency arising out of the war, armed rebellion or external aggression is dealt under which of the following articles?

    1) Article 352

    2) Article 353

    3) Article 356

    4) Article 371'''

                k='''Which of the following personalities is considered to be the originator of the Sankhya philosophy?

    1) Bharata Muni

    2) Kapila Muni

    3) Adi Shankaracharya

    4) Agastya Rishi'''

                l='''Mahatma Gandhi founded which of the following newspapers in 1903 at South Africa?

    1) Indian Opinion

    2) Harijan

    3) Indian Speaker

    4) India News'''

                m='''Which of the following is the capital of Ethiopia?

    1) Abuja

    2) Dar es Salaam

    3) Addis Ababa

    4) Harare'''

                n='''What is the name of the shaft that rotates the shaft in the gear box from the pistons in a typical automobile ?

    1) Crank Shaft

    2) Round Shaft

    3) Drive Shaft

    4) Axle'''

                o='''Which is the capital of the Union Territory of Dadra and Nagar Haveli?

    1) Panaji

    2) Dispur

    3) Silvassa

    4) None of These'''

                p='''Which is the oldest mountain range in India?

    1) Satpura Range

    2) Aravali Range

    3) Vindhya Range

    4) Pir Panjal Range'''

                q='''Chand-Bibi was the ruler of which city?

    1) Delhi

    2) Ahmednagar

    3) Bijapur

    4) Satara'''

                r='''Who is known as the Indian Napoleon?

    1) Samudra Gupta

    2) Skanda Gupta

    3) Ashoka

    4) None of These'''

                s='''Particle having the least mass is:

    1) Electron

    2) Proton

    3) Neutron

    4) None of These'''

                t='''What is the full form of "M.T.R", the name of the famous ready to eat food enterprise?

    1) Madurai Tiffin Room

    2) Madras Tiffin Room

    3) Mangalore Tiffin Room

    4) Mavalli Tiffin Room'''

                u='''Which of these cities does not have an Indian Institute of Management?

    1) Bengaluru

    2) Indore

    3) Ahmedabad

    4) Kharagpur'''

                v='''Which of these poet was popularly known as Vikatakavi?

    1) Chand Bardai

    2) Kalidasa

    3) Banabhatta

    4) Tenali Rama'''

                w='''Which one of following is largest coffee growing country in world?

    1) Brazil

    2) Korea

    3) Singapore

    4) Belgium'''

                x='''Niagara Falls was discovered by

    1) Alexander Eiffel

    2) Louis Hennepin

    3) James Cook

    4) Jean Henry Durant'''

                y='''Who invented Power loom?

    1) Edmund Cartwright

    2) Robert Wilhelm Bunsen

    3) Richard Trevithick

    4) Gaustav Robert Kirchhoff'''
                #This is the dictionary created for answers with the corresponding variables.
                da={a:'1',b:'3',c:'1',d:'2',e:'2',f:'4',g:'3',h:'2',i:'3',j:'1',k:'2',l:'1',m:'3',n:'1',o:'3',p:'2',q:'2',r:'1',s:'1',t:'4',u:'4',v:'4',w:'1',x:'2',y:'1'}
                import random
                #Imported random function to ramdomise 10 questions from 25 questions.
                ys=random.sample([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y],10)
                for i in range(10):
                    while True:
                     print(i+1,".",ys[i],sep="")
                     #Input to accept the answer
                     ans=input('''
    Type your option here: ''')
                 #This is for the negative marking scheme
                     if da[ys[i]]==ans:
                         marks+=4
                         correct+=1
                         break
                     elif ans=='':
                         marks=marks
                         unattem+=1
                         break
                     elif ans=='1' or ans=='2' or ans=='3' or ans=='4':
                         marks-=1
                         wrong+=1
                         break
                     else: #This is for the invalid inputs
                         print()
                         print('     Please enter valid input!!!!!!')
                         continue
                     print()
                print()
                 #This is the code for the result.
                percent=(marks/40)*100
                if percent>=90:
                    print("Congratulations! It was an outstanding performance.")
                elif percent>=70:
                    print("Very good. You posses a great knowledge")
                elif percent>=50:
                    print("Good. You did well")
                else:
                    #printing the result
                    print("Failures are stepping stones for success. Better luck next time")
                print("Your marks are",marks,'out of 40')
                print("Your percentage is",percent,"%")
                print("Number of questions which are answered correctly = ",correct)
                print("Number of questions which are answered wrong = ",wrong)
                print("Number of questions which are unattempted = ",unattem)
                Reply=input("Press ANY KEY to continue or enter 'e' to exit: ")
                print()
                if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'": # This is to exit the quiz after playing
                    break
                else:
                    continue
                print()
            elif n=='2':
                marks=0
                correct=0
                wrong=0
                unattem=0#initialising the variable for correct answer, wrong answer,etc.
                #The questions start here
                print('''============================->>> COMPUTER SCIENCE QUIZ <<<-===================================
            ''')
                A='''Who invented PYTHON Programming language?

        1) Guido Van Rossum

        2) Alexander Grahambell

        3) Michel Widenius

        4) Steve Jobs'''
                B='''Which of the following is not an input device?

        1) Microphone.

        2) Speaker.

        3) Keyboard.

        4) Mouse.'''
                C='''A vertical arrangement of information in a record is termed as:

        1) Row

        2) Vertical row

        3) Column

        4) None of the above'''
                D='''The right expansion of 'SQL' is?

        1) Structured Question Language

        2) Structured Query Language

        3) Syntaxed Query Language

        4) None of the above'''

                E='''Which function in Python is used to determine the MEMORY LOCATION of a variable?

        1) where

        2) address

        3) id

        4) ml'''

                F='''Which of the following are immutable?

        1) Tuple

        2) Lists

        3) Dictionary

        4) None of the above'''
                G='''Which of the following is not a hardware component?

        1) RAM

        2) ROM

        3) Operating system

        4) Processors'''
                H='''Which of the following is not an output device?

        1) Monitor

        2) Printer

        3) RAM

        4) Speaker'''
                I='''Which of the following is not an internal component of a computer?

        1) Monitor

        2) Computer Bus

        3) RAM

        4) ROM'''
                J='''Whcih type of error is raised when the arithmetic expression is too large to be represented?

        1) Index Error

        2) Value Error

        3) Import Error

        4) Overflow Error'''
                K='''Which pdf commands signifies 'list current break points?

        1) p

        2) c

        3) b

        4) cl'''
                L='''By how much (number) has the character limit in the social network Twitter increased now?

        1) 540

        2) 140

        3) 374

        4) 500'''
                M='''What is the predicted output of the following code:

                for i in range(4):
                    for j in range(4,i,-1):
                        print(j, end='')
                    else:
                        print()
                        
                The options are:

            1) 4321
               432
               43
               4

            2) 1
               12
               123
               1234

            3) 4
               44
               444
               4444

            4) 4
               4
               4
               4'''
                N='''Which of the following mathematical function produces 'SQUARE ROOT' of a number?

        1) math.sqrt(num)

        2) math.pow(num)

        3) math.root2(num)

        4) math.floor(num)'''
                O='''Which alphabet represents the presence of a complex number in an expression (In PYTHON)?

        1) i

        2) k

        3) c

        4) j'''
                P='''Who was the chief inventor of MySQL?

        1) Steve Jobs

        2) Bill gates.

        3) Michel Widenius

        4) Guido Van Rossum'''
                Q='''What is the name of the Dolphin in the logo of MySQL?

        1) Shishimaroo
         
        2) Pluto
         
        3) Darling
         
        4) Sakila'''
                R='''Which of the following is not the way in whcih the websites cannot track the user?

        1) IP Address

        2) HTTP Referrer

        3) VPN

        4) User Agent'''
                S='''What is the terminology for 'Unauthorised, monitoring of other people's commnunications'?

        1) Eavesdropping

        2) Phishing

        3) Pharming

        4) None of the above'''
                T='''What is a virus which self replicates itself and eats up the entire disk space?

        1) Snail

        2) Trojan Jorse

        3) Worm

        4) Turtle'''
                U='''What is the answer of 5//-3?

        1) -2

        2) 3

        3) -2.0

        4) 2'''
                V='''Which of the following is a unary operator?

        1) +=

        2) -=

        3) *

        4) ~'''
                W='''Which of the following is not a relational operator?

        1) =

        2) %=

        3) //=

        4) >='''
                X='''Which of the following are not literals in PYTHON?

        1) Keywords

        2) Boolean

        3) String

        4) Numeric'''
                Y='''Which of the following is not a key word in PYTHON?

        1) nonlocal

        2) if

        3) boolean

        4) raise'''
            #the answer key for the questions in the form of dictionary.
                da={A:'1',B:'2',C:'3',D:'2',E:'3',F:'1',G:'3',H:'3',I:'1',J:'4',K:'3',L:'2',M:'1',N:'1',O:'4',P:'3',Q:'4',R:'3',S:'1',T:'3',U:'1',V:'4',W:'1',X:'1',Y:'3'}
                import random
                #Iported random function to ramdomise 10 questions from 25 questions.
                ys=random.sample([A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y],10)
                for i in range(10):
                    while True:
                     print(i+1,".",ys[i],sep="")
                     #Input to accept the answer
                     ans=input('''
    Type your option here: ''')
                 #This is for the negative marking scheme
                     if da[ys[i]]==ans:
                         marks+=4
                         correct+=1
                         break
                     elif ans=='':
                         marks=marks
                         unattem+=1
                         break
                     elif ans=='1' or ans=='2' or ans=='3' or ans=='4':
                         marks-=1
                         wrong+=1
                         break
                     else: #This is for the invalid inputs
                         print()
                         print('     Please enter valid input!!!!!!')
                         continue
                     print()
                print()
                # For calculating the percentage.
                percent=(marks/40)*100
                if percent>=90:
                    print("Congratulations! It was an outstanding performance.")
                elif percent>=70:
                    print("Very good. You posses a great knowledge")
                elif percent>=50:
                    print("Good. You did well")
                else:
                    print("Failures are stepping stones for success. Better luck next time")
                    #Printing result of the quiz.
                print("Your marks are: ",marks,'out of 40')
                print("Your percentage is",percent,"%")
                print("Number of questions which are answered correctly = ",correct)
                print("Number of questions which are answered wrong = ",wrong)
                print("Number of questions which are unattempted = ",unattem)


                Reply=input("Press ANY KEY to continue or enter 'e' to exit: ")
                print()
                if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":
                    break
                else:
                    continue
                print()
            elif n=='3':
                while True:
                    print('''=====================================================
=========== Attempt JEE Mains mock test =============
=====================================================''')
                    print('''
          1.Physics MCQ 
          2.Physics (Integer Type Answer)
          3.Chemistry MCQ
          4.Chemistry (Integer Type Answer)
          5.Mathematics MCQ
          6.Mathematics (Interger Type Answer)
          7.Go to main menu''')
                #The input of the user from the menu.
                    n=input('''
        Type your input here: ''')
                    if n=='1':
                        marks=0
                        correct=0
                        wrong=0
                        un=0 #intialising the variable for right answers, wrong answers,etc.
                        #here are the questions.
                        print('''============================->>> PHYSICS OBJECIVE TYPE QUIZ<<<-===================================
                    ''')
                        A='''A river is flowing from west to east at a speed of 5 metres per minute.
  A man on the south bank of the river, capable of swimming at 10 metres per minute in still water,
  wants to swim across the river in the shortest time.
  He should swim in a direction:

        1) due north

        2) 30° north of west

        3) 30° east of north

        4) 60° east of north'''
                        B='''If the potential energy of a force is U=x²y+3xy then force on a particle at (-2,3) is:

        1) 3î+2ĵ

        2) -3î+2ĵ

        3) 3î-2ĵ

        4) -3î-2ĵ'''
                        C='''Which of the following is correct about the direction of static friction?

        1) It acts in the direction opposite of the applied force.

        2) It acts in the direction opposite of relative velocity betweent he bodies in contact.

        3) It acts in the direction opposite of relative acceleration.

        4) It direction may be known by using direction of acceleration of body.'''
                        D='''A ball moves with the speed 3m/s towards a heavy wall which is also moving towards the ball with speed 1m/s.
  The collision of the ball with the wall in inelastic (e=1/2). Find the speed of ball after collision with the wall.

        1) 2m/s

        2) 3m/s

        3) 4m/s

        4) 5m/s'''

                        E='''A ball of mass m=100g, suspended on a thread of length l=40cm, describes a circle in the horizontal plane.
  What is the kinetic energy of the ball, if the thread forms a constant angle θ=60° with the verical?

        1) 0.25 J

        2) 0.1 J

        3) 0.3 J

        4) 0.03 J'''

                        F='''The body moves in the positive direction of the x axis under the action of constant force F=ax,
  where a is a positive constant.
  At time t=0, the body is slightly to the right of the origin of the coordinates and its speed is zero.
  Find the dependence of kinetic energy of the body on the cooridnate.

        1) (3/2)ax²

        2) ax²

        3) (1/2)x²

        4) (3/4)x²'''

                        G='''A spring of stiffness 1000N/m is stretched initially by 10cm from undeformed position.
  The work required to stretch it by another 10cm is

        1) 5 N-m

        2) 7 N-m

        3) 10 N-m

        4) 15 N-m'''

                        H='''The potential energy for the force F=yzî+xzĵ+xyk^,if the zero of the potential energy is chosen at
  the point[2,2,2] is

        1) 8+xyz

        2) 8-xyz

        3) 4-xyz

        4) 4+xyz'''

                        I='''An ideal fluid flows through a lomg horizontal circular pipe. In one region of the pipe, it has a radius R.
  The pipe then widens to radius 2R. What is the ratio of the fluid speed in the region of radius R to the speed of fluid
  in region of pipe with radius 2R.

        1) 0.75

        2) 0.5

        3) 1

        4) 4'''

                        J='''From the top of a building if a ball is thrown upwards with speed 10m/s, it reaches the ground on 3s.
  If the ball is thrown horizontally from the top with the speed 20m/s, how far from the foot of the building
  it will land land on ground?

        1) 15√3

        2) 20√3

        3) 17

        4) 21'''
                        #this is the answer key
                        da={A:'1',B:'1',C:'4',D:'2',E:'3',F:'3',G:'4',H:'2',I:'4',J:'2'}
                        import random                  #importing random function for randomising the questions.
                        y=random.sample([A,B,C,D,E,F,G,H,I,J],5)
                        for i in range(5):
                            while True:
                                 print(i+1,".",y[i],sep="")
                                 ans=input("    Type your option here: ")
                                 print()
                                 #marking scheme
                                 if da[y[i]]==ans:
                                     marks+=4
                                     correct+=1
                                     break
                                 elif ans=='':
                                     marks=marks
                                     un+=1
                                     break
                                 elif ans=='1' or ans=='2' or ans=='3' or ans=='4':
                                     marks-=1
                                     wrong+=1
                                     break
                                 else:# for invalid inputs.
                                     print()
                                     print('     Please enter valid input!!!!!!')
                                     print()
                                 
                        print()
                        percent=(marks/20)*100                         #calculating percent obtained
                    #for displaying the result.
                        if percent>=90:
                            print("Congratulations! It was an outstanding performance.")
                        elif percent>=70:
                            print("Very good. You posses a great knowledge")
                        elif percent>=50:
                            print("Good. You did well")
                        else:
                            print("Failures are stepping stones for success. Better luck next time")
                        print("Your marks are: ",marks,'out of 20')
                        print("Your percentage is",percent,"%")
                        print("Number of questions which are answered correctly = ",correct)
                        print("Number of questions which are answered wrong = ",wrong)
                        print("Number of questions which are unattempted = ",un)


                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'": #incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()
                    elif n=='2':
                        marks=0   #initialsing the marks variable.
                        #here are the questions
                        print('============================->>> PHYSICS (Integer Answer Type) <<<-===================================')

                        aa='''A  particle  moves  in  the  x-y  plane  under  the  influence  of  a  force  such
  that  the linear momentum IsP(t) = A [ î cos kt -ĵ sin kt ]Where A and k are constants.
  The angle in degrees between force and momentum is___________________.'''

                        bb=''' A power  line  lies  along  the  east -west  direction  and
  carries  a  current  of  10  A. The force per meter due to earth's
  magnetic field of 10^-4 T is10^-X N/m. The value of x is_____________. '''

                        cc='''The sun's disc subtends an angle of 10^-2 rad at the earth.
  The radius of curvature ( in meters) of the mirror which will produce
  on a screen an image of the sun 2 cm in diameter is____________.'''

                        dd='''Light of wavelength 0.6 mm from a sodium lamp falls on a photo
  cell and causes the emission of photoelectrons for which the stopping potential is 0.5 V.
  With light of wavelength 0.4 mm from a mercury lamp whose stopping potential is 1.5 V.
  Then, the work function in eV of the photocell surface is (rounded off to rearest ones) ____________.'''

                        ee=''' On a horizontal surface lies a bar of mass m=11 kg. A spring of stiffness k=200N/m is attached to the bar.
  The coefficient of friction between the bar and the surface is  On a horizontal surface lies a bar of mass m=11 kg.
  A spring of stiffness k=200N/m is attached to the bar. The coefficient of friction between the bar and the surface is
  is µ= (1/√2). Initially, the spring is undeformed.Then applying a force F directed at an angle α= 45°to the horizontal
  to the free end of the spring, the bar was slowly moved . Find 'F'(in N). (Round off to nearest ones place)'''
                        #this is the answer key
                        db={aa:'90',bb:'3',cc:'4',dd:'2',ee:'54'}
                        import random              # importing the random fucnction for randomising the questions
                        y=random.sample([aa,bb,cc,dd,ee],5)
                        for i in range(5):
                            while True:
                             print()
                             print(i+1,".",y[i],sep="")
                             ans=input('''
                        Type your answer (Positive intergers only): ''')
                             if ans=='':
                                 break
                             else:
                                 try:
                                     ans1=float(ans)
                                
                                     if float(db[y[i]])==ans1:
                                         marks+=4
                                     else:
                                         marks==marks
                                     break
                                 except ValueError:
                                     print()
                                     print("Please enter valid input!!!")
                        print()
                        print("Your marks are: ",marks,'out of 20') # displaying the result.
                        if marks==20:
                            print('You mastered it. Fabulous!')
                        elif marks in range(15,20):
                            print('Marvellous! You can do it next time')
                        elif marks in range(5,15):
                            print('Well tried! Perform better next time')
                        else:
                            print('Try hard. You can do it!')
                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":#incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()
                    elif n=='3':
                        marks=0
                        correct=0                             #initialising variables for right answers, wrong answers, unattempted questions.
                        wrong=0
                        un=0
                        #here are the questions.
                        print('''============================->>> CHEMISTRY OBJECIVE TYPE QUIZ<<<-===================================
                    ''')  
                        a='''Perdict the oxidation number of Cr in CrO5
        1) 6

        2) 4

        3) 5

        4) 1'''
                        b='''A buffer solution of ammonia and ammonium chloride have concentration 0.1M and 0.2M respectively.
  If 1.825 g HCl is addded in this solution then (Volume of solution is 1L)

        1) pH of solution decreases by 0.4

        2) pH of solution increases by 0.4

        3) pH of solution decreases by 0.8

        4) pH of solution increases by 0.8'''
                        c='''A buffer solution was tested and 2 moles of acid were added to it which caused reduction of its pH by one unit.
  Determine its buffer capacity.

        1) 2

        2) 0.5

        3) 1

        4) 3'''
                        d='''Which of the following is a path function ?

        1) Volume

        2) Pressure

        3) Work

        4) Internal Energy'''
                        e='''Which of the following is intensive property?

        1) Temperature

        2) Internal Energy

        3) Mass

        4) Heat Capacity'''
                        f='''Which of the following is a feature of adiabatic expansion?

        1) ΔV<0

        2) ΔU<0

        3) ΔU>0

        4) ΔT=0'''
                        g='''Which of the following is an isolated system?

        1) Pressure Cooker

        2) Human Body

        3) Universe

        4) Cup of tea'''
                        h='''Which of the following is true for an adiabatic process?

        1) ΔH=0

        2) ΔW=0

        3) ΔQ=0

        4) ΔV=0'''
                        i='''Which of the following orbiatls contain 50% s character and 50 % p character?

        1) sp^3

        2) sp

        3) sp^(1/2)

        4) sp^2'''
                        j='''What is the representation of alcohol group

        1) -CHO

        2) -COOH

        3) -CN

        4) -OH'''
                        #here is the answer key stored in the form of a dictionary.
                        da={a:'1',b:'1',c:'1',d:'3',e:'4',f:'2',g:'3',h:'3',i:'2',j:'4'}
                        import random
                        y=random.sample([a,b,c,d,e,f,g,h,i,j],5)
                        for i in range(5):
                            while True:
                                 print(i+1,".",y[i],sep="")
                                 ans=input("    Type your option here: ")     #accepting the answer from the user.
                                 print()
                                 #marking scheme
                                 if da[y[i]]==ans:
                                     marks+=4
                                     correct+=1
                                     break
                                 elif ans=='':
                                     marks=marks
                                     un+=1
                                     break
                                 elif ans=='1' or ans=='2' or ans=='3' or ans=='4':
                                     marks-=1
                                     wrong+=1
                                     break
                                 else:
                                     print()
                                     print('     Please enter valid input!!!!!!')
                                     print()
                                 
                        print()
                        print("Your marks are: ",marks,'out of 20')
                        if marks==20:
                            print('You mastered it. Fabulous!')
                        elif marks in range(15,20):
                            print('Marvellous! You can do it next time')                #printing the result
                        elif marks in range(5,15):
                            print('Well tried! Perform better next time')
                        else:
                            print('Try hard. You can do it!')
                        print("Number of questions which are answered correctly = ",correct)
                        print("Number of questions which are answered wrong = ",wrong)
                        print("Number of questions which are unattempted= ",un)
                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":#incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()
                    elif n=='4':
                        marks=0             #initialising marks variable.
                        #here are the questions
                        print('''============================->>> CHEMISTRY (Integer Answer Type) <<<-===================================
                    ''')

                        a='''Solid phosphorous penta chloride contains a cation and an anion.
  The number of chlorine atoms present in one unit of cation is:________'''

                        b='''Number of σ-bonds present in pentane is:__________ '''

                        c='''How many baloons of 2l capacity can be filled with 'He' gas at STP from a cylinder of 4L capacity
  containing 'He' gas at 4 atm pressure and at 273 K temperature?'''

                        D='''The atomic number of the transitional element metal which forms green compound in +3 oxidation state
  and yellow orange compound in +6 oxidation state is:_____________'''

                        e='''The atomic number of an element which is the lightest in gaseous state is: ____________. '''
                        #the answwer key to the questions
                        d={a:'4',b:'16',c:'6',D:'24',e:'1'}
                        import random            #importing random function to randomise the questions.
                        y=random.sample([a,b,c,D,e],5)
                        for i in range(5):
                            while True:
                             print()
                             print(i+1,".",y[i],sep="")
                             ans=input('''
                        Type your answer (Positive intergers only): ''')
                             if ans=='':
                                 break
                             else:
                                 try:
                                     ans1=float(ans)
                                
                                     if float(d[y[i]])==ans1:
                                         marks+=4
                                     else:
                                         marks==marks
                                     break
                                 except ValueError:
                                     print()
                                     print("Please enter valid input!!!")
                        print()
                        percent=(marks/20)*100
                    #printing the result
                        if percent>=90:
                            print("Congratulations! It was an outstanding performance.")
                        elif percent>=70:
                            print("Very good. You posses a great knowledge")
                        elif percent>=50:
                            print("Good. You did well")
                        else:
                            print("Failures are stepping stones for success. Bettter luck next time")
                        print("Your marks are: ",marks,'out of 20')
                        print("Your percentage is",percent,"%")
                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":#incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()
                    elif n=='5':
                        marks=0
                        correct=0                 #initialising the marks variable and wrong  answers variable and unattempted questions to zero.
                        wrong=0
                        un=0
                        #here are the questions
                        print('''============================->>> MATHEMATICS OBJECIVE TYPE QUIZ<<<-===================================
                    ''')
                        a='''If the coefficients of 2nd, 3rd and 4th terms in the expansion of (1+x)^n are in A.P., Then n is equal to

        1) 3

        2) 5

        3) 7

        4) 9'''
                        b='''In how many ways 8 men and 8 women can be seated around a round table such that no two men can sit together?

        1) (8!)^2

        2) (7!)^2

        3) 6! 7!

        4) 7! 8!'''
                        c='''Which of the following term in the expansion of(x^2+(2/x))^18 is independent of x? (Where T r denotes the r th term)

        1) T 12

        2) T 13

        3) T 14

        4) T 15'''
                        d='''The rank of the word 'INDIA'?

        1) 46

        2) 32

        3) 56

        4) 39'''
                        e='''If the lines x+6y=13, 3x-y=1 and x+ky=15 are concurrent, then the value of k is

        1) 2

        2) 3

        3) 4

        4) 7'''
                        f='''What is the differential of sin(x)?

        1) cos(x)

        2) -cos(x)

        3) sec(x).tan(x).cot(x)

        4) -sin(x)'''
                        g='''If A=[1,2,3,4,5], then the number of proper subsets of A is

        1) 30

        2) 31

        3) 32

        4) 33'''
                        h='''What is the (A')' if A is a set?

        1) A

        2) 2^A

        3) A/2

        4) A/10'''
                        i='''What is the P(P(P(P(P(A))))) if A=[]?

        1) 1

        2) 2^4

        3) 2^5

        4) 2^16'''
                        j='''What is A Δ B?

        1) (A-B) U (B-A)

        2) (A-B)

        3) (A U B) U (A - B)

        4) None of the above'''
                        #here is the answer key
                        da={a:'3',b:'4',c:'2',d:'1',e:'4',f:'1',g:'2',h:'1',i:'4',j:'1'}
                        import random           #importing random function to randomise the questions
                        y=random.sample([a,b,c,d,e,f,g,h,i,j],5)
                        for i in range(5):
                            while True:
                                 print(i+1,".",y[i],sep="")
                                 ans=input('''
                Type your option here: ''') #accepting answer from te user
                                 print()
                                 if da[y[i]]==ans:      #evaluating answers
                                     marks+=4
                                     correct+=1
                                     break
                                 elif ans=='':
                                     marks=marks
                                     un+=1
                                     break
                                 elif ans=='1' or ans=='2' or ans=='3' or ans=='4':
                                     marks-=1
                                     wrong+=1
                                     break
                                 else:
                                     print()
                                     print('     Please enter valid input!!!!!!')
                                     print()
                        print()
                        print("Your marks are: ",marks,'out of 20')
                        #printing results
                        if marks==20:
                            print('You mastered it. Fabulous!')
                        elif marks in range(15,20):
                            print('Marvellous! You can do it next time')
                        elif marks in range(5,15):
                            print('Well tried! Perform better next time')
                        else:
                            print('Try hard. You can do it!')
                        print("Number of questions which are answered correctly = ",correct)
                        print("Number of questions which are answered wrong = ",wrong)
                        print("Number of questions which are unattempted = ",un)
                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":#incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()                    
                    elif n=='6':
                        marks=0       #initialising marks variable as zero.
                        #here are the quesions
                        print('============================->>> MATHEMATICS (Integer Answer Type) <<<-===================================')

                        a='''If out of 2n tickets, numbered as 1,2,3,....,2n, 3 distinct are chosen at random,
  and the probablity that they are in A.P is 1/10, then 'n' is'''

                        b='''Let z satisifies |z-2+3i|=2 then the maximum value of |z+10-2i| is ____________.'''

                        c='''The expression (1-i)^8+(1+i)^8 simplifies to'''

                        d='''If a,b,c belongs to R-{0}, such that a,b are the roots of the equationx^2+cx+d=0 and
 c,d are the roots of the equation x^2 + ax + b=0, then |a|+|b|+|c|+|d| is equal to'''

                        e='''If a,b,c belongs R-{0} and equation ax^2 + bx + 4=0 have common roots, then value of (b/(a+c))
 (round off to nearest ones).'''
                    #here is the answer key
                        dc={a:'8',b:'15',c:'32',d:'6',e:'1'}
                        
                        import random              #importing random function for randomising the order of the questions.
                        y=random.sample([a,b,c,d,e],5)
                        for i in range(5):
                            while True:
                             print()
                             print(i+1,".",y[i],sep="")
                             ans=input('''
                        Type your answer (Positive intergers only): ''')
                             if ans=='':
                                 break
                             else:
                                 try:
                                     ans1=float(ans)
                                
                                     if float(dc[y[i]])==ans1:
                                         marks+=4
                                     else:
                                         marks==marks
                                     break
                                 except ValueError:
                                     print()
                                     print("Please enter valid input!!!")
                        print()
                         #printing the result.
                        print("Your marks are: ",marks,'out of 20')
                        if marks==20:
                            print('You mastered it. Fabulous!')
                        elif marks in range(15,20):
                            print('Marvellous! You can do it next time')
                        elif marks in range(5,15):
                            print('Well tried! Perform better next time')
                        else:
                            print('Try hard. You can do it!')
                        Reply=input("Press ANY KEY to continue or enter 'e' to exit to main menu: ")
                        print()
                        if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":#incase the user tries to exit form the menu. the menu looping
                            break
                        else:
                            continue
                        print()   
                    elif n=='7':
                        break                 
            elif n=='4':
                print('''
The rules of the quiz are:

-> Each user will be given Five/Ten question per quiz.
-> For each RIGHT ANSWER '4' will be awarded. Whereas for every WRONG ANSWER '1' mark will be DEDUCTED from the total score.
-> If the question is left UNATTEMPTED, no mraks will be awarded or deducted.
-> Enter the input(ONLY DIGIT) after the phrase 'Type your input here: '.
-> The game will proceed once the question displayed is answered.
-> The Total Score will be displyed once all the questions are answered.
-> Here is a sample Question and answering format:

      1.Which is the Scotland's national animal?

      1) Lion
      
      2) Dragon
      
      3) Unicorn
      
      4) Panther

      Type your input here: 

      #The correct answer is "Unicorn". Therefore the correct format(ONLY DIGIT) of answering is:
      
      Type your input here: 3                                          <--ONLY CORRECT SYNTAX

      #Invalid inputs' example:

      Type your input here: 3)                                         }
      Type your input here: 3) Unicorn                                 }Wrong syntax
      Type your input here: Unicorn                                    }
       
      

=====================HAPPY GAMING=====================''')
#The above is to print the set of rules.
                Reply=input("Press ANY KEY to continue or enter 'e' to exit: ")
                print()
                if Reply=='e' or Reply=="'e'" or Reply=='E' or Reply=="'E'":
                    break
                else:
                    continue
                print()
            elif n=='5': # To end the quiz
                break
    t=("Bye!! ","Have a nice day!!")
    print(t[0]+t[1])# Concatenation of tuple elements
except:
    print("Error")
    print("Sorry for the inconvenience")
    import PROJECT_CLASS_XI_2
    print("The Files may have been lost or deleted. Please contact the programmers for further assistance")
