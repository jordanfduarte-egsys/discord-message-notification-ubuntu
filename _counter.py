import discord
import asyncio
import os
import gi
import threading
import time
from threading import Timer

gi.require_versions({
    'Gtk':  '3.0',
    'Wnck': '3.0',
    'Gst':  '1.0',
    'AppIndicator3':  '0.1',
    'Notify': '0.7'
})
from gi.repository import Gtk as gtk, GObject, Gdk, Wnck, GdkX11, Gst, AppIndicator3 as appindicator, Notify

APPINDICATOR_ID = 'myappindicator'
indicator = appindicator.Indicator.new(APPINDICATOR_ID, 'call-stop', appindicator.IndicatorCategory.SYSTEM_SERVICES)
ativo = False

class MyClass(GObject.Object):
    def __init__(self):

        super(MyClass, self).__init__()
        # lets initialise with the application name
        Notify.init("myapp_name")

    def send_notification(self, title, text, file_path_to_icon=""):

        n = Notify.Notification.new(title, text, file_path_to_icon)
        n.show()

def action() :
    try:
        gtk.main_quit()
        print("quit all")
    except:
        print("Nao tem thead de quit")



def quit(param = ""):
    global indicator
    global ativo
    ativo = False
    indicator.set_status(False)
    gtk.main_quit()
    r = Timer(1.0, action)
    r.start()
    gtk.main()
    print("TERMINOU THEAD -> QUIT")
    return 0

def start():
    global indicator
    global ativo
    ativo = True
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    menu = gtk.Menu()
    item = gtk.MenuItem("Fechar")
    item.connect("activate", quit)
    item.show()
    menu.append(item)
    indicator.set_menu(menu)
    gtk.main()
    print("TERMINOU THEAD -> START")    
    return 0

    

client = discord.Client()

#async def my_background_task():
    #print("Online!")
    # for guild in client.guilds:
    #     print(guild)
    #     await guild.ack()
    #thread = threading.Thread(target=start)
    #thread.daemon = True
    #thread.start()
    #print('para min privado')
    #await asyncio.sleep(100) # Sleep for 10 seconds
    #await client.wait_until_ready()
#    counter = 0
#    channel = client.get_channel(id=690620066664022039) # replace with channel_id
    #while not client.is_closed():
        #for guild in client.guilds:
            #print(guild)
            #await guild.ack()

#        counter += 1
#        await channel.send(counter)
        #await asyncio.sleep(60) # task runs every 60 seconds


@client.event
async def on_ready():
    print("Online!")
    # for guild in client.guilds:
    #     print(guild)
    #     await guild.ack()
    #     await asyncio.sleep(10) # Sleep for 10 seconds

    #thread = threading.Thread(target=quit)
    #thread.daemon = True
    #thread.start()


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        quit()
        print('eu mandei msm')
        return

    if message.content == "exit":
        if ativo == True:
            thread = threading.Thread(target=quit)
            thread.daemon = True
            thread.start()
            print('exit')
    elif isinstance(message.channel, discord.channel.DMChannel):
        if ativo == False:
            thread = threading.Thread(target=start)
            thread.daemon = True
            thread.start()
            print('para min privado')

    elif message.mention_everyone:
        my = MyClass()
        my.send_notification("@everyone ou @here", "Verifique")
        #if ativo == False:
        #    thread = threading.Thread(target=start)
        #    thread.daemon = True
        #    thread.start()
        #    print('@everyone ou @here')
    else:
        for i in message.mentions:
            if client.user.id == i.id:
                my = MyClass()
                my.send_notification("Mencionou Jordan Duarte", message.content)
                #if ativo == False:
                #    thread = threading.Thread(target=start)
                #    thread.daemon = True
                #    thread.start()
                #    print('mencionou menu nome')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.user.discriminator)
    print('------')


#client.loop.create_task(my_background_task())
client.run('YOU-TOKEN', bot=False)









