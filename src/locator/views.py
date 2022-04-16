from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from geopy import distance
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from participater.models import Location, Player
from django.utils import timezone
import math
# Create your views here.
def index(request, lat=None, long=None):
  if request.user.is_authenticated == True:
      cUser = request.user
      plGameUser = Player.objects.get(user=cUser)
    
    
    #with open ("log.txt", "a") as logfile:
      #logfile.write(f"LAT: {lat} LONG: {long} TIMESTAMP: {str(datetime.now())}\n")
      locData = Location(player=request.user, lat=lat, long=long, time=timezone.now())
      if lat != None and long != None:
        locData = Location(player=request.user, lat=lat, long=long, time=timezone.now())
        locData.save()
      print(lat, long)
      if lat==None and long==None:
        return render(request, 'index.html')
      else:
        print(length((lat,long), (0,0)))
        pl = Player.objects.filter(hunter=False)
        pl_dict = []
        for plObj in pl:
          try:
            dcPrp = {}
            cLoc = Location.objects.filter(player=plObj.user).reverse()[0]
            pLoc = Location.objects.filter(player=request.user).reverse()[0]
            dist = length((cLoc.lat, cLoc.long), (pLoc.lat, pLoc.long))
            dcPrp["name"] = plObj.user.username
            dcPrp["lat"] = round(cLoc.lat,2) 
            dcPrp["long"] = round(cLoc.long,2)
            if dist > 1000:
              
              dcPrp["distance"] = f"{round(dist/1000, 2)}km"
            else:
              dcPrp["distance"] = f"{round(dist, 2)}m"
            dcPrp["direct"] = compDir(cLoc.lat- pLoc.lat, cLoc.long-cLoc.long)
            pl_dict.append(dcPrp)
          except:
              continue
        
                        
          
        print(pl_dict)
        return render(request, 'index.html', {"lat":lat, "long":long, "player_list":pl_dict, "hunter":plGameUser.hunter})
  else:
    return render(request, "index.html")
@csrf_exempt
def logPassW(request):
  from django.contrib.auth.models import User
  if request.POST:
    try:
      user = User.objects.create_user(username=request.POST["user"],password=request.POST["pw"])
      newPlayer = Player(user=user, hunter=False)
      newPlayer.save()
      login(request, user)
    except:
      user = authenticate(username=request.POST["user"], password=request.POST["pw"])
      login(request, user)
    return render(request, 'index.html')
  else:
    return render(request, 'pw.html')


def length(coord1, coord2):
  return float(distance.distance(coord1,coord2).m)

def compDir(deltaX, deltaY):
  degrees_temp = math.atan2(deltaX, deltaY)/math.pi*180
  if degrees_temp < 0:
    degrees_final = 360 + degrees_temp
  else:
    degrees_final = degrees_temp
  compass_brackets = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
  compass_lookup = round(degrees_final / 45)
  return compass_brackets[compass_lookup]