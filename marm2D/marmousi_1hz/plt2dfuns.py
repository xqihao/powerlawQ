import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from mpl_toolkits.axes_grid1 import make_axes_locatable


### --------------------------------------------
def plot_check_model(field, nz, nx):
    fig = plt.figure(figsize=(7, 7))
    fig.subplots_adjust(left=.20, bottom=.16, right=.99, top=.97)

    ax = plt.gca()
    ##im = plt.imshow(field, extent=[0,(nx-1)*dx,(nz-1)*dz,0], aspect=(nx-1)*dx/(nz-1)/dz, cmap="jet")
    im = plt.imshow(field, aspect=1, cmap="jet")    

    plt.colorbar(im, orientation="horizontal")
#     plt.colorbar(im, location='bottom', shrink=0.8*nz/nx)
    
    plt.show()
    plt.close()
### --------------------------------------------
def plot_snapshot(title,filename,field, nz, nx, dz, dx, zlab, xlab, asp=1, clip=0.001, color="jet"):
    """ plot snapshot  """
    plt.figure(figsize=(7,4))
    fig = plt.subplots_adjust(left=0.15, bottom=0.1, top=0.95, right=0.95)
    plt.title(title)
    plt.xlim(0, (nx-1)*dx)
    plt.ylim((nz-1)*dz, 0)
    plt.xlabel(xlab, fontsize=14)
    plt.ylabel(zlab, fontsize=14)
    
    max_val = np.max(np.abs(field))
    
    image = plt.imshow(field,vmin=-max_val*clip,vmax=max_val*clip, \
                       extent=[0,(nx-1)*dx,(nz-1)*dz,0],aspect=asp,cmap=color)
    plt.colorbar(image,shrink=0.7)
    full_filename = './figs/'+filename + '.pdf'
    #plt.savefig(full_filename, dpi=800, bbox_inches="tight")
    plt.show()
    plt.close
### --------------------------------------------
#def plot_data(title,filename,data, nt, nx, dt, dx, zlab, xlab, clip=1, asp=2, color='jet'):
#
#    max_val = np.max(np.abs(data))
#    tmp = np.clip(data,-clip*max_val,clip*max_val) # Clip and scale data at fraction of max
#    plt.figure(figsize=(7,6))
#    plt.subplots_adjust(left=0.1, bottom=0.1, top=0.9, right=0.9)
#    image = plt.imshow(tmp,vmin=-max_val*clip,vmax=max_val*clip, \
#                       extent=[0, (nx-1)*dx, (nt-1)*dt,0], aspect=asp, cmap=color)
#    plt.title(title)
#    plt.colorbar(image, shrink=1./asp)
#    plt.xlim(0, (nx-1)*dx)
#    plt.ylim((nt-1)*dt, 0)
#    plt.xlabel(zlab, fontsize=14)
#    plt.ylabel(xlab, fontsize=14)
#    full_filename = './figs/'+filename + '.pdf'
#    plt.savefig(full_filename, dpi=800, bbox_inches="tight")
#    plt.show()
#    plt.close()
    
    
### --------------------------------------------
def plot_data(data, nz, nx, dz, dx, oz=0, ox=0, zlab="", xlab="", \
              alpha=0, clip=1, vrange=None, asp=2, allpos=False, bar=True, barlab="", barhorn=False, \
              shnk=0.7, fsize=(7,7), color="jet", title="", fname=""):
    
    if allpos:
        min_val = np.min(data)
        max_val = np.max(data)
        ### Clip and scale data at fraction of [min, max]
        data2   = np.clip(data,-clip*max_val,clip*max_val)
    else:
        max_val = np.max(np.abs(data))
        min_val = - max_val
         ### Clip and scale data at fraction of [-max, max]
        data2   = np.clip(data, clip*min_val, clip*max_val)

    ### gain the data along the vertical axis. This is used to illustrate seismogram better.
    scale = (np.arange(nz)*dz)**alpha    
    data2 = data2 * scale[:, None]
    
    plt.figure(figsize=fsize)
    #plt.subplots_adjust(left=0.1, bottom=0.1, top=0.9, right=0.9)    
    
    if vrange != None:
        image = plt.imshow(data2,vmin=vrange[0],vmax=vrange[1], \
                           extent=[ox, (nx-1)*dx, (nz-1)*dz,oz], aspect=asp, cmap=color)
    else: 
        image = plt.imshow(data2,vmin=min_val*clip,vmax=max_val*clip, \
                           extent=[ox, (nx-1)*dx, (nz-1)*dz,oz], aspect=asp, cmap=color)
        
    if title.strip():
        ### title, as the argument for the plot tile, is a string. 
        ### If it is empty (such as "" or "  "), it.strip() is false.
        plt.title(title)
    
    if barhorn:
        barorien = "horizontal"
    else:
        barorien = "vertical"
        
    if bar:
        if barlab.strip():
            cb = plt.colorbar(image, shrink=shnk, orientation=barorien)
            cb.set_label(label=barlab, size=16)
            #Set the colorbar scale font size.
            cb.ax.tick_params(labelsize=14)     
        else:
            plt.colorbar(image, shrink=shnk)
    
    plt.xlim(ox, (nx-1)*dx)
    plt.ylim((nz-1)*dz, oz)
    
    plt.xlabel(xlab, fontsize=16)
    plt.ylabel(zlab, fontsize=16)
    
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    if fname.strip():
        plt.savefig(fname, format="pdf", dpi=800, bbox_inches="tight")
        
    plt.show()
    plt.close()


