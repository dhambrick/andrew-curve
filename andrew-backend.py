import numpy as np 
import scipy as sp 
import scipy.special as spec 
import matplotlib.pyplot as plt
from sklearn import datasets

class AndrewCurve:
    def __init__(self):
        self.basisMap = {"fourier":self.fourier ,"legendre":self.legendre }

    def genAndrewCurve(self,basis,data):
        return self.basisMap[basis](data)

    def legendre(self,data):
        t = np.linspace(-1,1,100)
        print(t.shape)
        data = np.asarray(data)
        M,N = data.shape
        print(M,N)
        legendreVec = []
        for n in range(N):
            legendreVec.append(spec.eval_legendre(n,t))
        legendreVec = np.asarray(legendreVec)
        andrewProj = np.dot(data,legendreVec)
        print(andrewProj.shape)
        return {"t":t, "data":andrewProj}

    def fourier(self,data):
        t = np.linspace(-np.pi,np.pi,100)
        b0 = np.zeros(100)
        print(t.shape)
        data = np.asarray(data)
        M,N = data.shape
        print(M,N)
        b0[0] = 1/np.sqrt(2)
        fourierVec = []
        fourierVec.append(b0)
        n = N - 1
        eN = int((n-n%2)/2)
        for i in range(0,eN):
            fourierVec.append(np.sin((i+1)*t))
            fourierVec.append(np.cos((i+1)*t))
        fourierVec.append(np.cos((eN+1)*t))
        print(fourierVec)
        fourierVec = np.asarray(fourierVec)
        andrewProj = np.dot(data,fourierVec)
        print(andrewProj.shape)
        return {"t":t, "data":andrewProj}


N = 50
M = 5
iris = datasets.load_iris()
andrewCurve = AndrewCurve()
leg = andrewCurve.genAndrewCurve("legendre" , iris.data)
fourier1 = andrewCurve.genAndrewCurve("fourier", iris.data[:20,:])
fourier2 = andrewCurve.genAndrewCurve("fourier", iris.data[50:70,:])
fourier3 = andrewCurve.genAndrewCurve("fourier", iris.data[100:120,:])

plt.figure()
for proj in fourier1["data"]:
    plt.plot(fourier1["t"],proj , 'r')
for proj in fourier2["data"]:
    plt.plot(fourier2["t"],proj , 'b')
for proj in fourier3["data"]:
    plt.plot(fourier3["t"],proj , 'g')
plt.show()