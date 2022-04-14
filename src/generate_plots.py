import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

def read_file(filename):
    '''
    Read the file and return the data as a numpy array.
    '''
    data = []
    with open(filename) as f:
        for row in f:
            row_data = []
            for element in row.split(" "):
                row_data.append(np.float64(element))
            data.append(row_data)
    return np.array(data)

def plot_data():
    '''
    Plot and save the data.
    '''
    imgs = []
    step = 100
    NT = len(os.listdir('./outputs/'))*step
    for i in range(0, NT, step):
        data = read_file("./outputs/output_" + str(i) + ".txt")
        imgs.append(data)
    
    fig = plt.figure()
    viewer = fig.add_subplot(111)
    plt.ion() # Turns interactive mode on (probably unnecessary)
    fig.show() # Initially shows the figure

    for i in range(len(imgs)):
        print("Plotting Simulation Sample : " + str(i+1))
        viewer.clear() # Clears the previous image
        viewer.imshow(imgs[i]) # Loads the new image
        plt.pause(.0001) # Delay in seconds
        fig.canvas.draw() # Draws the image to the screen

# plot_data()

def generate_video():
    movie_name = "./static/movie.avi"

    c = 0
    imgs = []
    step = 100
    NT = len(os.listdir('./outputs/'))*step
    for i in range(0, NT, step):
        c += 1
        print("Plotting Simulation Sample : " + str(c))
        filename = "./outputs/output_" + str(i)
        data = read_file(filename + ".txt")
        plt.imshow(data)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.colorbar(orientation='vertical')
        plt.title('Advection Simulation Plot')
        plt.savefig(filename + '.png')
        plt.close()
        imgs.append(filename + '.png')
    
  
    frame = cv2.imread(imgs[0])
    height, width, _ = frame.shape  
    video = cv2.VideoWriter(movie_name, 0, 1, (width, height)) 
    for img in imgs: 
        video.write(cv2.imread(img)) 
      
    cv2.destroyAllWindows() 
    video.release()

generate_video()

# Visualize and save data for different timestamps in the simulation
# plot_data("./milestone-1/initial_gaussian.txt")

# plot_data("./milestone-1/simulation_10000_timesteps.txt")

# plot_data("./milestone-1/simulation_15000_timesteps.txt")

# plot_data("./milestone-1/simulation_user_specified_timestep.txt")