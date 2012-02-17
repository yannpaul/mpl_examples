import matplotlib.pyplot as plt
import numpy as np

NTIME = 500
ZOOMTIME = 50
ZOOMSTEP = ZOOMTIME / 2
ZOOMSTART = ZOOMSTEP*3

np.random.seed(101)
time = np.arange(NTIME)
radar = np.random.random(NTIME) * 10
fig = plt.figure()
axfull = fig.add_subplot(211)
axzoom = fig.add_subplot(212)

axfull.plot(time, radar)
axfull.set_ylim(-1,11)


axzoom.plot(time, radar)
axzoom.set_ylim(-1,11)
axzoom.set_xlim(ZOOMSTART, ZOOMSTART + ZOOMTIME)
zoomHighlight = axfull.axvspan(ZOOMSTART,
                               ZOOMSTART + ZOOMTIME,
                               facecolor = 'g',
                               alpha = 0.5)

plusArrow = plt.arrow(.91, .8, .02, 0, picker= True, 
                      overhang = 0.001,
                      width = .01,
                      transform = fig.transFigure, 
                      clip_on = False 
                      )

minusArrow = plt.arrow(.98, .6, -.02, 0, picker= True, 
                       overhang = 0.001,
                       width = .01,
                       transform = fig.transFigure, 
                       clip_on = False
                       )


def increaceTime():
    print zoomHighlight.get_xy()
    xlim = list(axzoom.get_xlim())
    if xlim[1] + ZOOMSTEP-1 < NTIME:
        xlim[0] += ZOOMSTEP
        xlim[1] += ZOOMSTEP
        axzoom.set_xlim(xlim)
        zoomHighlight.set_xy([[xlim[0], 0.],
                              [xlim[0], 1.],
                              [xlim[1], 1.],
                              [xlim[1], 0.],
                              [xlim[0], 0.]])
    print zoomHighlight.get_xy()
                              

def decreaceTime():
    '''
    When called, changes the xlim of axzoom by ZOOMSTEP, so long as the xlim
    are gte zero. Shifts the highlighted region (zoomHighlight) to new 
    limits.
    '''

    xlim = list(axzoom.get_xlim())
    if xlim[0] - ZOOMSTEP >= 0:
        xlim[0] -= ZOOMSTEP
        xlim[1] -= ZOOMSTEP
        axzoom.set_xlim(xlim)
        zoomHighlight.set_xy([[xlim[0], 0.],
                              [xlim[0], 1.],
                              [xlim[1], 1.],
                              [xlim[1], 0.],
                              [xlim[0], 0.]])


def onpick(event):
    thisarrow = event.artist
    mouseevent = event.mouseevent

    if thisarrow == plusArrow:
        increaceTime()
        plt.draw()
        return True
    if thisarrow == minusArrow:
        decreaceTime()
        plt.draw()
        return True
    return True
        
fig.canvas.mpl_connect('pick_event', onpick)

fig.savefig('slidingTime1.png')
plt.show()
