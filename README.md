# medical3D_display
Demo that displays two different 3D visualizations of the human heart (one generated by a trained AI engine, the other from actual MRI data) for comparison, using the VisPy library

* Dependencies: VisPy, PyQt4, h5py, numpy
* VisPy Installation Guide (Assuming python3, pip3, git is installed)
  * Linux Ubuntu
    * sudo pip3 install h5py
    * sudo pip3 install numpy
    * sudo apt-get install python3-pyqt4
    * sudo apt-get install python3-pyqt4.qtopengl
    * sudo git clone https://github.com/vispy/vispy.git && cd vispy && sudo python3 setup.py install --user
  * Mac OS X, Windows (Assuming Anaconda is installed; Anaconda comes with h5py and numpy)
  (NOTE: As of now, "conda install pyqt=4" does not work for Windows if Python3 version is higher than 3.5)
    * conda install pyqt=4
    * git clone https://github.com/vispy/vispy.git && cd vispy && python3 setup.py install --user

Screenshots (Left: LVall_10_GT, Right: LVall_10_Result)

![alt text](https://github.com/taekb/medical3D_display/blob/master/screenshots/LVall_10_capture1.png?raw=true)

![alt text](https://github.com/taekb/medical3D_display/blob/master/screenshots/LVall_10_capture2.png?raw=true)

![alt text](https://github.com/taekb/medical3D_display/blob/master/screenshots/LVall_10_capture3.png?raw=true)

