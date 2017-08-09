# -*- coding: utf-8 -*-
#   Copyright 2017 Daniel Jeong (@taekb)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import numpy as np
import h5py

from vispy import app, scene

# Create a SceneCanvas object with a 3D viewport
#fullscreen=True for fullscreen view of the canvas
canvas = scene.SceneCanvas(title='LVall_10: GT(Left), Result(Right)', keys='interactive')
#Add grid
grid = canvas.central_widget.add_grid()

print("Working..")
data_GT = h5py.File('LVall_10_GT.mat', 'r')
array_GT = data_GT['GT'][()]
data_RT = h5py.File('LVall_10_result.mat', 'r')
array_RT = data_RT['OutL'][()]


vb_GT = scene.widgets.ViewBox(name='GT', parent=canvas.scene) #GT ViewBox
vb_RT = scene.widgets.ViewBox(name='Result', parent=canvas.scene) #Result ViewBox

grid.padding = 6
grid.add_widget(vb_GT, 0, 0)
grid.add_widget(vb_RT, 0, 1)

# Create isosurface visual for GT
surface_GT = scene.visuals.Isosurface(array_GT, level=0.9,
                                   color=(0.5, 0.6, 1, 1), shading='smooth',
                                   parent=vb_GT.scene)
surface_GT.transform = scene.transforms.STTransform(translate=(-350, -170, -115))

# Create isosurface visual for RT (Result)
surface_RT = scene.visuals.Isosurface(array_RT, level=0.9,
				   color=(0.9, 0.6, 0.3, 1), shading='smooth',
				   parent=vb_RT.scene)
surface_RT.transform = scene.transforms.STTransform(translate=(-350, -170, -115))

# Add x,y,z axes
axis_GT = scene.visuals.XYZAxis(parent=vb_GT.scene)
axis_RT = scene.visuals.XYZAxis(parent=vb_RT.scene)
 
# Use a 3D Turntable camera
cam = scene.TurntableCamera(elevation=30, azimuth=30)
cam.set_range((-200, 200), (-200, 200), (-200, 200))
vb_GT.camera = cam
vb_RT.camera = cam
vb_GT.camera.aspect = vb_RT.camera.aspect = 1
vb_GT.camera.link(vb_RT.camera)


if __name__ == '__main__':
    canvas.show()
    if sys.flags.interactive == 0:
        app.run()
