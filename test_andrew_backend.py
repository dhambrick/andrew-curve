import numpy as np 
from andrew_backend import AndrewCurve

def test_fourier():
    andrew_curve = AndrewCurve()
    
    data = np.asarray(list(range(1,6))).reshape([1,5])
    t1 = np.linspace(-np.pi,np.pi,100)
    
    fourier1 = data[0,0] * (1.0/np.sqrt(2)) + data[0,1]*np.sin(t1) + data[0,2] * np.cos(t1) + data[0,3]*np.sin(2*t1) + data[0,4]*np.cos(2*t1)
    t2,fourier2 = andrew_curve.genAndrewCurve("fourier", data)
    assert t1 == t2
    assert fourier1 == fourier2
