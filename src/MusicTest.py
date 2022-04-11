# play_test.py
import pyglet
 
pyglet.options['search_local_libs'] = True
media = pyglet.media.load('D:\\Downloads\\DragonClientGDv1.0FreeEdition\\Resources\\1022162.mp3')
media.play()
 
# Ctrl+c to quit
try:
    pyglet.app.run()
except KeyboardInterrupt:
    pass