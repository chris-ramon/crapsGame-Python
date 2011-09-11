import web
from models.Craps import Craps

urls = (
    '/', 'index',
    '/game/(\d)', 'game'
)

render = web.template.render('templates/')

app = web.application(urls,globals())

class index:
    def GET(self):
        return render.mainPage()

class game:
    def POST(self, numberGame):
        if int(numberGame)==1:
            sideOne = Craps()       
            sideTwo = Craps()
            result = sideOne.side + sideTwo.side
            sideOne = sideOne.side
            sideTwo = sideTwo.side           
            msg=None
            if result==7 or result==11:
                msg = "You've win the game"           
            elif result==2 or result==3 or result==12:
                msg = "You've lost the game !"
            else:
                msg = "Keep playing"
            return render.game(sideOne,sideTwo,result,msg)
            
        if int(numberGame)==2:
            i = web.input()
            sideOne = Craps()
            sideTwo = Craps()
            result = sideOne.side + sideTwo.side
            msg=None

            if i.result == 7:
                msg = "You've lost"
            elif int(i.result) == result:
                msg = "You've win"
            else:
                msg = "You've lost"

            return render.game(sideOne.side,sideTwo.side,result,msg)
            

if __name__ == '__main__':
    app.run()
