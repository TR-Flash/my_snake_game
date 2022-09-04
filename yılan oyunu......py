
################################################################################


import turtle
import random

GENİSLİK = 500
YÜKSEKLİK = 500
YİYECEK_BOYUTU = 11
GECİKME = 100
offsets= {
        "up":(0,20),
        "down":(0,-20),
        "left":(-20,0),
        "right":(20,0)

    }

def sıfırlama():
    global yılan,yılan_yönü,yemek_pozisyonu,kalem
    yılan = [[0,0],[0,20],[0,40],[0,50],[0,60]]
    yılan_yönü= "up"
    yemek_pozisyonu = al_rastgele_yemek_pozisyonu()
    yiyecek.goto(yemek_pozisyonu)
    hareket_ettir_yılanı()


def hareket_ettir_yılanı():
    global yılan_yönü

    # Yılanın başı için bir sonraki pozisyon.
    yeni_kafa = yılan[-1].copy()
    yeni_kafa[0] = yılan[-1][0] + offsets[yılan_yönü][0]
    yeni_kafa[1] = yılan[-1][1] + offsets[yılan_yönü][1]

    # Kendi kendine çarpışma
    if yeni_kafa in yılan[:-1]:
        sıfırlama()
    else:

        yılan.append(yeni_kafa)
        if not yiyecekle_çarpışma():
            yılan.pop(0)

        if yılan[-1][0] > GENİSLİK / 2:
            yılan[-1][0] -= GENİSLİK
        elif yılan[-1][0] < - GENİSLİK / 2:
            yılan[-1][0] += GENİSLİK
        elif yılan[-1][1] > YÜKSEKLİK / 2:
            yılan[-1][1] -= YÜKSEKLİK
        elif yılan[-1][1] < - YÜKSEKLİK / 2:
            yılan[-1][1] += YÜKSEKLİK

        kalem.clearstamps()
        for segment in yılan:
            kalem.goto(segment[0], segment[1])
            kalem.stamp()
        screen.update()
        turtle.ontimer(hareket_ettir_yılanı, GECİKME)

def yiyecekle_çarpışma():
    global yemek_pozisyonu
    if alınan_mesafe(yılan[-1], yemek_pozisyonu) < 20:
        yemek_pozisyonu = al_rastgele_yemek_pozisyonu()
        yiyecek.goto(yemek_pozisyonu)
        return True
    return False

def al_rastgele_yemek_pozisyonu():
    x = random.randint(- GENİSLİK / 2 + YİYECEK_BOYUTU, GENİSLİK / 2 - YİYECEK_BOYUTU)
    y = random.randint(- YÜKSEKLİK / 2 + YİYECEK_BOYUTU, YÜKSEKLİK / 2 - YİYECEK_BOYUTU)
    return(x,y)

def alınan_mesafe(konum1, konum2):
    x1, y1 = konum1
    x2, y2 = konum2
    mesafe = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return mesafe

def ileri_git():
    global yılan_yönü
    if yılan_yönü != "down":
        yılan_yönü = "up"

def sağa_git():
    global yılan_yönü
    if yılan_yönü != "left":
        yılan_yönü = "right"

def aşağı_git():
    global yılan_yönü
    if yılan_yönü != "up":
        yılan_yönü = "down"

def sola_git():
    global yılan_yönü
    if yılan_yönü != "right":
        yılan_yönü = "left"

   # Ekran
screen = turtle.Screen()
screen.setup(GENİSLİK, YÜKSEKLİK)
screen.title("Yılan Oyunu")
screen.bgcolor("black")
screen.setup(500, 500)
screen.tracer(0)

   # Pen
kalem = turtle.Turtle("square")
kalem.penup()
kalem.pencolor("yellow")

   # Yiyecek
yiyecek = turtle.Turtle()
yiyecek.shape("circle") 
yiyecek.color("red")
yiyecek.shapesize(YİYECEK_BOYUTU / 20) #Default size of turtle "square" shape is 20.
yiyecek.penup()

   # Event handlers
screen.listen()
screen.onkey(ileri_git, "Up")
screen.onkey(sağa_git, "Right")
screen.onkey(aşağı_git, "Down")
screen.onkey(sola_git, "Left")


sıfırlama()
turtle.done()




  





















            
    
