import numpy as np 
from andrew_backend import AndrewCurve

def test_fourier():
    andrew_curve = AndrewCurve()
    
    data = np.asarray(list(range(1,6)))
    t1 = np.linspace(-np.pi,np.pi,100)
    
    fourier1 = data[0] * (1.0/np.sqrt(2)) + data[1]*np.sin(t1) + data[2] * np.cos(t1) + data[3]*np.sin(2*t1) + data[4]*np.cos(2*t1)
    t2,fourier2 = andrew_curve.genAndrewCurve("fourier", data)
    assert t1 == t2
    assert fourier1 == fourier2
