def gd(grad, v0, g, step_size=0.01, Nmax=100, tol=1e-6):
    '''
    grad: gradient function
    v0: initial value
    g: objective function
    '''    
    losses = []
    vs = np.zeros(v0.shape)
    v = v0
    gradv = grad(v)
    
    for i in range(Nmax):
        v = v - step_size * gradv
        gradv = grad(v)
        
        loss = g(v)
        losses.append(loss)
        vs = np.hstack((vs, v))

        eps = np.linalg.norm(gradv)
        if  eps <= tol:
            print('Reach termination criteria')
            break

    return v, losses, vs