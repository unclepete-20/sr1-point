from bmp_renderer import Render

frame = Render()

frame.glCreateWindow(200, 200)

frame.glViewPort(20, 20, 100, 100)

frame.glClearColor(0.25, 1, 0.50)

frame.glClear()

frame.glVertex(1, 1)

frame.glFinish("prueba.bmp")